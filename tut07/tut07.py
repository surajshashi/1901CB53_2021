import csv
import pandas as pd

# Function to count the non-zero bit values in ltp
def ltp_counter():
	with open('course_master_dont_open_in_excel.csv','r') as file:
		reader=csv.DictReader(file)
		ltp_count={}  # Dictionary to store the non-zero bit value of different subject code
		for row in reader:
			subcode=row['subno']
			ltp=row['ltp'].split('-')
			ltpcount=0
			for i in range(3):
				if(float(ltp[i])>0):
					ltpcount+=1
			ltp_count[subcode]=ltpcount
		return ltp_count  # Returning dictionary

# Function to store the student details
def stud_details():
	with open('studentinfo.csv','r') as file:
		reader=csv.DictReader(file)
		stud_info={}   #Dictionary to store details
		for row in reader:
			name=row['Name']
			rollnum=row['Roll No']
			email=row['email']
			aemail=row['aemail']
			contact=row['contact']
			stud_info[rollnum]=[name,email,aemail,contact]  # List of name,email,aemail,contact
		return stud_info  # Returning dictionary

# Function to find feedback not submitted and note it in worksheet
def feedback_not_submitted():
	df=pd.read_csv('course_registered_by_all_students.csv')
	ltp=ltp_counter()  # Calling ltp_counter function 

	req_feed={} # Dictionary for storing the course taken with respective ltp corresponding to different roll numbers

	rollnum_list=[] # List of all roll numbers

	for index, row in df.iterrows():
		subno=row['subno']
		rollnum=row['rollno']
		if(rollnum not in rollnum_list):
			rollnum_list.append(rollnum) # Adding roll numbers to list
		
		sublist=[subno,ltp[subno]] # List of subject code and ltp nonzero bit corresponding it
		try:
			req_feed[rollnum].append(sublist) # Appending list containing subject code and nonzero bit taken by corresponding student to list
		except:
			req_feed[rollnum]=[] # Creating the list to store subject and ltp taken by student
			req_feed[rollnum].append(sublist)
	df_sub=pd.read_csv('course_feedback_submitted_by_students.csv')
	lis=[]
	for roll in rollnum_list :
		df_roll=df_sub[df_sub['stud_roll']==roll] # Creating dataframe roll numbers wise
		for x in req_feed[roll]:
			df_2=df_roll[df_roll['course_code']==x[0] ]
			# Checking if feedback for every ltp present else appending it to lis
			if(df_2.shape[0]<x[1]):
				lis.append([roll,x[0]])

	data=[]
	stud_dict=stud_details() # Calling stud_details function 
	for i in lis:
		df_2=df[df['rollno']==i[0]]
		df_2=df_2[df_2['subno']==i[1]]
		df_3=df_2.iloc[0].values.tolist()
		df_3=df_3[:4]
		try:
			if(len(stud_dict[i[0]])>0):
				df_3=df_3+stud_dict[i[0]]
				
		except:
			df_3=df_3+['NA','NA','NA','NA']
		data.append(df_3)
	# Creating data frame for feedback remaining	
	data_df= pd.DataFrame(data,columns=['rollno','register_sem','schedule_sem','subno','Name','email','aemail','contact'])
	
	# Storing data frame in excel sheet 
	data_df.to_excel('course_feedback_remaining.xlsx',index=False)

feedback_not_submitted() # Calling function feedback_not_submitted
