from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import mysql.connector
import random 
from tkinter import messagebox

class cust_win():
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x650+0+0")

        #*************************** variables ******************************
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_number=StringVar()


        #*************************title*************************
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=('times new roman',18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,width=1295,height=50)

        #*************************image*************************
        img2=Image.open("img2.jpg")
        img2=img2.resize((100,50),Image. LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=50)

        #****************************label************************
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=('times new roman',12,'bold'))
        labelframeleft.place(x=5,y=50,width=425,height=550)

        #******************************labels and entry***********
        lbl_cust_ref=Label(labelframeleft,text="Customer ref",font=('new times roman',12,'bold'),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        enty_ref=Entry(labelframeleft,textvariable=self.var_ref,font=('times new roman',13,'bold'),width=29,state="readonly")
        enty_ref.grid(row=0,column=1)

        #****cust name

        cname=Label(labelframeleft,font=('arial',12,'bold'),text="Customer Name: ",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=('arial',13,'bold'),width=29)
        txtcname.grid(row=1,column=1)

        #mother name

        lblmname=Label(labelframeleft,font=('arial',12,'bold'),text="Mother Name     : ",padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,font=('arial',13,'bold'),width=29)
        txtmname.grid(row=2,column=1)

         #gender combobox

        label_gender=Label(labelframeleft,font=('arial',12,'bold'),text="Gender               : ",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=('arial',12,'bold'),width=27,state="reason1ys")
        combo_gender['value']=["male","female","others"]
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #email

        lblPostalCode=Label(labelframeleft,font=('arial',12,'bold'),text="Postal Code:",padx=2,pady=6)
        lblPostalCode.grid(row=4,column=0,sticky=W)
        txtPostalCode=ttk.Entry(labelframeleft,textvariable=self.var_email,font=('arial',13,'bold'),width=29)
        txtPostalCode.grid(row=4,column=1)

        #MObile combobox
        lblMobile=Label(labelframeleft,font=('arial',12,'bold'),text="Mobile: ",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=('arial',13,'bold'),width=29)
        txtMobile.grid(row=5,column=1)

         #Nationality

        lblNationality=Label(labelframeleft,font=('arial',12,'bold'),text="Nationality:",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)
        txtNationality=ttk.Entry(labelframeleft,textvariable=self.var_nationality,font=('arial',13,'bold'),width=29)
        txtNationality.grid(row=7,column=1)
        combo_nationality=ttk.Combobox(labelframeleft,font=('arial',12,'bold'),width=27,state="reason1ys")
        combo_nationality['value']=["Indian","American","British"]
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)

        #POstal Code

        lblPostalCode=Label(labelframeleft,font=('arial',12,'bold'),text="Postal Type",padx=2,pady=6)
        lblPostalCode.grid(row=8,column=0,sticky=W)
        txtPostalCode=ttk.Entry(labelframeleft,textvariable=self.var_post,font=('arial',13,'bold'),width=29)
        txtPostalCode.grid(row=8,column=1)

        #Number combobox

        lblNumber=Label(labelframeleft,font=('arial',12,'bold'),text="Number",padx=2,pady=6)
        lblNumber.grid(row=9,column=0,sticky=W)
        txtNumber=ttk.Entry(labelframeleft,textvariable=self.var_number,font=('arial',13,'bold'),width=29)
        txtNumber.grid(row=9,column=1)

        #Address combobox

        lbladdress=Label(labelframeleft,font=('arial',12,'bold'),text="Address",padx=2,pady=6)
        lbladdress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,font=('arial',13,'bold'),width=29)
        txtAddress.grid(row=10,column=1)

        #ID Proof

        lblIDProof=Label(labelframeleft,font=('arial',12,'bold'),text="IDProof",padx=2,pady=6)
        lblIDProof.grid(row=11,column=0,sticky=W)
        txtIDProof=ttk.Entry(labelframeleft,textvariable=self.var_id_proof,font=('arial',13,'bold'),width=29)
        txtIDProof.grid(row=11,column=1)
        combo_IDProof=ttk.Combobox(labelframeleft,font=('arial',12,'bold'),width=27,state="reason1ys")
        combo_IDProof['value']=["Aadhar card","Driving license","passport"]
        combo_IDProof.current(0)
        combo_IDProof.grid(row=11,column=1)

        #ID number
        
        lblIDNumber=Label(labelframeleft,font=('arial',12,'bold'),text="IDNumber",padx=2,pady=6)
        lblIDNumber.grid(row=12,column=0,sticky=W)
        txtIDNumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,font=('arial',13,'bold'),width=29)
        txtIDNumber.grid(row=12,column=1)

        #Address
        
        lbladdress=Label(labelframeleft,font=('arial',12,'bold'),text="Address",padx=2,pady=6)
        lbladdress.grid(row=13,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,font=('arial',13,'bold'),width=29)
        txtAddress.grid(row=13,column=1)

        #*********************** btns *********************************************

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=460,width=412,height=60)
 
        btnAdd=Button(btn_frame,text="Add",font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="update",font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)

        setDelete=Button(btn_frame,text="Delete",font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        setDelete.grid(row=0,column=2,padx=1)
                       
        btnReset=Button(btn_frame,text="Reset",font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnReset.grid(row=0,column=3,padx=1)

        #*********************** label frame *******************************************

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View details and search System",font=("arial",12,"bold"),padx=2,pady=8)
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By: ",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W)
        combo_SearchBy=ttk.Combobox(Table_Frame,font=('arial',12,'bold'),width=24,state="reason1y")
        combo_SearchBy['value']=["mobile","ref"]
        combo_SearchBy.current(0)
        combo_SearchBy.grid(row=0,column=1)

        txtSearch=ttk.Entry(Table_Frame,font=("arial",13,"bold"),width=29)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        #*************************** show data tables **************************************
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_Details_Table=ttk.Treeview(details_table,columns=("ref","name","mother","gender","mobile","email","post",
                                                                    "Nationality","IDproof","IDnumber","address"),xscrollcommand=scroll_x.set
                                                                    ,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_Details_Table.xview)
        scroll_y.config(command=self.cust_Details_Table.yview)

        self.cust_Details_Table.heading("ref",text="Refer No")
        self.cust_Details_Table.heading("name",text="Name")
        self.cust_Details_Table.heading("mother",text="Mother name")
        self.cust_Details_Table.heading("gender",text="Gender")
        self.cust_Details_Table.heading("post",text="postalCode")
        self.cust_Details_Table.heading("mobile",text="Mobile")
        self.cust_Details_Table.heading("email",text="Email")
        self.cust_Details_Table.heading("Nationality",text="Nationality")
        self.cust_Details_Table.heading("IDproof",text="id Proof")
        self.cust_Details_Table.heading("IDnumber",text="ID Number")
        self.cust_Details_Table.heading("address",text="Address")

        self.cust_Details_Table['show']="headings"

        self.cust_Details_Table.column("ref",width=100)
        self.cust_Details_Table.column("name",width=100)
        self.cust_Details_Table.column("mother",width=100)
        self.cust_Details_Table.column("gender",width=100)
        self.cust_Details_Table.column("post",width=100)
        self.cust_Details_Table.column("mobile",width=100)
        self.cust_Details_Table.column("email",width=100)
        self.cust_Details_Table.column("Nationality",width=100)
        self.cust_Details_Table.column("IDproof",width=100)
        self.cust_Details_Table.column("IDnumber",width=100)
        self.cust_Details_Table.column("address",width=100)

        self.cust_Details_Table.pack(fill=BOTH,expand=1)

        def add_data(self):
            if self.var_mobile.get()=="" or self.var_mother.get()=="":
                messagebox.showerror("Error","All fields are required")
            else:
                
                conn=mysql.connector.connect(host="127.0.1",hostname="root",password="Komal281",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s%s%s%s%s%s%s%s%s%s%s)",(self.var_ref.get(),
                                                                                      self.var_name.get(),
                                                                                      self.var_mother.get(),
                                                                                      self.var_gender.get(),
                                                                                      self.var_post.get(),
                                                                                      self.var_mobile.get(),
                                                                                      self.var_email.get(),
                                                                                      self.var_Nationality.get(),
                                                                                      self.var_IDproof.get(),
                                                                                      self.var_IDnumber.get(),
                                                                                      self.var_address.get()
                                                                                                     ))
                

                

        

        
        









        



       
        
        



















if __name__=="__main__" :
    root=Tk()
    obj=cust_win(root)
    root.mainloop()       