print ("Welcome to My Burger Shop")

try:
  size = input ("What size burger do you want? M, N, or L: ").strip().upper()
  while size not in ["M", "N", "L"]:
        print("Invalid choice. Please choose either M, N, or L.")
        size = input("What size burger do you want? M, N, or L: ").strip().upper()
except Exception as e:
  print("An error occurred:", e)


try:
  add_mushroon = input ("Do you want mushroom? Y or N: ").strip().upper()
  while add_mushroon not in ["Y", "N"]:
        print("Invalid choice. Please choose either Y or N.")
        add_mushroon = input("Do you want mushroom? Y or N: ").strip().upper()
except Exception as e:
  print("An error occurred:", e)


try:
  extra_cheese = input ("Do you want extra cheese? Y or N: ").strip().upper()
  while extra_cheese not in ["Y", "N"]:
        print("Invalid choice. Please choose either Y or N.")
        extra_cheese = input("Do you want extra cheese? Y or N: ").strip().upper()
except Exception as e:
  print("An error occurred:", e)



bill = 0

if size == "M":
  bill += 5
elif size == "N":
  bill += 8
else:
  size == "L"
  bill += 10


if add_mushroon == "Y":
  size == "L"
  bill += 2
else:
  bill += 1


if extra_cheese == "Y":
  bill += 1



print (f"Your Final Bill Is {bill}")

