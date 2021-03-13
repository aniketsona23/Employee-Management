from tkinter import *
from tkinter import messagebox as msg
import sql_use
import admin


def login(event):
    if user_ent.get() == "" or pass_ent.get() == "":
        msg.showerror("Error", "Please enter all details !")

    elif (user_ent.get(), pass_ent.get()) in sql_use.fetch_data("employee_login"):
        user_ent.config(highlightbackground="green")
        pass_ent.config(highlightbackground="green")
        msg.showinfo("Welcome", " Login Successful !")
        login_win.destroy()
        admin.admin_work()
    else:
        msg.showerror("Invalid Details", "Username or Password is incorrect !")


if __name__ == '__main__':
    login_win = Tk()

    login_win.geometry("800x500")
    login_win.title("Login Window")
    login_win.config(bg="#ffee58")
    login_win.resizable(0, 0)

    login_frame = PanedWindow(login_win, bd=6, relief=RIDGE, width=600, height=370, bg="navy").place(x=100, y=50)

    Label(login_frame, text="Username", font=('Bahnschrift semibold SemiCondensed', 26),
          bg="navy", fg="#ffee58").place(x=200, y=145)

    Label(login_frame, text="Password", font=('Bahnschrift semibold SemiCondensed', 26),
          bg="navy", fg="#ffee58").place(x=200, y=210)

    user_ent = Entry(login_frame, width=15, font=('Bahnschrift semilight Condensed', 23), highlightthickness=1, bd=4,
                     relief=SUNKEN, highlightbackground="black")

    pass_ent = Entry(login_frame, width=15, font=("Bahnschrift semilight Condensed", 23), highlightthickness=1, bd=4,
                     show="*", relief=SUNKEN, highlightbackground="black")

    Button(login_frame, text="Login", font=("Bahnschrift semibold SemiCondensed", 20), bd=3, bg="#ffee58",
           fg="navy", width=10, command=lambda: login(None))

    user_ent.place(x=390, y=153, height=40)
    pass_ent.place(x=390, y=219, height=40)

    user_ent.bind("<Return>", login)
    pass_ent.bind("<Return>", login)

    login_win.mainloop()
