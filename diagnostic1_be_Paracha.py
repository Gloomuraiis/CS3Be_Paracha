earth_weight = int(input())
destination = input()

if destination == "mars":
    mars_weight = earth_weight * 0.38
    print("{mars_weight} (You weigh a lot less!)")
if destination == "jupiter":
    jupiter_weight = earth_weight * 2.34
    print("{jupiter_weight} (You weigh much more!)")
elif destination == "moon":
    moon_weight = earth_weight * 0.16
    print("{moon_weight} (You are as lght as a feather!)")
return 

