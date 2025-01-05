#Creating and opening basic windows

# Try to expand more
'''
1] Save entered data in MySQL and give option to retrieve data [updated]    (HARD, FIND OUT)

Then Data Search


->Create Button in Save Data window to fetch all saved data; if no data notify no data entered


'''

import customtkinter as ctk
import time
import tkinter.messagebox as tkmb
import mysql.connector as mc

global entry1
global entry2
global checkbox

#__________________________________________________________________ LOGIN VERIFICATION

def login_verify_sign_in():
        username = entry1.get()
        password = entry2.get()
        cur.execute('select * from server')
        recs = cur.fetchall()
        if recs!=[]:
            for i in recs:
                try:
                    i = list(i)
                    if i[0].lower() == username.lower() and password == i[1]:
                        tkmb.showinfo("Login Status", message = "Login Successful")
                        after_login()
                    elif i[0].lower() != username.lower() and password == i[1]:
                        tkmb.showinfo("Login Status", message = "Invalid Username")
                    elif i[0].lower() == username.lower() and password != i[1]:
                        tkmb.showinfo("Login Status", message = "Invalid Password")
                    elif i[0].lower() != username.lower() and password != i[1]:
                        tkmb.showinfo("Login Status", message = "Invalid Username or Password\n\nIf you are a 'New User' please 'Sign Up' to continue")
                except:
                    tkmb.showinfo("Login Status", message = "System Error")
        elif recs==[]:
            tkmb.showinfo("Login Status", message = "Please 'Sign Up' to continue")
    
#__________________________________________________________________ SAVE
        
def save_c():
    username = entry1.get()
    password = entry2.get()
    car_brand = entry_lc1.get()
    car_model = entry_lc2.get()
    car_year = int(entry_lc3.get())
    
    if not car_brand and not car_model and not car_year:
        tkmb.showinfo(title = 'No Data', message = "No data entered yet")
    elif car_year<0 or car_year>2023:
        tkmb.showinfo(title = 'Invalid Input', message = "Enter valid year")
    else:
        command = "update server set C_Brand='{}', C_Model='{}', C_Year={} where username = '{}' and password = '{}'".format(car_brand, car_model, car_year, username, password)
        cur.execute(command)
        db.commit()
    time.sleep(1)
    tkmb.showinfo(title = "Data Saved", message = "Data successfully saved")
    
def save_p():
    username = entry1.get()
    password = entry2.get()
    phone_brand = entry_lp1.get()
    phone_model = entry_lp2.get()
    phone_year = int(entry_lp3.get())

    if not phone_brand and not phone_model and not phone_year:
        tkmb.showinfo(title = 'No Data', message = "No data entered yet")
    elif phone_year<0 or phone_year>2023:
        tkmb.showinfo(title = 'Invalid Input', message = "Enter valid year")
    else:
        command = "update server set P_Brand='{}', P_Model='{}', P_Year={} where username = '{}' and password = '{}'".format(phone_brand, phone_model, phone_year, username, password)
        cur.execute(command)
        db.commit()
    time.sleep(1)
    tkmb.showinfo(title = "Data Saved", message = "Data successfully saved")
    
def save_pd():
    username = entry1.get()
    password = entry2.get()
    age = int(entry_a.get())
    phone_num = int(entry_pn.get())
    language = entry_lc.get()

    if not (age and phone_num and language):
        tkmb.showinfo(title = 'No Data', message = "No data entered yet")
    elif age<0 or age>999:
        tkmb.showinfo(title = 'Invalid Input', message = "Enter 3-digit number")
    elif phone_num<0 or phone_num>99999999999:
        tkmb.showinfo(title = 'Invalid Input', message = "Enter 11-digit number")
    else:
        command = "update server set age={}, Phone_Num={}, Language='{}' where username = '{}' and password = '{}'".format(age, phone_num, language, username, password)
        cur.execute(command)
        db.commit()
    time.sleep(1)
    tkmb.showinfo(title = "Data Saved", message = "Data successfully saved")

#__________________________________________________________________ SIGN UP
            
def login_sign_up():
    username = entry1.get()
    password = entry2.get()
    cur.execute('select * from server')
    recs = cur.fetchall()
    for I in recs:
        I=list(I)
        if username.lower() in I[0].lower():
            tkmb.showinfo(title = "Error Signing In", message = "Username already exists!")
        elif username.lower() not in I[0].lower():
            command = "insert into server(Username, Password) values('{}','{}')".format(username, password)
            cur.execute(command)
            db.commit()
            after_login()
    
def sign_up():

    CSU_Val = checkbox.get()
    if CSU_Val ==0:
        return
    global entry1
    global entry2
    
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    window = ctk.CTk()
    window.geometry("350x300")
    window.title("Sign Up")

    frame = ctk.CTkFrame(master = window)
    frame.pack(padx = 20, pady = 20, fill = 'both', expand = True)

    label = ctk.CTkLabel(master = frame, text = "Login System  > Sign Up")
    label.pack(padx = 10, pady = 12)


    entry1 = ctk.CTkEntry(master = frame, placeholder_text = "Username")
    entry1.pack(padx = 10, pady = 12)


    entry2 = ctk.CTkEntry(master = frame, placeholder_text = "Password", show = "*")
    entry2.pack(padx = 10, pady = 12)


    button1 = ctk.CTkButton(master = frame, text = "Login", command = login_sign_up)
    button1.pack(side = 'left', padx = 10, pady = 12)

    button2 = ctk.CTkButton(master = frame,
                                      text = "Exit",
                                      fg_color="#871212",
                                      hover= True,
                                      hover_color= "black",
                                      command = window.destroy)
    button2.pack(side = 'right', padx = 10, pady = 12)
    window.mainloop()


#__________________________________________________________________ CAR AND PHONE DETAILS    
def car():
    global entry_lc1
    global entry_lc2
    global entry_lc3
    
    C1_Val = checkbox1.get()
    if C1_Val==0:
        return
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    window = ctk.CTk()
    window.geometry("400x250")
    window.title("Car Details")

    frame = ctk.CTkFrame(master = window)
    frame.pack(padx = 20, pady = 20, fill = 'both', expand = True)

    entry_lc1 = ctk.CTkEntry(master = frame, width = 180, placeholder_text = "Enter Car Brand")
    entry_lc1.pack(padx = 10, pady = 12)

    entry_lc2 = ctk.CTkEntry(master = frame, width = 180, placeholder_text = "Enter Car Model Name")
    entry_lc2.pack(padx = 10, pady = 12)

    entry_lc3 = ctk.CTkEntry(master = frame, width = 180, placeholder_text = "Enter Year of Purchase")
    entry_lc3.pack(padx = 10, pady = 12)
    
    buttonrc = ctk.CTkButton(master = frame,
                                      text = "Back",
                                      fg_color="#871212",
                                      hover= True,
                                      hover_color= "black",
                                      command = window.destroy)
    buttonrc.pack(side = 'right', padx = 10, pady = 12)

    buttonlc = ctk.CTkButton(master = frame,
                                      fg_color ="#a88f13",
                                      hover = True,
                                      hover_color = "black",
                                      text = "Save",
                                      text_color ="#b01717",
                                      command = save_c)
    buttonlc.pack(side = 'left', padx = 10, pady = 12)

    print("Entered Car Details")

    window.mainloop()

def phone():
    global entry_lp1
    global entry_lp2
    global entry_lp3
    
    C2_Val = checkbox2.get()
    if C2_Val==0:
        return
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    window = ctk.CTk()
    window.geometry("400x250")
    window.title("Phone Details")

    frame = ctk.CTkFrame(master =window)
    frame.pack(padx = 10, pady =20, fill ="both", expand = True)

    entry_lp1 = ctk.CTkEntry(master = frame, width = 180, placeholder_text = "Enter Phone Brand")
    entry_lp1.pack(padx = 10, pady = 12)

    entry_lp2 = ctk.CTkEntry(master = frame, width = 180, placeholder_text = "Enter Model Name")
    entry_lp2.pack(padx = 10, pady = 12)

    entry_lp3 = ctk.CTkEntry(master = frame, width = 180, placeholder_text = "Enter Year of Purchase")
    entry_lp3.pack(padx = 10, pady = 12)

    buttonrp = ctk.CTkButton(master = frame,
                           text = "Back",
                           fg_color = "#871212",
                           hover = True,
                           hover_color = "black",
                           command = window.destroy)
    buttonrp.pack(side = 'right', padx = 10, pady = 12)

    buttonlp = ctk.CTkButton(master = frame,
                                      fg_color ="#a88f13",
                                      hover = True,
                                      hover_color = "black",
                                      text = "Save",
                                      text_color ="#b01717",
                                      command = save_p)
    buttonlp.pack(side = 'left', padx = 10, pady = 12)
    
    print("Entered Phone Details")
    
    window.mainloop()

#__________________________________________________________________ AFTER LOGIN PAGE->PERSONAL DETAILS

def after_login():
    global checkbox1
    global checkbox2
    global entry_a
    global entry_pn
    global entry_lc
    
    time.sleep(2)
    print("Logged in Successfully...")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    window = ctk.CTk()
    window.geometry("390x320")
    window.title("Personal Details")

    frame = ctk.CTkFrame(master = window)
    frame.pack(padx = 20, pady = 20, fill = 'both', expand = True)

    entry_a = ctk.CTkEntry(master = frame, width= 210, placeholder_text = "Enter Your Age")
    entry_a.pack(padx = 10, pady = 12)

    entry_pn = ctk.CTkEntry(master = frame, width= 210, placeholder_text = "Enter Phone Number")
    entry_pn.pack(padx = 10, pady = 12)

    entry_lc = ctk.CTkEntry(master = frame, width= 210, placeholder_text = "Enter Language of Communication")
    entry_lc.pack(padx = 10, pady = 12)

    checkbox1 = ctk.CTkCheckBox(master = frame, text = "I have a car", onvalue = 1, offvalue = 0, command = car)
    checkbox1.place(x = 70, y = 170)      

    checkbox2 = ctk.CTkCheckBox(master = frame, text = "I have a phone", onvalue = 1, offvalue = 0, command = phone)
    checkbox2.place(x = 180, y = 170)


    buttonls = ctk.CTkButton(master = frame,
                                      fg_color ="#a88f13",
                                      hover = True,
                                      hover_color = "black",
                                      text = "Save",
                                      text_color ="#b01717",
                                      command = save_pd)
    buttonls.pack(side = 'left', padx = 10, pady = 12)
    
    buttonrs = ctk.CTkButton(master = frame,
                                      fg_color ="#871212",
                                      hover = True,
                                      hover_color = "black",
                                      text = "Logout",
                                      command = window.destroy)
    buttonrs.pack(side = 'right', padx = 10, pady = 12)

    window.mainloop()

# _______________________________________________________________________________________ MAIN PROGRAM

db = mc.connect(host = 'localhost', user = 'root', passwd = 'SQL', database = 'app')
cur = db.cursor()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


window = ctk.CTk()
window.geometry("350x300")
window.title("Login Page")

frame = ctk.CTkFrame(master = window)
frame.pack(padx = 20, pady = 20, fill = 'both', expand = True)


label = ctk.CTkLabel(master = frame, text = "Login System  > Sign In")
label.pack(padx = 10, pady = 12)


entry1 = ctk.CTkEntry(master = frame, placeholder_text = "Username")
entry1.pack(padx = 10, pady = 12)

entry2 = ctk.CTkEntry(master = frame, placeholder_text = "Password", show = "*")
entry2.pack(padx = 10, pady = 12)

checkbox = ctk.CTkCheckBox(master = frame, text = "New User? Sign Up", onvalue =1, offvalue = 0, command = sign_up)
checkbox.pack(padx = 10, pady = 12)


button1 = ctk.CTkButton(master = frame, text = "Login", command = login_verify_sign_in)
button1.pack(side = 'left', padx = 10, pady = 12)

button2 = ctk.CTkButton(master = frame,
                                  text = "Exit",
                                  fg_color ="#871212",
                                  hover = True,
                                  hover_color = "black",
                                  command = window.destroy)
button2.pack(side = 'right', padx = 10, pady = 12)
window.mainloop()


#Button Options
'''downloadButton = customtkinter.CTkButton(
    master=window,
    command=downloadVideo,
    text="Download",
    text_color="white",
    hover= True,
    hover_color= "black",
    height=35,
    width= 120,
    border_width=2,
    corner_radius=4,
    border_color= "#5d6266", 
    bg_color="#262626",
    fg_color= "#262626",
)'''
