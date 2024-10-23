import os
import subprocess
 
# Function to run a shell command
def run_command(command, cwd=None):
    try:
        subprocess.run(command, shell=True, check=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {command}\nError: {e}")
 
# Update the system's package list
print("Updating package list...")
run_command("sudo apt update -y")
 
# List of GitHub repositories to clone
repositories = [
    "https://github.com/danielmiessler/SecLists",
    "https://github.com/peass-ng/PEASS-ng/tree/master/winPEAS",
    "https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS",
    "https://github.com/itm4n/PrivescCheck",
    "https://github.com/fortra/impacket",
    "https://github.com/andrew-d/static-binaries",
    "https://github.com/dirkjanm/BloodHound.py",
    "https://github.com/ly4k/Certipy",  # Certipy repo
    "https://github.com/p0dalirius/Coercer"  # Coercer repo
]
 
# Directory to clone repositories into
clone_dir = "/opt"
 
# Ensure the /opt directory exists
if not os.path.exists(clone_dir):
    os.makedirs(clone_dir)
 
# Clone each repository
for repo in repositories:
    repo_name = repo.split("/")[-1]
    clone_path = os.path.join(clone_dir, repo_name)
    # Construct the git clone command
    clone_command = f"git clone {repo} {clone_path}"
    print(f"Cloning {repo} into {clone_path}...")
    # Run the git clone command
    run_command(clone_command)
 
# Install BloodHound.py
bloodhound_dir = os.path.join(clone_dir, "BloodHound.py")
print(f"Installing BloodHound.py in {bloodhound_dir}...")
run_command("sudo python3 setup.py install", cwd=bloodhound_dir)
 
# Install Coercer
coercer_dir = os.path.join(clone_dir, "Coercer")
print(f"Installing Coercer in {coercer_dir}...")
run_command("sudo python3 setup.py install", cwd=coercer_dir)
 
print("All repositories have been cloned and installations completed for BloodHound.py and Coercer.")
