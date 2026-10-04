# Write a program to input temperature and classify it:
# • Above 30°C → Hot
# • Between 15°C–30°C → Warm
# • Below 15°C → Cold


temp = int(input("Enter temperature: "))

if temp > 30:
    print("Hot")
elif temp >= 15:
    print("Warm")
else:
    print("Cold")