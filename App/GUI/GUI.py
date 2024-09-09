#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox, simpledialog
import threading
import time
import subprocess
import os
import sys
import json

# inf2023055	Αχιλλέας Ζήσης
# Βοήθεια για τον κώδικα πήρα από: https://www.youtube.com/watch?v=ibf5cx221hk

# Ορισμός του βασικού φακέλου για τη χρήση των άλλων αρχείων
base_dir = os.path.dirname(os.path.abspath(__file__))
proj_dir = os.path.join(base_dir, '..')
sys.path.append(proj_dir)

# Εισαγωγή του αρχείου API
from API.API import api

# Συνάρτηση που ελέγχει αν υπάρχουν αγώνες και αν όχι ανανεώνει κάθε 15 λεπτά
def new():
    matches_window = tk.Toplevel(root)
    matches_window.title("Επιλογή match")
    matches_window.geometry("540x360")

    try:
        matches = api()
        matches_listbox = tk.Listbox(matches_window, font=('Roboto', 12))
        matches_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        if not matches:
            matches_listbox.insert(tk.END, "Δεν υπάρχουν διαθέσιμοι αγώνες. Αναμονή για ανανέωση...")
            # Ανανεώνεται κάθε 15 λεπτά (900 δευτερόλεπτα)
            matches_window.after(900000, lambda: refresh_matches(matches_window))
        else:
            for match in matches:
                match_str = f"{match['homeTeam']['name']} vs {match['awayTeam']['name']}"
                matches_listbox.insert(tk.END, match_str)
                matches_listbox.bind('<Double-Button-1>', lambda event, m=match: get_player_predictions(m))
    except Exception as e:
        messagebox.showerror("Σφάλμα", f"Δεν ήταν εφικτό το fetch: {e}")

# Συνάρτηση που ανανεώνει τα παιχνίδια κάθε 15 λεπτά αν δεν υπάρχουν
def refresh_matches(matches_window):
    try:
        matches_window.destroy()
        new()
    except Exception as e:
        print(f"Σφάλμα ανανέωσης: {e}")

# Συνάρτηση που ζητάει προβλέψεις από τους δύο παίκτες
def get_player_predictions(match):
    # Νέο παράθυρο για τον Παίκτη 1
    player1_pred_window = tk.Toplevel(root)
    player1_pred_window.withdraw()

    player1_score = simpledialog.askstring("Πρόβλεψη Παίκτη 1", f"Δώσε την πρόβλεψή σου για τον επιλεγμένο αγώνα:")
    if player1_score is None:
    	player1_pred_window.destroy()
    	return

    player1_pred_window.destroy()

    # Νέο παράθυρο για τον Παίκτη 2
    player2_pred_window = tk.Toplevel(root)
    player2_pred_window.withdraw()

    player2_score = simpledialog.askstring("Πρόβλεψη Παίκτη 2", f"Δώσε την πρόβλεψή σου για τον επιλεγμένο αγώνα:")
    if player2_score is None:
    	player2_pred_window.destroy()
    	return

    player2_pred_window.destroy()

    # Έλεγχος αποτελεσμάτων κάθε 15 λεπτά αν δεν είναι διαθέσιμα
    check_match_results(match, player1_score, player2_score)

# Συνάρτηση για τον έλεγχο των αποτελεσμάτων του αγώνα και την καταμέτρηση πόντων
def check_match_results(match, player1_score, player2_score):
    while True:
        try:
            results = api()  # Ανάκτηση αποτελεσμάτων (προσομοίωση)
            match_result = find_match_result(results, match)  # Προσομοίωση εύρεσης αποτελέσματος

            if match_result:
                player1_points, player2_points = calculate_points(player1_score, player2_score, match_result)
                show_winner(player1_points, player2_points)
                break
            else:
                # Αν δεν υπάρχουν αποτελέσματα, περιμένει 15 λεπτά
                time.sleep(900)
        except Exception as e:
            print(f"Σφάλμα κατά τον έλεγχο αποτελεσμάτων: {e}")
            time.sleep(900)  # Αναμονή 15 λεπτών

# Συνάρτηση για την καταμέτρηση των πόντων
def calculate_points(player1_score, player2_score, match_result):
    player1_points, player2_points = 0, 0

    player1_predicted_home, player1_predicted_away = map(int, player1_score.split('-'))
    player2_predicted_home, player2_predicted_away = map(int, player2_score.split('-'))

    actual_home_score = match_result['homeTeam']
    actual_away_score = match_result['awayTeam']

    if (player1_predicted_home == actual_home_score and player1_predicted_away == actual_away_score):
        player1_points += 3  # Ο Παίκτης 1 πήρε σωστά το σκορ
    elif (player1_predicted_home > player1_predicted_away and actual_home_score > actual_away_score) or (player1_predicted_home < player1_predicted_away and actual_home_score < actual_away_score) or (player1_predicted_home == player1_predicted_away and actual_home_score == actual_away_score):
        player1_points += 2  # Ο Παίκτης 1 βρήκε τη νικήτρια ομάδα/την ισοπαλία

    if (player2_predicted_home == actual_home_score and player2_predicted_away == actual_away_score):
        player2_points += 3  # Ο Παίκτης 2 πήρε σωστά το σκορ
    elif (player2_predicted_home > player2_predicted_away and actual_home_score > actual_away_score) or (player2_predicted_home < player2_predicted_away and actual_home_score < actual_away_score) or (player2_predicted_home == player2_predicted_away and actual_home_score == actual_away_score):
        player2_points += 2  # Ο Παίκτης 2 βρήκε τη νικήτρια ομάδα/την ισοπαλία

    return player1_points, player2_points

# Συνάρτηση που εμφανίζει τον νικητή με βάση τους πόντους
def show_winner(player1_points, player2_points):
    if player1_points > player2_points:
        messagebox.showinfo("Νικητής", f"Ο παίκτης 1 κερδίζει με {player1_points} πόντους, ενώ ο παίκτης 2 συγκέντρωσε {player2_points} πόντους!")
    elif player2_points > player1_points:
        messagebox.showinfo("Νικητής", f"Ο παίκτης 2 κερδίζει με {player2_points} πόντους, ενώ ο παίκτης 1 συγκέντρωσε {player1_points} πόντους!")
    else:
        messagebox.showinfo("Ισοπαλία", f"Οι προβλέψεις είναι ισόβαθμες καθώς οι παίκτες συγκέντρωσαν {player1_points} πόντους!")

# Εύρεση αποτελεσμάτων αγώνα
def check_results():
    while True:
        try:
            api()  # ξαναχρήση του API
        except Exception as e:
            print(f"Δεν ήταν εφικτό το fetch: {e}")
        time.sleep(900)  # timer για 15 λεπτά πριν τον επανέλεγχο

# Εκκίνηση του ελέγχου αποτελεσμάτων (κάθε 15 λεπτά)
def start_checking_results():
    check_results_thread = threading.Thread(target=check_results)
    check_results_thread.daemon = True
    check_results_thread.start()

# Συνάρτηση που βρίσκει το αποτέλεσμα του συγκεκριμένου αγώνα
def find_match_result(results, match):
    for result in results:
        home_team = result['homeTeam']['name']
        away_team = result['awayTeam']['name']
        
        # Σύγκριση των ονομάτων των ομάδων για εύρεση του σωστού αποτελέσματος
        if home_team == match['homeTeam']['name'] and away_team == match['awayTeam']['name']:
            return result['score']['fullTime']  # Επιστροφή του αποτελέσματος του αγώνα

    return None  # Αν δεν βρεθεί το αποτέλεσμα

# Συνάρτηση για το παιχνίδι Tic-Tac-Toe
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

# Ρύθμιση του κύριου παραθύρου της εφαρμογής
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
