from datetime import datetime
from event import Event

class Seq(Event):
    def __init__(self,seq:str,user:str,time:list):
        super().__init__(user,time)
        self.seq=seq
    def addLine(self,line):
        self.seq+="\n"+line
    def __repr__(self):
        return f"Seq(user={self.user},seq='{self.seq}'))"
    def __str__(self):
        return f"{str(self.time)} {self.user} {self.seq}"
