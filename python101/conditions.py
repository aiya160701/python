#number = int(input("Please enter a number; "))

#x = 5

#if x < number:
 #   print(x, "is greater than" , number)
#else:
 #   print(x , "is less than" , number)

#name = input("Please enter your name: ")

#if name == "Aiya" or name == "Hamid": 
    #print("You are welcome")
#elif name == "Simon":
    #print("You are perfect boy" , name )
#else:
    #print ("You are not allowed")

# number = int(input("Please enter a number: "))
# x = 5

# if x > number:
#     print(x, "is greater than", number)
# else:
#     print(x, "is less than", number)

name = input("Please enter your name: ")
age = input("Enter your age: ")

age_limit = 21

if name == "Aiya" and int(age) >= age_limit:
    print("You're welcome to drink", name)

elif name == "Simon":
    print("You are banned", name)
    
else:
    print("You are too young")