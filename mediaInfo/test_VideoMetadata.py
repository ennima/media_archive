import sys
import unittest
#sys.path.append('../')
from VideoMetadata_lite import *

class VideoMetadataTest(unittest.TestCase):
	
	def test_it_should_be_able_to_construct(self):
		path = "R:\\VB2017\\HEY\\"
		file = "21H ROMA OSCAR-FT_DF007QCD.gxf"
		meta = VideoMetadata(path+file)
		meta.path_media_info = "C:\\Users\\ennima\\Documents\\Develops 2018\\Milenio\\restore_app\\mediaInfo\\mediainfo_bin\\MediaInfo.exe"
		meta.path_ffmpeg = "C:\\Users\\ennima\\Documents\\Develops 2018\\Milenio\\restore_app\\mediaInfo\\ffmpeg_bin\\ffprobe.exe"
		self.assertIsInstance(meta,VideoMetadata,"Es instancia")
		meta.get_ffmpeg()
		# meta.get_mediaInfo()

		print("general_name:",meta.general_name)
		print("general_complete_name:",meta.general_complete_name)
		print("general_format:",meta.general_format)
		print("general_file_size:",meta.general_file_size)
		print("general_file_size_bytes:",meta.general_file_size_bytes)
		print("general_old_path:",meta.general_old_path)
		print("general_created_date:",meta.general_created_date)
		print("general_modified_date:",meta.general_modified_date)
		print("general_wrapper:",meta.general_wrapper )

		print("video_duration:",meta.video_duration)
		print("video_mark_in:",meta.video_mark_in)
		print("video_mark_out:",meta.video_mark_out)
		print("video_aspect_ratio:",meta.video_aspect_ratio)
		print("video_codec:",meta.video_codec)
		print("video_color_space:",meta.video_color_space)
		print("video_color_chroma_subsamplig:",meta.video_color_chroma_subsamplig )
		print("video_Width:",meta.video_Width)
		print("video_Height:",meta.video_Height)
		print("video_frame_rate:",meta.video_frame_rate)
		print("video_scan_type:",meta.video_scan_type )
		print("video_bit_depth:",meta.video_bit_depth )

		print("audio_channels:",meta.audio_channels)
		print("audio_format:",meta.audio_format)
		print("audio_sampling_rate:",meta.audio_sampling_rate)
		print("audio_bit_depth:",meta.audio_bit_depth)

if __name__ == '__main__':
    unittest.main()