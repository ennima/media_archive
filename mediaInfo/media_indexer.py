from VideoMetadata_lite import *
from time_metrics import *

import requests



def VideoMetadataDate2Mysql(ffmpeg_date):
	date_time_str = ffmpeg_date
	date_time_obj = datetime.strptime(date_time_str, '%d/%m/%Y %H:%M')
	return date_time_obj.strftime("%Y-%m-%d %H:%M:%S")

def findClip(clip_name, endpoint):

	data = {"name":clip_name,"mode":"strict"}
	try:
		req = requests.get(endpoint,data=data).json()
	except Exception as e:
		print(e)
		return False
		# raise e
	else:
		# print(req)
		return req


def saveClip(clip, endpoint):
	try:
		req = requests.post(endpoint,data=clip).json()
	except Exception as e:
		print(e)
		return False
	else:
		return req

def updateClip(clip_prop, endpoint):
	try:
		req = requests.patch(endpoint,data=clip_prop).json()
	except Exception as e:
		print(e)
		return False
	else:
		return req

def getClipMetadata(clip_path, format_uid, rel_path):

	meta = VideoMetadata(clip_path)
	meta.path_media_info = "C:\\Users\\ennima\\Documents\\Develops 2018\\Milenio\\restore_app\\mediaInfo\\mediainfo_bin\\MediaInfo.exe"
	meta.path_ffmpeg = "C:\\Users\\ennima\\Documents\\Develops 2018\\Milenio\\restore_app\\mediaInfo\\ffmpeg_bin\\ffprobe.exe"

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


def isReplicated(clip_existente_x, nuevo_clip_x, origin_uid):
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
			upd = updateClip(new_prop, "http://127.0.0.1:3006/clips")
	return result
		

def processSingleClip(clip_existente_s,nuevo_clip_s, origin_uid_s):
	if('result' in clip_existente_s.keys()):
			print("No existe ", nuevo_clip_s["name"]," en el sistema.")
			print(saveClip(nuevo_clip_s, "http://127.0.0.1:3006/clips"))
	else:
		print("Existe")
		# print("Ext:",clip_existente_s)
		if(clip_existente_s["extension"] == nuevo_clip_s["extension"]):

			print("Duplicado")
			isReplicated(clip_existente_s, nuevo_clip_s, origin_uid_s)
				
		else:
			print("Nuevo Formato")
			print(saveClip(nuevo_clip_s, "http://127.0.0.1:3006/clips"))
	

def processClip(clip_existente,nuevo_clip, origin_uid_c):
	print(type(clip_existente))
	if(type(clip_existente) == dict):

		processSingleClip(clip_existente,nuevo_clip, origin_uid_c)
		
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
					isReplicated(item, nuevo_clip, origin_uid_c)
					pass

			
		else:
			print("Nuevo Formato, que guay.")
			processSingleClip(clip_existente[0],nuevo_clip, origin_uid_c)


clips_index = ["ALFOMBRA GENERAL-VO_DF007W64.gxf","ALFOMBRA YALITZA-BITE_DF007WA4.gxf","21H ROMA OSCAR-FT_DF007QCD.gxf"]
# clips_index = ["ALFOMBRA YALITZA-BITE_DF007WA4.gxf"]
path = "R:\\VB2017\\HEY\\"
origin_uid = 9


time_metric = TimeMetrics()
time_metric.init()
for item in clips_index:
	new_clip = getClipMetadata(os.path.join(path,item),1,"\\HH\\LLLL")
	new_clip["h_main_origin_uid"] = origin_uid
	new_clip["h_origins"] = '[{0}]'.format(origin_uid)
	
	endpoint = "http://127.0.0.1:3006/clips/find"

	clip_existe = findClip(new_clip["name"],endpoint)
	
	processClip(clip_existe,new_clip, origin_uid)

print(time_metric.get_elapsed_time())
	
	