print("_______________________________")
print("*********CURRENT DATE**********")

DateTODAY = int(input("Enter todays day :"))
if (DateTODAY<1 or DateTODAY>30):
    print("Wrong Date")

MonthTODAY = int(input("Enter todays month :"))
if MonthTODAY<1 or MonthTODAY>12:
    print("Wrong month")

YearTODAY = int(input("Enter todays year :"))

print("_______________________________")
print("*********BIRTH DATE***********")

DateBIRTH = int(input("Enter birth day :"))
if (DateBIRTH<1 or DateBIRTH>30):
    print("Wrong Date")

MonthBIRTH = int(input("Enter birth month :"))
if MonthBIRTH<1 or MonthBIRTH>12:
    print("Wrong month")
YearBIRTH = int(input("Enter birth year :"))

print("_______________________________")
print("********AGE CALCULATOR*********")

if DateTODAY>DateBIRTH:
    DateAGE = DateTODAY-DateBIRTH
else:
    DateAGE=DateBIRTH=DateTODAY

if MonthTODAY>MonthBIRTH:
    MonthAGE = MonthTODAY-MonthBIRTH
else:
    MonthAGE=MonthBIRTH-MonthTODAY

YearAGE = YearTODAY-YearBIRTH

print("Years : "+str(YearAGE)+" Months : "+str(MonthAGE)+" Days : "+str(DateAGE))