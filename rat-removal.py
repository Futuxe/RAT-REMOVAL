# cleanup_bot.py
import winreg
import subprocess
import os

def remove_all_traces():
    print("=== Bot Cleanup Tool ===\n")
    
    # 1. Remove from registry startup
    print("1. Removing from registry startup...")
    try:
        reg_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0,
            winreg.KEY_SET_VALUE
        )
        winreg.DeleteValue(reg_key, "SystemService")
        winreg.CloseKey(reg_key)
        print("   ✓ Removed 'SystemService' from registry")
    except:
        print("   ⚠ Not found in registry")
    
    # 2. Check Task Scheduler
    print("\n2. Checking Task Scheduler...")
    try:
        result = subprocess.run(
            ['schtasks', '/query', '/tn', 'WindowsUpdateService'],
            capture_output=True,
            text=True,
            shell=True
        )
        if result.returncode == 0:
            # Task exists, delete it
            subprocess.run(
                ['schtasks', '/delete', '/tn', 'WindowsUpdateService', '/f'],
                capture_output=True,
                shell=True
            )
            print("   ✓ Removed 'WindowsUpdateService' task")
        else:
            print("   ⚠ No scheduled task found")
    except:
        print("   ⚠ Could not check Task Scheduler")
    
    # 3. Kill running processes
    print("\n3. Killing running processes...")
    try:
        # Kill Python processes with common bot names
        subprocess.run(['taskkill', '/f', '/im', 'python.exe'], 
                      capture_output=True, shell=True)
        subprocess.run(['taskkill', '/f', '/im', 'pythonw.exe'], 
                      capture_output=True, shell=True)
        subprocess.run(['taskkill', '/f', '/im', 'DiscordBot.exe'], 
                      capture_output=True, shell=True)
        subprocess.run(['taskkill', '/f', '/im', 'bot.exe'], 
                      capture_output=True, shell=True)
        print("   ✓ Killed related processes")
    except:
        print("   ⚠ Could not kill processes")
    
    print("\n=== Cleanup Complete ===")
    print("Restart your computer to ensure all changes take effect.")

if __name__ == "__main__":
    remove_all_traces()
    input("\nPress Enter to exit...")
