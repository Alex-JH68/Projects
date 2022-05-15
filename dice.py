from pickle import STRING
import random
import csv
from tokenize import String
import pymongo 
from pymongo import MongoClient, mongo_client
import pandas as pd


def check_input(input_num):
    if input_num in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]:
        return int(input_num)
       

def check_input_dice(input_num):
    if input_num in ["4","6","8","12","20"]:
        return int(input_num)

#------------------------------MENU---------------------------------------------------------------------
def print_menu():
    print("------------------------")
    print("   [ Dice Simulator ]  ")
    print("please select a number")
    print("(1): Roll a Dice")
    print("(2): Check Last Roll")
    print("(3): Upload Last File to Server")
    print("(4): Delete all Logs")
    print("(5): Quit")
    print("------------------------")

while True:
    print_menu()
    
    option = input(">>>")
    #--------------------- OPTION 1 -------------------------------------------------------------------------------
    if option == "1":
      
        
        
        dice_sides = ""

        while dice_sides not in ["4","6","8","12","20"]:
            dice_sides = input("Select your dice[tetrahedron(4),cube(6),octahedron(8),dodecahedron(12),icosahedron(20)]:")
            if dice_sides in ["4","6","8","12","20"]:
                break                 
            else:
                print("Please select a Valid Dice")

        dice_face = check_input_dice(dice_sides)

        
        class dice: # create a class to roll inputed value
            def roll(self):
                n = random.randint(1,int( round(float(dice_face))))
                return n     

        dice_num_input = ""

        while dice_num_input not in  ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]:
            dice_num_input = input("Select the number of dice you wish to roll [1~20]:")  #inputting the number of die to throw
            if dice_num_input in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]:
                break
            else:
                print("Please Select a Valid Integer[1~20]")

        dice_num = check_input(dice_num_input) #result for the number of die rolled

        dice_throw = dice()

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

        print("------------------------------------------")

        if dice_num in range(   int( round(float(dice_num))) +1) and dice_num != 0: #conditional catchall statement
            print("You have rolled",dice_list,"giving you a total of",dice_sum)
        else:
            quit
  
  # write to a CSV file   

        dice_str=[str(int) for int in dice_list]   #
        dice_result=','.join(dice_str)             #Join the dice results together
        dice_results= ''.join(dice_result)         # 
        dice_type = "a"
        
        if dice_face == 4:
            dice_type = dice_type.replace("a","Tetrahedral")
        elif dice_face == 6:
            dice_type = dice_type.replace("a","Cubic")
        elif dice_face == 8:
            dice_type = dice_type.replace("a","Octahedral")
        elif dice_face == 12:
            dice_type = dice_type.replace("a","Dodecahedral")
        elif dice_face == 20:
            dice_type = dice_type.replace("a","Icosahedral")
            
        dice_total=str(dice_sum)

        dice_score=[dice_num,dice_results,dice_total,dice_type]


        if dice_num in range(   int( round(float(dice_num))) +1) and dice_num != 0:

            with open("./dice_log.csv","w") as file: #create the file as dice_log.csv
                header = ["number of dice","dice results","total score","dice type"]
                write = csv.DictWriter(file, fieldnames=header, lineterminator='\n')
                write.writeheader() #write the header
                dice_field=dict(zip(header,dice_score))
                write.writerow(dice_field) #write the score to file
                
                #read the newly created csv file
            with open("dice_log.csv") as file:
                reader = csv.reader(file) 
                for row in reader:
                    print(row)
        print("------------------------------------------")
        print("Results have been written to .csv")
        pressenter = input("Press Enter to Continue>>>")
    #---------------------------------OPTION 2-------------------------------------------------------------- 
    elif option == "2":
        with open("dice_log.csv") as file:
            reader = csv.reader(file) 
            for row in reader:
                print(row)
        dedinput=input("Press Enter to Return to Menu>>>")
    elif option == "3":
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
            
            deadinput= input("Press Enter to Continue>>>")
        if __name__ == "__main__":
            mongodb = MongoDB(dBName='Dataset',collectionName='dicelogs')
            mongodb.InsertData(path="dice_log.csv")

    elif option == "4":
        client = MongoClient("localhost", 27017, maxPoolSize=50)
        DB= client.get_database('Dataset')
        collection=DB.get_collection('dicelogs')

        res = collection.delete_many({})
        del_count=res.deleted_count
        print("Number of Entries Deleted: {}".format(del_count))
        input("Please press Enter to Continue>>>")


    elif option == "5":
        break
    else:
        print("Please choose a valid option")