
#Prompts the user for the number of Tests
#Note that this function will include call(s) to the input function
#Keep prompting until the number is an integer. 
#Returns the number of Tests
def getNumberOfTests():
    i=1
    while i == 1:
        try:
            numOfTests = int(input("Please enter number of tests."))
            i=0
            return numOfTests
        except:
            print("Invalid integer number.")
            i=1

#Prompts the user for the weigth of Assignments
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of assignments
def getWeightOfAssignments():
    i = 1
    while i == 1:
        try:
            assignmentWeight = float(input("Please enter weight of assignments."))
            if assignmentWeight >= 0 and assignmentWeight <= 1:
                i = 0
                return assignmentWeight
            else:
                print("Assignment weightage is not in range.")
                i = 1
        except:
            print("Invalid float number.")
            i = 1

#Prompts the user for the weigth of Midterms
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of midterms
def getWeightOfMidTerms():
    i = 1
    while i == 1:
        try:
            midtermWeight = float(input("Please enter weight of midterms."))
            if midtermWeight >= 0 and midtermWeight <= 1:
                i = 0
                return midtermWeight
            else:
                print("Midterm weightage is not in range.")
                i = 1
        except:
            print("Invalid float number.")
            i = 1

#Prompts the user for the weigth of the final
#Note that this function will include call(s) to the input function
#Keep prompting until the number is a float >= 0 and <= 1
#Returns the weight of final
def getWeightOfFinal():
    i = 1
    while i == 1:
        try:
            final = float(input("Please enter weight of final exam."))
            if final >= 0 and final <= 1:
                i = 0
                return final
            else:
                print("Final exam weightage is not in range.")
                i = 1
        except:
            print("Invalid float number.")
            i = 1

#returns True if the sum of the 3 arguments is 1, False otherwise
#Assign the default values 0.4 0.35 0.25 to wAssign, wMidtern and wFinal respectively
def checkWeights(wAssign = 0.4,wMidTerm = 0.35,wFinal = 0.25):
    total = wAssign + wMidTerm + wFinal
    if total == 1:
        return True
    else:
        return False


#calculate the numeric grade as specified in the course outline
def calculateNumericGrade(AvgAssignments,AvgTests,final,wOfAssign,wOfMidTerms,wFinal):
    calculate = AvgAssignments * wOfAssign + AvgTests * wOfMidTerms + final * wFinal
    return calculate

#convert the numeric grade to a letter according to the conversion table 
#in the course outline
def calculateLetterGrade(numericGrade):
    try:
        val = round(float(numericGrade))
        if val >= 0 and val <= 100:
            if val >= 90 and val <= 100:
                return 'A+'
            elif val >= 85 and val <= 89:
                return 'A'
            elif val >= 80 and val <= 84:
                return 'A-'
            elif val >= 77 and val <= 79:
                return 'B+'
            elif val >= 73 and val <= 76:
                return 'B'
            elif val >= 70 and val <= 72:
                return 'B-'
            elif val >= 67 and val <= 69:
                return 'C+'
            elif val >= 63 and val <= 66:
                return 'C'
            elif val >= 60 and val <= 62:
                return 'C-'
            elif val >= 57 and val <= 59:
                return 'D+'
            elif val >= 53 and val <= 56:
                return 'D'
            elif val >= 50 and val <= 52:
                return 'D-'
            else:
                return 'F'
        else:
            print('Numeric grade suppose to be between 0 - 100')
            return 0
    except:
        print('Not valid datatype')
        return 0


finalGrade= 0
avgAssignmentsGrade = 0
avgTestsGrade = 0
assignments = 0
midterms = 0
final = 0
#Repeat the last four lines if not equal to 1
check = 0
while check != 1:

        #Get the weight value of the assignments (call the appropriate function)
        assignments = getWeightOfAssignments()
        #Get the weight value of tests (call the appropriate function)
        midterms = getWeightOfMidTerms()
        #Get the weight value of the final (call the appropriate function)
        final = getWeightOfFinal()
        #Check the sum of weight values is 1 (call the appropriate function)
        check = checkWeights(assignments,midterms,final)
        if check != 1:
            print("Invalid total. Please insert weightage again.")


#Get the average grade obtained on the assignments
#Validate the input as a float between 0 and 100



i = 1
while i == 1:
        try:
            avgAssignmentsGrade = float(input("Please enter average assignments grades."))
            if avgAssignmentsGrade >= 0 and avgAssignmentsGrade <= 100:
                i = 0

            else:
                print("Average assignments grades are not in range.")
                i = 1
        except:
            print("Invalid float number.")
            i = 1


#Get the number of tests (call the appropriate function)

numberOfTests = getNumberOfTests()
#Prompt the user for each test grades and accumulate the value
#Validate the input as a float between 0 and 100
#Calculate the average test grade.

i = 1
while i <= numberOfTests:
        try:
            j = i
            testsGrade = float(input("Please provide Test "+ str(i) + " grade."))
            if testsGrade >= 0 and testsGrade <= 100:
                avgTestsGrade += testsGrade
                i += 1

            else:
                print("Test grades are not in range.")
                i = j
        except:
            print("Invalid float number.")
            i = j


avgTestsGrade = avgTestsGrade / numberOfTests



#Prompt and get the final grade
#Validate the input as a float between 0 and 100


i = 1
while i == 1:
        try:
            finalGrade = float(input("Please provide final grade."))
            if finalGrade >= 0 and finalGrade <= 100:
                i = 0

            else:
                print("Final grades are not in range.")
                i = 1
        except:
            print("Invalid float number.")
            i = 1

#Calculate and display the final numeric grade (call the appropriate function)
numericGrade = calculateNumericGrade(avgAssignmentsGrade,avgTestsGrade,finalGrade,assignments,midterms,final)
print("Your numeric grade is " + str(numericGrade))

#Calculate and display the final alphabetical grade (call the appropriate function)

print("Your letter grade is " + str(calculateLetterGrade(numericGrade)))