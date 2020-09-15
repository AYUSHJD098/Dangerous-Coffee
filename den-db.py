# Dengerous-Coffee(Image/File-Encrpter)-v0.1 2020
#Python: v3.7(Windows 10 x64 build)
#This Software Uses Sqlite(command-line)-Database ,
# to safely store the Data Of your choice.
#It Stores Data in Bianary form.
#This prevents to leak data if our Data data is intercepted,
# In Travel/Movement.
#Author : Ayush Jadhav , Contact : Jadhavayush1100@gmail.com
# Feel Free to Ulter the script as you  like (credit will be appreciated)

#Importing 
import sqlite3
from sys import exit

# Start/Stop swicth for computer 
program_is_running = True

#Data Object
class DataObject:
    def __init__ (self, name, img ):
        self.name = name 
        self.img = img

    @staticmethod
    def connect():
        #Say hello to conney! 
        #Conney will help us Communicate With Our Database, This connects Our DataBase
        conney  = sqlite3.connect('coffee.db')

        #Createing Cusror For Our Database
        #DataBase named img will be saved in same directory as your executable file!
        cur = conney.cursor()

        #This Aleart  That Our Database is coneccted !!!
        print("Database Connected succesfully!")
        return conney, cur

    def convert_bianary(self):
        #Opening the Image
        with open(self.img,'rb')  as f:
            bianary_img = f.read()
            return bianary_img

    def  create_tables(self):
        #Createing Tables and Columns For Our DataBase(img.db)
        # Create table 
        cur.execute('''CREATE TABLE img90
             (name text, img blob)''')
        conney.commit()

    def add_data(self , bianary_img, cur, conney):
        #Adding image and Name to DataBase!
        img_db = f"INSERT INTO img90  (name,img) Values (?,?) "
        data = (self.name, bianary_img)
        cur.execute(img_db, data)
        conney.commit()

#Menu
print("Menu-(Dengreous-Coffee)")
print('*' * 50)
print("Type [1] to post/input data")
print("Type [2]  to retrive data")
print("Type [3] to exit ")
print('*' * 50)
action = int(input("Enter Number for your choice command >>>")) 

while action != 3:

    #writeing data
    if action == 1 :
        

        name = input("Enter the name you want the file to be stored as in DataBase >>>>")
        img = input("Enter The location of File(ex: D:\images\img.png) >>>>")
        
        try:
            #making object
            dota = DataObject(name, img)

            #making connection
            conney , cur = dota.connect()

            #Creating table if you use this script 2nd time then you would have to comment this  command :0
            # dota.create_tables()
        except:
            print("Connection was unable to be established !", sqlite3.Error)
            print("Press ctrl+c to exit")
        #converting data to binary 
        bianary_img = dota.convert_bianary()


        try:
            #Adding data 
            dota.add_data(bianary_img,cur,conney)
            print("Data Added succesfully")
        except:
            print("Adding Data was unsuccessful")

        #Conney will save our changes with this command And closes the database
        conney.commit()
        cur.close()
        conney.close()
        break
    
    #REtriving data
    if action == 2: 
        #Conney will help us Communicate With Our Database, This connects Our DataBase
        conney  = sqlite3.connect('coffee.db')

        #Createing Cusror For Our Database
        #DataBase named img will be saved in same directory as your executable file!
        cur = conney.cursor()

        #This Aleart  That Our Database is coneccted !!!
        print("Database Connected succesfully!")
       
       # Querys Data base for Data
        sql_select_Query = cur.execute("select * from img90")
        for row in sql_select_Query:
            print(row[0])
            rsv_data = row[1]
        
        fn = input("input the name of data you wanna retrive and add a appropriate extention if not available>> ")
        with open(f"{fn}",'wb') as f:
            f.write(rsv_data)

    #Exiting
    if action == 3:  
        print("Exiting...")    
        break