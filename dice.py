import random
import csv
import pymongo 
from pymongo import MongoClient, mongo_client
import pandas as pd
import json


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# set up a class/object to roll a number between 1~6
class dice:
    def roll(self):
        n = random.randint(1,6)
        return n
dice_throw=dice()
roll_num = int(dice_throw.roll()) # our dice result


def check_input(input_num):
    if input_num in ["1","2","3","4","5","6"]:
        return int(input_num)
    else:       
        print("Please enter an integer from 1 to 6.")
        return 0

# check if the number inputted is a valid dice integer        
dice_num_input = input("Select the number of dice you wish to roll [1-6]:")  #inputting the number of die to throw

dice_num = check_input(dice_num_input) #result for the number of die rolled


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////
#create a function using the input of the roll number and create a list of dice results.

def rolling(n):    
    roll_list = []
    if  dice_num in range(   int( round(float(dice_num))) +1) and dice_num != 0:
        for i in range(n):
            roll = int(dice_throw.roll())
            roll_list.append(roll)
        return roll_list
    else:
        return []

dice_list=rolling(dice_num)    #list of dice rolls

dice_sum=sum(dice_list)  #sum of dice rolls

if dice_num in range(   int( round(float(dice_num))) +1) and dice_num != 0: #conditional catchall statement
    print("You have rolled",dice_list,"giving you a total of",dice_sum)
else:
    quit


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#writing our file to csv

dice_str=[str(int) for int in dice_list]   #
dice_result=','.join(dice_str)             #Join the dice results together
dice_results= ''.join(dice_result)         # 
dice_total=str(dice_sum)

dice_score=[dice_results,dice_total]


if dice_num in range(   int( round(float(dice_num))) +1) and dice_num != 0:

    with open("./dice_log.csv","w") as file: #create the file as dice_log.csv
        header = ["dice results","total score"]
        write = csv.DictWriter(file, fieldnames=header, lineterminator='\n')
        write.writeheader() #write the header
        dice_field=dict(zip(header,dice_score))
        write.writerow(dice_field) #write the score to file
    
    #read the newly created csv file
    with open("dice_log.csv") as file:
        reader = csv.reader(file) 
        for row in reader:
            print(row)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Import the csv data to a mongoDB DataBase
if dice_num in range(   int( round(float(dice_num))) +1) and dice_num != 0:
    class MongoDB(object):
        def __init__(self, dBName=None, collectionName=None):
            self.dBName=dBName
            self.collectionName=collectionName

            self.client = MongoClient("localhost", 27017, maxPoolSize=50)
            self.DB = self.client[self.dBName]
            self.collection = self.DB[self.collectionName]
        def InsertData(self,path=None):
            df=pd.read_csv(path)
            data=df.to_dict('records')
            self.collection.insert_many(data,ordered=False)
        
            print("Dice data has been exported to MongoDB")
    if __name__ == "__main__":
        mongodb = MongoDB(dBName='Dataset',collectionName='dicelogs')
        mongodb.InsertData(path="dice_log.csv")
