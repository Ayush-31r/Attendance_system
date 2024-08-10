                                                                                    #TOPIC : OFFICE ATTENDANCE AND DATABASE MANAGEMENT
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="THE_OFFICE")
cursor= mydb.cursor()                                                      #CREATION OF TABLES AND DATABASES

#cursor.execute("create table BIO_DATA(Emp_ID int(4) primary key,Post varchar(30) default 'clerk',Name varchar(20),DOB date,PH_NO varchar(20) not null,Email_ID varchar(250))")
table_create = "CREATE TABLE Attendance (EMP_ID INT(4) UNIQUE, Name CHAR(30))"
#cursor.execute(table_create)
print("                                                                           SETUP COMPLETE ")

                                                                                                   #CREATING A FUNCTION FOR CALLING THE WHOLE PROGRAM AT ONCE
print ("                                                   *********************************************************************** \n                                                   ******************** WELCOME TO OFFICE DIRECTORY ********************* \n                                                   **********************************************************************")
def choice():                
    print("What do you want to do? \n 1.Add Data \n 2.Check Data \n 3.Update Data \n 4.Add Attendance \n 5.Check Attendance \n 6.Exit ")

    a= int(input("Enter the desired task No. from above: "))

    if a == 1:
        first()
    elif a == 2:
        second()
    elif a == 3:
        third()
    elif a == 4:
        fourth()
    elif a == 5:
        fifth()
    elif a == 6:
        sixth()
    else:
        print( "!!!PLEASE SELECT ONLY FROM THE GIVEN CHOICES!!!")

def first():
                          #TO WRITE IN TABLE
    b=int(input("Enter the no. of record to be added: "))
    for i in range(b):
        ID=int(input("Enter the employee ID : "))
        POST=input("Enter the post of the employee : ")
        NAME= input("Enter name of the employee : ")
        DOB= input("Enter the date of birth (YYYY-MM-DD) : ")
        PH_NO= input("Enter the phone number : ")
        EMAIL= input("Enter the email_id : ")
        L = (ID,POST,NAME,DOB,PH_NO,EMAIL)
        lalala= "insert into BIO_DATA values (%s,%s,%s,%s,%s,%s)"
        cursor.execute(lalala,L)
        mydb.commit()
        print("---------RECORD ADDED SUCCESSFULLY--------")
        print("X--------------- X ---------------X")
    choice()

def second():
                          #TO READ FROM TABLE
    
    print(" Select the attribute on basis of which the search has to done \n 1. Emp_ID \n 2. Post  \n 3. Name \n 4. PH_NO \n 5. DOB")
    print( "                                        !!!PLEASE CAREFULLY ENTER THE NAME OF THE ATTRIBUTE FROM ABOVE!!!                                        ")                                        
    c = input( "Enter the name of the selected attribute : ")
    v= str(input("Enter the value of Selected Attribute : "))
    L2 = ["DOB" , "Post" , "Name" , "PH_NO"]
    L3 = ["Emp_ID"]
    if c in L2:
        cursor.execute("select * from BIO_DATA where " + c + "=" + " '" + v + "' ")
        result = cursor.fetchall()
        for x in result:
            print(x)
    elif c in L3:
        cursor.execute("select * from BIO_DATA where " + c + "=" + v)
        result = cursor.fetchall()
        for x in result:
            print(x)
    choice()


def third():
                            # TO UPDATE THE TABLE
                
     q= input(" Enter the Emp_ID of the employee to be changed : ")
     print (" Select the attribute you want to change \n 1. Post \n 2. PH_NO \n 3. Email_ID")
     print( "                                        !!!PLEASE CAREFULLY ENTER THE NAME OF THE ATTRIBUTE FROM ABOVE!!!                                        ")                                        
     p= input(" Enter the name of attribute to be changed : ")
     r = input (" Enter the new value : ")
     L4 = ["Post" , "Email_ID"]
     L5 = [ "PH_NO" ]
     if p in L5:
         s = "UPDATE BIO_DATA SET " + p + " = " + r + " where Emp_ID = " + q
         cursor.execute(s)
         mydb.commit()
     elif p in L4:
         k = "UPDATE BIO_DATA SET " + p + " = '" + r + "' where Emp_ID = " + q
         cursor.execute(k)
         mydb.commit()
     print(" UPDATED .....")
     
     choice()


def fourth():
                          #TO CHART ATTENDANCE

    dte = str(input("Enter Date (DD_MM_YYYY) : "))
    table_create = "ALTER TABLE Attendance ADD COLUMN " + dte + " CHAR(1)"
    cursor.execute(table_create)
    condit = "Y"
    while condit.lower() == "y":
        empid = str(input("Enter Employee ID to add Attendance : "))
        pa = input("Enter whether Present(P) or Absent(A) : ")
        table_insert = "INSERT INTO Attendance (" + dte + " , EMP_ID) VALUES ('" + pa + "' , " + empid + ")"
        cursor.execute(table_insert)
        mydb.commit()
        condit = input("Do you want to add more Attendance? (Y/N) : ")
        print("CHARTED...")


    def updation():
        temp_date = str(input("Enter Date (DD_MM_YYYY) : "))
        table_update = "ALTER TABLE Attendance ADD COLUMN " + temp_date + " CHAR(1)"
        cursor.execute(table_update)

        condit = "Y"
        while condit.lower() == "y":
            empid2 = str(input("Enter Employee ID to add Attendance : "))
            pa2 = input("Enter whether Present(P) or Absent(A) : ")
            table_insert2 = "UPDATE Attendance SET " + temp_date + " = '"+ pa2 +"' where Emp_ID = " +empid2 
            cursor.execute(table_insert2)
            mydb.commit()
            condit = input("Do you want to add more Attendance? (Y/N) : ")
            
        ans = input("Do you want tto add another day for attendance? (Y/N) : ")
        if ans.upper() == "Y":
            updation()
        else:
            return
        print("CHARTED...")            
    ans = input("Do you want to add Attendence for another Date? (Y/N) : ")
    if ans.upper() == "Y":
        updation()
    choice()            

    
def fifth():
                                             # TO VIEW ATTENDANCE

    E_ID= input( "Enter the Emp_ID : ")
    d= int(input( " Enter the No. of dates you want to see : "))
    for z in range (d):
        Dates= input(" Enter the required date : ")
        comm_a = "select Attendance.Emp_ID ,BIO_DATA.Name , " + Dates + " from Attendance,BIO_DATA where Attendance.Emp_ID = " + E_ID + " and Attendance.Emp_ID = BIO_DATA.Emp_ID" 
        cursor.execute(comm_a)
        result1= cursor.fetchall()
        for m in result1:
            print(m)
    choice()

def sixth():
    print("TERMINATING....")
    quit()
                                    #CALLING FUNCTIONS
choice()


            


