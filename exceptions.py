class JustNotCoolError(Exception):
  pass

x = 2
try:
  raise JustNotCoolError("This is not Cool")
  # raise Exception("I am a custom exception!")
  # print (x/0)
  # if not type(x) is str:
  #   raise TypeError("Only strings are allowed")
  
except NameError: 
  print("There is an Name error")
except ZeroDivisionError:
  print("End of the World! Why did you divide by zero")
except Exception as error:
  print(error)
else:
  print("No Error!")
finally:
  print("Always happen")



