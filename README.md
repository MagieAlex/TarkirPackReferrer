# 🐉 Tarkir Prerelease Pack Zuweiser

Ein einfaches Python-Tool mit grafischer Benutzeroberfläche zur fairen Verteilung von Tarkir PreRelease-Packs nach Spielerwünschen.

## 🔍 Was macht dieses Tool?

Dieses Tool hilft Organisator*innen (und Stefans) von Magic: The Gathering Prerelease Events (wie im aktuellen Tarkir: Dragonstorm) dabei, die limitierten Packs der fünf Tarkir-Clans (Abzan, Jeskai, Sultai, Mardu, Temur) **nach Wunschpriorität** unter den Spieler*innen zu verteilen.

Dabei wird berücksichtigt:
- die **Anzahl verfügbarer Packs pro Clan**
- bis zu **3 Wunschprioritäten pro Spieler**
- **faire Vergabe**: Unter allen Spielern derselben Priorität zum selben Pack wird ausgelost. Wer leer ausgeht, kommt in den Pool seines Zweitwunsches.


## 💻 Installation & Nutzung

### Voraussetzungen:
- Python 3.x
- `tkinter` (in Standard-Python bereits enthalten)

### Starten:

```bash
python tarkir_gui.py

```

### Eingaben:
Packs pro Clan: über eigene Felder für Abzan, Jeskai, Sultai, Mardu, Temur

Spielerwünsche: im Format Name: A,J,S (ein Spieler pro Zeile)

### Ausgabe:
Welcher Spielerin bekommt welches Pack

Wie viele Packs bleiben übrig

## Bild
![image](https://github.com/user-attachments/assets/a9f448c8-67d9-4027-ac58-b8570a77d848)




## 🧩 Erweiterungsideen
CSV-Import / Export

Zufallsvergabe bei Gleichstand

Web-Oberfläche

Integration in Turnierverwaltungssoftware

