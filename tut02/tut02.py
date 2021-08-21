def isDigit(x):
    return type(x) is int

def get_memory_score(input_nums):
    n=len(input_nums)
    invalid=[]
    mem=[]
    score=0
    for x in input_nums:
        if(isDigit(x)==False):
            invalid.append(x)
        else:
            if(x in mem):
                score+=1
                continue
            elif(len(mem)==5):
                mem.pop(0)
                mem.append(x)
            else:
                mem.append(x)
    if(len(invalid)!=0):
        print("Please enter a valid input list")
        print("Invalid inputs detected:",invalid)
        exit()
        return
    else:
        return score

input_nums = [3, 4, 5, 3, 2, 1]
print("Score:",get_memory_score(input_nums))