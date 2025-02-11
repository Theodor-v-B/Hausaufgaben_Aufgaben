# 1. Frage den Benutzer nach dem Gesamtpreis der Pizza.
# 2. Frage nach der Anzahl der gesamten Pizzastücke.
# 3. Erstelle eine Liste für die Personen, die gegessen haben.
# 4. Für jede Person:
#    a. Frage nach ihrem Namen.
#    b. Frage, wie viele Stücke sie gegessen hat.
#    c. Speichere diese Daten in einem Dictionary.
# 5. Berechne den Preis pro Stück: preis_pro_stück = gesamtpreis / anzahl_stücke.
# 6. Für jede Person berechne: kosten_person = gegessene_stücke * preis_pro_stück.
# 7. Zeige die Rechnung für jede Person an.
# 8. Falls die Summe der gegessenen Stücke größer als die Gesamtzahl ist, gib eine Fehlermeldung aus.



# Frage den Benutzer nach dem Gesamtpreis der Pizza
gesamtpreis = float(input("Gesamtpreis der Pizza: "))

# Frage nach der Anzahl der gesamten Pizzastücke
anzahl_stücke = int(input("Anzahl der Stücke in der Pizza: "))

# Erstelle ein Dictionary, um die Daten zu speichern
kostendaten = {}

# Anzahl der Personen abfragen
anzahl_personen = int(input("Anzahl der Personen: "))

# Gesamtanzahl der gegessenen Stücke
gesamtgegessene_stücke = 0

# Für jede Person (mehrere Eingaben)
for i in range(anzahl_personen):
    # Frage die Anzahl der gegessenen Stücke
    name = input(f"Gib den Namen von Person {i + 1} ein: ")
    stücke = int(input(f"Wieviele Stücke hat {name} gegessen? "))
    
    # Daten im Dictionary
    kostendaten[name] = stücke
    gesamtgegessene_stücke += stücke  # Addiere die gegessenen Stücke zur Gesamtanzahl

# Preis pro Stück
preis_pro_stück = gesamtpreis / anzahl_stücke

# Kosten pro Person
for person, stücke in kostendaten.items():
    kosten_person = stücke * preis_pro_stück
    # Zeige die Rechnung für jede Person an
    print(f"{person} hat {stücke} Stücke gegessen und muss {kosten_person:.2f} Euro zahlen.")

# Überprüfe, ob die Gesamtanzahl der gegessenen Stücke gültig ist??
if gesamtgegessene_stücke > anzahl_stücke:
    print("Fehler: Die Anzahl der gegessenen Stücke ist größer als die Gesamtanzahl der Pizzastücke.")

