#!/usr/bin/env python

print "--- Program to conver age into seconds ---"

'''
   Age = Years
   1 Day = 24(hours) * 60(minutes) * 60(seconds)
   1 Month = 24 * 30(days) * 60 * 60
   1 Year = 365(days) * 24 * 60 * 60
   Age in Seconds = Age * 365 * 24 * 60 * 60
'''   

def calcage():
   user_input = input("Enter your age in years: ")
   user_choice = input("Do you wish your age in days (d) OR seconds (s)?: ")
   if user_choice == "d":
     print("Your age in days is {} ".format(int(user_input) * 365))
   elif user_choice == "s":
     print("Your age in seconds is {} ".format(int(user_input)*365*24*60*60))
   else:
     print("You must have entered an invalid choice")

calcage()
