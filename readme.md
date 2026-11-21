# Verkaufsprogramm

Ein kleines Python-Programm, mit dem du Verkäufe erfasst und auswertest:

1. **Daten eingeben** – einen Verkauf eingeben und in `Sales.json` speichern
2. **Auswertung Produkte** – Kreisdiagramm mit dem Umsatz je Produkt
3. **Auswertung Wochenumsatz** – Liniendiagramm mit dem Umsatz je Wochentag und Produkt

Diese Anleitung ist für Einsteiger gedacht. Du musst nur die drei Schritte unten der Reihe nach ausführen.

---

## Was du vorher brauchst

Auf deinem Laptop müssen zwei Programme installiert sein:

| Programm | Wofür? | Download |
|----------|--------|----------|
| **Python** (ab Version 3.8) | führt das Programm aus | https://www.python.org/downloads/ |
| **Git** | lädt das Projekt von GitHub herunter | https://git-scm.com/downloads |

> **Windows-Tipp:** Setze bei der Python-Installation unbedingt den Haken bei **„Add Python to PATH"**. Sonst findet dein Laptop den Befehl `python` später nicht.

Ob alles installiert ist, prüfst du im Terminal (Windows: *Eingabeaufforderung* oder *PowerShell*, macOS/Linux: *Terminal*):

```bash
python --version
git --version
```

Beide Befehle sollten eine Versionsnummer anzeigen. Auf macOS und Linux heißt der Python-Befehl meistens `python3` statt `python`. Benutze dann in dieser Anleitung überall `python3` und `pip3`.

---

## Schritt 1: Projekt von GitHub herunterladen (`git clone`)

Öffne das Terminal und wechsle in den Ordner, in dem das Projekt liegen soll (z. B. deine Dokumente). Dann lade das Projekt herunter:

```bash
git clone https://github.com/DEIN-NAME/DEIN-REPO.git
```

> Ersetze die Adresse durch den echten Link deines Repositorys. Du findest ihn auf der GitHub-Seite des Projekts hinter dem grünen Knopf **„Code"**.

Danach liegt ein neuer Ordner mit dem Namen des Repositorys auf deinem Laptop.

---

## Schritt 2: In den Arbeitsordner wechseln und Bibliotheken installieren

Wechsle in den gerade heruntergeladenen Ordner (ersetze `DEIN-REPO` durch den Ordnernamen):

```bash
cd DEIN-REPO
```

Das Programm nutzt die Bibliothek **matplotlib** für die Diagramme. Installiere sie mit:

```bash
pip install matplotlib
```

Alles andere (`json`, `datetime`) bringt Python schon von selbst mit und muss nicht installiert werden.

### Optional: Abhängigkeiten festhalten (`requirements.txt`)

Wenn du die Abhängigkeiten festhalten willst, damit du das Projekt später auf einem anderen Rechner aufsetzen kannst, speichert

```bash
pip freeze > requirements.txt
```

die installierten Pakete in der Datei `requirements.txt`. Auf dem anderen Rechner installierst du sie dann mit:

```bash
pip install -r requirements.txt
```

> **Tipp:** `pip freeze` listet alle Pakete auf, die in der aktuellen Python-Umgebung installiert sind. Am sauberesten wird die Liste, wenn du das Projekt in einer eigenen Umgebung (siehe „Häufige Probleme" → `venv`) installiert hast.

---

## Schritt 3: Programm starten

Stelle sicher, dass du noch im Projektordner bist, und starte das Programm:

```bash
python verkauf.py
```

Es erscheint das Hauptmenü:

```
===== Hauptmenü =====
1. Daten eingeben
2. Auswertung Produkte (Kreisdiagramm)
3. Auswertung Wochenumsatz (Liniendiagramm)
Exit zum Beenden
```

Tippe eine Zahl ein und bestätige mit **Enter**:

| Eingabe | Was passiert? |
|---------|---------------|
| `1` | Du wählst ein Produkt per Nummer und gibst die verkaufte Menge ein. Der Verkauf wird gespeichert. |
| `2` | Ein Fenster mit dem Kreisdiagramm (Umsatz je Produkt) öffnet sich. |
| `3` | Ein Fenster mit dem Liniendiagramm (Umsatz je Wochentag, aktuelle Woche) öffnet sich. |
| `Exit` | Das Programm wird beendet. |

> Solange ein Diagramm-Fenster offen ist, wartet das Programm. Schließe das Fenster, dann siehst du wieder das Menü.

---

## Wichtige Dateien

| Datei | Inhalt |
|-------|--------|
| `verkauf.py` | das Programm |
| `Products.json` | Liste der Produkte mit Preisen |
| `Sales.json` | gespeicherte Verkäufe (wird vom Programm gefüllt) |
| `requirements.txt` | Liste der benötigten Bibliotheken (nur vorhanden, wenn du sie wie oben erzeugt hast) |

`Products.json` und `Sales.json` müssen **im selben Ordner wie das Programm** liegen. Gibt es `Sales.json` noch nicht, legt das Programm sie beim ersten gespeicherten Verkauf selbst an.

---

## Häufige Probleme

**`python` wird nicht gefunden**
Probiere `python3` statt `python`. Unter Windows hilft oft auch `py`. Wenn nichts davon geht, installiere Python neu und setze den Haken bei „Add Python to PATH".

**`pip` wird nicht gefunden**
Probiere `python -m pip install matplotlib` (bzw. `python3 -m pip install matplotlib`).

**Fehlermeldung `externally-managed-environment` (macOS/Linux)**
Erstelle zuerst eine eigene Umgebung für das Projekt und installiere dann darin:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install matplotlib
```

Unter Windows aktivierst du die Umgebung mit `.venv\Scripts\activate`. Die Umgebung musst du bei jedem neuen Terminal-Fenster erneut aktivieren, bevor du das Programm startest.

**`ModuleNotFoundError: No module named 'matplotlib'`**
Die Bibliothek ist nicht installiert (oder in einer anderen Python-Umgebung). Führe Schritt 2 erneut aus.

**„Es sind noch keine Verkaufsdaten vorhanden!"**
Gib zuerst über Menüpunkt `1` mindestens einen Verkauf ein.

**Das Wochendiagramm sagt, es gibt keine Verkäufe**
Menüpunkt `3` zeigt nur die **aktuelle Kalenderwoche** (Montag bis Sonntag). Verkäufe aus früheren Wochen werden dort nicht angezeigt, sind aber im Kreisdiagramm (Menüpunkt `2`) enthalten.