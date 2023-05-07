from tkinter import *
import time
import datetime
from playsound import playsound

heading = Tk()
heading.title('Alarm Clock')


def setalarm():
    alarmtime = f"{hrs.get()}:{mins.get()}:{secs.get()}"
    print('Alarm time :',alarmtime)
    if (alarmtime != "::"):
        alarmclock(alarmtime)


def alarmclock(alarmtime):
    while True:
        time.sleep(1)
        time_now = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}"
        print(time_now)
        if time_now == alarmtime:
            Wakeup = Label(heading, font=('courier',25,'italic'),
            text="Its time to get up", bg="black", fg="white").grid(row=6, columnspan=3)
            print("wake up!")
            playsound('E:\\Songs\\ring tones\\take on me.mp3')
            break

hrs = StringVar()
mins = StringVar()
secs = StringVar()

greet = Label(heading, font=('courier', 20, 'bold'),text="Set an Alarm").grid(row=1, columnspan=3)

hrbtn = Entry(heading, textvariable=hrs, width=5, font=('arial', 20, 'bold')).grid(row=2, column=1)

minbtn = Entry(heading, textvariable=mins, width=5, font=('arial', 20, 'bold')).grid(row=2, column=2)

secbtn = Entry(heading, textvariable=secs, width=5, font=('arial', 20, 'bold')).grid(row=2, column=3)

setbtn = Button(heading, text="Set Alarm", command=setalarm, bg="black", fg="white", font=('arial', 20, 'bold')).grid(row=4, columnspan=3)

timeleft = Label(heading, font=('arial', 20, 'bold')).grid()

mainloop()
