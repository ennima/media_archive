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

def getClipMetadata(clip_path):

	meta = VideoMetadata(clip_path)
	meta.path_media_info = "C:\\Users\\ennima\\Documents\\Develops 2018\\Milenio\\restore_app\\mediaInfo\\mediainfo_bin\\MediaInfo.exe"
	meta.path_ffmpeg = "C:\\Users\\ennima\\Documents\\Develops 2018\\Milenio\\restore_app\\mediaInfo\\ffmpeg_bin\\ffprobe.exe"

	time_metric = TimeMetrics()
	time_metric.init()


	meta.get_ffmpeg()

	# print("general_name:",meta.general_name)
	# print("general_file_size_bytes:",meta.general_file_size_bytes)
	# print("video_duration:",meta.video_duration)
	# print("video_aspect_ratio:",meta.video_aspect_ratio)
	# print("Screen Size:",meta.video_Width+"x"+meta.video_Height)

	# print("general_created_date:",VideoMetadataDate2Mysql(meta.general_created_date))
	# print("general_modified_date:",VideoMetadataDate2Mysql(meta.general_modified_date))

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
		"format_uid":1,
		"a_owner_uid":1,
		"a_groups":'["editors", "viewers", "ingesters", "admins"]',
		"a_users":"[]",
		"h_main_origin_uid":0,
		"h_origins":"[]",
		"license":"Milenio Lic",
		"restored_count":0

	}
	# print(new_clip)
	
	# meta.__del__()
	print(time_metric.get_elapsed_time())
	return new_clip

def processClip(clip_existente,nuevo_clip):
	print(type(clip_existente))
	if(type(clip_existente) == dict):

		if('result' in clip_existente.keys()):
			print("No existe ", nuevo_clip["name"]," en el sistema.")
			print(saveClip(nuevo_clip, "http://127.0.0.1:3006/clips"))
		else:
			print("Existe")
			# print("Ext:",clip_existente)
			if(clip_existente["extension"] == nuevo_clip["extension"]):
				print("Duplicado")
				if(clip_existente["h_main_origin_uid"] == origin_uid):
					print("No guardar")
				else:
					print("Replicado")
					print(clip_existente["h_origins"])
					js = json.loads(clip_existente["h_origins"])
					print(js[0])
					if(nuevo_clip["h_main_origin_uid"] in js):
						print("No guardar")
					else:
						print("Agregar a host origins.")
						js.append(nuevo_clip["h_main_origin_uid"])
						print(js)
						print(json.dumps(js))
			else:
				print("Nuevo Formato")
				print(saveClip(nuevo_clip, "http://127.0.0.1:3006/clips"))
	else:
		print("FUCK")


clips_index = ["ALFOMBRA GENERAL-VO_DF007W64.gxf","ALFOMBRA YALITZA-BITE_DF007WA4.gxf","21H ROMA OSCAR-FT_DF007QCD.gxf",]
path = "R:\\VB2017\\HEY\\"
origin_uid = 9


# file = "21H ROMA OSCAR-FT_DF007QCD.gxf"
for item in clips_index:
	new_clip = getClipMetadata(os.path.join(path,item))
	new_clip["h_main_origin_uid"] = origin_uid
	new_clip["h_origins"] = '[{0}]'.format(origin_uid)
	# print(json.dumps(new_clip))
	print("\n\n")
	endpoint = "http://127.0.0.1:3006/clips/find"
	clip_existe = findClip(new_clip["name"],endpoint)
	
	processClip(clip_existe,new_clip)
	
	
	