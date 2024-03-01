# Python libraries being imported
from threading import *
from tkinter import *
import datetime
import time
import winsound


# Creating object for GUI from tkinter library
root = Tk()

# Setting dimensions of the GUI object to be small and unintrusive
root.geometry("250x200")


# Defining threading function
def threading():
    t1 = Thread(target=alarm)
    t1.start()


def alarm():
    # Loop to run Alarm clock continuously
    while True:
        # Set Alarm 
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Wait for one seconds
        time.sleep(1)

        # Using datetime module to read current date and time from PC
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        # Function that checks if set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")
            # Command from winsound module to play alarm clock audio
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)


# Creating the buttons of the GUI for User to choose time as well as adding labels
Label(root, text="Alarm Clock", font="Impact 20", fg="red").pack(pady=10)
Label(root, text="Set Time", font="Impact 15").pack()

frame = Frame(root)
frame.pack()

# Adding the hours for the Alarm Clock
hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
         '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
         '22', '23', '24')
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

# Adding the minutes for the Alarm Clock
minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
           '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
           '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32',
           '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43',
           '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54',
           '55', '56', '57', '58', '59', '60')

minute.set(minutes[0])
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

# Adding the seconds for the alarm clock
second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07','08', '09', '10',
           '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21',
           '22', '23', '24', '25', '26', '27', '28', '29', '30', '31','32',
           '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43',
           '44', '45', '46', '47','48', '49', '50', '51', '52', '53', '54',
           '55', '56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

# Creating last button for user to set the Alarm
Button(root, text="Set Alarm", font="Impact 10", command=threading).pack(pady=20)

# Running the GUI object for the alarm clock
root.mainloop()