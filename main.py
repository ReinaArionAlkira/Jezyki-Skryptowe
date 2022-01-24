import random

# funkcja rozpoczynająca grę
# tworzenie talii, losowanie pozycji

def WygenerujGre():
  # listy pomocnicze do tworzenia pełnej karty
  kartyKolor = ["KIER", "KARO", "TREFL", "PIK"]
  kartyFigura = ["9", "10", "J", "Q", "K", "A"]
  talia = []
  
  # uzupełnianie tablicy talia kartami
  for x in kartyKolor:
    for y in kartyFigura:
      talia.append(y + " " + x)

  # tasowanie talii
  random.shuffle(talia)
  # przypisywanie pozycji pól według kolejności i wstawianie tam wylosowanych kart
  mapa = {}
  i = 0
  for x in kartyKolor:
    for y in kartyFigura:
      if i == len(talia)-1:
        mapa[y + " " + x] = "[]"
      mapa[y + " " + x] = talia[i]
      i += 1
  return mapa, talia 
# funkcja zmieniająca karte na mapie
def zamienKarty(mapa, karta):
  kartaNaMapie = mapa[karta]
  mapa[karta] = karta
  return kartaNaMapie

# zamiana kart z dłoni na pole dopóki trzymaną kartąnie będzie As Pik
def rotacjaKart(mapa, talia):
  listaKrokow = []
  trzymanaKarta = talia[len(talia) - 1]
  while trzymanaKarta != "A PIK":
    krok = trzymanaKarta + " -> "
    trzymanaKarta = zamienKarty(mapa, trzymanaKarta)
    krok += trzymanaKarta
    listaKrokow.append(krok)
  listaKrokow.append("A PIK -> []")
  zamienKarty(mapa, trzymanaKarta)
  return listaKrokow


def sprawdzWynik(mapa):
  wygrana = True
  for x in mapa:
    if mapa[x] != x:
      wygrana = False
      break
  return wygrana

def naWyjscie(mapa):
  wynik = ""
  for x in mapa:
    wynik += x + " => " + mapa[x] + "\n"
  return wynik

def main():  
  liczbaGier = 0
  while True:
    liczbaGier += 1
    mapa, talia = WygenerujGre()
    listaKrokow = rotacjaKart(mapa, talia)
    if sprawdzWynik(mapa):
      print("Wygrana po " + str(liczbaGier) + " próbach.")
      # print("\n".join(listaKrokow))
      # print("\n" + naWyjscie(mapa))
      break
  
  open('listaKrokow.txt', 'w').write("\n".join(listaKrokow))
  open('rezultat.txt', 'w').write("WYGRANA " + str(liczbaGier))
  print("Lista kroków została zapisana w pliku listaKrokow.txt.")
  print("Użyj skryptu createSite.py aby wygenerować wizualizację w postaci pliku HTML")

main()   

