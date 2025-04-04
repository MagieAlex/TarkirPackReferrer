# 🐉 Tarkir Prerelease Pack Zuweiser

Ein einfaches Python-Tool mit grafischer Benutzeroberfläche zur fairen Verteilung von Tarkir PreRelease-Packs nach Spielerwünschen.

## 🔍 Was macht dieses Tool?

Dieses Tool hilft Organisator*innen (und Stefans) von Magic: The Gathering Preelease Events (z. B. „Khans of Tarkir“ oder „Dragons of Tarkir“) dabei, die limitierten Packs der fünf Tarkir-Clans (Abzan, Jeskai, Sultai, Mardu, Temur) **nach Wunschpriorität** unter den Spieler*innen zu verteilen.

Dabei wird berücksichtigt:
- die **Anzahl verfügbarer Packs pro Clan**
- bis zu **3 Wunschprioritäten pro Spieler**
- **faire Vergabe**: Wer zuerst einen verfügbaren Wunsch erfüllt bekommt, erhält diesen.


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
![image](https://github.com/user-attachments/assets/9eaea770-a9d7-43df-9567-b708a8fe2ba3)



## 🧩 Erweiterungsideen
CSV-Import / Export

Zufallsvergabe bei Gleichstand

Web-Oberfläche

Integration in Turnierverwaltungssoftware

