import subprocess

def list_installed_apps_windows(write_to_file=False, filename="listapps-output-win.txt"):
    cmd = 'powershell "Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate"'
    
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    
    if write_to_file:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(result.stdout)
    else:
        print(result.stdout)

if __name__ == "__main__":
    list_installed_apps_windows(write_to_file=True)
