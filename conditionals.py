import time

temperature = str(input("Enter a number between 0 and 120: "))

#if
if (temperature <= 4):
	print("water is solid")

elif (temperature < 100):
	print("water is a liquid")

elif (temperature < 120):
	print(Number is invalid)
else:
	print("Water is a vapor")
time.sleep(3)
