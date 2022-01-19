import os

class Test:

	def __init__(self):
		path = "./tests.txt"
		
		if(self.checkfile(path)):
			print("File excisting")
			data = self.readfile(path)
			print(f"{path}: {data}")
			self.writetofile(path, ["lol", "baum", "jahhaf"])
			data = self.readfile(path)
			print(f"{path}: {data}")
		else:
			print(f"{path} not found, creating file")
			self.new_file(path)
			if self.checkfile(path):
				print(f"{path} created successfully")
			else:
				print(f"Error while creating file at {path}")

	def checkfile(self, path):
		return os.path.exists(path)

	def new_file(self, path):
		f = open(path, "w")
		f.close()

	def readfile(self, path):
		returner = []
		f = open(path, "r")
		for line in f:
			returner.append(line.replace("\n", ""))
		
		f.close()
		return returner

	def writetofile(self, path, data):
		stringdata = ""
		for d in data:
			stringdata += str(d)+"\n"

		f = open(path, "w")
		f.write(stringdata)
		f.close()


if __name__ == '__main__':
	Test()

