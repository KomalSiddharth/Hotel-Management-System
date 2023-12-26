from tkinter import *
from PIL import Image,ImageTk 
from customer import cust_win
from room import Roombooking
class HotelManagementSystem():
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        #*****************************first image***************************
        img1=Image.open("hi.jpg")
        img1=img1.resize((1550,140),Image. LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        #*****************************second image***************************
        img2=Image.open("img2.jpg")
        img2=img1.resize((1550,140),Image. LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        #********************************title*******************************
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=('times new roman',40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=160,width=1550,height=50)
        #*************************mainframe**********************************
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=150,width=1550,height=620)
        #**********************************frametitle***********************
        lbl_menu=Label(main_frame,text="MENU",font=('times new roman',20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)
        #*************************buttonframe**********************************
        btn_frame=Frame(self.root,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=195,width=228,height=190)
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=('times new roman',14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",width=22,font=('times new roman',14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",width=22,font=('times new roman',14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="REPORT",width=22,font=('times new roman',14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        input_btn=Button(btn_frame,text="LOGOUT",width=22,font=('times new roman',14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        input_btn.grid(row=4,column=0,pady=1)

        
        #********************************right side image******************************
        img1=Image.open("hi.jpg")
        img1=img1.resize((1310,590),Image. LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(main_frame,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)
        
         #********************************right side image******************************
        img2=Image.open("img2.jpg")
        img2=img2.resize((230,210),Image. LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg1=Label(main_frame,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=230,height=210)
        
        #s********************************right side image******************************
        img3=Image.open("img3.jpg")
        img3=img3.resize((230,190),Image. LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=230,height=190)
        
        def cust_details(self):
            self.new_window=Toplevel(self.root)
            self.app=cust_win(self.new_window)
            

if __name__=="__main__" :
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()       