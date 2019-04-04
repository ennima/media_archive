from VideoMetadata_lite import *
from time_metrics import *

import requests



def VideoMetadataDate2Mysql(ffmpeg_date):
	date_time_str = ffmpeg_date
	date_time_obj = datetime.strptime(date_time_str, '%d/%m/%Y %H:%M')
	return date_time_obj.strftime("%Y-%m-%d %H:%M:%S")

def findLog(clip_name, endpoint):
	print(" Findlog Endpoint:", endpoint)
	new_transaction = {
		"clip_uid":0,
		"action": "Find",
		"user_uid":1,
		"host_uid":0,
		"app_uid":3,
		"description":clip_name
	}

	try:
		req = requests.post(endpoint,data=new_transaction).json()
	except Exception as e:
		print(e)
		return False
		# raise e
	else:
		# print(req)
		return req

def findClip(clip_name, end_base, endpoint):

	data = {"name":clip_name,"mode":"strict"}
	findLog(clip_name,end_base + "/transactions")
	try:
		req = requests.get(end_base+endpoint,data=data).json()
	except Exception as e:
		print(e)
		return False
		# raise e
	else:
		# print(req)
		return req


def saveLog(clip_uid, clip_name, endpoint):
	print(" INDEXLOG Endpoint:", endpoint)
	new_transaction = {
		"clip_uid":clip_uid,
		"action": "Indexing",
		"user_uid":1,
		"host_uid":0,
		"app_uid":3,
		"description":clip_name
	}

	try:
		req = requests.post(endpoint,data=new_transaction).json()
	except Exception as e:
		print(e)
		return False
		# raise e
	else:
		# print(req)
		return req

def saveClip(clip, end_base, endpoint):
	try:
		req = requests.post(end_base+endpoint,data=clip).json()
	except Exception as e:
		print(e)
		return False
	else:
		print("---REQ: ",req)
		saveLog(req["insertId"], clip["name"], end_base+"/transactions")
		return req


def updateLog(clip_uid, prop_name, endpoint):
	print(" Updating Endpoint:", endpoint)
	new_transaction = {
		"clip_uid":clip_uid,
		"action": "Update",
		"user_uid":1,
		"host_uid":0,
		"app_uid":3,
		"description":prop_name
	}

	try:
		req = requests.post(endpoint,data=new_transaction).json()
	except Exception as e:
		print(e)
		return False
		# raise e
	else:
		# print(req)
		return req


def updateClip(clip_prop, e_base, endpoint):
	updateLog(clip_prop["clip_uid"], "h_origins: "+clip_prop["h_origins"], e_base+"/transactions")
	try:
		req = requests.patch(e_base+endpoint,data=clip_prop).json()
	except Exception as e:
		print(e)
		return False
	else:

		return req


def updateClipProp(clip_prop, key_name, e_base, endpoint):
	updateLog(clip_prop["clip_uid"], key_name+": "+clip_prop[key_name], e_base+"/transactions")
	try:
		req = requests.patch(e_base+endpoint,data=clip_prop).json()
	except Exception as e:
		print(e)
		return False
	else:

		return req

def getClipMetadata(clip_path, format_uid, rel_path):

	meta = VideoMetadata(clip_path)
	meta.path_media_info = "C:\\Users\\GVadmin\\Documents\\develops 2017\\Milenio\\media_archive\\mediaInfo\\mediainfo_bin\\MediaInfo.exe"
	meta.path_ffmpeg = "C:\\Users\\GVadmin\\Documents\\develops 2017\\Milenio\\media_archive\\mediaInfo\\ffmpeg_bin\\ffprobe.exe"

	time_metric = TimeMetrics()
	time_metric.init()


	meta.get_ffmpeg()

	new_clip = {
		"name":os.path.basename(clip_path)[:-4],
		"extension":os.path.basename(clip_path)[-4:],
		"size_bytes": meta.general_file_size_bytes,
		"duration":meta.video_duration,
		"aspect":meta.video_aspect_ratio,
		"size_screen":meta.video_Width+"x"+meta.video_Height,
		"created_date":VideoMetadataDate2Mysql(meta.general_created_date),
		"modified_date":VideoMetadataDate2Mysql(meta.general_modified_date),
		"tags":"Stratus, Milenio, Archivo",
		"thumbnail":"",
		"proxy":"",
		"o_pxy_id":"",
		"o_asset_type":"Clip",
		"format_uid": format_uid,
		"a_owner_uid":1,
		"a_groups":'["editors", "viewers", "ingesters", "admins"]',
		"a_users":"[]",
		"h_main_origin_uid":origin_uid,
		"h_origins":"[{0}]".format(origin_uid),
		"license":"Milenio Lic",
		"restored_count":0,
		"path":rel_path

	}
	# print(new_clip)
	
	# meta.__del__()
	print(time_metric.get_elapsed_time())
	return new_clip


def isReplicated(clip_existente_x, nuevo_clip_x, origin_uid, e_bas):
	result = False
	
	if(clip_existente_x["h_main_origin_uid"] == origin_uid):
		print("No guardar")
	else:
		print("Replicado en otro origen")
		result = True
		js = json.loads(clip_existente_x["h_origins"])
		
		if(nuevo_clip_x["h_main_origin_uid"] in js):
			print("No guardar")
		else:
			''' Add origin to hosting origins array '''
			js.append(nuevo_clip_x["h_main_origin_uid"])
			new_prop = {
						"clip_uid":clip_existente_x["clip_uid"],
						"h_origins":json.dumps(js)
						}
			upd = updateClip(new_prop, e_bas, "/clips")
	return result
		

def processSingleClip(clip_existente_s,nuevo_clip_s, origin_uid_s, e_base):
	if('result' in clip_existente_s.keys()):
			print("No existe ", nuevo_clip_s["name"]," en el sistema.")
			print(saveClip(nuevo_clip_s, e_base,"/clips"))
	else:
		print("Existe")
		# print("Ext:",clip_existente_s)
		if(clip_existente_s["extension"] == nuevo_clip_s["extension"]):

			print("Duplicado")
			isReplicated(clip_existente_s, nuevo_clip_s, origin_uid_s, e_base)
				
		else:
			print("Nuevo Formato")
			print(saveClip(nuevo_clip_s, e_base,"/clips"))
	

def processClip(clip_existente,nuevo_clip, origin_uid_c, end_ba):
	print(type(clip_existente))
	if(type(clip_existente) == dict):

		processSingleClip(clip_existente,nuevo_clip, origin_uid_c, end_ba)
		
	else:
		existe_formats = []
		for item in clip_existente:
			existe_formats.append(item["format_uid"])
			
		if(nuevo_clip["format_uid"] in existe_formats):
			print(nuevo_clip["format_uid"])
			print("Ya existe con este formato")
			
			for item in clip_existente:
				print(item["format_uid"])
				if(nuevo_clip["format_uid"] == item["format_uid"]):
					isReplicated(item, nuevo_clip, origin_uid_c, end_ba)
					pass

			
		else:
			print("Nuevo Formato, que guay.")
			processSingleClip(clip_existente[0],nuevo_clip, origin_uid_c, end_ba)


def validClip(root, file, origin_uid_c):
	result = False
	video_extensions = ['.gxf','.mov', '.asf', '.mp4', '.mxf', '.cmf']
	print("---validClip:",file.encode("utf-8"))
	extension = file[-4:]
	rel_path = root[2:]
	print("   Ext:", extension)
	print("   path:", rel_path)
	format_uid = 0
	if(str.upper(extension) == str.upper('.gxf')):
		format_uid = 1
	else:
		format_uid = 0

	if(extension in video_extensions):

		result = True
		print("Es un VIdeo:",file.encode("utf-8"))
		print("---- Path: ",os.path.join(root,file).encode("utf-8"))
		new_clip = getClipMetadata(os.path.join(root, file), format_uid, rel_path)
		new_clip["h_main_origin_uid"] = origin_uid_c
		new_clip["h_origins"] = '[{0}]'.format(origin_uid_c)
		
		endpoint = "/clips/find"

		clip_existe = findClip(new_clip["name"],endpoint_base,endpoint)
		if(clip_existe['path'] == None):
			print("Update Path to:",rel_path," ClipID:",clip_existe['clip_uid'])
			new_prop = {
						"clip_uid":clip_existe['clip_uid'],
						"path":rel_path
						}
			update_clip_prop = updateClipProp(new_prop, "path", endpoint_base, "/clips")
			print(update_clip_prop)
		else:
			("Path OK")

		processClip(clip_existe,new_clip, origin_uid_c, endpoint_base)

	return result


def scrapFs(videos_path_1,dirs_to_scrap, origin_uid_c):
	curr_dir = "--"
	clip_counter = 0
	indexado = 0
	indexed_clips = 0
	for root, dirs, files in os.walk(videos_path_1):
		
		for file in files:
			clip_counter += 1
			if(dirs_to_scrap == "all"):
				if(os.path.exists(os.path.join(root, file))):
					if(validClip(root, file, origin_uid_c)):
						indexed_clips += 1
			else:
				if(dirs_to_scrap[0] in root):
					
					curr_dir = dirs_to_scrap[0]
					print("---- Pathpr:",root)
					print("---- Clip:",file.encode("utf-8"))
					print(os.path.join(root,file))
					if(validClip(root, file, origin_uid_c)):
						indexed_clips += 1
					indexado = 1
					break

				else:
					curr_dir = "-/-/-/"
					if(indexado):
						print("BOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
						break
	return {"indexed_clips":indexed_clips,"clip_counter":clip_counter}




endpoint_base = "http://127.0.0.1:3006"
# videos_path = "Y:\\StratusArchive\\"
videos_path = "R:\\"
storage_origin_file = "istorage_srvr"
dirs_to_scrap1 = ["XEN\\t_188161L6\\Archivo\\HEY"]
# dirs_to_scrap1 = "all"

origin_uid = -1
if(os.path.exists(os.path.join(videos_path,storage_origin_file))):
	print("Hay Origen")
	with open(os.path.join(os.path.join(videos_path,storage_origin_file))) as id_file:
		origin_uid = int(id_file.read())
		print("origin_uid:",origin_uid)
else:
	print("Origen Desconocido")


# clips_index = ["ALFOMBRA GENERAL-VO_DF007W64.gxf","ALFOMBRA YALITZA-BITE_DF007WA4.gxf","21H ROMA OSCAR-FT_DF007QCD.gxf"]
# clips_index = ["ALFOMBRA YALITZA-BITE_DF007WA4.gxf"]
# path = "R:\\VB2017\\HEY\\"
# origin_uid = 9


time_metric = TimeMetrics()
time_metric.init()

srap_fs = scrapFs(videos_path,dirs_to_scrap1, origin_uid)


# print(getClipMetadata("R:\\VB2017\\AFICION\\ABIERTO AUSTRALIA-VO_DF007OOS.gxf", "00", "test"))

# print(getClipMetadata("R:\\VB2017\\HEY\\21H ROMA OSCAR-FT_DF007QCD.gxf", "00", "test"))

print("Origin:",origin_uid, "Total CLips:",srap_fs["clip_counter"], "indexed_clips:",srap_fs["indexed_clips"])
# for item in clips_index:
# 	new_clip = getClipMetadata(os.path.join(path,item),1,"\\HH\\LLLL")
# 	new_clip["h_main_origin_uid"] = origin_uid
# 	new_clip["h_origins"] = '[{0}]'.format(origin_uid)
	
# 	endpoint = "/clips/find"

# 	clip_existe = findClip(new_clip["name"],endpoint_base,endpoint)

# 	processClip(clip_existe,new_clip, origin_uid, endpoint_base)

print(time_metric.get_elapsed_time())
	
	