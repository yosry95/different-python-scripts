import os 
import numpy as np
import shutil

root_dir =os.getcwd()
subfolders = [f.name for f in os.scandir(root_dir) if f.is_dir() ]  
#print(subfolders)

for folders in subfolders:
	subfolders2 = [f.name for f in os.scandir(root_dir+'\\' + folders) if f.is_dir() ]
	for folder in subfolders2:
		os.makedirs(root_dir +'\\data\\train\\' + folder)
		# os.makedirs(root_dir +'data/val' + folder)
		os.makedirs(root_dir +'\\data\\validation\\' + folder)
		allFileNames = os.listdir(os.getcwd() +'\\PetImages\\' + folder)
		np.random.shuffle(allFileNames)
		train_FileNames, test_FileNames = np.split(np.array(allFileNames),
                                                          [int(len(allFileNames)*0.7)])	
		for file in train_FileNames:
			shutil.copy(os.getcwd() +'\\PetImages\\' + folder +'\\' + file,os.getcwd() +'\\data\\train\\' + folder +'\\'+file)
		for file in test_FileNames:
			shutil.copy(os.getcwd() +'\\PetImages\\' + folder +'\\' + file,os.getcwd() +'\\data\\validation\\' + folder +'\\'+file)	