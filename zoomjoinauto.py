import datetime
import webbrowser as wb
import pyautogui as pyg
import time
from tkinter import *

def format_time(t):
    cur_date=datetime.datetime.now()
    cur_date=str(cur_date).split()
    cur_date=cur_date[0].split('-')
    cur_date=list(map(int,cur_date))
    t=t.split()
    t=list(map(int,t))
    meettime=datetime.datetime(cur_date[0],cur_date[1],cur_date[2],t[0],t[1],0)
    return meettime



def join_meeting(link,meet_time):
    date_time=format_time(meet_time)
    wait_time=(date_time-datetime.datetime.now()).total_seconds()
    print("time left=", wait_time/60,"minutes")
    
    time.sleep(wait_time)

    wb.open(link)
    time.sleep(5)
    pyg.click(x=1073, y=267, clicks=1, interval=0, button="left")
    time.sleep(10)


link=input("Enter meet link: ")

meet_time=input("Enter joining time in HH MM format: ")

join_meeting(link, meet_time)

