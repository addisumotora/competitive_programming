def countingValleys(steps, path):
    
    count = 0
    laps = 0
    
    for i in path:
        if i=='U':
            count+=1
            if count==0:
                laps+=1
        else:
            count-=1
    
    return laps