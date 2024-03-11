#Login Screen:-
from tkinter import*
from tkinter import messagebox
import time

lg = Tk()

def login():
    email = t1.get()
    password = t2.get()
    
    rules = "[]{},/?!#$%^&*()-~`""/-+ "
    limit = len(email)
    
    space = email.count(" ")
    error_count = 0


    first_char = email[0]
    if (first_char.isalpha() and limit < 30):
            
        if  (("@gmail" in email and ".com" in email )):
            
            if any(char in rules for char in email):
                    messagebox.showerror("Error","Invalid Symbols are not allowed\nin Email!!!")
                    error_count+=1
                    clear()
                    
            else:
                print("")
                    
                if space == 0:
                    print("")
                    
                else:
                    messagebox.showerror("Error","Please Don't Leave\n Space in Email")
                    error_count+=1
        else:
            messagebox.showerror("Error","Invalid it's have not @ and . in Email!!!")
            clear()
            error_count+=1
    else:
        messagebox.showerror("Error","First Character\nmust be character")    
        error_count+=1
        
#password :-----
    
    length = len(password)

    if length <= 10:
        
        if any(char.isalpha() for char in password) and any(char.isnumeric() for char in password):
            
            print(".")
            
            if any(char in rules for char in password):
                if error_count == 0:
                    messagebox.showinfo("Welcome","Login Successfully")
                    lg.destroy()
                
            else:
                messagebox.showerror("Error","Please use Special Symbols in Password")
            
        else:
            messagebox.showerror("Error","Please Use alphabetical and also numeric in Password") 
            clear()       

    else:
        messagebox.showerror("Error","limit exceed in Password\nShould Be under (10)limit")
        clear()
    
    
    
def clear():
    t1.delete(0,END) 
    t2.delete(0,END)
    
    
def new_frame():
    global rg
    rg = Tk()
    rg.title("Rules Log-In")
    
    frrame = Frame(rg,bg="#CCFFCC")
    rg.config(bg="#CCFFCC")


    

    frrame.pack()
    rg.geometry("400x400")
    rg.after(15000,window)
    rule = Label(frrame,text="____Email-Rules____",font=("Arial",15,"bold"),bg="#CCFFCC",fg="#006600")
    rule.pack(pady=10)
     
    rule1 = Label(frrame,text="1.First Character must be character in Email.",font=("Arial",10,"bold"),bg="#CCFFCC",fg="#006600")
    rule1.pack()
    
    rule2 = Label(frrame,text="2.Compulsary to add @ and . in Email.",font=("Arial",10,"bold"),bg="#CCFFCC",fg="#006600")
    rule2.pack()
    
    rule3 = Label(frrame,text="3.Invalid Symbols are not allowed Examle:- %!&.",font=("Arial",10,"bold"),bg="#CCFFCC",fg="#006600")
    rule3.pack()
    
    rule_s = Label(frrame,text="____Password-Rules____",font=("Arial",15,"bold"),bg="#CCFFCC",fg="#006600")
    rule_s.pack(pady=10)
     
    rule4 = Label(frrame,text="4.limit exceed in Password Should Be under (10)limit.",font=("Arial",10,"bold"),bg="#CCFFCC",fg="#006600")
    rule4.pack()
    
    rule5 = Label(frrame,text="5.Please use Special Symbols in Password.",font=("Arial",10,"bold"),bg="#CCFFCC",fg="#006600")
    rule5.pack()
    
    rule6 = Label(frrame,text="6.Please Use alphabetical and also numeric in Password.",font=("Arial",10,"bold"),bg="#CCFFCC",fg="#006600")
    rule6.pack()
    
    
        
def window():
    rg.destroy()
         


lg.geometry("400x400")
lg.title("Log-In")
lg.config(bg="#FFFFFF")


frame = Frame(lg,bg="#FFFFFF")
frame.pack()



l = Label(frame,text="Log-In",bg="#FFFFFF",font=("Arial",22 ,"bold"),fg="#000000")
l.pack(pady=15)


l1 = Label(frame,text="E-Mail",bg="#FFFFFF",font="italic",fg="#000000")
l1.pack(pady=15)

t1 = Entry(frame,font=22)
t1.pack()


l2 = Label(frame,text="Password",bg="#FFFFFF",font="italic",fg="#000000")
l2.pack(pady=15)

t2 = Entry(frame,font=22)
t2.pack()

button = Button(frame,text="Login",font="bold",bg="#FFFFFF",command=login,fg="#000000")
button.pack(pady=20)

button1 = Button(frame,text="Clear",font="bold",bg="#FFFFFF",command=clear,fg="#000000")
button1.pack(pady=5)


message_label = Button(frame,bg="#FFFFFF",text="Rules",command=new_frame,fg="#000000")
message_label.pack(pady=15)


lg.mainloop()

