
import zipfile
try:
	from termcolor import colored
except:
	print("colored module not found ")
	print("Install it by : pip install colored")

print(colored('''Created By : mR pErFeCt
GitHub Link : git clone https://github.com/MrPft/termux-setup 
Youtube Channel : mR pErFeCt
Youtube Link : 
	''','blue'))

print("")

print(colored("Remind : Don't use for illegal purpose",'red'))

print("")

print(colored("1. Dictonary Attack",'yellow'))
print(colored("2. Brute Force Attack",'yellow'))
print(colored("3. Exit",'yellow'))
print("")
command = str(input(colored("Enter => ",'red')))

if command == "1":
	
	
	print("")
	zip = str(input(colored("Enter the path of ZipFile => ",'green')))
	Zip = zipfile.ZipFile(zip)
		
		
	print("")	
	wordlist = str(input(colored("Enter the path of wordlist => ",'green')))
	
	list = open(wordlist,'r')
	
	
	for i in list.readlines():
		password = i.strip()
		try:
			
			Zip.extractall(pwd=password.encode())
			print("")
			print(colored(f"Password Found => ",'green'),password)
			break
		except:
			print("")
			print(colored("Trying Password => ",'red'),password)
		
		
		
		
elif command == "2":
	print("")
	zip = str(input(colored("Enter the path of ZipFile => ",'green')))
	Zip = zipfile.ZipFile(zip)
	
	i = 0
	while True:
		i += 1
		password = str(i)
		try:
			print("")
			Zip.extractall(pwd=password.encode())
			print(colored("Password Found => ",'green'),password)
			break
		except:
			print(colored("Trying password => ",'red'),password)
	
	
elif command == "3":
	quit()
else:
	print(colored("You entered invalid command ",'red'))
	
	
		
	










