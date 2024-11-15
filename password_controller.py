def Password_controller(password):
  length = len(password)
  if length > 8:
    return ("Password succesfully set")
  else:
    return ("Password have to be more than 8 characters")


password = input("Enter your password: ")
result = Password_controller(password)
print (result)
