import os, subprocess
version_url = "https://raw.githubusercontent.com/pmshydra/dev/main/version.txt"
version_file = "version.txt"
# Define the repository URL
repo_url = "https://github.com/pmshydra/dev.git"
    # Define the local directory to clone the repository
repo_dir = "."
# Check if the version file exists
if os.path.exists(version_file):
    # Read the contents of the version file
    with open(version_file, 'r') as file:
        current_version = file.read().strip()
    
    # Fetch the contents of the version URL
    response = subprocess.run(['curl', '-s', version_url], capture_output=True, text=True)
    remote_version = response.stdout.strip()
    
    # Compare the current version with the remote version
    if current_version != remote_version:
        # Clone the git repository
        subprocess.run(['git', 'clone', repo_url, repo_dir])
else:
    # Clone the git repository if the version file doesn't exist
    subprocess.run(['git', 'clone', repo_url, repo_dir])


