#write a class Train which has methods to book a ticket, get status (no.of seats) and get fare info of train running under indian railways

class Train:
	def __init__(self, name, fare, seats):
		self.name = name
		self.fare = fare
		self.seats = seats
	def getStatus(self):
		print("* * * * * * * ")
		print(f"The name of the train is {self.name}")
		print(f"The no.of seats available in this train is {self.seats}")
		print("* * * * * * *")
		
	def fareInfo(self):
		print(f"The fare of the ticket is Rs.{self.fare}")	
		
	def bookTicket(self):
		if (self.seats>0):
			print(f"Your ticket has been booked! Your seat number is {self.seats}")
			self.seats = self.seats - 1
		else:
			print("Sorry ): this train is full kindely try in tatkal")
#	def cancelTicket(self,seatNo):
	#	pass

intercity = Train("Intercity Express: 14507",90,300)
intercity.getStatus()
intercity.fareInfo()	
intercity.bookTicket()
intercity.getStatus() #this shows how many tickets are left after the first ticket get booked															