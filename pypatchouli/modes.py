class Mode:
    def __init__(self,**options):
        self.deleteLines=0
        self.isdate=""
        self.ymd=["","",""]
        for key in options:
            value=options[key]
            exec("self."+key+"=value")
class Modes(dict): 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.__dict__ = self
ja=Modes()
ja["windows"]=Mode(
    headerLength=0,
    isdate=r"[0-9][0-9][0-9][0-9]\.[0-9][0-9]\.[0-9][0-9] .曜日",
    ymd=[
        r"^[0-9][0-9][0-9][0-9]", #Year
        r"(?<=[0-9][0-9][0-9][0-9]\.)[0-9][0-9](?=\.)", #Month
        r"(?<=[0-9][0-9][0-9][0-9]\.[0-9][0-9]\.)[0-9][0-9]" #Day
    ],
    isNewLine=r"^[0-9][0-9]:[0-9][0-9] .+ .+",
    hm=[
        r"^[0-9][0-9]",
        r"(?<=^[0-9][0-9]:)[0-9][0-9]"
    ],
    user=r"(?<=^[0-9][0-9]:[0-9][0-9] ).*?(?= .+)",
    body=r"(?<=^[0-9][0-9]:[0-9][0-9] {{user}} ).+",
    isInviteCancel=r""
)
ja["android"]=Mode(
    headerLength=2,
    isdate=r"[0-9][0-9][0-9][0-9]/[0-9]?[0-9]/[0-9]?[0-9]\((日|月|火|水|木|金|土)\)",
    ymd=[
        r"^[0-9][0-9][0-9][0-9]", #Year
        r"(?<=[0-9][0-9][0-9][0-9]/)[0-9]?[0-9]", #Month
        r"(?<=[0-9][0-9][0-9][0-9]/{{M}}/)[0-9]?[0-9]" #Day
    ],
    isNewLine=r"^[0-9]?[0-9]:[0-9]?[0-9]\t(.+)\t(.+)",
    hm=[
        r"^[0-9]?[0-9]",
        r"(?<=^{{h}}:)[0-9]?[0-9]"
    ],
    user=r"(?<=^{{h}}:{{m}}\t)(.+)(?=\t(.+))",
    body=r"(?<=^{{h}}:{{m}}\t{{user}}\t).+",
)
