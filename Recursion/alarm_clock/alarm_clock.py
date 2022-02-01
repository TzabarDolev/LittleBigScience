import datetime
from playsound import playsound
import time
import random
import os
import json
import numpy as np

def run_alarm():
    f = open('alarm_clock_data.json')
    data = json.load(f)
    time_input = data['time']
    try:
        alarm_hour = int(time_input[0:2])
        alarm_minute = int(time_input[3:])
    except:
        print('hour format error')
        run_alarm()

    if alarm_hour > 24 or alarm_hour < 0 or alarm_minute > 59 or alarm_minute < 0:
        print('there is no such hour')
        run_alarm()

    print('setting the alarm clock for {}:{}'.format(time_input[0:2], time_input[3:]))

    while True:
        x = datetime.datetime.now()
        if x.hour == alarm_hour and x.minute == alarm_minute:
            print('alarm is on')
            songs = os.listdir(data['songs_dir'])
            random.shuffle(songs)
            for song in songs:
                playsound(os.path.join(data['songs_dir'], song))
            break
        else:
            if alarm_hour > x.hour or alarm_hour == x.hour and alarm_minute > x.minute:
                minutes_left = np.mod(alarm_minute - x.minute, 60)
                hours_left = np.mod(alarm_hour - x.hour, 24)
            else:
                minutes_left = np.mod(alarm_minute - x.minute, 60)
                hours_left = alarm_hour - x.hour + 23

            print('time is {}:{}, you still have {} hours and {} minutes to sleep'.format(x.hour, x.minute, hours_left, minutes_left))
            time.sleep(30)


if __name__ == '__main__':
    run_alarm()

