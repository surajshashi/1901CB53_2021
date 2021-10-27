import os
import shutil
import re

# Function for adding padding to season and episode

def num_with_padding(digit,padding):
	left_padding =(padding-len(str(digit)))*'0'
	num=left_padding+str(digit)
	return num

# Function for copying the files from wrong_srt to corrected_srt directory

def copying_folder(series):
	path_parent = os. path. dirname(os. getcwd())
	os.chdir(path_parent)
	src=os.path.join(os.getcwd(),'wrong_srt',series)
	dst=os.path.join(os.getcwd(),'corrected_srt',series)
	try:
		shutil.copytree(src=src,dst=dst)
	except:
		pass

# Function for correcting filenames of Breakin Bad series

def bb_corrected(series,season_padding,episode_padding):
	files=os.listdir(os.getcwd())
	for file in files:
		regex=r's(\d+)e(\d+)'
		match=re.search(regex,file)
		season_digit=int(match.group(1))
		episode_digit=int(match.group(2))
		season=num_with_padding(season_digit,season_padding)
		episode=num_with_padding(episode_digit, episode_padding)
		correct_file=re.sub(r'\w+ [0-9]{3}p\.\w+\.\w+', 'Season '+season +' Episode '+episode, file)
		os.rename(file,correct_file)

# Function for correcting filenames of Game of Thrones series

def got_corrected(series,season_padding,episode_padding):
	files=os.listdir(os.getcwd())
	for file in files:
		regex=r'([0-9])x(\d+)'
		match=re.search(regex, file)
		season_digit=int(match.group(1))
		episode_digit=int(match.group(2))
		season=num_with_padding(season_digit, season_padding)
		episode=num_with_padding(episode_digit, episode_padding)
		correct_file=re.sub(r'[0-9]x\d+', "Season " + season +" Episode " + episode, file)
		correct_file=re.sub(r'\.\w+\.\w+\.\w+\.\w+', '', correct_file)
		os.rename(file,correct_file)

#Function for correcting filenames of Lucifer series

def lucifer_corrected(series,season_padding,episode_padding):
	files=os.listdir(os.getcwd())
	for file in files:
		
		regex=r'([0-9])x(\d+)'
		
		
		match=re.search(regex, file)
		season_digit=int(match.group(1))
		episode_digit=int(match.group(2))
		
		season=num_with_padding(season_digit, season_padding)
		episode=num_with_padding(episode_digit, episode_padding)
		correct_file=re.sub(r'[0-9]x\d+', "Season " + season +" Episode " + episode, file)
		correct_file=re.sub(r'\.\w+\.\w+\.\w+', '', correct_file)
		os.rename(file,correct_file)


def regex_renamer():

	# Taking input from the user

	print("1. Breaking Bad")
	print("2. Game of Thrones")
	print("3. Lucifer")

	webseries_num = int(input("Enter the number of the web series that you wish to rename. 1/2/3: "))
	season_padding = int(input("Enter the Season Number Padding: "))
	episode_padding = int(input("Enter the Episode Number Padding: "))

	# Making corrected_srt directory

	try:
		os.mkdir('corrected_srt')
	except:
		pass

	# Moving to corrected_srt directory

	os.chdir('corrected_srt')

	# Created dictionary of series name and input numbers

	web_dic={1:'Breaking Bad', 2:'Game of Thrones', 3:'Lucifer'}
	series=web_dic[webseries_num]
	
	# Deleting series directory if it pre exits in corrected_srt
	try:
		path=os.path.join(os.getcwd(),series)
		shutil.rmtree(path)		
	except:
		pass

	#Calling copyyin_folder function

	copying_folder(series)

	# Moving to series directory in corrected_srt
	os.chdir('corrected_srt\\'+series)
	
	#Calling functions based on choice opted by user

	if(webseries_num==1):
		bb_corrected(series,season_padding,episode_padding)
	elif(webseries_num==2):
		got_corrected(series,season_padding,episode_padding)
	else:
		lucifer_corrected(series, season_padding, episode_padding)
	

# Calling regex_rename function
regex_renamer()