import subprocess

def list_installed_apps_mac(write_to_file=False, filename="listapps-output-macos.txt"):
    cmd = ['system_profiler', 'SPApplicationsDataType']
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if write_to_file:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(result.stdout)
    else:
        print(result.stdout)

if __name__ == "__main__":
    list_installed_apps_mac(write_to_file=True)
