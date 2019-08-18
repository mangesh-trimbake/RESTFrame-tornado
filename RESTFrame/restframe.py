import sys

import os
import shutil
import datetime
import re

class RestFrame:
	"""docstring for ClassName"""
	def __init__(self, arg):
		self.model_table = arg

	def creatHandler(self,path):
		ModelNames = self.getModelNames()
		ModelName = self.getModelName()
		model_names = self.get_model_names()
		model_name = self.get_model_name()

		# print(ModelNames,ModelName,model_names,model_name)
		src_file = "./res/handlers/ModelsHandler.py"
		dst_file = path + ""+ModelNames + "Handler.py"

		shutil.copy(src_file,dst_file)

		filedata = None
		with open(dst_file, 'r') as file:
		  filedata = file.read()

		# print(filedata)

		# Replace the target string
		# filedata.replace(r"ModelNames.+", ModelNames)
		# filedata.replace('ModelName', ModelName)
		# filedata.replace('model_names', model_names)
		# filedata.replace('model_name', model_name)


		
		# print(re.findall("ModelNames.+", filedata))

		replaced = re.sub(r"ModelNames", ModelNames, filedata)
		replaced = re.sub(r"ModelName", ModelName, replaced)
		replaced = re.sub(r"model_names", model_names, replaced)
		replaced = re.sub(r"model_name", model_name, replaced)

		# print(replaced)

		# Write the file out again
		with open(dst_file, 'w') as file:
		  file.write(replaced)

		print(ModelNames + "Handler.py created")


	def getModelNames(self):
		ModelNames = self.model_table
		ModelNames = ModelNames.split("_")
		ModelNames = "".join(w.capitalize() for w in ModelNames)
		return ModelNames

	def getModelName(self):
		ModelNames = self.model_table
		ModelNames = ModelNames.split("_")
		ModelNames = "".join(w.capitalize() for w in ModelNames)
		if(ModelNames[:-3] =="ies"):
			ModelNames[0:-3]+"y"
		else:
			ModelNames = ModelNames[0:-1]

		return ModelNames

	def get_model_names(self):
		ModelNames = self.model_table
		return ModelNames

	def get_model_name(self):
		ModelNames = self.model_table
		if(ModelNames[:-3] =="ies"):
			ModelNames[0:-3]+"y"
		else:
			ModelNames = ModelNames[0:-1]

		return ModelNames

		


if __name__ == '__main__':
	first_args =  sys.argv[1]
	second_args = sys.argv[2]
	if(str(first_args) == "rest"):
		rest_frame = RestFrame(second_args)
		rest_frame.creatHandler("../Controllers/")
