#funkcja rozpoczynająca grę
#tworzenie talii, losowanie pozycji

def WygenerujGre(talia):
  #listy pomocnicze do tworzenia pełnej karty
  kartyKolor = ["KIER", "KARO", "TREFL", "PIK"]
  kartyFigura = ["9", "10", "J", "Q", "K", "A"]
  
  #przypisywanie pozycji pól według kolejności iwstawianie tam wylosowanych kart
  mapa = {}
  i = 0
  for x in kartyKolor:
    for y in kartyFigura:
      if i == len(talia)-1:
        mapa[y + " " + x] = "[]"
      mapa[y + " " + x] = talia[i]
      i += 1
  return mapa
#funkcja zmieniająca karte na mapie
def zamienKarty(mapa, karta):
  kartaNaMapie = mapa[karta]
  mapa[karta] = karta
  return kartaNaMapie

#zamiana kart z dłoni na pole dopóki trzymaną kartąnie będzie As Pik
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

def odczytajTalieZWejscia():
  dozwoloneKolory = ["KIER", "KARO", "TREFL", "PIK"]
  dozwoloneFigury = ["9", "10", "J", "Q", "K", "A"]

  try:
    taliaStr = open('wejscie.txt').read()
    talia = taliaStr.split("\n");
    # Sprawdzanie rozmiaru talii
    if (len(talia) != 24):
      print("Niepoprawna ilość kart na wejściu. Wpisz 24 karty w formacie FIGURA KOLOR. Dozwolone figury to: " + ",".join(dozwoloneFigury) + "; dozwolone kolory: " + ",".join(dozwoloneKolory))
      exit(1)

    # Sprawdzanie duplikatów
    if (len(talia) != len(set(talia))):
      print("Karty na wejściu nie mogą się powtarzać!")
      exit(1)

    for karta in talia:
      [figura, kolor] = karta.split(' ')
      if figura not in dozwoloneFigury:
        print("Figura " + figura + " nie jest dozwoloną figurą. Dozwolone figury to: " + ",".join(dozwoloneFigury))
        exit(1)
      if kolor not in dozwoloneKolory:
        print("Kolor " + kolor + " nie jest dozwolonym kolorem. Dozwolone kolory to: " + ",".join(dozwoloneKolory))
        exit(1)

    return talia;
  except Exception as e:
    print("Nie udało się odczytać pliku, czy plik wejscie.txt istnieje?")
    print(e)
    exit(1);

def main():  
  talia = odczytajTalieZWejscia()
  mapa = WygenerujGre(talia)

  listaKrokow = rotacjaKart(mapa, talia)
  
  if (sprawdzWynik(mapa)):
    print("Gratulacja! Podana na wejściu talia jest talią, która wygrywa grę w " + str(len(listaKrokow)) + " krokow!")
  else:
    print("Niestety, talia podana na wejściu przegrywa grę")

  open('listaKrokow.txt', 'w').write("\n".join(listaKrokow))
  open('rezultat.txt', 'w').write("WYGRANA 1")
  print("Lista kroków została zapisana w pliku listaKrokow.txt.")
  #print("Użyj skryptu createSite.py aby wygenerować wizualizację w postaci pliku HTML")
    
main()

