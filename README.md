# Project-Dice Simulator

This project involves rolling a different amount of dice, writing the results to csv, and uploading it to a server.

##Technologies used

* Python
* csv
* pymongo

# Features

* Able to select 1~6 dice and roll them
* Import the results from csv to a database
* delete all stored dice roll data on the database 

Features still needed for a more complete program:

* ability to input more than just 6-sided die
* implementing more dice to roll instead of just 6.
* selectively updating and replacing specific rolls on mongoDB

Handles only valid inputs:
* cannot put in non-negative integers
* cannot put in string values that are non-numeric
* cannot put in decimal, floating or irrational numbers
