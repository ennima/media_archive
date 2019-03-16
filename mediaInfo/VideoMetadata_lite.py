from headers import *

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
		# print("Created")
		# print("Video File: ",video)
		self.video = video
		(self.mode, self.ino, self.dev, self.nlink, self.uid, self.gid, self.size, self.atime, self.mtime, self.ctime) = os.stat(video)

		self.general_created_date =  time.strftime("%d/%m/%Y %H:%M", time.localtime(self.ctime))
		self.general_modified_date =  time.strftime("%d/%m/%Y %H:%M", time.localtime(self.mtime))
		self.general_file_size_bytes = self.size
		
		# if(os.path.exists(self.path_media_info)):
		# 	print("Genial existe media info")
		# else:
		# 	print("No se encontro media info")
	def __del__(self):
		print("----------------Object VideoMetadata: deleted")

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
		# print("-------------#------",aspect_dec_l)
		if((float(aspect_dec_l)>1.20) and (float(aspect_dec_l) < 1.25)):
			# print("# Aspect: 5:4")
			aspect_ratio = "5:4"
		elif((float(aspect_dec_l)>1.29) and (float(aspect_dec_l) < 1.34)):
			# print("# Aspect: 4:3")
			aspect_ratio = "4:3"
		elif((float(aspect_dec_l)>1.59) and (float(aspect_dec_l) < 1.61)):
			# print("# Aspect: 16:10")
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

