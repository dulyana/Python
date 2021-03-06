
 
for i in range(1,100): 
    for j in range(2,i): 
        if(i % j==0): 
            break          
    else: 
        if i==1:
            continue
        print(i) 
