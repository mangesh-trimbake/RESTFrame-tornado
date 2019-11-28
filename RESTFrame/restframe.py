import sys
import errno
import os
import shutil
import datetime
import re

class RestFrame:
	"""docstring for ClassName"""
	def __init__(self, arg):
		self.model_table = arg
		self.ModelNames = ""
		self.ModelName = ""
		self.model_names = ""
		self.model_name = ""

	def creatHandler(self,path):
		self.ModelNames = self.getModelNames()
		self.ModelName = self.getModelName()
		self.model_names = self.get_model_names()
		self.model_name = self.get_model_name()

		# print(self.ModelNames,self.ModelName,self.model_names,self.model_name)
		src_file = "./res/handlers/ModelsHandler.py"
		dst_file = path + ""+self.ModelNames + "Handler.py"

		# shutil.copy(src_file,dst_file)
		try:
		    shutil.copy(src_file, dst_file)
		except IOError as e:
		    # ENOENT(2): file does not exist, raised also on missing dest parent dir
		    if e.errno != errno.ENOENT:
		        raise
		    # try creating parent directories
		    os.makedirs(os.path.dirname(dst_file))
		    shutil.copy(src_file, dst_file)
		    print(dst_file)

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

		replaced = re.sub(r"ModelNames", self.ModelNames, filedata)
		replaced = re.sub(r"ModelName", self.ModelName, replaced)
		replaced = re.sub(r"model_names", self.model_names, replaced)
		replaced = re.sub(r"model_name", self.model_name, replaced)

		# print(replaced)

		# Write the file out again
		with open(dst_file, 'w') as file:
		  file.write(replaced)

		print(self.ModelNames + "Handler.py created")


	def getModelNames(self):
		ModelNames = self.model_table
		ModelNames = ModelNames.split("_")
		ModelNames = "".join(w.capitalize() for w in ModelNames)
		return ModelNames

	def getModelName(self):
		ModelNames = self.model_table
		ModelNames = ModelNames.split("_")
		ModelNames = "".join(w.capitalize() for w in ModelNames)
		if(ModelNames[-3:] =="ies"):
			ModelNames = ModelNames[0:-3]+"y"
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

	def getRoutes(self):
		route = self.model_table
		route = route.replace("_","-")

		print('(r"/'+route+'", '+self.ModelNames+"),")
		print('(r"/'+route+'/add", '+self.ModelNames+"Add"+"),")
		print('(r"/'+route+'/([^/]+)", '+self.ModelNames+"Show"+"),")
		print('(r"/'+route+'/update/([^/]+)", '+self.ModelNames+"Update"+"),")






if __name__ == '__main__':
	first_args =  sys.argv[1]
	second_args = sys.argv[2]
	if(str(first_args) == "rest"):
		rest_frame = RestFrame(second_args)
		# print(len(sys.argv))
		if(len(sys.argv)>=4):
			controller_path = "../Controllers/" + sys.argv[3]+ "/"
		else:
			controller_path = "../Controllers/"
		rest_frame.creatHandler(controller_path)

		rest_frame.getRoutes()
