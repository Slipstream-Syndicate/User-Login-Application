#Database Management

import mysql.connector as mc
import tkinter.messagebox as tkmb
db = mc.connect(host = 'localhost', user = 'root', passwd = 'SQL', database = 'app')
cur = db.cursor()

'''
#Create the table
command = "create table server(Username varchar(100) PRIMARY KEY, Password varchar(20), Age int, Phone_Num int, Language varchar(20), C_Brand varchar(15), C_Model varchar(30), C_Year int(4), P_Brand varchar(15), P_Model varchar(30), P_Year int(4))"
cur.execute(command)
'''
def login_verify_sign_in():
    username = entry1.get()
    password = entry2.get()
    recs = cur.fetchall()
    for i in recs:
        try:
            i = list(i)
            if i[0].lower() == username.lower() and password == i[1]:
                tkmb.showinfo("Login Status", message = "Login Successful")
                after_login()
            elif i[0].lower !=username.lower() and password == i[1]:
                tkmb.showinfo("Login Status", message = "Invalid Username")
            elif i[0].lower ==username.lower() and password != i[1]:
                tkmb.showinfo("Login Status", message = "Invalid Password")
            else:
                tkmb.showinfo("Login Status", message = "Invalid Username and Password")
        except:
            print("System Error")
            
def login_sign_up():
    username = entry1.get()
    password = entry2.get()
    command = "insert into server(Username, Password) values('{}','{}')".format(username, password)

def save_data():
    #GET ALL DATA, UPDATE
    username = entry1.get()
    password = entry2.get()
    age = int(entry_a.get())
    phone_num = int(entry_pn.get())
    language = entry_lc.get()
    car_brand = entry_lc1.get()
    car_model = entry_lc2.get()
    car_year = int(entry_lc3.get())
    phone_brand = entry_lp1.get()
    phone_model = entry_lp2.get()
    phone_year = int(entry_lp3.get())

    if not (age and phone_num and language and car_brand and car_model and car_year and phone_brand and phone_model and phone_year):
        tkmb.showinfo(title = 'No Data', message = "You have no data entered yet")
    elif age<0 or age>999:
        tkmb.showinfo(title = 'Invalid Input', message = "Enter 3-digit number")
    elif phone<0 or phone>99999999999:
        tkmb.showinfo(title = 'Invalid Input', message = "Enter 11-digit number")
    elif car_year<0 or phone_year<0 or car_year>2023 or phone_year>2023:
        tkmb.showinfo(title = 'Invalid Input', message = "Enter valid year")
    else:
        command = "update server set age={}, Phone_Num={}, Language='{}', C_Brand='{}', C_Model='{}', C_Year='{}', P_Brand='{}', P_Model='{}', P_Year='{}' where username = '{}' and password = '{}'".format(age, phone_num, language, car_brand, car_model, car_year, phone_brand, phone_model, phone_year, username, password)
        cur.execute(command)
        db.commit()
