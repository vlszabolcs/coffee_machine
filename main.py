from coffee_types import coffeeTypes
from machine import machine_state
from tqdm import tqdm
import time


x=0

def itemRead(userInput):

    global item_name
    global item_water
    global item_coffee
    global item_milk
    global item_cash

    item_name = userInput["name"]
    item_water = int(userInput["water"])
    item_coffee = int(userInput["coffee"])
    item_milk = int(userInput["milk"])
    item_cash = int(userInput["price"])

def machinePrint():
    print(f"water  : ",machine_state["water"],"ml")
    print(f"coffee : ",machine_state["coffee"],"g")
    print(f"milk   : ",machine_state["milk"],"ml")
    cash= machine_state["penny"]*1+machine_state["nickel"]*5+machine_state["dime"]*10+machine_state["quarter"]*25
    print(f"cash    : ",cash,"$")
    return 0

def preChechk():
    userchoice=int(input("What would you like? ( espresso (0) / latte (1) / cappuccino (2) ): "))

    if userchoice == 4 :
         return 3
    
    itemRead(coffeeTypes[userchoice])
    error=""

    if (machine_state["water"] -item_water)>=0:
       machine_state["water"]-=item_water
    else:
        error="water"
    
    if (machine_state["coffee"]-item_coffee) >=0:
        machine_state["coffee"]-=item_coffee
    else:
        error= error+" coffe"
    
    if (machine_state["milk"]-item_milk)>= 0:
        machine_state["milk"]-=item_milk
    else:
        error += " milk"
    
    if error != "":
        print(f"Sorry there is not enough ", error, " in the machine for the ", item_name)
        return 4
    else:
        return 1
       
def pay():
    needCoin = item_cash
    firstRun=True

    while needCoin > 0:

        if firstRun :
            coIN=int(input("Your "+ str(item_name)+" is " +str(item_cash)+"$ ! Pleas pay with 1, 5, 10, 25 coin here -->> "))
           
            firstRun=False
        else:
            coIN=int(input(f"Insert: "+ str(needCoin) + " -->> "))

        while coinCounter(coIN) :
            coIN=int(input("Pleas pay with 1, 5, 10, 25 coin -->> "))
            
        needCoin-=coIN
            
    if needCoin != 0:
        print(f"Here the exchange: ", abs(needCoin))

    return 2

def coinCounter(coins):
    match coins:
        case 1:
            machine_state.update({"penny": +1})
            return False 
        case 5:
            machine_state["nickel"]+=1
            return False
        case 10:    
            machine_state["dime"]+=1
            return False
        case 25:
            machine_state["quarter"]+=1
            return False
        case _:
            return True

def makeCoffee():
    for i in tqdm (range (item_water), 
               desc="Loading…", 
               ascii=False, ncols=80):
        time.sleep(0.01)
      
    print("Complete.")
    return 4

def saveData():
    machine_state.update({"water": machine_state["water"]})
    return 0

while True :
        match x:
            case 0:
                x=preChechk()
            case 1:
                x=pay()
            case 2:
                x=makeCoffee()
            case 3:
                x=machinePrint()
            case 4:
                x=saveData()
   
        