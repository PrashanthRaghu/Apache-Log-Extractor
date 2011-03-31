# A simple python parser to extract the messages of different logging levels of Apache .
# Author : Prashanth Raghu 
# Git Hub Name : prashanthraghu


import sys

errors = {}

errortypes = ["emerg" , "alert" , "crit" , "error" , "warn" , "notice" , "info" , "debug"]

count = 0 

for errortype in errortypes:
	errors[errortype] = []

for file in sys.argv:
	
	if count == 0:
                count = 1
		continue; 			
	
	logfile = open( file , "r" )

	# Sort the errors 

	for log in logfile:
		for errortype in errortypes:
			if errortype in log:
				errors[errortype].append(log)
	count = count + 1
         


# Print them individually , better to write to a Database here !! preferably Sqllite !!
for errortype in errortypes:
	print errors[errortype]





