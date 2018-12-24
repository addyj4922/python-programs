import datetime
now = datetime.datetime.now()
class Time:
    def __init__(self,__hour=now.hour,__minute = now.minute,__second = now.second):
        self.__hour=__hour
        self.__minute=__minute
        self.__second=__second
    def gethour(self):
        print(self.__hour)
    def getminute(self):
        print(self.__minute)
    def getsecond(self):
        print(self.__second)
    def setTime(self,secs):
        self.secs=secs
        h=int(self.secs/3600)
        self.__hour=h
        self.secs=secs-(h*3600)
        m=int(self.secs/60)
        self.__minute=m
        self.secs=self.secs-(m*60)
        s=self.secs
        self.__second=s

o=Time()
o.setTime(555550)
o.gethour()
o.getminute()
o.getsecond()