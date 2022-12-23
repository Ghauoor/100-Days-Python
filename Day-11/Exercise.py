import time

name = input("Enter your Name : ")
# date =
timestamp = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
print(timestamp)
if hour < 12:
    print("Good Morning,", name)
elif 12 <= hour < 17:
    print("Good Afternoon,", name)
elif 17 <= hour < 20:
    print("Good Evening,", name)
else:
    print("Good Night,", name)
