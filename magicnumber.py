#!/usr/bin/env python

import sys,os

magicnum = 5
userpick = 0

def user_input():
   userpick = input("Enter the lucky number between 0 and 10: ")
   if userpick == 5:
      print("You picked the magic number")
      sys.exit()
   else:
      print("You couldn't pick the magic number, try again")

while (magicnum != userpick):
   user_input()
