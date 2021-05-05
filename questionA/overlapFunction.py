def checkOverLapse(x1,x2,x3,x4):
    #simple if check if lines ends inside one another (avoids using larger function)
    if (x1 < x3 < x2 or x1 < x4 < x2):
        return "2 lines overlap"
    else:
        #print('does not exist inbetween, rechecking or cross-over')  
        if(x1 - x2) < (x3-x4):
            result = recheck(x1,x2,x3,x4)
        else:
            result = recheck(x3,x4,x1,x2)
    
    return result

#main function to check if they overlap
def recheck(a,b,start,end):
    overlap=False
    for num in range(a,b):
        
        if num in range(start, end):
            overlap=True
            #overlapAt ='overlap at:{}'.format(num)
                
        #else:
                #overlapNone ='does not overlap at:{}'.format(num)
        
    if overlap !=False:
        return "2 lines overlap"
    else: 
        return "2 lines does not overlap"