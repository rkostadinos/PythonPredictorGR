import requests
import json
import os
import tkinter as tk
from tkinter import messagebox
# inf2021192 Κωνσταντίνος Ράπτης

# Ο σύνδεσμος του API και το token για να μπορέσουμε να χρησιμοποιήσουμε τα δεδομένα του API
uri = 'https://api.football-data.org/v4/matches'
headers = {'X-Auth-Token': 'f3512f1017274e95a9559ea0d9a2debf'}

# Αρχείο για τα ψεύτικα αποτελέσματα
FAKE_RESULTS_FILE = os.path.join(os.path.dirname(__file__), 'pseudo_results.json')

def api():
    try:
        # Προσπάθεια να πάρουμε δεδομένα από το API
        response = requests.get(uri, headers=headers)
        
        if response.status_code == 200:
            matches = response.json().get('matches', [])
            # Αν δεν υπάρχουν αποτελέσματα, επιστρέφουμε ψεύτικα δεδομένα
            if not matches:
                print("Δεν υπάρχουν διαθέσιμοι αγώνες από το API. Φόρτωση ψεύτικων δεδομένων...")
                return get_pseudo_results()
            return matches
        else:
            # Αν υπάρξει σφάλμα, επιστρέφουμε ψεύτικα αποτελέσματα
            print(f"Σφάλμα API: {response.status_code}")
            return get_pseudo_results()
    
    except Exception as e:
        # Αν υπάρξει πρόβλημα με το API, χρησιμοποιούμε τα ψεύτικα δεδομένα
        print(f"Σφάλμα κατά τη σύνδεση με το API: {e}")
        return get_pseudo_results()

# Συνάρτηση που φορτώνει ψεύτικα αποτελέσματα από το αρχείο JSON
def get_pseudo_results():
    try:
        with open(FAKE_RESULTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Σφάλμα κατά τη φόρτωση ψεύτικων δεδομένων: {e}")
        return []  # Επιστρέφει κενή λίστα αν υπάρξει σφάλμα
