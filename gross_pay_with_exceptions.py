hour = input ("Enter Hours: ")

try:
  hour = float (hour)
except ValueError:
  print ("Error, please enter numeric input for hour")
  quit ()
  
rate = input ("Enter rates: ")

try:
  rate = float (rate)
except ValueError :
  print ("Error, please enter numeric input for rate")
  quit ()


if hour < 40:
  pay = round (hour*rate,2)
else:
  overtime = hour - 40
  pay = round (40 * rate + overtime * rate * 1.5, 2)

print (f" pay : {pay}")

