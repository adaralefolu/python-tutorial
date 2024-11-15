def format_name(f_name, l_name):
  if f_name.strip() == "" or l_name.strip() == "":
    return "Name or last name cannot be empty"

  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()

  return f"{formatted_f_name} {formatted_l_name}"

f_name = input("Enter First Name: ")
l_name = input("Enter Last Name: ")

output = format_name(f_name, l_name)
print (output)
