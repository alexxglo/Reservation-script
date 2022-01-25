import tkinter
from tkinter import *
import tkinter.messagebox
from datetime import date
import datetime
import calendar
from HoverInfo import HoverInfo
# this creates lists available in the form dropdowns.
list_of_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
list_of_classes = [1, 2, 3, 4, 5]


def make_order_of_days():
    tuple_days = []
    for i in range(8):
        tuple_days.append((i + 1, calendar.day_name[(date.today() + datetime.timedelta(days=i)).weekday()]))
    return tuple_days


def convert_day_to_current_value(day, current_days_list):
    for i in range(7):
        if day == current_days_list[i][1]:
            return current_days_list[i][0]


def disable_button(submit_btn):
    submit_btn.config(state=DISABLED)
    submit_btn.update()


def on_click():
    tkinter.messagebox.showinfo("Congratulations!", "Your request was succesful!")
    root.destroy()

def hide_me(event):
    event.place_forget()


def get_data():
    days_ordered = make_order_of_days()
    day_chosen = convert_day_to_current_value(day_selected.get(), days_ordered)
    us_input = {"username": username.get(), "password": password.get(), "day_selected": day_chosen,
                "gym_selected": gym_selected.get(), "class_selected": class_selected.get()}
    with open('config.txt', 'w') as file:
        file.write("username " + us_input.get("username") + '\n')
        file.write("password " + us_input.get("password") + '\n')
        file.write("day_selected " + str(us_input.get("day_selected")) + '\n')
        file.write("gym_selected " + str(us_input.get("gym_selected")) + '\n')
        file.write("class_selected " + str(us_input.get("class_selected")) + '\n')
    print(us_input)


# Creating object 'root' of Tk()
root = Tk()

# Providing Geometry to the form
root.geometry("500x500")

# Providing title to the form
root.title('Reservation for World Class')

# this creates 'Label' widget for Registration Form and uses place() method.
label_title = Label(root, text="Reservation World Class", width=20, font=("bold", 20))
# place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_title.place(x=90, y=60)

# this creates 'Label' widget for Fullname and uses place() method.
label_username = Label(root, text="Username", width=20, font=("bold", 10))
label_username.place(x=80, y=130)

# this will accept the input string text from the user.
username = Entry(root)
username.place(x=240, y=130)

# this creates 'Label' widget for Password and uses place() method.
label_password = Label(root, text="Password", width=20, font=("bold", 10))
label_password.place(x=68, y=180)

password = Entry(root)
password.place(x=240, y=180)

# this creates 'Label' widget for Gyms and uses place() method.
label_gym = Label(root, text="Gym", width=20, font=("bold", 10))
label_gym.place(x=70, y=230)

# the variable 'var' mentioned here holds Integer Value, by default 0
gym_selected = IntVar()

# this creates 'Radio button' widget and uses place() method
Radiobutton(root, text="Sudului", padx=0, variable=gym_selected, value=437).place(x=225, y=230)
Radiobutton(root, text="City Park", padx=20, variable=gym_selected, value=443).place(x=290, y=230)

# this creates 'Label' widget for Days and uses place() method.
label_day = Label(root, text="Day", width=20, font=("bold", 10))
label_day.place(x=70, y=280)

# the variable 'c' mentioned here holds String Value, by default ""
day_selected = StringVar()
day_options = OptionMenu(root, day_selected, *list_of_days)
day_options.config(width=15)
day_selected.set('Select day')
day_options.place(x=240, y=280)

# this creates 'Label' widget for Class and uses place() method.
label_class = Label(root, text="Class", width=20, font=('bold', 10))
label_class.place(x=75, y=330)

# the variable 'var1' mentioned here holds Integer Value, by default 0
class_selected = IntVar()
class_options = OptionMenu(root, class_selected, *list_of_classes)
class_options.config(width=15)
class_selected.set('Select class')
class_options.place(x=240, y=330)

secret_btn = Button(root, width=0, height=0, bg="black", fg='white')
secret_btn.place(x=480, y=66)
secret_btn.hover = HoverInfo(secret_btn, "Thank you for using my script!")

# this creates button for submitting the details provided by the user
submit_btn = Button(root, text='Save', width=20, bg="black", fg='white',
                    command=lambda: [get_data(), hide_me(submit_btn), on_click()])
submit_btn.place(x=180, y=380)

# this will run the mainloop.
root.mainloop()
