# -*- coding: cp949 -*-

from datetime import datetime



class rsvchecking:
    rsvtime=datetime.now()
    def __init__(self, day, hour, minute, second):
        self.rsvtime=datetime(2016,8,day,hour,minute,second)
        self.timeover = 0
    def rsvcheck(self):
        while self.timeover==0:
            if(self.rsvtime.day==datetime.now().day&self.rsvtime.hour==datetime.now().hour&self.rsvtime.minute==datetime.now().minute&self.rsvtime.second==datetime.now().second):
                self.timeover = 1
                print("time's up")
                return self.timeover

