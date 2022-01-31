class RailwayForm:
	formType = "RailwayForm"

	def printData(self):
		print(f"Name is {self.name}")	
		print(f"Train is {self.train}")
		
anandApplication = RailwayForm()
anandApplication.name = "Anand"
anandApplication.train =  "APSK"
anandApplication.printData()		