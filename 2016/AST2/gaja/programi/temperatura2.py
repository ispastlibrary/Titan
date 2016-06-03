#! /usr/bin/python3
#-*-coding: utf-8 -*-
# converts temperature to Fahrenheit or Celsius

import os
import time
 
def print_options():
    os.system('clear')
    print("Options:")
    print(" 'p' print options")
    print(" 'c' convert from Celsius")
    print(" 'f' convert from Fahrenheit")
    print(" 'q' quit the program")
 
def celsius_to_fahrenheit(c_temp):
    return 9.0 / 5.0 * c_temp + 32
 
def fahrenheit_to_celsius(f_temp):
    return (f_temp - 32.0) * 5.0 / 9.0
 
choice = "p"
while choice != "q":
    if choice == "c":
        c_temp = float(input("Celsius temperature: "))
        print("Fahrenheit:", celsius_to_fahrenheit(c_temp))
        choice = input("option: ")
    elif choice == "f":
        f_temp = float(input("Fahrenheit temperature: "))
        print("Celsius:", fahrenheit_to_celsius(f_temp))
        time.sleep(5)
        print_options()
        choice = input("option: ")
    elif choice != "q": #Alternatively choice != "q": so that print when anything unexpected inputed
        os.system('clear')
        print_options()
        choice = input("option: ")
