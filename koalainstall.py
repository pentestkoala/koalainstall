import os

def install():
	print("[+] Install Seclists..")
	os.system("git clone https://github.com/danielmiessler/SecLists /usr/share/wordlists/SecLists")

	path = "/opt"
	print("[+] Create all the directories")
	os.system('mkdir ' + str(path) + 'privesc')
	os.system('mkdir ' + str(path) + 'shells')
	os.system('mkdir ' + str(path) + 'privesc/linux')
	os.system('mkdir ' + str(path) + 'privesc/windows')

	print("[+] Install static binaries..")
	os.system("git clone https://github.com/andrew-d/static-binaries " + str(path) + "/static-binaries")

	print("[+] Install evilwinrm..")
	os.system("git clone https://github.com/Hackplayers/evil-winrm " + str(path) + "/shells/evilwin-rm")

	print("[+] Install nishang..")
	os.system("git clone https://github.com/samratashok/nishang " + str(path) + "/shells/nishang")

	print("[+] Install JAWS..")
	os.system("git clone https://github.com/411Hall/JAWS " + str(path) + "/privesc/windows/JAWS")

	print("[+] Install PowerTools..")
	os.system("git clone https://github.com/PowerShellMafia/PowerSploit/ " + str(path) + "/privesc/windows/PowerTools")

	print("[+] Windows-Exploit-Suggester..")
	os.system("git clone https://github.com/AonCyberLabs/Windows-Exploit-Suggester " + str(path) + "/privesc/windows/windows-exploit-suggester")

	print("[+] LinEnum..")
	os.system("git clone https://github.com/rebootuser/LinEnum " + str(path) + "/privesc/linux/LinEnum")

	print("[+] Suid3num..")
	os.system("git clone https://github.com/Anon-Exploiter/SUID3NUM " + str(path) + "/privesc/linux/Suid3num")

	print("[+] Privilege-escalation-awesome-scripts-suite..")
	os.system("git clone https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite " + str(path) + "/privesc")

if __name__=="__main__":
	install()
