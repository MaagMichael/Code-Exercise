import json
from datetime import datetime

import matplotlib.pyplot as plt

# Namen der Dateien (müssen im selben Ordner wie dieses Programm liegen)
PRODUKTE_DATEI = "Products.json"
VERKAEUFE_DATEI = "Sales.json"

#  -------------------- Hilfsfunktionen zum Laden und Speichern von JSON-Dateien
def lade_json(dateiname):
    """Liest eine JSON-Datei und gibt den Inhalt als Liste zurück."""
    try:
        with open(dateiname, "r", encoding="utf-8") as datei:
            return json.load(datei)
    except FileNotFoundError:
        # Gibt es die Datei noch nicht, starten wir mit einer leeren Liste
        return []


def speichere_json(dateiname, daten):
    """Schreibt eine Liste in eine JSON-Datei."""
    with open(dateiname, "w", encoding="utf-8") as datei:
        json.dump(daten, datei, indent=2, ensure_ascii=False)

# -------------------- Menüfunktionen für die verschiedenen Optionen im Hauptmenü

# Menupunkt 1: Daten eingeben
def daten_eingeben():
    """Menüpunkt 1: Verkauf eingeben und speichern."""
    produkte = lade_json(PRODUKTE_DATEI)

    # Produkte mit Nummern anzeigen
    print("\n--- Daten eingeben ---")
    for nummer, produkt in enumerate(produkte, start=1):
        print(f"{nummer}. {produkt['Produkt']} ({produkt['Preis (EUR)']:.2f} EUR)")

    # Produkt auswählen
    auswahl = input("Welches Produkt? (Nummer eingeben): ")
    if not auswahl.isdigit() or not (1 <= int(auswahl) <= len(produkte)):
        print("Ungültige Auswahl!")
        return
    produkt = produkte[int(auswahl) - 1]

    # Verkaufsmenge eingeben
    menge = input("Verkaufsmenge: ")
    if not menge.isdigit() or int(menge) < 1:
        print("Bitte eine ganze Zahl größer als 0 eingeben!")
        return
    menge = int(menge)

    # Umsatz berechnen: Menge mal Preis
    umsatz = round(menge * produkt["Preis (EUR)"], 2)

    # Neuen Datensatz erstellen
    jetzt = datetime.now()
    datensatz = {
        "Datum": jetzt.strftime("%Y-%m-%d"),
        "Uhrzeit": jetzt.strftime("%H:%M"),
        "Produkt": produkt["Produkt"],
        "Anzahl": menge,
        "Umsatz": umsatz,
    }

    # An die bestehenden Verkäufe anhängen und speichern
    verkaeufe = lade_json(VERKAEUFE_DATEI)
    verkaeufe.append(datensatz)
    speichere_json(VERKAEUFE_DATEI, verkaeufe)

    print(f"Gespeichert: {menge} x {produkt['Produkt']} = {umsatz:.2f} EUR")

# Menupunkt 2: Auswertung Produkte
def auswertung_produkte():
    """Menüpunkt 2: Kreisdiagramm mit dem Umsatz je Produkt."""
    produkte = lade_json(PRODUKTE_DATEI)
    verkaeufe = lade_json(VERKAEUFE_DATEI)

    if not verkaeufe:
        print("\nEs sind noch keine Verkaufsdaten vorhanden!")
        return

    # Umsatz je Produkt aufsummieren (alle Produkte starten bei 0)
    umsatz_je_produkt = {produkt["Produkt"]: 0.0 for produkt in produkte}
    for verkauf in verkaeufe:
        name = verkauf["Produkt"]
        if name in umsatz_je_produkt:
            umsatz_je_produkt[name] += verkauf["Umsatz"]

    namen = list(umsatz_je_produkt.keys())
    werte = list(umsatz_je_produkt.values())
    gesamt = sum(werte)

    if gesamt == 0:
        print("\nDer Gesamtumsatz ist 0 - es gibt nichts darzustellen.")
        return

    # Für jedes Produkt eine eigene Farbe
    farben = plt.get_cmap("tab10")(range(len(namen)))

    # Beschriftung im Diagramm: Umsatz in Euro und Prozentanteil
    def beschriftung(prozent):
        if prozent == 0:
            return ""  # Produkte ohne Umsatz nicht beschriften
        euro = prozent / 100 * gesamt
        return f"{euro:.2f} EUR\n{prozent:.1f} %"

    fig, ax = plt.subplots(figsize=(8, 6))
    keile, _texte, _prozente = ax.pie(
        werte,
        colors=farben,
        autopct=beschriftung,
        startangle=90,
        counterclock=False,
        wedgeprops={"edgecolor": "white"},
    )

    # Legende mit Produktname und Umsatz
    legendentexte = [f"{n} ({w:.2f} EUR)" for n, w in zip(namen, werte)]
    ax.legend(keile, legendentexte, title="Produkte",
              loc="center left", bbox_to_anchor=(1, 0.5))

    ax.set_title(f"Umsatz je Produkt (Gesamt: {gesamt:.2f} EUR)")
    ax.axis("equal")  # Kreis statt Ellipse
    plt.tight_layout()
    plt.show()

# Menupunkt 3: Auswertung Wochenumsatz
def auswertung_wochenumsatz():
    """Menüpunkt 3: Wochenumsatz (kommt später)."""
    print("\nDiese Funktion kommt später.")

# -------------------- Hauptmenü
def main():
    """Hauptmenü: läuft in einer Schleife, bis der Benutzer 'Exit' eingibt."""
    while True:
        print("\n===== Hauptmenü =====")
        print("1. Daten eingeben")
        print("2. Auswertung Produkte (Kreisdiagramm)")
        print("3. Auswertung Wochenumsatz")
        print("Exit zum Beenden")

        wahl = input("Ihre Wahl: ").strip().lower()

        if wahl == "1":
            daten_eingeben()
        elif wahl == "2":
            auswertung_produkte()
        elif wahl == "3":
            auswertung_wochenumsatz()
        elif wahl == "exit":
            print("Programm beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe, bitte 1, 2, 3 oder Exit eingeben.")


main()