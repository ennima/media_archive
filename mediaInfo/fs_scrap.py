from VideoMetadata_lite import *
from time_metrics import *

import requests




def validClip(root, file):
	result = False
	video_extensions = ['.gxf','.mov', '.asf', '.mp4', '.mxf', '.cmf']
	print("---validClip:",file)
	extension = file[-4:]
	rel_path = root[2:]
	print("   Ext:", extension)
	print("   path:", rel_path)
	if(extension in video_extensions):

		result = True
		print("Es un VIdeo")

	return result



videos_path = "C:\\Users\\ennima\\Documents\\Develops 2018\\Milenio\\restore_app\\mediaInfo\\"
videos_path = "R:\\"
storage_origin_file = "istorage_srvr"
dirs_to_scrap1 = ["Main"]
# dirs_to_scrap1 = "all"

origin_uid = -1

if(os.path.exists(os.path.join(videos_path,storage_origin_file))):
	print("Hay Origen")
	with open(os.path.join(os.path.join(videos_path,storage_origin_file))) as id_file:
		origin_uid = int(id_file.read())
else:
	print("Origen Desconocido")


def scrapFs(videos_path_1,dirs_to_scrap):
	curr_dir = "--"
	clip_counter = 0
	indexado = 0
	indexed_clips = 0
	for root, dirs, files in os.walk(videos_path_1):
		
		for file in files:
			clip_counter += 1
			if(dirs_to_scrap == "all"):
				if(validClip(root, file)):
					indexed_clips += 1
			else:
				if(dirs_to_scrap[0] in root):
					
					curr_dir = dirs_to_scrap[0]
					if(validClip(root, file)):
						indexed_clips += 1
					indexado = 1

				else:
					curr_dir = "-/-/-/"
					if(indexado):
						print("BOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
						break
	return {"indexed_clips":indexed_clips,"clip_counter":clip_counter}



srap_fs = scrapFs(videos_path,dirs_to_scrap1)

print("Origin:",origin_uid, "Total CLips:",srap_fs["clip_counter"], "indexed_clips:",srap_fs["indexed_clips"])


