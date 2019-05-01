import sys
import random
import json

# Command line parameters
number1= sys.argv[1] 
number2= sys.argv[2] 
number3= sys.argv[3]
number4= sys.argv[4]
number5= sys.argv[5]
number6= sys.argv[6]

# Input error check. We can accept only digits and avoild literals
if number1.isdigit() != True or number2.isdigit() != True or number3.isdigit() != True or number4.isdigit() != True or number5.isdigit() != True or number6.isdigit() != True:
  print ('Please enter digits only')
  print ('Exiting...')
  exit()

# Append the digits to a list
vol = [number1,number2,number3,number4,number5,number6]

def subtraction():
    # Convert the elements in vol to numbers
	int_vol = list(map(int, vol))
	
    # Print original values	
	print()
	print('Digits entered: ', int_vol)
	number = int(input("Enter value to subtract: "))
		
	# Subtract a value from each element in the list
	result = list() 
	for i in int_vol:
	  result.append(i - number)
	
	# Convert result to int and print it
	int_result = list(map(int, result))
	print('Digits after subtraction by ', number, ' are', int_result)
	print()
	menu()

def multiplication():
    # Convert the elements in vol to numbers
	int_vol = list(map(int, vol))
	
    # Print original values	
	print()
	print('Digits entered: ', int_vol)
	number = int(input("Enter value to multipy: "))
		
	# Subtract a value from each element in the list
	result = list() 
	for i in int_vol:
	  result.append(i * number)
	
	# Convert result to int and print it
	int_result = list(map(int, result))
	print('Digits after multiplication by ', number, ' are', int_result)
	# Create a dictioanary from int_vol and int_result
	dictionary = dict(zip(int_vol, int_result))
	print('Original and after multiplication values are saved to numbers.json')
	# Save the result to JSON file
	

	with open('numbers.json', 'w') as filehandle:
	  json.dump(dictionary, filehandle)
	print('Dictionary :', json.dumps(dictionary))
	print()
	menu()

def print_random_number():
  # Print random number from the list
  print()
  print('Random digit',random.choice(vol))
  print()
  menu()

def sort_lowest():
  # Print lowest to highest
  vol_sorted_lowest = vol
  vol_sorted_lowest.sort()
  print()
  print('Sorted list (lowest to highest):', vol_sorted_lowest)
  print()
  menu()

def sort_highest():
  # Print highest to lowest
  vol_sorted_highest = vol
  vol_sorted_highest.sort(reverse=True)
  print()
  print('Sorted list (highest to lowest):', vol_sorted_highest)
  print()
  menu()    

def menu():
    print("************MAIN MENU**************")
    #time.sleep(1)
    print()
	
    choice = input("""
      A: Perform subtraction and show output on screen comma separated.
      B: Perform multiplication and store result in a JSON file
      C: Pick randomly a number and show it on screen.
      D: Print sorted (highest to lowest) array/list numbers.
      E: Print sorted (lowest to highest) array/list numbers.
      Q: Quit/Log Out
      Please enter your choice: """)

    if choice == "A" or choice =="a":
        subtraction()
    elif choice == "B" or choice =="b":
        multiplication()
    elif choice == "C" or choice =="c":
        print_random_number()
    elif choice == "D" or choice == "d":
        sort_highest()
    elif choice == "E" or choice == "e":
        sort_lowest()
    elif choice == "Q" or choice == "q":
        sys.exit
    else:
        print()
        print("You must only select either A,B,C,D,E or Q.")
        print("Please try again")
        print()
        menu()
		
menu()
