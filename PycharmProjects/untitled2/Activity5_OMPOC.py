cgpa = raw_input("Enter current cumulative GPA: ")
takencred = raw_input("Enter number of taken credits: ")
currentcred = raw_input("Enter number of current credits: ")
target = raw_input("Enter target cumulative GPA: ")

currentGPA = (float(target)*(float(takencred) + float(currentcred)) - float(cgpa)*float(takencred))/float(currentcred)
print ("The GPA of the current semester needed to achieve is: ", currentGPA)