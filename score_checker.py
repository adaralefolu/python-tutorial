print ("Welcome to score checker!!")
input_score = input ("Enter score: ")

try:
  score = float (input_score)
except ValueError:
  print ("Bad score. Enter decimal number")
  quit ()

if score >= 0.0 and score <= 1.0:
  
  if score >= 0.9:
    print ("Your grade is A")
  
  elif score >= 0.8:
    print ("Your grade is B")

  elif score >= 0.7 :
    print ("Your grade is C")

  elif score >= 0.6 :
    print ("Your grade is D")

  elif score < 0.6 :
    print ("Your grade is E")

  else:
    print ("Your grade is F")

else:
  print ("Bad score")
