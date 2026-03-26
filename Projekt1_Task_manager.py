#seznam úkolů
ukoly = []  

#fukce pro přidání úkolu
def pridat_ukol(ukoly):
    # cyklus pro zadání názvu
    while True:
        nazev = input("Zadejte název úkolu: ")
        if nazev:
            break
        print("Nezadal jste název úkolu.")

    # cyklus pro zadání popisu
    while True:
        popis = input("Zadejte popis úkolu: ")
        if popis:
            break
        print("Nezadal jste popis úkolu.")

    # přidání do seznamu
    ukoly.append({"Nazev": nazev, "Popis": popis})
    print(f"Úkol '{nazev}' byl přidán")

#funkce pro zobrazení seznamu úkolů
def zobrazit_ukoly(seznam):
      if not seznam:
            print("Žádné úkoly v seznamu")
      else:
         print("\nSeznam ukolů:")
         for i, ukol in enumerate(seznam, 1):
            print(f"{i}. Název: {ukol['Nazev']}, Popis: {ukol['Popis']}")         

#funkce pro odstranění úkolu
def odstranit_ukol(ukoly):
      if not ukoly:
            print("Žádné úkoly k odstranění")
            return
      
      while True:
        zobrazit_ukoly(ukoly)
        try:
         cislo = int(input("Zadejte číslo úkolu ke smazání: "))
         if 1 <= cislo <= len(ukoly):
            odstraneny = ukoly.pop(cislo - 1)
            print(f"Úkol '{odstraneny['Nazev']}' byl smazán")
            break
         else:
             print("Neplatné číslo, zadejte číslo mezi 1 a", len(ukoly))
        except ValueError:
          print("Neplatný vstup, zadejte číslo")                             
    
      
def hlavni_menu():
    while True:
          print("\n Správce úkolů - Hlavní menu")
          print("1. Přidat nový úkol")
          print("2. Zobrazit všechny úkoly")
          print("3. Odstranit úkol")
          print("4. Konec programu")
          volba = input("Vyberte možnost (1-4):")

          if volba == "1":
                pridat_ukol(ukoly)            
          elif volba == "2":
               zobrazit_ukoly(ukoly)
          elif volba == "3":
               odstranit_ukol(ukoly)
          elif volba == "4":
               print("Konec programu")
               break
          else :
               print("Špatně zadané číslo, zkus to znovu")
               volba = input("Vyberte možnost (1-4):")      
hlavni_menu()