import random

# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Haft Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    #print(currentGasLevel)
    return currentGasLevel
# Variable calls the value of gasLevelGauge Function
gasLevelIndicator = gasLevelGauge()

# Create If-ELIF-ELSE statements using the comparative Operator == Equal to in order to display gas level messages to display gas level messages
def gasLevelAlert():
    if gasLevelIndicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***\nCalling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("***WARNING***\nYour gas tank is extremely LOW\nThe closest gasoline station is")
    elif gasLevelIndicator == "Quarter Tank":
        print("You are on a QUARTER TANK of gas\nStart planing a visit to the gas station!!!")
    elif gasLevelIndicator == "Haft Tank":
        print("You are on a HAFT TANK of gas\nYou have 125 more miles to empty!!!")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("You are on a THREE QUARTER TANK of gas\nYou have 205 more miles to empty!!!")
    else:
        print("You have a FULL TANK of gas, Congratulations.\nYou have 310 more miles to empty!!!")


 # Call Functions Here
gasLevelGauge()
gasLevelAlert()