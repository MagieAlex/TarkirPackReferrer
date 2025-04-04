import tkinter as tk
from tkinter import messagebox
from collections import defaultdict
import random

clans = {
    "A": "Abzan",
    "J": "Jeskai",
    "S": "Sultai",
    "M": "Mardu",
    "T": "Temur"
}
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
            if ":" not in line:
                continue
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

    spieler_liste = list(wishes.keys())

    # Wunschbasierte Verteilung in 3 Runden
    for wunsch_stufe in range(3):
        # Schritt 1: Sammle Spieler, die noch kein Pack haben + Wunsch auf dieser Stufe äußern
        clan_to_players = defaultdict(list)
        for spieler in spieler_liste:
            if spieler in zuweisung:
                continue
            if wunsch_stufe < len(wishes[spieler]):
                clan = wishes[spieler][wunsch_stufe]
                clan_to_players[clan].append(spieler)

        # Schritt 2: Zufallsvergabe pro Clan
        for clan, bewerber in clan_to_players.items():
            random.shuffle(bewerber)
            freie_packs = pack_rest.get(clan, 0)
            for spieler in bewerber[:freie_packs]:
                zuweisung[spieler] = clan
                pack_rest[clan] -= 1

    # Fallback-Verteilung aus anderen Clans
    for spieler in spieler_liste:
        if spieler in zuweisung:
            continue
        übrige_clans = [clan for clan in clan_namen if clan not in wishes[spieler] and pack_rest.get(clan, 0) > 0]
        if übrige_clans:
            clan = random.choice(übrige_clans)
            zuweisung[spieler] = clan
            pack_rest[clan] -= 1
        else:
            zuweisung[spieler] = "KEIN PACK MEHR VERFÜGBAR"

    # Ausgabe
    output_text.insert(tk.END, f"=== Pack-Zuweisung ===\n")
    for spieler in spieler_liste:
        clan = zuweisung[spieler]
        fallback = ""
        if clan not in wishes[spieler]:
            fallback = " (außerhalb Wunschliste)" if "KEIN" not in clan else ""
        output_text.insert(tk.END, f"{spieler} bekommt ein {clan}-Pack{fallback}\n")
    
    output_text.insert(tk.END, "\n=== Übrige Packs ===\n")
    for clan, rest in pack_rest.items():
        output_text.insert(tk.END, f"{clan}: {rest} Pack(s)\n")

# GUI
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

tk.Button(root, text="Zuweisung starten", command=verteile_packs).pack(pady=10)
output_text = tk.Text(root, height=15, width=50)
output_text.pack()

root.mainloop()
