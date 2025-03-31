import os
import hashlib
import time
import tkinter as tk
from tkinter import filedialog, messagebox
import socket

# Base de signatures de virus (exemple)
VIRUS_SIGNATURES = {
    "eicar": "44d88612fea8a8f36de82e1278abb02f",  # EICAR test file (faux virus de test)
    "malware_sample": "5d41402abc4b2a76b9719d911017c592"  # Hash fictif pour un malware
}

# Dossiers à scanner par défaut
SCAN_PATHS = [
    "C:/Users/Public",  # Windows
    "/home/user/Downloads"  # Linux/Mac
]

def hash_file(file_path):
    """Calcule le hash MD5 d'un fichier."""
    try:
        with open(file_path, "rb") as f:
            file_hash = hashlib.md5(f.read()).hexdigest()
        return file_hash
    except Exception as e:
        print(f"[Erreur] Impossible d'analyser {file_path}: {e}")
        return None

def scan_system():
    """Scanne les fichiers et détecte les menaces."""
    start_time = time.time()
    infected_files = []
    
    for path in SCAN_PATHS:
        print(f"[Scan] Analyse du dossier: {path}")
        for root, _, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = hash_file(file_path)
                if file_hash and file_hash in VIRUS_SIGNATURES.values():
                    infected_files.append(file_path)
                    print(f"[Alerte] Virus détecté: {file} ({file_path})")
    
    duration = time.time() - start_time
    print(f"\n[Scan Terminé] {len(infected_files)} fichier(s) infecté(s) détecté(s) en {duration:.2f} sec")
    
    if infected_files:
        generate_report(infected_files)
    else:
        print("Aucune menace détectée.")

def scan_network(ip_range):
    """Scanne un réseau pour détecter les machines actives."""
    print(f"[Scan Réseau] Analyse de {ip_range}")
    for i in range(1, 255):
        ip = f"{ip_range}.{i}"
        response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
        if response == 0:
            print(f"[Réseau] Machine active détectée : {ip}")

def generate_report(infected_files):
    """Génère un rapport avec des recommandations."""
    with open("virus_report.txt", "w") as f:
        f.write("=== Rapport d'analyse ===\n")
        for file in infected_files:
            f.write(f"Virus détecté : {file}\n")
        f.write("\nRecommandations:\n")
        f.write("1. Supprimez les fichiers infectés immédiatement.\n")
        f.write("2. Mettez à jour votre antivirus.\n")
        f.write("3. Évitez d'ouvrir des fichiers suspects provenant d'e-mails inconnus.\n")
        f.write("4. Faites une analyse complète du système.\n")
    print("[Info] Rapport généré: virus_report.txt")

# Interface graphique

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        SCAN_PATHS.append(directory)
        messagebox.showinfo("Dossier ajouté", f"Le dossier {directory} a été ajouté au scan.")

def start_scan():
    scan_system()
    messagebox.showinfo("Scan terminé", "Analyse du système terminée. Consultez la console pour les résultats.")

def start_network_scan():
    ip_range = entry_ip.get()
    if ip_range:
        scan_network(ip_range)
        messagebox.showinfo("Scan Réseau", "Analyse réseau terminée. Consultez la console pour les résultats.")
    else:
        messagebox.showerror("Erreur", "Veuillez entrer une adresse IP de réseau valide.")

root = tk.Tk()
root.title("Détecteur de Virus")
root.geometry("400x300")

tk.Label(root, text="Détection de virus et scan réseau").pack()

tk.Button(root, text="Ajouter un dossier à scanner", command=browse_directory).pack()
tk.Button(root, text="Lancer le scan système", command=start_scan).pack()

tk.Label(root, text="Adresse IP de réseau :").pack()
entry_ip = tk.Entry(root)
entry_ip.pack()
tk.Button(root, text="Scanner le réseau", command=start_network_scan).pack()

root.mainloop()

if __name__ == "__main__":
    scan_system()
