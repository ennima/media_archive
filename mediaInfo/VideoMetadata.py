import os, time, subprocess
import numpy as np
from datetime import datetime, date, timedelta
from subprocess import check_output

class VideoMetadata:

	path_media_info = "MediaInfo.exe"
	path_ffmpeg = "ffprobe.exe"
	#General info
	general_name = "empty"
	general_complete_name = "empty"
	general_format = "empty"
	general_file_size = "empty"
	general_file_size_bytes = "empty"
	general_old_path = "empty"
	general_created_date = "empty"
	general_modified_date = "empty"
	general_wrapper ="empty"

	video_duration = "empty"
	video_mark_in = "empty"
	video_mark_out = "empty"
	video_aspect_ratio = "empty"
	video_codec = "empty"
	video_color_space = "empty"
	video_color_chroma_subsamplig ="empty"
	video_Width = "empty"
	video_Height = "empty"
	video_frame_rate = "empty"
	video_scan_type ="empty"
	video_bit_depth ="empty"

	audio_channels = "empty"
	audio_format = "empty"
	audio_sampling_rate = "empty"
	audio_bit_depth = "empty"

	def __init__(self,video):
		print("Created")
		print("Video File: ",video)
		self.video = video
		(self.mode, self.ino, self.dev, self.nlink, self.uid, self.gid, self.size, self.atime, self.mtime, self.ctime) = os.stat(video)

		self.general_created_date =  time.strftime("%d/%m/%Y %H:%M", time.localtime(self.ctime))
		self.general_modified_date =  time.strftime("%d/%m/%Y %H:%M", time.localtime(self.mtime))
		self.general_file_size_bytes = self.size
		
		if(os.path.exists(self.path_media_info)):
			print("Genial existe media info")
		else:
			print("No se encontro media info")

	def get_ffmpeg_dimensions(self, dimension):
		dimensions_split = dimension.split(" ")
		#print(dimensions_split)
		dimensions = dimensions_split[0].split("x")
		#print("#DIMENSIONS: ",dimensions)
		self.video_Width = dimensions[0]
		self.video_Height = dimensions[1]


	def get_aspect_ratio(self,width, height):
		aspect_ratio = "empty"
		aspect_dec = width/height
		aspect_dec_l = "{0:.2f}".format(aspect_dec)
		print("-------------#------",aspect_dec_l)
		if((float(aspect_dec_l)>1.20) and (float(aspect_dec_l) < 1.25)):
			print("# Aspect: 5:4")
			aspect_ratio = "5:4"
		elif((float(aspect_dec_l)>1.29) and (float(aspect_dec_l) < 1.34)):
			print("# Aspect: 4:3")
			aspect_ratio = "4:3"
		elif((float(aspect_dec_l)>1.59) and (float(aspect_dec_l) < 1.61)):
			print("# Aspect: 16:10")
			aspect_ratio = "16:10"
		elif((float(aspect_dec_l)>1.77) and (float(aspect_dec_l) < 1.79)):
			aspect_ratio = "16:9"

		self.video_aspect_ratio = aspect_ratio

	def get_size_bytes(self):
		#print("Size: ",self.size)
		return self.size

	def get_old_date(self):
		minor_date = ""
		if(self.mtime < self.ctime):
			print("Modified minor")
			minor_date = time.strftime("%d/%m/%Y %H:%M", time.localtime(self.mtime))
		else:
			print("Created minor")
			minor_date = time.strftime("%d/%m/%Y %H:%M", time.localtime(self.ctime))
		
		return minor_date

	def get_mediaInfo(self):
		out = check_output([self.path_media_info, self.video])
		out_str = out.decode("utf-8")
		out_split = out_str.split("\r\n")
		general_info = False
		video_info = False
		audio_info = False
		print(out_str)
		for data in out_split:
			print(data.strip())
			if("General" in data):
				print("Get general info")
				general_info = True
				video_info = False
				audio_info = False


			if((general_info) and ("Format" in data)):
				data_split = data.split(":")
				#print("-Format:",data_split)
				isFormat = data_split[0].split("/")
				#print(isFormat,"   -   ", len(isFormat))
				if(len(isFormat) == 1):
					#print("#"+isFormat[0].strip()+"#")
					if(isFormat[0].strip() == "Format"):
						#print("Es el formato: ",data_split[1].strip())
						self.general_format = data_split[1].strip()


			if((general_info) and  ("File size" in data)):
				data_split = data.split(":")
				#print(data_split[1])
				self.general_file_size = data_split[1].strip()


			if((general_info) and ("Complete name" in data)):
				data_split = data.split(" :")
				print("data_split: ",data_split)

				self.general_complete_name = data_split[1].strip()
				print("data_split 1: ",data_split[1].strip())
				name = self.general_complete_name.split(".")
				print("NAME: ",name)
				self.general_name = name[0].strip()
				self.general_wrapper = name[1].strip().upper()


			if((general_info) and ("Track name" in data)):
				data_split = data.split(":")
				#print(data_split)
				old_path = data_split[1]+":"+data_split[2]
				#print(old_path.strip())
				self.general_old_path = old_path


			if("Video" in data):
				general_info = False
				video_info = True
				audio_info = False





			# if((video_info) and ("Duration" in data)):
			# 	data_split = data.split(":")
			# 	#print(data_split)
			# 	# duration_split = data_split[1].split()
			# 	# print(duration_split)
			# 	if(("s" or "ms") in data_split[1]):
			# 		#print("##########String formated")
			# 		formato_final = "%H:%M:%S.%f"
			# 		formato_actual ="%S s %f ms"
			# 		#print(datetime.strptime(data_split[1].strip(), formato_actual).strftime(formato_final))
			# 		self.video_duration = datetime.strptime(data_split[1].strip(), formato_actual).strftime(formato_final)
			# 	elif(("h" or "min") in data_split[1]):
			# 		print("HORAS")
			# 		formato_final = "%H:%M:%S.%f"
			# 		formato_actual ="%H h %M min"
			# 		self.video_duration = datetime.strptime(data_split[1].strip(), formato_actual).strftime(formato_final)
			# 	elif("min" in data_split[1]):
			# 		formato_final = "%H:%M:%S.%f"
			# 		formato_actual ="%M min"
			# 		self.video_duration = datetime.strptime(data_split[1].strip(), formato_actual).strftime(formato_final)





			if((video_info) and ("Codec ID" in data)):
				data_split = data.split(":")
				#print("-Format:",data_split)
				isCodec = data_split[0].split("/")
				#print(isFormat,"   -   ", len(isFormat))
				if(len(isCodec) == 1):
					#print("#"+isFormat[0].strip()+"#")
					if(isCodec[0].strip() == "Codec ID"):
						print("Es el Codec: ",data_split[1].strip())
						self.video_codec = data_split[1].strip()

			if((video_info) and ("Width" in data)):
				data_split = data.split(":")
				split_w = data_split[1].split()
				#print("W:",split_w)
				if(len(split_w)==3):
					temp_w = split_w[0]+split_w[1]
					#print(temp_w)
				elif(len(split_w)==2):
					temp_w = split_w[0]

				self.video_Width = temp_w

			if((video_info) and ("Height" in data)):
				data_split = data.split(":")
				split_w = data_split[1].split()
				#print("H:",split_w)
				if(len(split_w)==3):
					temp_w = split_w[0]+split_w[1]
					#print(temp_w)
				elif(len(split_w)==2):
					temp_w = split_w[0]

				self.video_Height = temp_w


			if((video_info) and ("aspect ratio" in data)):
				data_split = data.split(":")
				aspect = data_split[1]+":"+data_split[2]
				self.video_aspect_ratio = aspect.strip()

			if((video_info) and ("Frame rate" in data) and not("mode" in data)):
				data_split = data.split(":")
				fps = data_split[1].split()
				# print(type(fps[0]))
				# print(float(fps[0]))
				tmp = float(fps[0])
				self.video_frame_rate = (str(tmp))


			if((video_info) and ("Scan type" in data)):
				data_split = data.split(":")
				self.video_scan_type = data_split[1].strip()


			if((video_info) and ("Color space" in data)):
				data_split = data.split(":")
				self.video_color_space = data_split[1].strip()


			if((video_info) and ("Chroma subsampling" in data)):
				data_split = data.split(":")
				tmp = data_split[1]+":"+data_split[2]+":"+data_split[3]
				self.video_color_chroma_subsamplig = tmp.strip()


			if((video_info) and ("Bit depth" in data)):
				data_split = data.split(":")
				self.video_bit_depth = data_split[1].strip()


			if("Audio" in data):
				general_info = False
				video_info = False
				audio_info = True

				return True


	def get_ffmpeg(self):
		command = [self.path_ffmpeg, '-i', self.video]
		p = subprocess.Popen(command, stderr=subprocess.PIPE)
		text = p.stderr.read()
		retcode = p.wait()
		text = text.decode('utf-8').split("\r\n")
		info_metadata = False

		count_audio = 0

		for data in text:
			#print(data)

			if("Metadata:" in data):
				info_metadata = True
			
			if (info_metadata) and ("at_mark_in" in data):
				#print("Mark In")
				data_split = data.strip().split(" ")
				#print(data_split[1])
				if(self.video_mark_in == "empty"):
					self.video_mark_in = data_split[1]
			
			if (info_metadata) and ("at_mark_out" in data):
				#print("Mark Out")
				data_split = data.strip().split(" ")
				#print(data_split[1])
				if(self.video_mark_out == "empty"):
					self.video_mark_out = data_split[1]

			if("Duration:" in data):
				info_metadata = False
				data_split = data.strip().split()

				if(self.video_duration == "empty"):
					self.video_duration = data_split[1].replace(",","")
			
			if("Video:" in data):
				data_split = data.strip().split(",")
				#print(data_split)
				video_codec_split = data_split[0].split("Video: ")
				#print(video_codec_split[1])
				
				if(self.video_codec == "empty"):
					self.video_codec = video_codec_split[1].strip()
				
				#print(data_split)
				#print(data_split[1])

				if("(" in data_split[1]):
					#print("#####Color complejo")
					#print(data_split[1],data_split[2])
					#print(data_split[1].split("("))
					color_split = data_split[1].split("(")
					color = color_split[0].strip()
					#print(color)
					if("yuv" in color):
						if(self.video_color_space == "empty"):
							self.video_color_space = "YUV"
						color_split = color.split("yuv")
						#print(color_split)

						if("p" in color_split[1]):
							chroma = color_split[1].split("p")
							#print("chroma: ", chroma)
							if(self.video_color_chroma_subsamplig == "empty"):
								self.video_color_chroma_subsamplig = chroma[0]
					#print("### NEXT: ",data_split[3])
					if(self.video_Width == "empty"):
						self.get_ffmpeg_dimensions(data_split[3].strip())
					
					if(self.video_aspect_ratio == "empty"):
						self.get_aspect_ratio(int(self.video_Width), int(self.video_Height))
					
					fps_split = data_split[4].strip().split(" ")
					#print(fps_split)
					if(self.video_frame_rate == "empty"):
						self.video_frame_rate = fps_split[0]

				else:
					print("##Color normal")
					print(data_split[1])

			if ("Audio:" in data):
				count_audio += 1
				#print("Audio ch: ", count_audio)
				data_split = data.strip().split(",")

				#print(data_split)
				format_split = data_split[0].split("Audio:")
				#print(format_split)
				if(self.audio_format == "empty"):
					self.audio_format = format_split[1]

				if(self.audio_sampling_rate == "empty"):
					self.audio_sampling_rate = data_split[1]
				
				if(self.audio_bit_depth == "empty"):
					self.audio_bit_depth = data_split[3]

			if("Unknown:" in data):
				if(self.audio_channels == "empty"):
					self.audio_channels = count_audio

