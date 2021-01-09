listOfOperands = ['+' , '-' , '*' , '/', '%' , '=', 'd' , '^'] #List of operands used for if-else statement to compare the user input to this list to see if the input is a number or operator
myStack = [] #stack created so it can be displayed when 'd' is inputted.
result = 0 #defining result to use later
maxValue = 2147483647
minValue = -2147483648 # min and max value defined to ensure that the arithmetic is saturated
listOfNumbers = ['1' , '2', '3', '4' , '5' , '6', '7', '8', '9', '0']

print ("You can now start interacting with the SRPN calculator")

# function that checks if the user input is in infix notation or not
def isInfix(userIn):
  for i in range(len(listOfOperands)):
    if listOfOperands[i] in list(userIn):
      for j in range(len(listOfNumbers)):
        if listOfNumbers[j] in list(userIn):
          return True
  return False

# function that checks whether an input contains special characters or not
import re
def checkIfSpecial(userIn):
    string_check= re.compile('[@_!#$&()<>?\|}{~:]')
    if(string_check.search(userIn) == None):
        return False
    else:
        return True

# function that check whether the user input contains only letters or not
def checkIfLetters(userIn):
  if str.isalpha(userIn):
    return True

#function to ensure the arithmetic is saturated
def saturation(result):
  if (result >= maxValue):
    return maxValue
  if (result <= minValue):
    return minValue
  return result

#function that will return true if there is less than 2 elments in the stack.
def stackUnderflow(userIn):
  for c in listOfOperands:
    if (c == userIn):
      return len(myStack) < 2
  return True

#function that will return true if there is more than 23 items in the stack.
def stackOverflow (userIn):
  for c in listOfOperands:
    if (c == userIn):
      return len(myStack) > 23
  return True

#main while loop where all the calculations are done.
while (True):
  userIn = input() #to allow for user input
  inputIntoCharacters = list(userIn)
  userInputList = userIn.split(' ')
  if (userIn == ""): # if the user presses enter without inputting anything, then program won't crash due to this.
    pass
  else:
      if (isInfix(userIn) ==  True and inputIntoCharacters[0] != "-"): #if infix, then does calculations in the following way. This infix only works using single digit numbers.
        if (userIn == "="):
          print(myStack[-1]) # when user inputs '=' stack is printed.
        for k in range(len(userIn)):
          if inputIntoCharacters[k] not in listOfOperands:
            myStack.append(inputIntoCharacters[k]) #adds the numbers into the stack
        for l in range(len(inputIntoCharacters)):
          if inputIntoCharacters[l] in listOfOperands:
            position = l
            #finds the position of the operator in the string.
        #shows what to do with each operator.
        if (inputIntoCharacters[l - 1] == "+"):
          result = int(int(myStack[0]) + int(myStack[-1]))
        elif (inputIntoCharacters[l - 1] == "-"):
          result = int(int(myStack[0]) - int(myStack [-1]))
        elif (inputIntoCharacters[l - 1] == "*"):
          result = int(int(myStack[0]) * int(myStack [-1]))
        elif (inputIntoCharacters[l - 1] == "/"):
          result = int(int(myStack[0]) / int(myStack [-1]))
        elif (inputIntoCharacters[l - 1] == "%"):
          result = int(int(myStack[0]) % int(myStack [-1]))
        elif (inputIntoCharacters[l - 1] == "^"):
          result = int(int(myStack[0]) ** int(myStack [-1]))
        myStack.remove(myStack[-1]) # at the end of the operation, the two numbers are removed from the stack and the result is added to the stack.
        myStack.remove(myStack[-1])
        myStack.append(result)
      else:
        if ("d" in userIn):
              print(*myStack, sep = "\n") #if 'd' is inputted then the stack is printed with each element on a different line
        if (inputIntoCharacters[0] == "#" and inputIntoCharacters[1] == " " and inputIntoCharacters[-2] == " " and inputIntoCharacters[-1] == "#"):
          pass # if a comment is inputted by the user then the program ignores it and does not attempt to use equations on th ecomment.
        else:
          if (userIn == "d"):
            pass
          elif (checkIfLetters(userIn) == True or checkIfSpecial(userIn) == True or " " in userIn):
            for i in range(len(inputIntoCharacters)):
              print("Unrecognised operator or operand \"%s\"." % inputIntoCharacters[i])
              #if a letter or special character that is not d and not an operand then the program prints this for each character.
          else:
            if (userIn not in listOfOperands): #checks the list of operands to see if the user has inputted a number or not.
              myStack.append(userIn) #if the input is not an operand then it is added to the stack
            else:
              if(userIn == "="):
                print (myStack[-1]) #result is the last element in the stack so to print the result when '=' is inputted then we have to print the last element in the stack.
            #print(myStack)
              else:
                if (stackUnderflow(userIn) and userIn in listOfOperands):
                  print("Stack underflow.") #calls stackUnderflow function, if it returns true then there is a stack underflow which will be outputted.
                  #myStack.remove(userIn)
                elif (stackOverflow(userIn) and userIn in listOfOperands):
                  print("Stack overflow.") #calls stackOverflow function, if it returns true then there is a stack overflow which will be outputted.
                  #myStack.remove(userIn)
                else: #else used to tell the program what to do for each operand inputted. The last 2 numbers in the stack are used. These 2 numbers are then removed from the stack and the result is added to the stack.
                  if(userIn == "+"):
                    result = int(myStack[-2]) + int(myStack[-1])
                  elif(userIn == "-"):
                    result = int(myStack[-2]) - int(myStack[-1])
                  elif(userIn == "*"):
                    result = int(myStack[-2]) * int(myStack[-1])
                  elif(userIn == "/"):
                    if (int(myStack [-1]) == 0):
                      print ("Divide by 0.") # if the denominator is zero then this error is printed.
                    else:
                      result = int(int(myStack[-2]) / int(myStack[-1]))
                  elif(userIn == "%"):
                    result = int(myStack[-2]) % int(myStack[-1])
                  elif(userIn == "^"):
                    result = int(myStack[-2]) ** int(myStack[-1])
                  myStack.remove(myStack[-1])
                  myStack.remove(myStack[-1])
                  myStack.append(saturation(result))
