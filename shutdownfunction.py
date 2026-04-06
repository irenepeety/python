import subprocess
import time

def shutdown(delay):
    print(f"System will shutdown in {delay} seconds...")
    time.sleep(delay)
    subprocess.call("shutdown /s /t 1")

def restart(delay):
    print(f"System will restart in {delay} seconds...")
    time.sleep(delay)
    subprocess.call("shutdown /a")

def menu():
    while True:
        print("\n==== SYSTEM CONTROL MENU ====")
        print("1. Shutdown")
        print("2. Restart")
        print("3. Cancel Shutdown")
        print("4. Exit")

        choice = input("enter your choice: ")