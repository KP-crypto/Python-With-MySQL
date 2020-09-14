import mysql.connector as connector

class DBHelper:
     ######## Initilize Class Constructor #################
    def __init__(self):
        self.con=connector.connect(host='localhost',port=3306,user='root',password='********',database='pythontest')
        query="create table if not exists user(userid int primary key,username varchar(20),salary int)"
        cur=self.con.cursor()
        cur.execute(query)
        print("table created successfully")
        
      

    ########## Insert Records Into Table ######################

    def insert_user(self,userid,username,salary):
        query = "insert into user(userid,username,salary) values({},'{}',{})".format(userid,username,salary)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('Records saved into table')
        cur.close()
        self.con.close()

  #################  Fetch User Records ##################


    def fetch_user_record(self):
        query="select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)
       cur.close()
        self.con.close()

################### Update User ######################

    def updte_user(self,userid,newname,newsalary):
        query="update user set username='{}',salary={} where userid={}".format(newname,newsalary,userid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Record updated successfully")
        cur.close()
        self.con.close()


############## Delete User ##################################
    def delete_user(self,userid):
        query="delete from user where userid={}".format(userid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user deleted successfuly")
        cur.close()
        self.con.close()

########  Main Programme Starts here ##################

helper=DBHelper()
#helper.insert_user(2,'Deepti',16000)
#helper.insert_user(3,'Suresh',18000)
#helper.insert_user(4,'Jayshree',19000)
#helper.insert_user(5,'Gauri',15000)
#helper.fetch_user_record()
#helper.updte_user(3,'jana',13000)
#helper.fetch_user_record()
#helper.delete_user(3)
helper.fetch_user_record()




