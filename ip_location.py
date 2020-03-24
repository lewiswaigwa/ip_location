'''
Author: Romeos CyberGypsy
Name: ip_location.py
Function: Extracting ip address location
'''
################################
#Copying code doesn't make you a coder
#Seek to understand
###############################

import sys
import time
import bs4
import requests
from colorama import *
from termcolor import colored

class Locate:
	def __init__(self):
		banner = '''
		░▀█▀░█▀█░░░█░░░█▀█░█▀▀░█▀█░▀█▀░▀█▀░█▀█░█▀█
        	░░█░░█▀▀░░░█░░░█░█░█░░░█▀█░░█░░░█░░█░█░█░█
        	░▀▀▀░▀░░░░░▀▀▀░▀▀▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀▀▀░▀░▀'''
		print(colored(banner,"yellow"))
		print("\n")
		print(colored("Written by Romeos CyberGypsy"))
		try:
			self.locate_ip()

		except KeyboardInterrupt:
			print(colored("[-]Exiting safely!!","red"))
			sys.exit()

	def locate_ip(self):
		ip = input(f"{Fore.RED}[{Fore.BLUE}*{Fore.RED}]{Fore.GREEN}Enter target ip address:{Fore.YELLOW}")
		choice = input(f"{Fore.RED}[{Fore.BLUE}*{Fore.RED}]{Fore.GREEN}Would you like to save your output to a text file?(Y/n){Fore.BLUE}")
		if choice == "N" or choice == "n":
			pass

		elif choice == "Y" or choice == "y":
			filename = input(f"{Fore.RED}[{Fore.BLUE}*{Fore.RED}]{Fore.GREEN}Enter a name for text file to save output:{Fore.YELLOW}")
			file = open(filename+".txt", "w")

		else:
			print(colored("[-] Invalid choice!!Exiting"))
			time.sleep(1)
			sys.exit()

		print(f"{Fore.RED}[{Fore.BLUE}*{Fore.RED}]{Fore.GREEN}Locating IP...")

		headers = {"User-agent" : "Mozilla/5.1"}
		try:
			data = requests.get("https://whatismyipaddress.com/ip/"+ip, headers = headers)
		except Exception as e:
			print(e)
			sys.exit()
		soup = bs4.BeautifulSoup(data.text, 'html.parser')
		findings = soup.find_all("table")

		for line in findings:
			print(colored(line.get_text(),"yellow"))
			try:
				file.write(line.get_text())

			except:
				pass

		if choice == "Y" or choice == "y":
			file.close()


if __name__ == '__main__':
	obj = Locate()
