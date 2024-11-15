print ("Welcome to Love Calculator")
name_1 = input ("Enter your name: ")
name_2 = input ("Enter lover's name: ")

combined_name = name_1 + name_2
lower_case_name = combined_name.lower()

t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

true = t + r + u + e

l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

print (f"{love_score}")

if love_score < str (10) or love_score >str (85):
  print (f"Your Love score is {love_score} you go together like coke and mentos")

elif love_score <= str (40) or love_score <= str (70) :
  print (f"Your Love score is {love_score} you are alright together")

else:
  print (f"Your Love score is {love_score}")
