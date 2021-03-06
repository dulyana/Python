Unit = int(input("Enter the number of Unites : "))
UnitPrice = 0

if Unit==0:
    UnitPrice=0
elif Unit>=1 and Unit<=29:
    UnitPrice = (Unit*5)
elif Unit>=30 and Unit<=59:
    UnitPrice=(29 * 5) + ((Unit-29)*20)
elif Unit>=60 and Unit<=119:
    UnitPrice=(29 * 5) + (29*20) + ((Unit-60)*150)
elif Unit>=120 and Unit<=199:
    UnitPrice=(29 * 5) + (29*20) + (59*150) +((Unit-120)*500)
elif Unit>=200:
    UnitPrice=(29 * 5) + (29*20) + (59*150) +(79*500)+((Unit-200)*1000)


print("The total Price is : Ru. " +str(UnitPrice))    

