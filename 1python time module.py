import time
if time.localtime().tm_hour <= 5:
    print("Good morning, sir!")
elif time.localtime().tm_hour <= 12:
    print("Good afternoon, Sir!")
elif time.localtime().tm_hour <= 17:
    print("Good evening, sir!")
elif time.localtime().tm_hour <= 21:
    print("good time huh")
else:
    print("Good night, sir!")
# This code will print the time of day based on the current hour.