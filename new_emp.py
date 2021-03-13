from tkinter import *
from tkinter import messagebox as msg
import sql_use


def new_employee(notebook,tree, master, update=False):
    # Making the Window
    new_win = Toplevel(master=master)
    new_win.geometry("950x500")
    new_win.resizable(0, 0)
    new_win.title("New Employee")
    new_win.config(bg="navy")
    new_win.focus_force()

    def add():
        if id_ent.get() in sql_use.fetch_data("emp_data", "emp_id"):
            msg.showerror("Duplicate ID", "Employee with this id already exists !")
        else:
            try:
                variables = int(phone_ent.get()), int(base_ent.get()), int(med_ent.get()), int(adv_ent.get()), int(
                    bon_ent.get())

                variables = tuple(map(lambda x: -x if x < 0 else x, variables))

            except ValueError:
                msg.showerror("Invalid Input", "Please enter valid inputs")

            else:

                sno = len(tree[0].get_children()) + 1
                info_values = sno, name_ent.get(), id_ent.get(), variables[0], post_ent.get(),
                enter_ent.get(), leave_ent.get()
                salary_values = (sno, name_ent.get(), id_ent.get()) + variables[1:]

                if all(info_values + salary_values):

                    info_values_sql = f'''{sno},'{name_ent.get()}','{id_ent.get()}',{phone_ent.get()},
                                        '{post_ent.get()}', '{enter_ent.get()}','{leave_ent.get()}' '''
                    salary_values_sql = f'''{sno}, '{name_ent.get()}', '{id_ent.get()}', {base_ent.get()},
                                        {med_ent.get()},{adv_ent.get()},{bon_ent.get()}'''
                    if update:
                        answer = msg.askyesno("Confirmation", "Are you sure you want to update?")
                        if answer:
                            sql_use.update_data("emp_data", values=info_values_sql)
                            sql_use.update_data("emp_salary", values=salary_values_sql)
                            tree[0].item(selected, text="", values=info_values)
                            tree[1].item(selected, text="", values=salary_values)
                    else:
                        sql_use.insert_data("emp_data", values=info_values_sql)
                        sql_use.insert_data("employee_login",
                                            values=(id_ent.get(), phone_ent.get(), id_ent.get() + name_ent.get()[:4]))
                        sql_use.insert_data("emp_salary", values=salary_values_sql)

                        tree[0].insert("", END, values=info_values)
                        tree[1].insert("", END, values=salary_values)

                    msg.showinfo("Successful", "New Member Added Successfully !")
                else:
                    msg.showerror("Empty Fields", "Please Complete All Fields!")

    Label(new_win, text="Base Salary", font=('Bahnschrift semiBold SemiCondensed', 22), bg="navy", fg="#ffee58").place(
        x=500,
        y=30)
    Label(new_win, text="Medical", font=('Bahnschrift semiBold SemiCondensed', 22), bg="navy", fg="#ffee58").place(
        x=500, y=110)
    Label(new_win, text="Advance", font=('Bahnschrift semiBold SemiCondensed', 22), bg="navy", fg="#ffee58").place(
        x=500, y=190)
    Label(new_win, text="Bonus", font=('Bahnschrift semiBold SemiCondensed', 22), bg="navy", fg="#ffee58").place(x=500,
                                                                                                                 y=270)

    base_ent = Entry(new_win, font=('Bahnschrift semiLight SemiCondensed', 20), bd=4)
    med_ent = Entry(new_win, font=('Bahnschrift semiLight SemiCondensed', 20), bd=4)
    adv_ent = Entry(new_win, font=('Bahnschrift semiLight SemiCondensed', 20), bd=4)
    bon_ent = Entry(new_win, font=('Bahnschrift semiLight SemiCondensed', 20), bd=4)

    base_ent.place(x=670, y=30)
    med_ent.place(x=670, y=110)
    adv_ent.place(x=670, y=190)
    bon_ent.place(x=670, y=270)

    Label(new_win, text="Name", font=('Bahnschrift semiBold SemiCondensed', 22), relief=RIDGE, fg="navy", width=10,
          bd=4).place(x=10,
                      y=30)
    Label(new_win, text="ID", font=('Bahnschrift semiBold SemiCondensed', 21), relief=RIDGE, fg="navy", width=10,
          bd=4).place(x=10,
                      y=110)
    Label(new_win, text="Phone", font=('Bahnschrift semiBold SemiCondensed', 21), relief=RIDGE, fg="navy", width=10,
          bd=4).place(x=10,
                      y=190)
    Label(new_win, text="Post", font=('Bahnschrift semiBold SemiCondensed', 21), relief=RIDGE, fg="navy", width=10,
          bd=4).place(x=10,
                      y=270)
    Label(new_win, text="Enter Time", font=('Bahnschrift semiBold SemiCondensed', 21), relief=RIDGE, fg="navy",
          width=10, bd=4).place(
        x=10, y=350)
    Label(new_win, text="Leave Time", font=('Bahnschrift semiBold SemiCondensed', 21), relief=RIDGE, fg="navy",
          width=10, bd=4).place(
        x=500, y=350)

    name_ent = Entry(new_win, font=('Bahnschrift semiLight SemiCondensed', 20), bd=5)
    id_ent = Entry(new_win, font=('Bahnschrift semiLight SemiCondensed', 20), bd=5)
    phone_ent = Entry(new_win, font=('Bahnschrift semiLight SemiCondensed', 20), bd=5)
    post_ent = Entry(new_win, font=('Bahnschrift semiLight SemiCondensed', 20), bd=5)
    enter_ent = Entry(new_win, font=('Bahnschrift semiLight SemiCondensed', 20), bd=5)
    leave_ent = Entry(new_win, font=('Bahnschrift semiLight SemiCondensed', 20), bd=5)

    add_but = Button(new_win, text="Add", font=('Bahnschrift semiLight SemiCondensed', 20), bg='#ffee58', fg="navy",
                     width=15, command=add)
    add_but.place(x=370, y=430)

    name_ent.place(x=170, y=30)
    id_ent.place(x=170, y=110)
    phone_ent.place(x=170, y=190)
    post_ent.place(x=170, y=270)
    enter_ent.place(x=170, y=350)
    leave_ent.place(x=670, y=350)

    if update:

        selected = tuple(filter(all, (tree[0].selection(), tree[1].selection())))
        if len(selected) == 2:
            selected = tree[0].selection()

        # value=selected.
        print(selected)
        add_but["text"] = "Update"
        selected_emp = tree[0].item(selected)["values"]
        employee_data = sql_use.fetch_data("emp_data", condition=f"emp_id='{selected_emp[1]}'")[0]
        employee_salary = sql_use.fetch_data("emp_salary", condition=f"id='{selected_emp[1]}'")[0]

        name_ent.insert(0, employee_data[0])

        id_ent.insert(0, employee_data[1])
        phone_ent.insert(0, employee_data[2])
        post_ent.insert(0, employee_data[3])
        enter_ent.insert(0, employee_data[4])
        leave_ent.insert(0, employee_data[5])
        base_ent.insert(0, employee_salary[2])
        med_ent.insert(0, employee_salary[3])
        adv_ent.insert(0, employee_salary[4])
        bon_ent.insert(0, employee_salary[5])

    new_win.mainloop()


if __name__ == '__main__':
    new_employee(None,None, None)
