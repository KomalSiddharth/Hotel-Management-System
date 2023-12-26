from tkinter import *
from  PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
class app:
    def __init__(self,root):
        self.root=root
        self.root.title("Social App")
        self.root.geometry("1250x650+230+220")
        lbl_Title=Label(self.root,text="SOCIAL APP",font=('times new roman',18,'bold'),bg="black",fg="white",relief=RIDGE)
        lbl_Title.place(x=0,width=1250,height=50)

        img2=Image.open("Layer 6.png")
        img2=img2.resize((80,50),Image. LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=80,height=50)


        LabelFrameCenter=LabelFrame(self.root,bd=2,relief=RIDGE)
        LabelFrameCenter.place(x=225,y=100,width=825,height=650)
       
        LabelCenter=Label(self.root,text="Welcome to social app! the app for sociopaths!",font=('times new roman',12,'bold'),fg="black")
        LabelCenter.place(x=0,y=110,width=825)

        lbl_fname=Label(LabelFrameCenter,font=('new times roman',12,'bold'),padx=1,pady=20)
        lbl_fname.grid(row=0,column=0,sticky=W)
        txt_fname=Entry(LabelFrameCenter,font=('times new roman',13,'bold'),width=49,state="readonly")
        txt_fname.grid(row=1,column=1)

        lbl_lname=Label(LabelFrameCenter,font=('new times roman',12,'bold'),padx=15,pady=20)
        lbl_lname.grid(row=2,column=0,sticky=W)
        txt_lname=Entry(LabelFrameCenter,font=('times new roman',13,'bold'),width=49,state="readonly")
        txt_lname.grid(row=2,column=1)

        lbl_loc=Label(LabelFrameCenter,font=('new times roman',12,'bold'))
        lbl_loc.grid(row=3,column=0,sticky=W)
        txt_loc=Entry(LabelFrameCenter,font=('times new roman',13,'bold'),width=79,state="readonly")
        txt_loc.grid(row=3,column=1)

        LabelCenter=LabelFrame(self.root,bd=2,relief=RIDGE)
        LabelCenter.place(x=260,y=320,width=760,height=90)
        lbl_pic=Label(LabelCenter,font=('new times roman',12,'bold'),padx=10,pady=30)
        lbl_pic.grid(row=4,column=0,sticky=W)
        txt_pic=Entry(LabelCenter,font=('times new roman',13,'bold'),width=79,state="readonly")
        txt_pic.grid(row=4,column=1)

        lbl_email=Label(LabelFrameCenter,font=('new times roman',12,'bold'),pady=160)
        lbl_email.grid(row=5,column=0,sticky=W)
        txt_email=Entry(LabelFrameCenter,font=('times new roman',13,'bold'),width=79,state="readonly")
        txt_email.grid(row=5,column=1)
       
        btnAdd=Button(text="SUBMIT",font=("arial",11,"bold"),bg="black",fg="white",width=79,height=2)
        btnAdd.grid(row=0,column=0,padx=250,pady=500)

        Labelfoot=Label(self.root,text="Account already Exists! Login Here",font=('times new roman',12,'bold'),fg="black")
        Labelfoot.place(x=0,y=560,width=825)










       
    

        
if __name__=="__main__" :
    root=Tk()
    obj=app(root)
    root.mainloop()       
        
        