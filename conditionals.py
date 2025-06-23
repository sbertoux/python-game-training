to_user = "Pick a number.  Any number."
result = input(to_user)
result_num = int(result)
result_type = type(result_num)
print ('Your number is ', result_num)
if result_num < 0:
    print("the number is negative.")
elif result_num == 0:
    print("Your number is 0")
else:
    print("your number is positive")


count = 5 
while count >0 :
    print(count)
    count = count - 1


guess = 3
num = input('guess a number between 1 and 5 ')
int_num = int(num)
while guess != int_num: 
    print ("guess again")
    num = input('try another number between 1 and 5 ')
    int_num = int(num)
else:
    print("you did it!")
    
    






