import sys
sys.path.append("pypatchouli")
from modes import ja
import re
from seq import Seq

def match(expression,text):
    m=re.compile(expression).search(text)
    if m:
        return m.group()
    return None
def resafe(txt):
    for v in list("\\*+.>{}()[]$-|"):
        txt=txt.replace(v,"\\"+v)
    return txt

def isDate(line,mode):
    return match(mode.isdate,line)==line
def isNewLine(line,mode):
    return match(mode.isNewLine,line)==line

class Parse:
    def __init__(self,text,mode=ja.windows):
        lines=text.split("\n")[mode.headerLength:]
        Y=0
        M=0
        D=0
        talks=list()
        for line in lines:
            if(line==""):
                continue
            if isDate(line,mode):
                Y=match(mode.ymd[0],line)
                M=match(mode.ymd[1],line)
                D=match(mode.ymd[2].replace("{{M}}",resafe(M)),line)
                
            elif isNewLine(line,mode):
                h=match(mode.hm[0],line)
                m=match(mode.hm[1].replace("{{h}}",resafe(h)),line)
                user=match(mode.user
                            .replace("{{h}}",resafe(h))
                            .replace("{{m}}",resafe(m))
                        ,line)
                body=match(mode.body.replace("{{user}}",resafe(user))
                                    .replace("{{h}}",resafe(h))
                                    .replace("{{m}}",resafe(m))
                            ,line)
                talks.append(Seq(body,user,[Y,M,D,h,m]))
            else:
                
                talks[-1].addLine(line)
        self.talks=talks

        self._i=0
    def __str__(self):
        result=""
        for seq in self.talks:
            result+=str(seq)+"\n"
        return result[:-1]
    def __getitem__(self, item):
        if isinstance(item, slice):
            return self.talks[item.start:item.stop]
        return self.talks[item]
    def __iter__(self):
         return self
    def __next__(self):
        if self._i == len(self.talks):
            raise StopIteration()
        result=self.talks[self._i]
        self._i += 1
        return result
    def __list__(self):
        return self.talks
    def __len__(self):
        return len(self.talks)
        