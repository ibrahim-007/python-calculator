def cal(x, y):
  while True:  
    choice = input("Enter Choice ")
    ans = 0
    if choice.__eq__("+"):
        ans = x + y
        return ans
    elif choice.__eq__("-"):
        ans = x - y
        return ans
    elif choice.__eq__("*"):
        ans = x * y
        return ans
    elif choice.__eq__("/"):
        if y != 0:
          ans = x / y
          return ans
        else:
           print("Cannot divide by zero: ")
           return False
    else:
        print("Wrong input try again")

def runit():   
  while True:
     try:
         num1 = int(input("Enter First Number: "))
         num2 = int(input("Enter Second Number: "))
     except ValueError:
          print("Invalid number! Please enter Integers only.")
          continue
   
     result = cal(num1,num2)
     if result is not False:
      print("Result ", result)

     newCal = input("Would you like to do another calculation? (y/n)").strip().lower()
     if newCal.__eq__("y"):
      continue
     elif newCal.__eq__("n"): 
      break    
runit()
 