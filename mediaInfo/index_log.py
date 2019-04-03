# -*- coding: utf-8 -*-
import os, sys

counter = 0
feos = []
videos_path_1 = "R:\\VB2017\\Noticias\\"
for root, dirs, files in os.walk(videos_path_1):
	print(root)
	# print(dirs)
	# print(files)
	for file in files:
		if("Ñ" in file):
			print("---------- ",file)
			feos.append(file)
			counter += 1
		else:
			print(file)

print("Total Ñ:",counter)
print(feos)