# This file is not yet used !
from tkinter import *
from tkinter import ttk, messagebox as msg
import sql_use


def employee_work(emp_id):
    employee_win = Tk()
    employee_win.geometry("500x400")

    name = sql_use.fetch_data("emp_data", "name", f"emp_id='{emp_id}'")
    employee_win.title(f"Employee - {name}")

    ntb = ttk.Notebook(employee_win, width=400, height=400)
    tab1 = Frame(ntb, background="navy")
    tab2 = Frame(ntb, background="navy")
    tab3 = Frame(ntb, background="navy")
    ntb.add(tab1, text="Change Password")
    ntb.add(tab2, text="Inbox")
    ntb.add(tab3, text="Request Advance")
    ntb.pack(fill="x")

    def tab1_work():
        def change_password():
            if all((new_pass.get(), cur_pass.get(), check_pass.get())):
                password = sql_use.fetch_data("employee_login", "password", condition=f"id='{emp_id}'")[0]
                if cur_pass.get() == password:
                    if new_pass.get() == check_pass.get():
                        sql_use.update_data("employee_login", f"password='{new_pass.get()}'", f"id='{emp_id}'")
                        new_pass.set("")
                        cur_pass.set("")
                        check_pass.set("")
                        msg.showinfo("Success", "Password Changed !")
                    else:
                        msg.showerror("Not matched", "Passwords don't match!")
                else:
                    msg.showerror("Invalid", "Current Password is Incorrect !")
            else:
                msg.showerror("Empty Fields", "Please Fill all Fields!")

        Label(tab1, text="Current Password", font=("Bahnschrift semibold SemiCondensed", 19), bg="navy",
              fg="#ffee58").place(x=20, y=60)
        Label(tab1, text="New Password", font=("Bahnschrift semibold SemiCondensed", 19), bg="navy",
              fg="#ffee58").place(x=20, y=140)
        Label(tab1, text="Retype Password", font=("Bahnschrift semibold SemiCondensed", 19), bg="navy",
              fg="#ffee58").place(x=20, y=220)

        cur_pass = StringVar()
        new_pass = StringVar()
        check_pass = StringVar()
        Entry(tab1, textvariable=cur_pass, font=("Bahnschrift semiLight SemiCondensed", 17), show="*", bd=5).place(
            x=220, y=60)
        Entry(tab1, textvariable=new_pass, font=("Bahnschrift semiLight SemiCondensed", 17), show="*", bd=5).place(
            x=220, y=140)
        Entry(tab1, textvariable=check_pass, font=("Bahnschrift semiLight SemiCondensed", 17), show="*", bd=5).place(
            x=220, y=220)

        Button(tab1, text="Change Password", font=("Bahnschrift semiLight SemiCondensed", 17), bg="#ffee58",
               fg="navy", command=change_password).place(x=140, y=300)

    def tab2_work():
        pass

    def tab3_work():
        Label(tab3, text="Amount", font=("Bahnschrift semiLight SemiCondensed", 20), fg="#ffee58",
              bg="navy").place(x=50, y=50)
        Label(tab3, text="Reason", font=("Bahnschrift semiLight SemiCondensed", 20), fg="#ffee58",
              bg="navy").place(x=50, y=150)

        def request_adv():
            if amount.get() >= 500 and reason.get(0.0, END):
                confirm = msg.askyesno("Confirm", "Confirm your Advance Request ...")
                if confirm:
                    sql_use.insert_data("advance_request", f"'{emp_id}',{amount.get()}, '{reason.get(0.0, END)}'")
                    msg.showinfo("Success", "Sent Request")
                    amount.set(0)
                    reason.delete(0.0, END)
                else:
                    pass
            elif amount.get() < 500:
                msg.showerror("Invalid Amount", "Please enter more than limit")
            elif not reason.get(0.0, END):
                msg.showerror("Reason", "Please enter a reason")

        amount = IntVar()
        Entry(tab3, textvariable=amount, font=("Bahnschrift semiLight SemiCondensed", 17), bd=5).place(x=170, y=50)
        reason = Text(tab3, font=("Bahnschrift semiLight SemiCondensed", 17), width=25, height=5, bd=3)
        reason.place(x=170, y=120)

        Button(tab3, text="Request", font=("Bahnschrift semiLight SemiCondensed", 17), fg="navy", bg="#ffee58",
               command=request_adv).place(x=150, y=310)

    tab1_work()
    tab2_work()
    tab3_work()
    ntb.select(tab3)
    employee_win.mainloop()


if __name__ == '__main__':
    employee_work("ASA - 1")
