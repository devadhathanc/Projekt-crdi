import random
import datetime
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
root=Tk()
root.title("CS Project")
root.geometry("350x360")
root.resizable(False,False)


def booktab():
    labelmn=Label(root,text="BOOKINGS", font="Cordia 20 bold",bg="grey",fg="black")
    labelmn.pack(fill="both")

    def btab():
        labelmn.destroy()
        rinfo_but.destroy()
        rserv_but.destroy()
        pay_but.destroy()
        exit_but.destroy()
        bookings_but.destroy()
        labelrb1=Label(root,text="ROOM BOOKINGS", font="Cordia 20 bold",bg="grey",fg="black")
        labelrb1.pack(fill="both")
        all_lbl=Label(root,text="",font="lucida 10",fg="black")
        all_lbl.place(x=95,y=320)
        global phone_value

        #backend
        def verify():
            
            name = name_value.get()
            phone = phone_value.get()
            datein = dtin_value.get()
            dateout = dtout_value.get()
            location = loc_value.get()

            def is_number(n):
                is_number = True
                try:
                    num = int(n)
                except ValueError:
                    is_number = False
                return is_number
            def nu(n):
                for i in n:
                    if i in "1234567890/":
                        nu=True
                    else:
                        nu=False
                        break
                


            if name=="":
                messagebox.showerror("Error","Please enter your name")
            elif phone=="":
                messagebox.showerror("Error","Please enter your correct phone number")
            elif is_number(phone)==False:
                messagebox.showerror("Error","Please enter your correct phone number")
            
            elif datein=="":
                messagebox.showerror("Error","Please enter the correct date")
            elif nu(datein)==False:
                messagebox.showerror("Error","Please enter your correct date")
            elif dateout=="":
                messagebox.showerror("Error","Please enter correct the correct date")
            elif nu(dateout)==False:
                messagebox.showerror("Error","Please enter your correct date")
            elif location=="":
                messagebox.showerror("Error","Please enter the Location")
            else:
                all_lbl.config(text="All Good👍, Proceed Further",font="lucida 9 bold italic")
                vr_but.destroy()
                global nxt1_but
                nxt1_but=Button(root,text="NEXT",font="lucida 8 bold",command=nxt)
                nxt1_but.place(x=115,y=280)

                #backend--which creates a new file
                with open(name+'.txt','w') as f:
                    f.write('Name:'+name+'\n')
                    f.write('Phone No:'+phone+'\n')
                    f.write('From:'+datein+'\n')
                    f.write('Till:'+dateout+'\n')
                    f.write('Destination:'+location+'\n')
                
                #backend--which stores in the databases
                store_list=(name,phone,datein,dateout,location)

                mycon=mysql.connector.connect(host='localhost',user='root',passwd='mypass',database='csproj')
                cursor=mycon.cursor()
                sql_insert_val = 'insert into bookings_management(Name,Phone,date_in,date_out,locations) values(%s,%s,%s,%s,%s)'
                cursor.execute(sql_insert_val,store_list)         # should already have a table named "bookings_management"
                mycon.commit()
                mycon.close()

        
        def nxt():
            nxt1_but.destroy()
            global rbill
            rbill={}
            def back():
                labelrb1.destroy()
                etbut.destroy()
                bk_but.destroy()
                lbl1.destroy()
                l.destroy()
                l1.destroy()
                l2.destroy()
                l3.destroy()
                b1.destroy()
                b2.destroy()
                b3.destroy()
                b4.destroy()
                btab()

            def book():
                l.destroy()
                l1.destroy()
                l2.destroy()
                l3.destroy()
                b1.destroy()
                b2.destroy()
                b3.destroy()
                b4.destroy()
                bk_but.destroy()
                etbut.destroy()
                
                def bck():
                    extbut.destroy()
                    lbl1.destroy()
                    lb.destroy()
                    lb1.destroy()
                    lb2.destroy()
                    labelrb1.destroy()
                    btab()
                    
                
                t1=b1val.get()
                t2=b2val.get()
                t3=b3val.get()
                t4=b4val.get()
                global trbill
                trbill=t1*3500+t2*4000+t3*4500+t4*5000
                rbill["Room Charge"]=trbill

                lbl1.config(text="Booking Confirmed!",font="lucida 13 bold italic underline")
                extbut = Button(root,text=" BACK ",font="lucida 8 bold", command=bck, activebackground="gray")
                extbut.place(x=10,y=50)

            
                for x,y in rbill.items():
                        lb=Label(root,text=x+"   ----->   "+str(y),font="lucida 10 italic",fg="black")
                        lb.pack(padx=2,pady=5)

                g=trbill
                lb1=Label(root,text="________________________",font="bold 7")
                lb1.pack(padx=3,pady=2)
                lb2=Label(root,text="Total     --->     "+str(g)+" Rs.",font="lucida 10 italic")
                lb2.pack(padx=3,pady=2)


                
                


            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            name_entry.destroy()
            phone_entry.destroy()
            dtin_entry.destroy()
            dtout_entry.destroy()
            loc_entry.destroy()
            clr1_but.destroy()
            vr_but.destroy()
            extbut.destroy()
            all_lbl.destroy()

            etbut = Button(root,text=" BACK ",font="lucida 8 bold", command=back, activebackground="gray")
            etbut.place(x=225,y=280)
            bk_but=Button(root,text="BOOK",font="lucida 8 bold",command=book)
            bk_but.place(x=90,y=280)
            lbl1= Label(root,text="Select Rooms",font="Cordia 12 bold ",fg="black")
            lbl1.pack(padx=10,pady=20)
            l = Label(root, text = "1. Standard Non-AC - Rs. 3500",font="lucida 9")
            l.place(x=100,y=90)
            l1 = Label(root, text = "2. Standard AC - Rs. 4000",font="lucida 9")
            l1.place(x=100,y=110)
            l2 = Label(root, text = "3. 3-Bed Non-AC - Rs. 4500",font="lucida 9")
            l2.place(x=100,y=130)
            l3 = Label(root, text = "3-Bed AC - Rs. 5000",font="lucida 9")
            l3.place(x=100,y=150)

            b1val=IntVar()
            b2val=IntVar()
            b3val=IntVar()
            b4val=IntVar()
            b1 = Entry(root,width=3,textvariable=b1val)
            b2 = Entry(root,width=3,textvariable=b2val)
            b3 = Entry(root,width=3,textvariable=b3val)
            b4 = Entry(root,width=3,textvariable=b4val)
            b1.place(x=300,y=90)
            b2.place(x=300,y=110)
            b3.place(x=300,y=130)
            b4.place(x=300,y=150)
        
        def clear():
            name_entry.delete(0,END)
            phone_entry.delete(0,END)
            dtin_entry.delete(0,END)
            dtout_entry.delete(0,END)
            loc_entry.delete(0,END)

        def exit():
            labelrb1.destroy()
            label1.destroy()
            label2.destroy()
            label3.destroy()
            label4.destroy()
            label5.destroy()
            extbut.destroy()
            name_entry.destroy()
            phone_entry.destroy()
            dtin_entry.destroy()
            dtout_entry.destroy()
            loc_entry.destroy()
            clr1_but.destroy()
            vr_but.destroy()
            booktab()
        


        #frontend
        

        label1=Label(root,text="Name",font="15")
        label1.place(x=30,y=70)

        label2=Label(root,text="Phone",font="15")
        label2.place(x=30,y=110)

        label3=Label(root,text="Date in",font="15")
        label3.place(x=30,y=150)

        label4=Label(root,text="Date out",font="15")
        label4.place(x=30,y=190)

        label5=Label(root,text="Location",font="15")
        label5.place(x=30,y=230)

        #entry
        name_value=StringVar()
        phone_value=StringVar()
        dtin_value=StringVar()
        dtout_value=StringVar()
        loc_value= StringVar()

        #input
        name_entry=Entry(root,font="10",bd=3,textvariable=name_value)
        phone_entry=Entry(root,font="10",bd=3,textvariable=phone_value)
        dtin_entry=Entry(root,font="10",bd=3,textvariable=dtin_value)
        dtout_entry=Entry(root,font="10",bd=3,textvariable=dtout_value)
        loc_entry=Entry(root,font="10",bd=3,textvariable=loc_value)

        #inputlocs
        name_entry.place(x=120,y=70)
        phone_entry.place(x=120,y=110)
        dtin_entry.place(x=120,y=150)
        dtout_entry.place(x=120,y=190)
        loc_entry.place(x=120,y=230)

        #button
        
        vr_but=Button(root,text="VERIFY",font="lucida 8 bold",command=verify)
        vr_but.place(x=50,y=280)    
        
        clr1_but=Button(root,text="CLEAR",font="lucida 8 bold",command=clear)
        clr1_but.place(x=165,y=280)

        extbut = Button(root,text=" BACK ",font="lucida 8 bold", command=exit, activebackground="gray")
        extbut.place(x=225,y=280)
    
    
    def ritab():
        labelmn.destroy()
        rinfo_but.destroy()
        rserv_but.destroy()
        pay_but.destroy()
        exit_but.destroy()
        bookings_but.destroy()

        labelrb2=Label(root,text="ROOM INFOS", font="Cordia 20 bold",bg="grey",fg="black")
        labelrb2.pack(fill="both")
        

        lbl= Label(root,text="Select the Room types below",font="Cordia 12 bold ",fg="black")
        lbl.pack(padx=10,pady=20)
        l = Label(root, text = "1 ---> Standard Non-AC Rooms\n2 ---> Standard AC Rooms         \n3 ---> 3 Bed Non-AC Rooms      \n4 ---> 3 Bed AC Rooms               \n")
        l.pack(padx=10,pady=10)

        def close():
            labelrb2.destroy()
            lbl.destroy()
            l.destroy()
            nxt2_but.destroy()
            nxt3_but.destroy()
            nxt4_but.destroy()
            nxt5_but.destroy()
            ext2_but.destroy()
            booktab()

        def one():
            lbl.config(text = "Standard Non-AC Rooms",font="Cordia 12 bold ",fg="black")
            l.config(text=("Room amenities include: \n1 Double Bed, Television, Telephone,Double-Door Cupboard,\n1 Coffee table with 2 sofa, Balcony and an attached washroom \nwith hot/cold water.\n"))
            
           

        def two():
            lbl.config(text = "Standard AC Rooms",font="Cordia 12 bold ",fg="black")
            l.config(text=("Room amenities include: \n1 Double Bed, Television, Telephone,Double-Door Cupboard, \n1 Coffee table with 2 sofa, Balcony and an attached \nwashroom with hot/cold water + Window/Split AC.\n"))


        def three():
            lbl.config(text = "3 Bed Non-AC Rooms",font="Cordia 12 bold ",fg="black")
            l.config(text=("Room amenities include: \n1 Double Bed + 1 Single Bed, Television,Telephone, \na Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1 Side table,\nBalcony with an Accent table with 2 Chair and an attached \nwashroom with hot/cold water.\n"))


        def four():
            lbl.config(text = "3 Bed AC Rooms",font="Cordia 12 bold ",fg="black")
            l.config(text=("Room amenities include: \n1 Double Bed + 1 Single Bed, Television, Telephone, \na Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1 Side table,\nBalcony with an Accent table with 2 Chair and an attached \nwashroom with hot/cold water + Window/Split AC.\n"))


        nxt2_but = Button(root, text = "1", activebackground="gray", command=one)
        nxt2_but.place(x=130,y=250)

        nxt3_but = Button(root, text = "2", activebackground="gray", command=two)
        nxt3_but.place(x=155,y=250)

        nxt4_but = Button(root, text = "3", activebackground="gray",command=three)
        nxt4_but.place(x=180,y=250)

        nxt5_but = Button(root, text = "4", activebackground="gray", command= four)
        nxt5_but.place(x=205,y=250)

        ext2_but = Button(root, text = "Close", command = close, activebackground="gray")
        ext2_but.place(x=155,y=310)


    def rstab():
        labelmn.destroy()
        rinfo_but.destroy()
        rserv_but.destroy()
        pay_but.destroy()
        exit_but.destroy()
        bookings_but.destroy()

        labelrb2=Label(root,text="ROOM SERVICES", font="Cordia 20 bold",bg="grey",fg="black")
        labelrb2.pack(fill="both")

        lbl1= Label(root,text="MENU CARD",font="Cordia 12 bold ",fg="black")
        lbl1.pack(padx=10,pady=20)
        l = Label(root, text = "")
        l.place(x=100,y=90)
        l1 = Label(root, text = "")
        l1.place(x=100,y=110)
        l2 = Label(root, text = "")
        l2.place(x=100,y=130)
        l3 = Label(root, text = "")
        l3.place(x=100,y=150)
        l4 = Label(root, text = "")
        l4.place(x=100,y=170)
        l5 = Label(root, text = "")
        l5.place(x=100,y=190)
        l6 = Label(root, text = "")
        l6.place(x=100,y=210)
        l7 = Label(root, text = "")
        l7.place(x=100,y=230)
        l8 = Label(root, text = "")
        l8.place(x=100,y=250)
        
        

        def close():
            labelrb2.destroy()
            lbl1.destroy()
            l.destroy()
            bvr_but.destroy()
            sp_but.destroy()
            mc_but.destroy()
            si_but.destroy()
            ic_but.destroy()
            ext2_but.destroy()
            ord_but.destroy()
            
            booktab()


        
        
        
        def beverages():
            
            bvr_but.destroy()
            sp_but.destroy()
            mc_but.destroy()
            si_but.destroy()
            ic_but.destroy()
            ord_but.destroy()
            global bill
            bill={}

            def done():
                
                al = [b1,b2,b3,b4,b5,b6,b7,b8]
                for i in al:
                    if i.get()=='':
                        i.insert(0,0)
                        i=i
                t1=int(b1.get())*20
                t2=int(b2.get())*25
                t3=int(b3.get())*25
                t4=int(b4.get())*25
                t5=int(b5.get())*30
                t6=int(b6.get())*50
                t7=int(b7.get())*70
                t8=int(b8.get())*70
                t=t1+t2+t3+t4+t5+t6+t7+t8
                bill["Beverages"]=t

            def bck():
                extbut.destroy()
                ord_but.destroy()
                lbl1.destroy()
                l.destroy()
                l1.destroy()
                l2.destroy()
                l3.destroy()
                l4.destroy()
                l5.destroy()
                l6.destroy()
                l7.destroy()
                l8.destroy()

                b1.destroy()
                b2.destroy()
                b3.destroy()
                b4.destroy()
                b5.destroy()
                b6.destroy()
                b7.destroy()
                b8.destroy()

                labelrb2.destroy()
                bvr_but.destroy()
                sp_but.destroy()
                mc_but.destroy()
                si_but.destroy()
                ic_but.destroy()
                d_but.destroy()
                rstab()


            extbut = Button(root,text=" BACK ",font="lucida 7", command=bck, activebackground="gray")
            extbut.place(x=125,y=310)
            d_but = Button(root, text = "DONE",font="lucida 7", command = done, activebackground="gray")
            d_but.place(x=175,y=310)
            ext2_but.destroy()
            lbl1.config(text = "BEVERAGES",font="Cordia 12 bold ",fg="black")
            l.config(text="1   Regular Tea............. 20.00", font="lucida 8")
            l1.config(text="2   Masala Tea.............. 25.00", font="lucida 8")
            l2.config(text="3   Coffee.................. 25.00", font="lucida 8")
            l3.config(text="4   Cold Drink.............. 25.00", font="lucida 8")
            l4.config(text="5   Bread Jam............... 30.00", font="lucida 8")
            l5.config(text="6   Veg. Sandwich........... 50.00", font="lucida 8")
            l6.config(text="7   Cheese Toast Sandwich... 70.00", font="lucida 8")
            l7.config(text="8   Grilled Sandwich........ 70.00", font="lucida 8")
            

            b1 = Entry(root,width=3)
            b2 = Entry(root,width=3)
            b3 = Entry(root,width=3)
            b4 = Entry(root,width=3)
            b5 = Entry(root,width=3)
            b6 = Entry(root,width=3)
            b7 = Entry(root,width=3)
            b8 = Entry(root,width=3)
            b1.place(x=300,y=90)
            b2.place(x=300,y=110)
            b3.place(x=300,y=130)
            b4.place(x=300,y=150)
            b5.place(x=300,y=170)
            b6.place(x=300,y=190)
            b7.place(x=300,y=210)
            b8.place(x=300,y=230)


            
           

        def soups():
            bvr_but.destroy()
            sp_but.destroy()
            mc_but.destroy()
            si_but.destroy()
            ic_but.destroy()
            ord_but.destroy()

            def done():
                al = [p1,p2,p3,p4,p5]
                for i in al:
                    if i.get()=='':
                        i.insert(0,0)
                        i=i
                t1=int(p1.get())*110
                t2=int(p2.get())*110
                t3=int(p3.get())*110
                
                t4=int(p4.get())*110
                t5=int(p5.get())*110

                t=t1+t2+t3+t4+t5
                bill["Soups"]=t

            def bck():
                extbut.destroy()
                ord_but.destroy()
                lbl1.destroy()
                l.destroy()
                l1.destroy()
                l2.destroy()
                l3.destroy()
                l4.destroy()
                l5.destroy()
                l6.destroy()
                l7.destroy()
                l8.destroy()

                p1.destroy()
                p2.destroy()
                p3.destroy()
                p4.destroy()
                p5.destroy()

                labelrb2.destroy()
                bvr_but.destroy()
                sp_but.destroy()
                mc_but.destroy()
                si_but.destroy()
                ic_but.destroy()
                d_but.destroy()
                rstab()

            extbut = Button(root,text=" BACK ",font="lucida 7", command=bck, activebackground="gray")
            extbut.place(x=125,y=310)
            d_but = Button(root, text = "DONE",font="lucida 7", command = done, activebackground="gray")
            d_but.place(x=175,y=310)
            ext2_but.destroy()
            lbl1.config(text = "SOUPS",font="Cordia 12 bold ",fg="black")
            l.config(text="9   Tomato Soup............ 110.00", font="lucida 8")
            l1.config(text="10   Hot & Sour............. 110.00", font="lucida 8")
            l2.config(text="11   Veg. Noodle Soup....... 110.00", font="lucida 8")
            l3.config(text="12   Sweet Corn............. 110.00", font="lucida 8")
            l4.config(text="13   Veg. Munchow........... 110.00", font="lucida 8")

            p1 = Entry(root,width=3)
            p2 = Entry(root,width=3)
            p3 = Entry(root,width=3)
            p4 = Entry(root,width=3)
            p5 = Entry(root,width=3)
            p1.place(x=300,y=90)
            p2.place(x=300,y=110)
            p3.place(x=300,y=130)
            p4.place(x=300,y=150)
            p5.place(x=300,y=170)
            
        def maincourse():
            bvr_but.destroy()
            sp_but.destroy()
            mc_but.destroy()
            si_but.destroy()
            ic_but.destroy()
            ord_but.destroy()


            def done():
                al = [m1,m2,m3,m4,m5,m6,m7,m8]
                for i in al:
                    if i.get()=='':
                        i.insert(0,0)
                        i=i
                t1=int(m1.get())*110
                t2=int(m2.get())*110
                t3=int(m3.get())*120
                t4=int(m4.get())*140
                t5=int(m5.get())*140
                t6=int(m6.get())*140
                t7=int(m7.get())*140
                t8=int(m8.get())*140

                t=t1+t2+t3+t4+t5+t6+t7+t8
                bill['Main Course']=t

            def bck():
                extbut.destroy()
                ord_but.destroy()
                lbl1.destroy()
                l.destroy()
                l1.destroy()
                l2.destroy()
                l3.destroy()
                l4.destroy()
                l5.destroy()
                l6.destroy()
                l7.destroy()
                l8.destroy()

                m1.destroy()
                m2.destroy()
                m3.destroy()
                m4.destroy()
                m5.destroy()
                m6.destroy()
                m7.destroy()
                m8.destroy()

                labelrb2.destroy()
                bvr_but.destroy()
                sp_but.destroy()
                mc_but.destroy()
                si_but.destroy()
                ic_but.destroy()
                d_but.destroy()
                rstab()

            extbut = Button(root,text=" BACK ",font="lucida 7", command=bck, activebackground="gray")
            extbut.place(x=125,y=310)
            d_but = Button(root, text = "DONE",font="lucida 7", command = done, activebackground="gray")
            d_but.place(x=175,y=310)
            ext2_but.destroy()
            lbl1.config(text = "MAIN COURSE",font="Cordia 12 bold ",fg="black")
            l.config(text="14   Shahi Paneer........... 110.00", font="lucida 8")
            l1.config(text="15   Kadai Paneer........... 110.00", font="lucida 8")
            l2.config(text="16   Palak Paneer........... 120.00", font="lucida 8")
            l3.config(text="17   Matar Mushroom......... 140.00", font="lucida 8")
            l4.config(text="18   Mix Veg................ 140.00", font="lucida 8")
            l5.config(text="19   Jeera Aloo............. 140.00", font="lucida 8")
            l6.config(text="20   Dal Fry................ 140.00", font="lucida 8")
            l7.config(text="21   Aloo Matar............. 140.00", font="lucida 8")

            m1 = Entry(root,width=3)
            m2 = Entry(root,width=3)
            m3 = Entry(root,width=3)
            m4 = Entry(root,width=3)
            m5 = Entry(root,width=3)
            m6 = Entry(root,width=3)
            m7 = Entry(root,width=3)
            m8 = Entry(root,width=3)
            m1.place(x=300,y=90)
            m2.place(x=300,y=110)
            m3.place(x=300,y=130)
            m4.place(x=300,y=150)
            m5.place(x=300,y=170)
            m6.place(x=300,y=190)
            m7.place(x=300,y=210)
            m8.place(x=300,y=230)


        def sindian():
            bvr_but.destroy()
            sp_but.destroy()
            mc_but.destroy()
            si_but.destroy()
            ic_but.destroy()
            ord_but.destroy()

            def done():
                al = [s1,s2,s3,s4,s5,s6,s7,s8]
                for i in al:
                    if i.get()=='':
                        i.insert(0,0)
                        i=i
                t1=int(s1.get())*90
                t2=int(s2.get())*110
                t3=int(s3.get())*100
                t4=int(s4.get())*110
                t5=int(s5.get())*130
                t6=int(s6.get())*130
                t7=int(s7.get())*130
                t8=int(s8.get())*140

                t=t1+t2+t3+t4+t5+t6+t7+t8
                bill["South Indian"]=t

            def bck():
                extbut.destroy()
                ord_but.destroy()
                lbl1.destroy()
                l.destroy()
                l1.destroy()
                l2.destroy()
                l3.destroy()
                l4.destroy()
                l5.destroy()
                l6.destroy()
                l7.destroy()
                l8.destroy()

                s1.destroy()
                s2.destroy()
                s3.destroy()
                s4.destroy()
                s5.destroy()
                s6.destroy()
                s7.destroy()
                s8.destroy()

                labelrb2.destroy()
                bvr_but.destroy()
                sp_but.destroy()
                mc_but.destroy()
                si_but.destroy()
                ic_but.destroy()
                d_but.destroy()
                rstab()

            extbut = Button(root,text=" BACK ",font="lucida 7", command=bck, activebackground="gray")
            extbut.place(x=125,y=310)
            d_but = Button(root, text = "DONE",font="lucida 7", command = done, activebackground="gray")
            d_but.place(x=175,y=310)
            ext2_but.destroy()
            lbl1.config(text = "SOUTH INDIAN",font="Cordia 12 bold ",fg="black")
            l.config(text="22   Plain Rice.............. 90.00", font="lucida 8")
            l1.config(text="23   Veg Pulao.............. 110.00", font="lucida 8")
            l2.config(text="24   Plain Dosa............. 100.00", font="lucida 8")
            l3.config(text="25   Onion Dosa............. 110.00", font="lucida 8")
            l4.config(text="26   Masala Dosa............ 130.00", font="lucida 8")
            l5.config(text="27   Paneer Dosa............ 130.00", font="lucida 8")
            l6.config(text="28   Rice Idli.............. 130.00", font="lucida 8")
            l7.config(text="29   Sambhar Vada........... 140.00", font="lucida 8")

            s1 = Entry(root,width=3)
            s2 = Entry(root,width=3)
            s3 = Entry(root,width=3)
            s4 = Entry(root,width=3)
            s5 = Entry(root,width=3)
            s6 = Entry(root,width=3)
            s7 = Entry(root,width=3)
            s8 = Entry(root,width=3)
            s1.place(x=300,y=90)
            s2.place(x=300,y=110)
            s3.place(x=300,y=130)
            s4.place(x=300,y=150)
            s5.place(x=300,y=170)
            s6.place(x=300,y=190)
            s7.place(x=300,y=210)
            s8.place(x=300,y=230)

        def icecreams():
            bvr_but.destroy()
            sp_but.destroy()
            mc_but.destroy()
            si_but.destroy()
            ic_but.destroy()
            ord_but.destroy()

            def done():
                al = [i1,i2,i3,i4,i5]
                for i in al:
                    if i.get()=='':
                        i.insert(0,0)
                        i=i
                t1=int(i1.get())*60
                t2=int(i2.get())*60
                t3=int(i3.get())*60
                t4=int(i4.get())*60
                t5=int(i5.get())*60

                t=t1+t2+t3+t4+t5
                bill["IceCreams"]=t

            def bck():
                extbut.destroy()
                ord_but.destroy()
                lbl1.destroy()
                l.destroy()
                l1.destroy()
                l2.destroy()
                l3.destroy()
                l4.destroy()
                l5.destroy()
                l6.destroy()
                l7.destroy()
                l8.destroy()

                i1.destroy()
                i2.destroy()
                i3.destroy()
                i4.destroy()
                i5.destroy()

                labelrb2.destroy()
                bvr_but.destroy()
                sp_but.destroy()
                mc_but.destroy()
                si_but.destroy()
                ic_but.destroy()
                d_but.destroy()
                rstab()

            extbut = Button(root,text=" BACK ",font="lucida 7", command=bck, activebackground="gray")
            extbut.place(x=125,y=310)
            d_but = Button(root, text = "DONE",font="lucida 7", command = done, activebackground="gray")
            d_but.place(x=175,y=310)
            ext2_but.destroy()
            lbl1.config(text = "ICE CREAMS",font="Cordia 12 bold ",fg="black")
            l.config(text="30   Vanilla................. 60.00", font="lucida 8")
            l1.config(text="31   Strawberry.............. 60.00", font="lucida 8")
            l2.config(text="32   Coffee.................. 60.00", font="lucida 8")
            l3.config(text="33   Pineapple............... 60.00", font="lucida 8")
            l4.config(text="34   Butter Scotch........... 60.00", font="lucida 8")

            i1 = Entry(root,width=3)
            i2 = Entry(root,width=3)
            i3 = Entry(root,width=3)
            i4 = Entry(root,width=3)
            i5 = Entry(root,width=3)
            i1.place(x=300,y=90)
            i2.place(x=300,y=110)
            i3.place(x=300,y=130)
            i4.place(x=300,y=150)
            i5.place(x=300,y=170)

            
        lr=[]
        def remv():
            for lb in lr:
                lb.destroy()


        def order():
            global t
            t=bill
            lbl1.destroy()
            bvr_but.destroy()
            sp_but.destroy()
            mc_but.destroy()
            si_but.destroy()
            ic_but.destroy()
            ord_but.destroy()
            ext2_but.destroy()
            lbl=Label(root,text="--FOOD COST--",font="lucida 15 italic underline", fg="black")
            lbl.pack(padx=10,pady=20)

            def bck():
                

                labelrb2.destroy()
                bvr_but.destroy()
                sp_but.destroy()
                mc_but.destroy()
                si_but.destroy()
                ic_but.destroy()
                lbl.destroy()
                extbut.destroy()
                lb1.destroy()
                lb2.destroy()
                remv()
                

                rstab()

            

            extbut = Button(root,text=" BACK ",font="lucida 7", command=bck, activebackground="gray")
            extbut.place(x=20,y=40)

            
            for x,y in bill.items():
                    lb=Label(root,text=x+"   ----->   "+str(y),font="lucida 9 italic",fg="black")
                    lb.pack(padx=3,pady=2)
                    lr.append(lb)
                
            g=sum(bill.values())
            lb1=Label(root,text="________________________",font="bold 7")
            lb1.pack(padx=3,pady=2)
            lb2=Label(root,text="Total     --->     "+str(g)+" Rs.",font="lucida 10 italic")
            lb2.pack(padx=3,pady=2)
            
            
            

            

        bvr_but = Button(root, text = "BEVERAGES",font=("lucida",10), activebackground="gray", command=beverages)
        bvr_but.place(relx=0.5,rely=0.5,anchor="center")
        bvr_but.pack(padx=10,pady=3)

        sp_but = Button(root, text = "SOUPS",font=("lucida",10), activebackground="gray", command=soups)
        sp_but.place(relx=0.5,rely=0.5,anchor="center")
        sp_but.pack(padx=10,pady=3)

        mc_but = Button(root, text = "MAIN COURSE",font=("lucida",10), activebackground="gray",command=maincourse)
        mc_but.place(relx=0.5,rely=0.5,anchor="center")
        mc_but.pack(padx=10,pady=3)

        si_but = Button(root, text = "SOUTH INDIAN",font=("lucida",10), activebackground="gray", command= sindian)
        si_but.place(relx=0.5,rely=0.5,anchor="center")
        si_but.pack(padx=10,pady=3)

        ic_but = Button(root, text = "ICE CREAMS",font=("lucida",10), activebackground="gray", command= icecreams)
        ic_but.place(relx=0.5,rely=0.5,anchor="center")
        ic_but.pack(padx=10,pady=3)

        ext2_but = Button(root, text = "CLOSE",font="lucida 7", command = close, activebackground="gray")
        ext2_but.place(x=125,y=310) 

        ord_but = Button(root, text = "ORDER",font="lucida 7", command = order, activebackground="gray")
        ord_but.place(x=175,y=310)
        


    def ptab():
        ph=phone_value.get()
        print(ph)
        labelmn.destroy()
        rinfo_but.destroy()
        rserv_but.destroy()
        pay_but.destroy()
        exit_but.destroy()
        bookings_but.destroy()

        labelrb2=Label(root,text="PAYMENTS", font="Cordia 20 bold",bg="grey",fg="black")
        labelrb2.pack(fill="both")
        
        def cont():
            
            phone_lst = phone2_value.get()
            

            if phone_lst==int(ph):
                lbl.destroy()
                lbl1.destroy()
                nxt1_but.destroy()
                phone2_entry.destroy()
                lb_l=Label(root,text="-- BILL --",font="lucida 15 italic underline", fg="black")
                lb_l.pack(padx=10,pady=20)

                def bck():

                    labelrb2.destroy()
                    extbut.destroy()
                    lbl.destroy()
                    extbut.destroy()
                    lb1.destroy()
                    lb2.destroy()
                    lb3.destroy()
                    lb4.destroy()
                    clr2_but.destroy()

                    rstab()

                extbut = Button(root,text=" BACK ",font="lucida 7", command=bck, activebackground="gray")
                extbut.place(x=20,y=40)
                
                
                room_cost=trbill
                food_cost=sum(t.values())
                print(room_cost,food_cost)
                g=room_cost+food_cost
                print(g)
                gst=round((18/100*g),2)
                tot=g+gst
                lb=Label(root,text="Room Charges     --->     "+str(room_cost)+" Rs.",font="lucida 10 italic")
                lb.pack(padx=3,pady=2)
                l_b=Label(root,text="Food Cost     --->     "+str(food_cost)+" Rs.",font="lucida 10 italic")
                l_b.pack(padx=3,pady=2)
                lb1=Label(root,text="________________________",font="bold 7")
                lb1.pack(padx=3,pady=2)
                lb2=Label(root,text="Subtotal     --->     "+str(g)+" Rs.",font="lucida 10 italic")
                lb2.pack(padx=3,pady=2)
                lb3=Label(root,text="     GST       --->     "+str(gst)+" Rs.",font="lucida 10 italic")
                lb3.pack(padx=3,pady=2)
                lb4=Label(root,text="  TOTAL     ----->     "+str(tot)+" Rs.",font="lucida 12 bold")
                lb4.pack(padx=3,pady=2)

            else:
                lb_norec=Label(root,text="No records associated with the number "+str(phone_lst)+"\nEnter a correct value",)
                lb_norec.pack(padx=1,pady=20)
                
                def clear1():
                    phone2_entry.delete(0,END)
                    lb_norec.destroy()
                clr2_but=Button(root,text="CLEAR",font="lucida 8 bold",command=clear1)
                clr2_but.place(x=165,y=280)

                
        def exit():
            extbut.destroy()
            lbl.destroy()
            lbl1.destroy()
            phone2_entry.destroy()
            nxt1_but.destroy()
            labelrb2.destroy()
            booktab()

        extbut = Button(root,text=" BACK ",font="lucida 7", command=exit, activebackground="gray")
        extbut.place(x=225,y=280)
        lbl=Label(root,text="Please enter your details below",font="lucida 13 italic ", fg="black")
        lbl.pack(padx=10,pady=40)
        phone2_value=IntVar()
        lbl1=Label(root,text="Phone : ",font="lucida 12 bold ", fg="black")
        lbl1.place(x=80,y=140)
        phone2_entry=Entry(root,font="8",bd=3,textvariable=phone2_value)
        phone2_entry.place(x=155,y=142,width=100,height=20)
        nxt1_but=Button(root,text="CONTINUE",font="lucida 7 bold",command=cont)
        nxt1_but.place(x=135,y=250)


    def etab():
        labelmn.destroy()
        rinfo_but.destroy()
        rserv_but.destroy()
        pay_but.destroy()
        exit_but.destroy()
        bookings_but.destroy()

        labelrb2=Label(root,text="HAPPY DAYS", font="Cordia 20 bold",bg="grey",fg="black")
        labelrb2.pack(fill="both")

    bookings_but=Button(text="  Bookings  ",command=btab,activebackground="gray")
    bookings_but.place(relx=0.5, rely=0.25, anchor=CENTER)

    rinfo_but = Button(text="  Rooms Info  ",command=ritab,activebackground="gray")
    rinfo_but.place(relx=0.5, rely=0.4, anchor=CENTER)

    rserv_but = Button(text="  Room services  ",command=rstab,activebackground="gray")
    rserv_but.place(relx=0.5, rely=0.55, anchor=CENTER)

    pay_but = Button(text="  Payments  ",command=ptab,activebackground="gray")
    pay_but.place(relx=0.5, rely=0.7, anchor=CENTER)

    exit_but = Button(text="   Exit   ",command=etab,activebackground="gray")
    exit_but.place(relx=0.5, rely=0.85, anchor=CENTER)
booktab()



root.mainloop()