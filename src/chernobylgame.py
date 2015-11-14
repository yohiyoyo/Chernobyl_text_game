# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Roman"
__date__ = "$13-Nov-2015 3:46:08 PM$"

import time
import sys

# FUNCTIONS
def displayResource(fileName):
    "this loads and prints a resource"
    with open (fileName, "r") as myfile:
        data=myfile.read()
    print (data)
def menu():
   "this prints the menu with an input"
   return input("Welcome to the temp title. Please type in what you would like to do. \n \n"
      "To begin game: type in 'START' \n \n"
      "To Quit: type in 'QUIT' or 'EXIT' \n \n"
      "For Help/instructions: type in 'HELP' \n \n >>")
      
def help():
    "this prints the help"
    print ("hey")


def gameIntro():
    "This print the intro"
    print("the sign will forever be ingrained in your memory. The end of the road, but also the beginning.")
    displayResource("C:\\Users\\Roman\\Documents\\NetBeansProjects\\ChernobylGame\\src\\resources\\pripyat.txt")
    print ("Pripyat 1970")
    cls()
    
    print("Just 2 months ago, you were invited by the Department of Nuclear energy")
    return;

def cls():
    "this clears the screen"
    jump = 0
    for jump in range(0,100):
        print ("\n")
        jump = jump+1
        
        
        
        

menuInput = menu().lower()

if menuInput == ("start"):
    print("Game begins in : \n")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    cls()
    gameIntro()
elif menuInput == "quit" or menuInput == "exit":
    confirmInput = input("Are you sure? Y/N")
    if confirmInput == ("Y"):
        sys.exit()
elif menuInput == "help":
    help()
elif menuInput == "dev": #bypasses the start counter
    gameIntro()
    
    
