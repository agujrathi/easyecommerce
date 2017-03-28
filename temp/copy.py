import os

a=5

while a<89:
	print "copying"
	print a

	command = "cp target.png "+"battery-"+str(a)+".png"
	print command
	os.system(command)
	a=a+1
