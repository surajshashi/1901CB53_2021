def output_by_subject():
    f=open("regtable_old.csv","r")
    count=0
    for line in f:
        if(count==0):
            count=count+1
            continue
        cells=line.split(",")
        rollno=str(cells[0])
        register_sem=str(cells[1])
        subno=str(cells[3])
        sub_type=str(cells[8])
        subFileName="output_by_subject\\"+subno+".csv"
        f_sub=open(subFileName,"a")
        f_sub.close()
        f_sub=open(subFileName,"r")
        if(len(f_sub.readlines())==False):
            f_sub.close()
            f_sub=open(subFileName,"a")
            f_sub.write("rollno,register_sem,subno,sub_type\n")
            f_sub.close()
        f_sub=open(subFileName,"a")
        f_sub.write(rollno +","+ register_sem +","+ subno +","+ sub_type)
        f_sub.close()
    f.close()
    return

def output_individual_roll():
    f=open("regtable_old.csv","r")
    count=0
    for line in f:
        if(count==0):
            count=count+1
            continue
        cells=line.split(",")
        rollNum=str(cells[0])
        register_sem=str(cells[1])
        subno=str(cells[3])
        sub_type=str(cells[8])
        rollFileName="output_individual_roll\\"+rollNum+".csv"
        f_roll=open(rollFileName,"a")
        f_roll.close()
        f_roll=open(rollFileName,"r")
        if(len(f_roll.readlines())==False):
            f_roll.close()
            f_roll=open(rollFileName,"a")
            f_roll.write("rollno,register_sem,subno,sub_type\n")
            f_roll.close()
        f_roll=open(rollFileName,"a")
        f_roll.write(rollNum +","+ register_sem +","+ subno +","+ sub_type)
        f_roll.close()
    f.close()
    return

output_individual_roll()
output_by_subject()