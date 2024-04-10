# Python has functions for creating, reading, updating, and deleting files.
#open a file
myFile = open('myfile.txt','w')

#get info in the file
print('Name', myFile.name)
print('Is closed', myFile.closed)
print('Opening Mode', myFile.mode)

#write to file
myFile.write('I love Python')
myFile.write(' And Math')
myFile.close()

#append to file
myFile = open('myfile.txt','a')
myFile.write(' I also like php')
myFile.close()

#read from a file
myFile = open('myfile.txt','r+')
text = myFile.read(100)
print(text)


