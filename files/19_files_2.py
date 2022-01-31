#creating a new file and 
f = open('mydata_1.txt','r')
f1 = open('abc.txt','w')  #if 'abc' file is not exist in the device, it'll create that file for you
for data in f:
	f1.write(data)
