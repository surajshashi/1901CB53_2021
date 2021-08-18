def meraki_helper(n):
    count=0
    for x in range(len(n)):
        val=str(n[x])
        if(len(val)==1):
            print("Yes, {} is a Meraki number".format(n[x]))
            count+=1
            continue
        flag=0
        for y in range(len(val)-1):
            num1,num2=int(val[y]),int(val[y+1])
            if(abs(num1-num2)!=1):
                flag=1
                print("No, {} is NOT a Meraki number".format(n[x]))
                break
        if(flag==0):
            print("Yes, {} is a Meraki number".format(n[x]))
            count+=1    
    return count


input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]
meraki_num=meraki_helper(input)
print("Input list contains {} Meraki and {} NON Meraki numbers".format(meraki_num,len(input)-meraki_num))
