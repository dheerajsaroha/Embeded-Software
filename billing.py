from tkinter import *
import math
from tkinter import ttk
import datetime
import random,os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import messagebox,END
from PIL import Image, ImageTk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pdf_mail import sendpdf
import qrcode
from validate_email import validate_email



# ===================================================
root=Tk()

class FirstPage:
    def __init__(self, root):
        self.root = root
        
        
        self.root.geometry("1920x1080+1+1")
        self.root.title("Grocery Store")
        self.root.config(bg="#f5b878")
        # self.root.iconify()
        self.icon=PhotoImage(file="supermarket.png")
        self.root.iconphoto(True,self.icon)
        
        # Create a frame to add a border around the label
        self.label_frame = Frame(root, bd=2, relief="solid", bg="#f5b878")
        self.label_frame.pack(pady=10)

        # Create and place the label in the frame with matching background
        self.label = Label(self.label_frame, text="Nitin Grocery Store", font=("Arial", 24,"bold"), bg="#f5b878")
        self.label.pack(padx=10, pady=10)

        # # Make sure to replace 'your_image.png' with the actual image path
        self.image = PhotoImage(file="hand-drawn-pattern-background_23-2150822444.png")
        self.image_label = Label(root, image=self.image)
        self.image_label.pack(pady=20)

        # Create and place the Start button, linking it to the go_to_second_page function
        self.start_button = Button(root, text="START", font=("Antons", 32,"bold"), bg="green", fg="white", command=self.go_to_second_page,height=18)
        self.start_button.pack(fill=X, padx=10, pady=10)

    def go_to_second_page(self):
        # Destroy the current page (first page)
        for widget in self.root.winfo_children():
            widget.destroy()
        
        
        # Open the second page
        Bill_App(self.root)



# ==============================================================



class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.title("Billing Software")
        self.root.geometry("1920x1080+1+1")
        bg_color="#074463"
        ft_style="times new roman"
        

        # ==================Variables ===================================
        # =============Cosmetic====================================
        
        self.bth_soap=IntVar()
        self.shmpo=IntVar()
        self.conditioner=IntVar()
        self.facewash=IntVar()
        self.lotion=IntVar()
        self.hairoil=IntVar()
        self.sunscreen=IntVar()
        self.moisture=IntVar()
        self.foundation=IntVar()
        

        # =============Fruits====================================

        self.apple=IntVar()
        self.banana=IntVar()
        self.grapes=IntVar()
        self.guava=IntVar()
        self.pears=IntVar()
        self.pomergranates=IntVar()
        self.apricot=IntVar()
        self.dragon=IntVar()
        self.pineapple=IntVar()

        # =============Vegetables====================================

        self.potatao=IntVar()
        self.tamato=IntVar()
        self.mushroom=IntVar()
        self.carrot=IntVar()
        self.peas=IntVar()
        self.bittergouard=IntVar()
        self.pumpkin=IntVar()
        self.capsicum=IntVar()
        self.cabbage=IntVar()

        # =============beverages====================================

        self.dew=IntVar()
        self.sprite=IntVar()
        self.limca=IntVar()
        self.frooti=IntVar()
        self.mixed_juice=IntVar()
        self.natural_juice=IntVar()
        self.coffee=IntVar()
        self.energy_drink=IntVar()
        self.beer=IntVar()

        # ==================== total price and total tax variable ==============================
        self.cosmetic_price=StringVar()
        self.fruits_price=StringVar()
        self.vegetables_price=StringVar()
        self.beverages_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.fruits_tax=StringVar()
        self.vegetables_tax=StringVar()
        self.beverages_tax=StringVar()

        # ============== Customer =======================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.c_bill_no=StringVar()
        self.search_bill=StringVar()
        self.c_email=StringVar()
        x=random.randint(1,1000)
        self.c_bill_no.set(str(x))
        



        # Customer Details
        F1=LabelFrame(self.root,text="Customer Details",font=(ft_style,15,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE)
        F1.place(x=0,y=0,relwidth=1)
        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=(ft_style,18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=20,textvariable=self.c_name,font=("arial",14,"bold"),bd=4,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphn_lbl=Label(F1,text="Customer Phone No.",bg=bg_color,fg="white",font=(ft_style,18,"bold")).grid(row=0,column=3,padx=20,pady=5)
        cphn_txt=Entry(F1,width=20,textvariable=self.c_phone,font=("arial",14,"bold"),bd=4,relief=SUNKEN).grid(row=0,column=4,padx=10,pady=5)

        cemail_lbl=Label(F1,text="Customer Email",bg=bg_color,fg="white",font=(ft_style,18,"bold")).grid(row=0,column=5,padx=20,pady=5)
        cemail_txt=Entry(F1,width=20,textvariable=self.c_email,font=("arial",14,"bold"),bd=4,relief=SUNKEN).grid(row=0,column=6,padx=10,pady=5)

        cbil_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=(ft_style,18,"bold")).grid(row=0,column=7,padx=20,pady=5)
        cbill_txt=Entry(F1,width=20,textvariable=self.c_bill_no,font=("arial",14,"bold"),bd=4,relief=SUNKEN).grid(row=0,column=8,padx=10,pady=5)

        # btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=2,bg="white",font=(ft_style,12,"bold")).grid(row=0,column=9,padx=10,pady=5)
        


        # ==================Costmetic Frame ====================#
        F2=LabelFrame(self.root,text=" Cosmetic Item ",font=(ft_style,15,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE)
        F2.place(x=5,y=85,height=540,width=325)
        bth_label=Label(F2,text="Bath Soap",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bth_txt=Entry(F2,width=10,textvariable=self.bth_soap,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=0,column=1,padx=10,pady=10,sticky="e")

        shmpo_label=Label(F2,text="Shampoo",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        shmpo_txt=Entry(F2,width=10,textvariable=self.shmpo,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=1,column=1,padx=10,pady=10,sticky="e")

        conditioner_label=Label(F2,text="Conditionor",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        conditioner_txt=Entry(F2,width=10,textvariable=self.conditioner,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=2,column=1,padx=10,pady=10,sticky="e")

        face_wash_label=Label(F2,text="Facewash",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        face_wash_txt=Entry(F2,width=10,textvariable=self.facewash,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=3,column=1,padx=10,pady=10,sticky="e")

        lotion_label=Label(F2,text="Lotion",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        lotion_txt=Entry(F2,width=10,textvariable=self.lotion,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=4,column=1,padx=10,pady=10,sticky="e")

        hair_label=Label(F2,text="Hair Oil",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        hair_txt=Entry(F2,width=10,textvariable=self.hairoil,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=5,column=1,padx=10,pady=10,sticky="e")

        sunscr_label=Label(F2,text="Sunscreen",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        sunscr_txt=Entry(F2,width=10,textvariable=self.sunscreen,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=6,column=1,padx=10,pady=10,sticky="e")

        moisture_label=Label(F2,text="Moisturizer",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=7,column=0,padx=10,pady=10,sticky="w")
        moisture_txt=Entry(F2,width=10,textvariable=self.moisture,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=7,column=1,padx=10,pady=10,sticky="e")

        foundation_label=Label(F2,text="Foundation",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=8,column=0,padx=10,pady=10,sticky="w")
        foundation_txt=Entry(F2,width=10,textvariable=self.foundation,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=8,column=1,padx=10,pady=10,sticky="e")



        # ===================Fruits ====================
        F3=LabelFrame(self.root,text=" Fruits",font=(ft_style,15,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE)
        F3.place(x=340,y=85,height=540,width=325)

        apple_label=Label(F3,text="Apples",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        apple_txt=Entry(F3,width=10,textvariable=self.apple,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=0,column=1,padx=10,pady=10,sticky="e")

        banana_label=Label(F3,text="Banana",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        banana_txt=Entry(F3,width=10,textvariable=self.banana,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=1,column=1,padx=10,pady=10,sticky="e")

        grapes_label=Label(F3,text="Grapes",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        grapes_txt=Entry(F3,width=10,textvariable=self.grapes,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=2,column=1,padx=10,pady=10,sticky="e")

        guava_label=Label(F3,text="Guava",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        guava_txt=Entry(F3,width=10,textvariable=self.guava,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=3,column=1,padx=10,pady=10,sticky="e")

        pears_label=Label(F3,text="Pears",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        pears_txt=Entry(F3,width=10,textvariable=self.pears,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=4,column=1,padx=10,pady=10,sticky="e")

        pomegranate_label=Label(F3,text="Pomegranate",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        pomegranate_txt=Entry(F3,width=10,textvariable=self.pomergranates,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=5,column=1,padx=10,pady=10,sticky="e")

        apricot_label=Label(F3,text="Apricot",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        apricot_txt=Entry(F3,width=10,textvariable=self.apricot,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=6,column=1,padx=10,pady=10,sticky="e")

        dragon_label=Label(F3,text="Dragon Fruit",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=7,column=0,padx=10,pady=10,sticky="w")
        dragon_txt=Entry(F3,width=10,textvariable=self.dragon,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=7,column=1,padx=10,pady=10,sticky="e")

        pineapple_label=Label(F3,text="Pineapple",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=8,column=0,padx=10,pady=10,sticky="w")
        pineapple_txt=Entry(F3,width=10,textvariable=self.pineapple,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=8,column=1,padx=10,pady=10,sticky="e")


        # ======================= Vegetables ==========================
        F4=LabelFrame(self.root,text=" Vegetables",font=(ft_style,15,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE)
        F4.place(x=675,y=85,height=540,width=325)

        potato_label=Label(F4,text="Potato",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        potato_txt=Entry(F4,width=10,textvariable=self.potatao,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=0,column=1,padx=10,pady=10,sticky="e")

        tamato_label=Label(F4,text="Tamato",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        tamato_txt=Entry(F4,width=10,textvariable=self.tamato,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=1,column=1,padx=10,pady=10,sticky="e")

        mushrom_label=Label(F4,text="Mushroom",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        mushrom_condnr_txt=Entry(F4,width=10,textvariable=self.mushroom,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=2,column=1,padx=10,pady=10,sticky="e")

        caroot_label=Label(F4,text="Caroot",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        caroot_txt=Entry(F4,width=10,textvariable=self.carrot,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=3,column=1,padx=10,pady=10,sticky="e")

        peas_label=Label(F4,text="Peas",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        peas_txt=Entry(F4,width=10,textvariable=self.peas,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=4,column=1,padx=10,pady=10,sticky="e")

        bitter_label=Label(F4,text="Bitter Gourd",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        bitter_txt=Entry(F4,width=10,textvariable=self.bittergouard,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=5,column=1,padx=10,pady=10,sticky="e")

        pumpkin_label=Label(F4,text="Pumpkin",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        pumpkin_txt=Entry(F4,width=10,textvariable=self.pumpkin,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=6,column=1,padx=10,pady=10,sticky="e")

        capsicum_label=Label(F4,text="Capsicum",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=7,column=0,padx=10,pady=10,sticky="w")
        capsicum_txt=Entry(F4,width=10,textvariable=self.capsicum,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=7,column=1,padx=10,pady=10,sticky="e")

        cabbage_label=Label(F4,text="Cabbage",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=8,column=0,padx=10,pady=10,sticky="w")
        cabbage_txt=Entry(F4,width=10,textvariable=self.cabbage,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=8,column=1,padx=10,pady=10,sticky="e")


        # ===========================Beverages ======

        F5=LabelFrame(self.root,text="Beverages",font=(ft_style,15,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE)
        F5.place(x=1010,y=85,height=540,width=325 )

        dew_label=Label(F5,text="Mountain Dew",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        dew_txt=Entry(F5,width=10,textvariable=self.dew,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=0,column=1,padx=10,pady=10,sticky="e")

        sprite_label=Label(F5,text="Sprite",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        sprite_txt=Entry(F5,width=10,textvariable=self.sprite,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=1,column=1,padx=10,pady=10,sticky="e")

        limca_label=Label(F5,text="Limca",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        limca_txt=Entry(F5,width=10,textvariable=self.limca,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=2,column=1,padx=10,pady=10,sticky="e")

        frooti_label=Label(F5,text="Frooti",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        frooti_txt=Entry(F5,width=10,textvariable=self.frooti,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=3,column=1,padx=10,pady=10,sticky="e")

        mixed_juice_label=Label(F5,text="Mixed Juice",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        mixed_juice_txt=Entry(F5,width=10,textvariable=self.mixed_juice,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=4,column=1,padx=10,pady=10,sticky="e")

        nature_label=Label(F5,text="Natural Juice",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        nature_txt=Entry(F5,width=10,textvariable=self.natural_juice,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=5,column=1,padx=10,pady=10,sticky="e")

        coffee_label=Label(F5,text="Coffee",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        coffee_txt=Entry(F5,width=10,textvariable=self.coffee,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=6,column=1,padx=10,pady=10,sticky="e")

        energy_drink_label=Label(F5,text="Energy Drink",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=7,column=0,padx=10,pady=10,sticky="w")
        energy_drink_txt=Entry(F5,width=10,textvariable=self.energy_drink,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=7,column=1,padx=10,pady=10,sticky="e")

        beer_label=Label(F5,text="Fruit Beer",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=8,column=0,padx=10,pady=10,sticky="w")
        beer_txt=Entry(F5,width=10,textvariable=self.beer,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=8,column=1,padx=10,pady=10,sticky="e")

        # ======================= Bill Area ==============
        F6=Frame(self.root,bd=5,relief=GROOVE)
        F6.place(x=1345,y=85,height=540,width=510)

        bill_title=Label(F6,text=" Your Bill",font=(ft_style,18,"bold"),bd=7,relief=GROOVE,bg=bg_color,fg="white").pack(fill=X)
        scroll_y=Scrollbar(F6,orient=VERTICAL)
        self.txtarea=Text(F6,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)


        # ===============Button Menu Frame =================

        F7=LabelFrame(self.root,text=" Bill Menu ",font=(ft_style,15,"bold"),fg="gold",bg=bg_color,bd=10,relief=GROOVE)
        F7.place(x=0,y=635,height=270,relwidth=1)

        cosmetic_label=Label(F7,text=" Total Cosmetics Price",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        cosmetic_txt=Entry(F7,width=10,textvariable=self.cosmetic_price,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=0,column=1,padx=10,pady=10,sticky="e")

        fruit_label=Label(F7,text=" Total Fruits Price",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        fruit_txt=Entry(F7,width=10,textvariable=self.fruits_price,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=1,column=1,padx=10,pady=10,sticky="e")

        vegetables_label=Label(F7,text=" Total Vegetables Price",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        vegetables_txt=Entry(F7,width=10,textvariable=self.vegetables_price,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=2,column=1,padx=10,pady=10,sticky="e")

        beverages_label=Label(F7,text=" Total Beverages Price",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        beverages_txt=Entry(F7,width=10,textvariable=self.beverages_price,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=3,column=1,padx=10,pady=10,sticky="e")

        # ======================== Tax on item ================================
        cosmetic_tax_label=Label(F7,text=" Cosmetics Tax",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=3,padx=10,pady=10,sticky="w")
        cosmetic_tax_txt=Entry(F7,width=10,textvariable=self.cosmetic_tax,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=0,column=4,padx=10,pady=10,sticky="e")

        fruit_tax_label=Label(F7,text=" Fruits Tax",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=3,padx=10,pady=10,sticky="w")
        fruit_tax_txt=Entry(F7,width=10,textvariable=self.fruits_tax,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=1,column=4,padx=10,pady=10,sticky="e")

        vegetables_tax_label=Label(F7,text=" Vegetables Tax",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=3,padx=10,pady=10,sticky="w")
        vegetables_tax_txt=Entry(F7,width=10,textvariable=self.vegetables_tax,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=2,column=4,padx=10,pady=10,sticky="e")

        beverages_tax_label=Label(F7,text=" Beverages Tax",bd=2,font=(ft_style,15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=3,padx=10,pady=10,sticky="w")
        beverages_tax_txt=Entry(F7,width=10,textvariable=self.beverages_tax,font=(ft_style,15,"bold"),bd=4,bg="white").grid(row=3,column=4,padx=10,pady=10,sticky="e")

        # =================================Button =================================
        button_frame=Frame(F7,bd=7,relief=GROOVE)
        button_frame.place(x=665,width=1180,height=230)
        total_btn=Button(button_frame,command=self.total,text="Total",fg="white",bg="cadetblue",bd=7,pady=20,padx=45,font=("Arial",16,"bold"),width=21).grid(row=0,column=0,padx=10,pady=10)
        generate_btn=Button(button_frame,command=self.bill_area,text="Generate Bill",fg="white",bg="cadetblue",bd=7,pady=20,padx=45,font=("Arial",16,"bold"),width=21).grid(row=0,column=1,padx=10,pady=10)
        share_btn=Button(button_frame,text="Share",command=self.share,fg="white",bg="cadetblue",bd=7,pady=20,padx=45,font=("Arial",16,"bold"),width=21).grid(row=1,column=0,padx=10,pady=10)
        pay_btn=Button(button_frame,text="Pay Bill",command=self.payment,fg="white",bg="cadetblue",bd=7,pady=20,padx=45,font=("Arial",16,"bold"),width=21).grid(row=1,column=1,padx=10,pady=10)
        pdf_btn=Button(button_frame,text="Bill Pdf",command=self.save_pdf,fg="white",bg="cadetblue",bd=7,pady=20,padx=45,font=("Arial",16,"bold"),width=21).grid(row=0,column=2,padx=10,pady=10)
        search_btn=Button(button_frame,text="Search",command=self.find_bill,fg="white",bd=7,pady=20,padx=45,bg="cadetblue",font=("Arial",16,"bold"),width=21).grid(row=1,column=2,padx=10,pady=10)
        # exit_btn=Button(button_frame,text="Exit",command=self.Exit_app,fg="white",bg="cadetblue",bd=7,pady=20,padx=45,font=("Arial",16,"bold"),width=22).grid(row=1,column=2,padx=10,pady=10)
        
        F8=LabelFrame(self.root,bd=10,relief=GROOVE,bg=bg_color)
        F8.place(x=0,y=910,height=100,relwidth=1)
        back_button = Button(F8, text="Back", font=("Arial", 16,"bold"), bg="cadetblue",pady=15,padx=18, fg="white", command=self.go_to_first_page,bd=7,width=44).grid(row=0,column=1,padx=8,pady=5)
        clear_btn = Button(F8,text="Clear",command=self.clear_data,fg="white",bg="cadetblue",bd=7,pady=15,padx=18,font=("Arial",16,"bold"),width=44).grid(row=0,column=5,padx=8,pady=5)

        # back_button.pack(fill=BOTH, padx=10, pady=10,expand=True)
        exit_btn=Button(F8,text="Exit",command=self.Exit_app,fg="white",bg="cadetblue",bd=7,pady=15,padx=36,font=("Arial",16,"bold"),width=44).grid(row=0,column=7,padx=8,pady=5)


    def total(self):
        # self.cosm_bth_soap=int(self.bth_soap.get())
        # self.cos_bth_soap=self.cosm_bth_soap*49

        # self.cosm_shampoo=int(self.shmpo.get())
        # self.cos_shampoo=self.cosm_shampoo*59

        # self.cosm_conditioner=int(self.conditioner.get())
        # self.cos_conditioner=self.cosm_conditioner*199

        # self.cosm_facewash=int(self.facewash.get())
        # self.cos_facewash=self.cosm_facewash*99

        # self.cosm_hairoil=int(self.hairoil.get())
        # self.cos_hairoil=self.cosm_hairoil*79

        # self.cosm_lotion=int(self.lotion.get())
        # self.cos_lotion=self.cosm_lotion*149

        # self.cosm_sunscreen=int(self.sunscreen.get())
        # self.cos_sunscreen=self.cosm_sunscreen*149

        # self.cosm_moisture=int(self.moisture.get())
        # self.cos_moisture=self.cosm_moisture*99
        
        # self.cosm_foundation=int(self.foundation.get())
        # self.cos_foundation=self.cosm_foundation*249
        self.cos_bth_soap=self.bth_soap.get()*49
        self.cos_shampoo=self.shmpo.get()*59
        self.cos_conditioner=self.conditioner.get()*199
        self.cos_facewash=self.facewash.get()*99
        self.cos_hairoil=self.hairoil.get()*79
        self.cos_lotion=self.lotion.get()*149
        self.cos_sunscreen=self.sunscreen.get()*149
        self.cos_moisture=self.moisture.get()*99
        self.cos_foundation=self.foundation.get()*249

        


        self.total_cosmetic_price=float(
            self.cos_bth_soap+
            self.cos_shampoo+
            self.cos_conditioner+
            self.cos_facewash+
            self.cos_hairoil+
            self.cos_lotion+
            self.cos_sunscreen+
            self.cos_moisture+
            self.cos_foundation
        )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. " +str(self.c_tax))
        # =================Fruits=====================
        self.fruits_apple=self.apple.get()*18
        self.fruits_banana=self.banana.get()*7
        self.fruits_grapes=self.grapes.get()*70
        self.fruits_guava=self.guava.get()*19
        self.fruits_pears=self.pears.get()*15
        self.fruits_pomergranates=self.pomergranates.get()*29
        self.fruits_apricot=self.apricot.get()*29
        self.fruits_dragon=self.dragon.get()*89
        self.fruits_pineapple=self.pineapple.get()*79

        self.total_fruits_price=float(
            self.fruits_apple+
            self.fruits_banana+
            self.fruits_grapes+
            self.fruits_guava+
            self.fruits_pears+
            self.fruits_pomergranates+
            self.fruits_apricot+
            self.fruits_dragon+
            self.fruits_pineapple

        )
        self.fruits_price.set("Rs. "+str(self.total_fruits_price))
        self.f_tax=round((self.total_fruits_price*0.03),2)
        self.fruits_tax.set("Rs. "+str(self.f_tax))

        # ===================Vegetables===================================
        self.veg_potatao=self.potatao.get()*7
        self.veg_tamato=self.tamato.get()*15
        self.veg_mushroom=self.mushroom.get()*9
        self.veg_carrot=self.carrot.get()*9
        self.veg_peas=self.peas.get()*59
        self.veg_bittergouard=self.bittergouard.get()*19
        self.veg_pumpkin=self.pumpkin.get()*49
        self.veg_capsicum=self.capsicum.get()*29
        self.veg_cabbage=self.cabbage.get()*49
        
        self.total_vegetables_price=float(
            self.veg_potatao+
            self.veg_tamato+
            self.veg_mushroom+
            self.veg_carrot+
            self.veg_peas+
            self.veg_bittergouard+
            self.veg_pumpkin+
            self.veg_capsicum+
            self.veg_cabbage
        )
        self.vegetables_price.set("Rs. "+str(self.total_vegetables_price))
        self.v_tax=round((self.total_vegetables_price*0.03),2)
        self.vegetables_tax.set("Rs. " + str(self.v_tax))
        
        # =======================beverages==========================
        self.bev_dew=self.dew.get()*80
        self.bev_sprite=self.sprite.get()*80
        self.bev_limca=self.limca.get()*95
        self.bev_frooti=self.frooti.get()*100
        self.bev_mixed_juice=self.mixed_juice.get()*120
        self.bev_natural_juice=self.natural_juice.get()*149
        self.bev_coffee=self.coffee.get()*149
        self.bev_energy_drink=self.energy_drink.get()*120
        self.bev_beer=self.beer.get()*179

        self.total_beverages_price=float(
            self.bev_dew+
            self.bev_sprite+
            self.bev_limca+
            self.bev_frooti+
            self.bev_mixed_juice+
            self.bev_natural_juice+
            self.bev_coffee+
            self.bev_energy_drink+
            self.bev_beer
        )
        self.beverages_price.set("Rs. "+str(self.total_beverages_price))
        self.b_tax=round((self.total_beverages_price*0.05),2)
        self.beverages_tax.set("Rs. " + str(self.b_tax))
        # self.total_bill=float(self.total_cosmetic_price+self.cosmetic_tax+self.total_fruits_price+self.fruits_tax+self.vegetables_price+self.vegetables_tax+self.total_beverages_price+self.beverages_tax)
        # self.is_valid=validate_email(self.c_email.get(),verify=True)


        self.Total_bill=round((float(self.total_cosmetic_price + self.total_fruits_price + self.total_vegetables_price + self.total_beverages_price + self.c_tax + self.f_tax + self.v_tax + self.b_tax)),2)
        if self.c_name.get()=="" or self.c_name.get()==" ":
            messagebox.showerror("!! Notice !!","Customer Name can't be Empty!")
        elif (self.c_name.get()).isalpha() != True:
            messagebox.showerror("Error","Customer Name must be Alphabetically")
        elif self.c_phone.get()=="" or self.c_phone.get()== " ":
            messagebox.showerror("!! Notice !!","Customer Phone can't be Empty!")
        elif (self.c_phone.get()).isdigit()!= True:
            messagebox.showerror("Error","Mobile number must be Numeric Value!")
        elif len(self.c_phone.get()) <10 or len(self.c_phone.get()) >10:
            messagebox.showerror("Error","Mobile number must be of 10 digits!")
        elif self.c_email.get() == "" or self.c_email.get()==" ":
            messagebox.showerror("Error","Customer email can't be Empty!")
        # elif self.c_email.get()!=self.is_valid:
        #     messagebox.showerror("Error","Email is Invalid")

        elif self.total_cosmetic_price ==0 and self.total_fruits_price==0 and self.total_vegetables_price==0 and self.total_beverages_price==0:
            messagebox.showerror("!! Notice !!","No item is selected")

        
        # else:
        #     self.welcome_bill()
        
    # ====================== Generate Bill =============================
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\t\t Welcome to Grocery Store")
        self.txtarea.insert(END,f"\nBill Number: {self.c_bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\nCustomer Phone : {self.c_phone.get()}")
        self.txtarea.insert(END,f"\nCustomer Email : {self.c_email.get()}")
        self.txtarea.insert(END,f"\n=========================================================")
        self.txtarea.insert(END,"\n Products \t\t\t   Qty \t\t Price \t\t")
        self.txtarea.insert(END,f"\n=========================================================")

    def bill_area(self):
        self.cust_phone=self.c_phone.get()
        self.is_valid=validate_email(self.c_email.get(),verify=True)
        # if self.is_valid:
        #     messagebox.showinfo("Info","Valid Email")
        # else:
        #     messagebox.showerror("Error","Invalid email")
        
        if self.c_name.get()=="" or self.c_name.get()==" ":
            messagebox.showerror("Customer name Necessary","Enter Customer name")
        elif self.c_phone.get()=="":
            messagebox.showerror("Customer Phone no. is necessary","Enter Customer Phone no.")
        elif (self.c_phone.get()).isdigit()!= True:
            messagebox.showerror("Error","Mobile number must be Numeric Value!")
        elif len(self.c_phone.get()) <10 or len(self.c_phone.get()) >10:
            messagebox.showerror("Error","Mobile number must be of 10 digits!")
        elif self.c_email.get() == "" or self.c_email.get()==" ":
            messagebox.showerror("Error","Customer email can't be Empty!")
        
        # elif self.c_email.get()!=self.is_valid:
        #     messagebox.showerror("Error","Email is Invalid")
            
        elif self.total_cosmetic_price ==0 and self.total_fruits_price==0 and self.total_vegetables_price==0 and self.total_beverages_price==0:
            messagebox.showerror("Error","No item is selected")

        

        else:
            
            self.welcome_bill()
            # ====================== Cosmetic ==========================================
            if self.bth_soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap    \t\t\t {self.bth_soap.get()} \t\t {self.cos_bth_soap}")
            if self.shmpo.get()!=0:
                self.txtarea.insert(END,f"\n Shampoo      \t\t\t {self.shmpo.get()} \t\t {self.cos_shampoo}")
            if self.conditioner.get()!=0:
                self.txtarea.insert(END,f"\n Conditioner  \t\t\t {self.conditioner.get()} \t\t {self.cos_conditioner}")
            if self.facewash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash    \t\t\t {self.facewash.get()} \t\t {self.cos_facewash}")
            if self.hairoil.get()!=0:
                self.txtarea.insert(END,f"\n Hair Oil     \t\t\t {self.hairoil.get()} \t\t {self.cos_hairoil}")
            if self.lotion.get()!=0:
                self.txtarea.insert(END,f"\n Body Lotion  \t\t\t {self.lotion.get()} \t\t {self.cos_lotion}")
            if self.sunscreen.get()!=0:
                self.txtarea.insert(END,f"\n Sunscreen    \t\t\t {self.sunscreen.get()} \t\t {self.cos_sunscreen}")
            if self.moisture.get()!=0:
                self.txtarea.insert(END,f"\n Moisturizer  \t\t\t {self.moisture.get()} \t\t {self.cos_moisture}")
            if self.foundation.get()!=0:
                self.txtarea.insert(END,f"\n Foundation   \t\t\t {self.foundation.get()} \t\t {self.cos_foundation}")

            # =+=========================Fruits ======================================
            if self.apple.get()!=0:
                self.txtarea.insert(END,f"\n Apple        \t\t\t {self.apple.get()} \t\t {self.fruits_apple}")
            if self.banana.get()!=0:
                self.txtarea.insert(END,f"\n Banana       \t\t\t {self.banana.get()} \t\t {self.fruits_banana}")
            if self.grapes.get()!=0:
                self.txtarea.insert(END,f"\n Grapes       \t\t\t {self.grapes.get()} \t\t {self.fruits_grapes}")
            if self.guava.get()!=0:
                self.txtarea.insert(END,f"\n Guava        \t\t\t {self.guava.get()} \t\t {self.fruits_guava}")
            if self.pears.get()!=0:
                self.txtarea.insert(END,f"\n Pears        \t\t\t {self.pears.get()} \t\t {self.fruits_pears}")
            if self.pomergranates.get()!=0:
                self.txtarea.insert(END,f"\n Pomergranate \t\t\t {self.pomergranates.get()} \t\t {self.fruits_pomergranates}")
            if self.apricot.get()!=0:
                self.txtarea.insert(END,f"\n Apricot      \t\t\t {self.apricot.get()} \t\t {self.fruits_apricot}")
            if self.dragon.get()!=0:
                self.txtarea.insert(END,f"\n Dragon Fruit \t\t\t {self.dragon.get()} \t\t {self.fruits_dragon}")
            if self.pineapple.get()!=0:
                self.txtarea.insert(END,f"\n Pineapple    \t\t\t {self.pineapple.get()} \t\t {self.fruits_pineapple}")

            # ==============================Vegetables =============================================
            if self.potatao.get()!=0:
                self.txtarea.insert(END,f"\n Potato       \t\t\t {self.potatao.get()} \t\t {self.veg_potatao}")
            if self.tamato.get()!=0:
                self.txtarea.insert(END,f"\n Tamato       \t\t\t {self.tamato.get()} \t\t {self.veg_tamato}")
            if self.mushroom.get()!=0:
                self.txtarea.insert(END,f"\n Mushroom     \t\t\t {self.mushroom.get()} \t\t {self.veg_mushroom}")
            if self.carrot.get()!=0:
                self.txtarea.insert(END,f"\n Carrot       \t\t\t {self.carrot.get()} \t\t {self.veg_carrot}")
            if self.peas.get()!=0:
                self.txtarea.insert(END,f"\n Peas         \t\t\t {self.peas.get()} \t\t {self.veg_peas}")
            if self.bittergouard.get()!=0:
                self.txtarea.insert(END,f"\n BitterGouard \t\t\t {self.bittergouard.get()} \t\t {self.veg_bittergouard}")
            if self.pumpkin.get()!=0:
                self.txtarea.insert(END,f"\n Pumpkin      \t\t\t {self.pumpkin.get()} \t\t {self.veg_pumpkin}")
            if self.capsicum.get()!=0:
                self.txtarea.insert(END,f"\n Capsicum     \t\t\t {self.capsicum.get()} \t\t {self.veg_capsicum}")
            if self.cabbage.get()!=0:
                self.txtarea.insert(END,f"\n Cabbage      \t\t\t {self.cabbage.get()} \t\t {self.veg_cabbage}")

            # =================================Beaverages =================================================
            if self.dew.get()!=0:
                self.txtarea.insert(END,f"\n Mountain Dew \t\t\t {self.dew.get()} \t\t {self.bev_dew}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite       \t\t\t {self.sprite.get()} \t\t {self.bev_sprite}")
            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca        \t\t\t {self.limca.get()} \t\t {self.bev_limca}")
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti       \t\t\t {self.frooti.get()} \t\t {self.bev_frooti}")
            if self.mixed_juice.get()!=0:
                self.txtarea.insert(END,f"\n Mixed Juice  \t\t\t {self.mixed_juice.get()} \t\t {self.bev_mixed_juice}")
            if self.natural_juice.get()!=0:
                self.txtarea.insert(END,f"\n Natural Juice\t\t\t {self.natural_juice.get()} \t\t {self.bev_natural_juice}")
            if self.coffee.get()!=0:
                self.txtarea.insert(END,f"\n Coffee       \t\t\t {self.coffee.get()} \t\t {self.bev_coffee}")
            if self.energy_drink.get()!=0:
                self.txtarea.insert(END,f"\n Energy Drink \t\t\t {self.energy_drink.get()} \t\t {self.bev_energy_drink}")
            if self.beer.get()!=0:
                self.txtarea.insert(END,f"\n Beer         \t\t\t {self.beer.get()} \t\t {self.bev_beer}")

            self.txtarea.insert(END,f"\n.........................................................")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax  \t\t\t\t\t {self.cosmetic_tax.get()}")
            if self.fruits_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Fruits Tax    \t\t\t\t\t {self.fruits_tax.get()}")
            if self.vegetables_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Vegetables Tax \t\t\t\t\t {self.vegetables_tax.get()}")
            if self.beverages_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Beverage Tax   \t\t\t\t\t {self.beverages_tax.get()}")

            self.txtarea.insert(END,f"\n Total Bill : {self.Total_bill}")
            self.txtarea.insert(END,f"\n.........................................................")
            self.save_bill()
    
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save bill? ")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("/home/dheeraj/Bills/"+(str(self.c_bill_no.get()))+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Bill Saved","Bill Saved Successfully!")
        else:
            return
    

    def save_pdf(self):
        op = messagebox.askyesno("Notification", "Do you want to save bill as pdf? ")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            
            # Use a directory like the user's home directory
            directory = os.path.expanduser("/home/dheeraj/Bills/")  # User's home directory
            filename = f"{self.c_name.get()}_{self.c_bill_no.get()}.pdf"
            file_path = os.path.join(directory, filename)
            
            try:
                # Create a PDF file
                c = canvas.Canvas(file_path, pagesize=letter)
                width, height = letter
                
                # Draw the text into the PDF with a monospaced font
                text_object = c.beginText(40, height - 20)
                text_object.setFont("Courier", 12)  # Use Courier for fixed-width
                for line in self.bill_data.splitlines():
                    # Replace tab characters with spaces
                    line = line.replace('\t', '    ')
                    text_object.textLine(line)
                c.drawText(text_object)
                c.showPage()
                c.save()
                
                messagebox.showinfo("Inforamtion", f"Bill saved as {file_path}")
            except Exception as e:
                messagebox.showerror("Save Error", f"An error occurred: {e}")
        else:
            return
    
    def find_bill(self):
        present="no"
        for i in os.listdir("/home/dheeraj/Bills/"):
            if i.split('.')[0]==str(self.c_name.get())+str(self.c_bill_no.get()):
                f1=open(f"/home/dheeraj/Bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if  present=="no":
            messagebox.showerror("Error", "Bill not found")
    
    def get_bill_data(self):
        self.bill_data = ""
        for self.line in self.txtarea.get("1.0", END).splitlines():
            self.bill_data += self.line + "\n"
        return self.bill_data
    
        

    def clear_data(self):
        op=messagebox.askyesno("Notice","Do you really want to Clear?")
        if op>0:
        # =============Cosmetic====================================
        
            self.bth_soap.set(0)
            self.shmpo.set(0)
            self.conditioner.set(0)
            self.facewash.set(0)
            self.lotion.set(0)
            self.hairoil.set(0)
            self.sunscreen.set(0)
            self.moisture.set(0)
            self.foundation.set(0)
            

            # =============Fruits====================================

            self.apple.set(0)
            self.banana.set(0)
            self.grapes.set(0)
            self.guava.set(0)
            self.pears.set(0)
            self.pomergranates.set(0)
            self.apricot.set(0)
            self.dragon.set(0)
            self.pineapple.set(0)

            # =============Vegetables====================================

            self.potatao.set(0)
            self.tamato.set(0)
            self.mushroom.set(0)
            self.carrot.set(0)
            self.peas.set(0)
            self.bittergouard.set(0)
            self.pumpkin.set(0)
            self.capsicum.set(0)
            self.cabbage.set(0)

            # =============beverages====================================

            self.dew.set(0)
            self.sprite.set(0)
            self.limca.set(0)
            self.frooti.set(0)
            self.mixed_juice.set(0)
            self.natural_juice.set(0)
            self.coffee.set(0)
            self.energy_drink.set(0)
            self.beer.set(0)

            # ==================== total price and total tax variable ==============================
            self.cosmetic_price.set("")
            self.fruits_price.set("")
            self.vegetables_price.set("")
            self.beverages_price.set("")

            self.cosmetic_tax.set("")
            self.fruits_tax.set("")
            self.vegetables_tax.set("")
            self.beverages_tax.set("")

            # ============== Customer =======================
            self.c_name.set("")
            self.c_phone.set("")
            self.c_bill_no.set("")
            self.search_bill.set("")
            self.c_email.set("")
            x=random.randint(1,1000)
            self.c_bill_no.set(str(x))
            self.txtarea.delete('1.0',END)

    # def share(self):
    #     # Email details
    #     self.sender_email = "btcl220010159010gjust@gmail.com"
    #     self.receiver_email = self.c_email.get()
    #     self.app_password = "ygzg iegt icij hyfr"  # Use the generated app password here

    #     # Email subject and body
    #     self.subject = f"Your Order Confirmation: {self.c_bill_no.get()}"
    #     self.body = f"""Dear {self.c_name.get()},\n 
    # Thank you for your recent order! Your order number is {self.c_bill_no.get()}\n
    # Your Bill details are as below : \n
    # {self.get_bill_data()}\n
    
    # We appreciate your business and look forward to serving you again soon..\n
    # Best regards, \n
    # Nitin Grocery Store """

    #     self.msg = MIMEMultipart()
    #     self.msg['From'] = self.sender_email
    #     self.msg['To'] = self.receiver_email
    #     self.msg['Subject'] = self.subject
    #     self.msg.attach(MIMEText(self.body, 'plain'))

    #     try:
    #         self.server = smtplib.SMTP('smtp.gmail.com', 587)
    #         self.server.starttls()
    #         self.server.login(self.sender_email, self.app_password)  # Use app password here
    #         self.server.sendmail(self.sender_email, self.receiver_email, self.msg.as_string())
    #         self.server.quit()

    #         # print("Email sent successfully!")
    #         messagebox.showinfo("Message","Email Sent Successfuly")
    #     except Exception as e:
    #         # print(f"Failed to send email: {e}")
    #         messagebox.showerror("Error",f"Failed to send email: {e}")
    def share(self):
        self.sender_email="btcl220010159010gjust@gmail.com"
        self.receiver_email=self.c_email.get()
        self.app_password="ygzg iegt icij hyfr"
        self.subj=f"Grocery Bill on your demand: {self.c_bill_no.get()}"
        self.body=f"""Dear {self.c_name.get()},\n 
Thank you for your recent order! Your order number is {self.c_bill_no.get()}\n
Your Bill is attached with this email as your demand. Download from there : \n
We appreciate your business and look forward to serving you again soon..\n
Best regards, \n
Nitin Grocery Store\n Address: Near GJUST, Hisar """
        k=sendpdf(self.sender_email,self.receiver_email,self.app_password,self.subj,self.body,self.c_name.get()+"_"+self.c_bill_no.get(),"/home/dheeraj/Bills")
        try:
            k.email_send()
            print("Email sent successfully!")
            messagebox.showinfo("Message","Email Sent Successfuly")
        except Exception as e:
            print(f"Failed to send email: {e}")
            messagebox.showerror("Error",f"Failed to send email: {e}")
            
    def payment(self):
        # self.upi_id="dheerajsaroha2892002@oksbi"
        # self.phonepe_url=f"upi://pay?pa={self.upi_id}&pn=Recipient%20Nitin Grocery Store&am={self.Total_bill}"
        # self.google_pay=f"upi://pay?pa={self.upi_id}&pn=Recipient%20Nitin Grocery Store&am={self.Total_bill}"
        # self.paytm_url=f"upi://pay?pa={self.upi_id}&pn=Recipient%20Nitin Grocery Store&am={self.Total_bill}"
        
        # self.phonepe_qr=qrcode.make(self.phonepe_url)
        # self.google_pay_qr=qrcode.make(self.google_pay)
        # self.paytm_qr=qrcode.make(self.paytm_url)
        # messagebox.showinfo("Payment",f"{self.google_pay_qr.show()}")
        
        # UPI details
        self.upi_id = "dheerajsaroha2892002@oksbi"
        self.phonepe_url = f"upi://pay?pa={self.upi_id}&pn=Recipient%20Nitin%20Grocery%20Store&am={self.Total_bill}"
        self.google_pay_url = f"upi://pay?pa={self.upi_id}&pn=Recipient%20Nitin%20Grocery%20Store&am={self.Total_bill}"
        self.paytm_url = f"upi://pay?pa={self.upi_id}&pn=Recipient%20Nitin%20Grocery%20Store&am={self.Total_bill}"
        
        # Generate QR codes
        self.phonepe_qr = qrcode.make(self.phonepe_url)
        self.google_pay_qr = qrcode.make(self.google_pay_url)
        self.paytm_qr = qrcode.make(self.paytm_url)
        
        # UI Elements
        self.qr_label = Label(self.root)
        self.qr_label.pack(pady=20)
        img = self.google_pay_qr._img  # Access the QR code image from the qrcode object
        self.show_qr_code_dialog(img)
        
    # def show_qr_code(self, qr_image):
    #     # Resize QR code for display
    #     qr_image = qr_image.resize((200, 200), Image.Resampling.LANCZOS)
    #     qr_image_tk = ImageTk.PhotoImage(qr_image)
    #     self.qr_label.config(image=qr_image_tk)
    #     self.qr_label.image = qr_image_tk
        
    def show_qr_code_dialog(self, qr_image, timeout=30):
        # Create a top-level window for the QR code
        qr_window = Toplevel(self.root)
        qr_window.title("Scan QR Code")
        qr_window.geometry("300x400")

        qr_image = qr_image.resize((200, 200), Image.Resampling.LANCZOS)
        qr_image_tk = ImageTk.PhotoImage(qr_image)
        qr_label = Label(qr_window, image=qr_image_tk)
        qr_label.image = qr_image_tk  # Keep a reference
        qr_label.pack(pady=10)

        timer_label = Label(qr_window, text=f"Time left: {timeout} seconds")
        timer_label.pack(pady=5)

        def update_timer():
            nonlocal timeout
            timeout -= 1
            timer_label.config(text=f"Time left: {timeout} seconds")
            if timeout <= 0:
                qr_window.destroy()
                self.show_payment_status(False)
            else:
                qr_window.after(1000, update_timer)  # Update every second

        qr_window.after(1000, update_timer)

        # Simulate Payment Buttons
        def simulate_success():
            qr_window.destroy()
            self.show_payment_status(True)

        def simulate_failure():
            qr_window.destroy()
            self.show_payment_status(False)

        success_button = Button(qr_window, text="Simulate Payment Success", command=simulate_success)
        success_button.pack(pady=5)

        failure_button = Button(qr_window, text="Simulate Payment Failure", command=simulate_failure)
        failure_button.pack(pady=5)

    def show_payment_status(self, success):
        if success:
            messagebox.showinfo("Payment Status", "Payment Successful!")
        else:
            messagebox.showwarning("Payment Status", "Payment Failed! Please try again.")
        
        


    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()
    

    def go_to_first_page(self):
        # Destroy the current page (first page)
        for widget in self.root.winfo_children():
            widget.destroy()
        # Open the second page
        FirstPage(self.root)
        

 

application=FirstPage(root)
root.mainloop()