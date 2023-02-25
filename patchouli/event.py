from datetime import datetime

class Event:
    def __init__(self,user:str,time:list):
        self.user=user
        self.time=datetime(int(time[0]),int(time[1]),int(time[2]),int(time[3]),int(time[4]))
    def __repr__(self):
        return f"Event(user={self.user},time='{self.time}'))"
    def __str__(self):
        return f"{str(self.time)} {self.user}"

class InviteCancel(Event):
    def __init__(self,user:str,time:list,target:str):
        super().__init__(user,time)
        self.target=target
    def __repr__(self):
        return f"InviteCancel(user={self.user},time='{self.time}',target='{self.target}'))"
    def __str__(self):
        return f"{str(self.time)} {self.user} InviteCancel to {self.target}"