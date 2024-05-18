import tkinter as tk
from tkinter import messagebox
import threading
import time
import subprocess
import os
import sys
import json

#inf2023055  Αχιλλέας Ζήσης
#Βοήθεια για τον κώδικα πήρα από: https://www.youtube.com/watch?v=ibf5cx221hk

base_dir = os.path.dirname(os.path.abspath(__file__))
proj_dir = os.path.join(base_dir, '..')
sys.path.append(proj_dir)
from API.API import api

def new():
    matches_window = tk.Toplevel(root)
    matches_window.title("Επιλογή match")
    matches_window.geometry("540x360")
    
    try:
        matches = api()
        matches_listbox = tk.Listbox(matches_window)
        matches_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        for match in matches:
            matches_listbox.insert(tk.END, f"{match['homeTeam']['name']} vs {match['awayTeam']['name']}")
    except Exception as e:
        messagebox.showerror("Σφάλμα", f"Δεν ήταν εφικτό το fetch: {e}")

def start_checking_results():
    check_results_thread = threading.Thread(target=check_results)
    check_results_thread.daemon = True
    check_results_thread.start()

def check_results():
    while True:
        try:
            api()  # ξαναχρήση του API
        except Exception as e:
            print(f"Δεν ήταν εφικτό το fetch: {e}")
        time.sleep(100 * 60)  # timer για 100 λεπτά πριν τον επανέλεγχο

def ttt():
    script_dir = os.path.join(base_dir, '..', 'App Mini-Game')
    script_path = os.path.join(script_dir, 'TicTacToe.py')
    if os.path.exists(script_path):
        try:
            os.chdir(script_dir)
            subprocess.run(['python', script_path], check=True)
        except subprocess.CalledProcessError as e:
            os.chdir(base_dir)
            print(f"Σφάλμα: {e}")
        else:
            os.chdir(base_dir)
            print(f"Ολοκληρώθηκε.")
            
root = tk.Tk()
root.title("Predictor")
root.geometry("720x480")
    
label = tk.Label(root, text="Predictor", font=('Roboto', 24))
label.pack(pady=96, padx=16)

button1 = tk.Button(root, text="Νέο παιχνίδι", command=new, font=('Roboto', 13))
button1.pack(pady=12, padx=12)

button2 = tk.Button(root, text="Τρίλιζα", command=ttt, font=('Roboto', 13))
button2.pack(pady=12, padx=12)
    
start_checking_results()
    
root.mainloop()
