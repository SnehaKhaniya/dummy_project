import datetime

current_time = datetime.datetime.now()
print(current_time)
hour = current_time.hour
print(hour)

if(hour >= 0 and hour <= 3):
    print("GOOD NIGHT")
elif(hour <= 11):
    print("GOOD MORNING")
elif(hour <= 16):
    print("GOOD AFTERNOON")
else:
    print("GOOD EVENING")
