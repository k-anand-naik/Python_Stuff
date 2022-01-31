#--> Implement a student library system using OOPs where student can borrow a book from the list of books.
#--> Create a separate library and student class. Your program must be menu driven. You are free to choose methods and attributes of your choice to implement this fuctionality

class library:
	def __init__(self, listOfBooks):
		self.books = listOfBooks
	
	def displayAvailableBooks(self):
		print("Books present in this library are:")
		for book in self.books:
			print(" *" + books)
	
	def borrowBooks(self, bookName):
		if bookName in self.books:
			print(f"You have been issued {bookName}. Please keep it safe and return it witnin 30 days")
			self.books.remove(bookName)
			return True
		else:
			print("Sorry, This book is either not available or has already been issued to someone else. Please 					wait until the book is available.")
			return False
		
	def returnBook(self, bookName):
		self.books.append(books)
		print("Thanks for returning this book! Hope you enjoid reading it. Have a great day ahead!")

class student:
	def requestBook(self):
		self.book = input("Enter the name of the book you want to borrow: ")
		return self.book
	
	def returnBook(self):
		self.book = input("Enter the name of the book you want to return: ")
		return self.book

if __name__ == " __main__ ":
	centralLibrary = librabry(["Algorithms", "django", "Clrs", "Python Notes"])
	student = student()
	#centralLibrary.displayAvailableBooks()
	while(True):
		welcomeMsg = ''' ===== Welcome to Central Library =====
		Please choose an option:
			1. List of the books
			2.Rrequest a bool 
			3.Add/return a book
			4.Exit the library
			'''
		print(welcomeMsg)
			
		a = int(input("Enter your choice: "))
		if a == 1:
			centralLibrary.displayAvailableBooks()
		elif a == 2:
			centralLibrary.borrowBooks(student.requestBooks())
		elif a == 3:
			centralLibrary.returnBooks(student.requestBooks())
		elif a == 4:
			print("Thanks for choosing Central Library. Have a great day ahead.")
		else:
			print("Invalid choice!")																																																																																	