"Auhor: Dennis Ebisintei"
"License: MIT"
"The code below is free to modify"


#conditional statements
# if, elif, else
#Temperature:
# below 50 degrees cold, 
# above 50 degrees warm
#30 degrees very cold
#20 degrees very very cold
#10 degrees snow
#1 degrees Freezing point

#Hot Temperature
#40 Degrees = warm
#50 Degrees = Hot
#60 Degrees = Very Hot
#70 Degrees = Very Very Hot
#80 Degrees = Extremely hot
#90 Degrees = Very Extremely hot
#100 Degrees = Boiling point

#Temperature Advisor
print("Temperature Avisor")
print("Welcome to the temperature Advisor")
print("")
print("       #####List of useful commands#####")
print("       quit- to quite the program type: 150")
print("       Enter between 1 and 100 to get an advice on the temperature unit of your location")
print("")


temperature = ""
while temperature != "quit":
    print("")
    print("Enter temperature Unit below: Note The unit should be in integer")
    # temperature = int(input(">"))
    try: # To catch errors in input
        temperature = int(input(">"))
        if temperature < 10:
            print("Temperature: Temperature is at freezing point")
            print("Advice: Please Get out of there Now.")
        elif temperature < 20:
            print("Temperature: It's Very Very cold")
            print("Advice: Dod't remove your blankets and stay close to a fire")
        elif temperature < 30:
            print("Temperature: Its cold, were war,m cloths")
            print("Advice: Don't Drink cold water")
        elif temperature < 35:
            print("Temperature: Temperature is neutral")
            print("Advice: You can eat both cold or warm foods")
        elif temperature < 40:
            print("Temperature: Temperature is Hot")
            print("Advice: Drink only a cup of water")
        elif temperature < 50:
            print("Temperature: Temperature is Hot")
            print("Advice: Drink At least 2 cups of water")
        elif temperature < 60:
            print("Temperature: Temperature is very Hot")
            print("Advice: Were Light Cloths")
            print("Advice: Drink at least 3 cups of water every 2 hoours of work")
            print("Advice: This will reduce the rate of fatigue by 20 percent")
        elif temperature < 70:
            print("Temperature: The Temperature is very Hot")
            print("Advice: The Temperature is not favourable for your skin")
            print("Advice: The only way to survive in this location is to put on a coated suit.")
        elif temperature < 80:
            print("Temperature: The Temperature is Extremely high and near boiling point")
            print("Advice: Don't Take of your coated suit. The maximum time you can spend in this location is 2 hours")
        elif temperature < 90:
            print("Temperature: Temperature is at boling point")
            print("Advice: Please leave this location immediately")
            print("Advice: Don't Drink Any water. Drinking water will result to immediate exhaustation")
        else:
            print("You entered a wrong temeperature value try again")
        print("Thanks for using temperature advisor")
    except:
        print("Invalid input")
    
