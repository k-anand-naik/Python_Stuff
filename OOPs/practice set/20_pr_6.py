#Can you change the self parameter inside a class to something else(say "anand"). Try changing self to "slf" or "anand" and see the effects (Ans: Yes we can change)
class Sample:
	def __init__(self, name):
		self.name = name

#	def __init__(slf, name):
#		slf.name = name

#	def __init__(Anand, name):
#		Anand.name = name

obj = Sample("Anand")
print(obj.name)				