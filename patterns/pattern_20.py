num = int(input("Enter the number of rows: "))
ch = 64
for row in range(1,num+1):
	for col in range(1,row+1):
		ch = ch+1
		print("{0}{1}".format(chr(ch),row),end=" ")
	print()

for row in range(num-1,0,-1):
	for col in range(1,row+1):
		ch = ch+1
		print("{0}{1}".format(chr(ch),row),end=" ")
	print()
	

#Enter the number of rows: 5
#A1
#B2 C2
#D3 E3 F3
#G4 H4 I4 J4
#K5 L5 M5 N5 O5
#P4 Q4 R4 S4
#T3 U3 V3
#W2 X2
#Y1																																						