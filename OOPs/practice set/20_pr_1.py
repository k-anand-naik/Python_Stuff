#create a class programmer for storing information of few programmers workng at microsoft

class Programmer:
	company = "Microsoft"
	def __init__(self, name, product):
		self.name = name
		self.product = product
	def getInfo(self):
		print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")

harry = Programmer("Harry\n","skype")
alka = Programmer("Alka\n","Github")
harry.getInfo()
alka.getInfo()						