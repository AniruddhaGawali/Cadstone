import datetime
import time
from playsound import playsound as ps

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            ps('./YouTuber.mp4')
            break
        time.sleep(1)

def main():
    print("Enter the time for the alarm (format: HH:MM:SS)")
    alarm_time = input(">> ")
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")
        return
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
