class object_dict(dict):
	def __setattr__(self, name, value):
		if callable(value):
				value = value.__get__(self, self.__class__)
		self.__setitem__(name, value)

	def __getattr__(self, value):
		return self.__getitem__(value)

	def save(self, filename, mode):
		json_object = json.dumps(self, indent=2)
		with open(filename, mode) as file:
			file.write(json_object)
