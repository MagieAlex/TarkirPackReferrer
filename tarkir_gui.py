import tkinter as tk
from tkinter import messagebox
from collections import defaultdict
import random

# Clan-Abkürzungen zu Namen
clans = {
    "A": "Abzan",
    "J": "Jeskai",
    "S": "Sultai",
    "M": "Mardu",
    "T": "Temur"
}

# Umgekehrt für Einzeltabellenzuordnung
clan_namen = ["Abzan", "Jeskai", "Sultai", "Mardu", "Temur"]

clan_entry_fields = {}

def parse_packs():
    packs = {}
    try:
        for clan in clan_namen:
            val = int(clan_entry_fields[clan].get())
            packs[clan] = val
    except ValueError:
        messagebox.showerror("Fehler", "Alle Pack-Felder müssen ganze Zahlen sein.")
    return packs

def parse_players(text):
    players = {}
    try:
        for line in text.strip().split("\n"):
            name, wunsch_text = line.split(":")
            wünsche = [clans[w.upper()] for w in wunsch_text.strip().split(",") if w.upper() in clans]
            players[name.strip()] = wünsche
    except:
        messagebox.showerror("Fehler", "Spieler-Eingabe fehlerhaft (z.B. Anna: J,A,T)")
    return players

def verteile_packs():
    output_text.delete("1.0", tk.END)
    packs = parse_packs()
    wishes = parse_players(player_text.get("1.0", tk.END))
    zuweisung = {}
    pack_rest = packs.copy()

    # Wunschbasierte Vergabe (Prio 1 → 3)
    for wunsch_stufe in range(3):
        for spieler, wunschliste in wishes.items():
            if spieler in zuweisung:
                continue
            if wunsch_stufe < len(wunschliste):
                clan = wunschliste[wunsch_stufe]
                if pack_rest.get(clan, 0) > 0:
                    zuweisung[spieler] = clan
                    pack_rest[clan] -= 1

    # Fallback-Verteilung: zufälliger Clan außerhalb Wunschliste
    for spieler in wishes:
        if spieler in zuweisung:
            continue
        # Suche übrige Clans, die nicht in den Wünschen sind
        übrige_clans = [clan for clan in clan_namen if clan not in wishes[spieler] and pack_rest.get(clan, 0) > 0]
        if übrige_clans:
            clan = random.choice(übrige_clans)
            zuweisung[spieler] = clan
            pack_rest[clan] -= 1
        else:
            zuweisung[spieler] = "KEIN PACK MEHR VERFÜGBAR"

    # Ausgabe
    output_text.insert(tk.END, "=== Pack-Zuweisung ===\n")
    for spieler, clan in zuweisung.items():
        output_text.insert(tk.END, f"{spieler} bekommt ein {clan}-Pack\n")
    
    output_text.insert(tk.END, "\n=== Übrige Packs ===\n")
    for clan, rest in pack_rest.items():
        output_text.insert(tk.END, f"{clan}: {rest} Pack(s)\n")

# GUI aufbauen
root = tk.Tk()
root.title("Tarkir PreRelease-Zuweiser")

frame_packs = tk.LabelFrame(root, text="Anzahl PreRelease Packs pro Clan")
frame_packs.pack(padx=10, pady=5)

for clan in clan_namen:
    row = tk.Frame(frame_packs)
    row.pack(fill="x", padx=5, pady=2)
    tk.Label(row, text=clan, width=10, anchor="w").pack(side=tk.LEFT)
    entry = tk.Entry(row, width=5)
    entry.insert(0, "0")
    entry.pack(side=tk.LEFT)
    clan_entry_fields[clan] = entry

tk.Label(root, text="Spielerwünsche (z.B. Anna: J,A,T)").pack()
player_text = tk.Text(root, height=10, width=50)
player_text.pack()
player_text.insert(tk.END, "Anna: J,A,T")

tk.Button(root, text="Zuweisung starten", command=verteile_packs).pack(pady=5)

output_text = tk.Text(root, height=15, width=50)
output_text.pack()

root.mainloop()
