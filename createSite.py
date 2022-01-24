kartyKolor = ["KIER", "KARO", "TREFL", "PIK"]
kartyFigura = ["9", "10", "J", "Q", "K", "A"]

def generujMapePozycji():
  mapaPozycji = {}

  for idxFigura, figura in enumerate(kartyFigura):
    for idxKolor, kolor in enumerate(kartyKolor):
      mapaPozycji[figura + " " + kolor] = [idxFigura, idxKolor]

  return mapaPozycji

"""
[
  [9 KIER] [9 KARO] [9 TRELF] [9 PIK],
  [10 KIER] [10 KARO] [10 TRELF] [10 PIK],
  ...
]
"""

def wygenerujPustaMape():
  mapa = []
  for figura in kartyFigura:
    wiersz = []
    for kolor in kartyKolor:
      wiersz.append("X")
    mapa.append(wiersz)
  return mapa

def odkryjCalaMape(mapa, mapaPozycji):
  for key in mapaPozycji:
    pozycja = mapaPozycji[key]
    mapa[pozycja[0]][pozycja[1]] = key

def wykonajKrokNaMapie(mapa, mapaPozycji, krok):
  [trzymana, otrzymana] = krok.split(" -> ")
  pozycja = mapaPozycji[trzymana]
  mapa[pozycja[0]][pozycja[1]] = trzymana
  return otrzymana

def mapaNaTabeleHTML(mapa, reka):
  html = "<table>\n"
  html += "<tr>\n"
  html += "<td>Kier</td><td>Karo</td><td>Trelf</td><td>Pik</td>\n"
  html += "</tr>\n"

  for wiersz in mapa:
    html += "<tr>\n"
    for kolumna in wiersz:
      html += "<td>" + kolumna + "</td>"
    html += "</tr>\n"
  
  # łapka uwu
  html += "<tr><td colspan='4'>Trzymana Karta: " + reka + "</td></tr>\n"

  html += "</table>"
  
  return html
  

def ramyHTMLGora():
  html = ""
  html += "<!DOCTYPE html>\n"
  html += "<html lang=\"pl\">\n"
  html += "  <head>\n"
  html += "    <meta charset=\"utf-8\" />\n"
  html += "    <title>Raport - Wizualizacja</title>\n"
  html += "    <style>td { text-align: center; width: 300px; } table, tr, td { border: solid 1px black } }</style>\n"
  html += "  </head>\n"
  html += "  <body><center>\n"
  return html

def ramyHTMLDol():
  html = "</center></body>\n" 
  html += "</html>\n"

  return html;

def generujHTMLa(listaKrokow, czyWygrana, liczbaGier):
  html = ramyHTMLGora()
  html += "<h1>" + czyWygrana + " po " + liczbaGier + " grach" + "</h1>"
  html += "<table>\n"
  html += " <tr>\n"
  html += "   <td>Krok</td> <td>Plansza</td>"
  html += " </tr>\n"

  i = 0
  mapaPozycji = generujMapePozycji()
  mapa = wygenerujPustaMape()

  # Krok 0
  kartaWReku = listaKrokow[0].split(" -> ")[0];
  html += "<tr>\n"
  html += "<td>0.</td>"
  html += "<td>" + mapaNaTabeleHTML(mapa, kartaWReku) + "</td>"
  html += "</tr>"

  for krok in listaKrokow:
    i += 1
    kartaWReku = wykonajKrokNaMapie(mapa, mapaPozycji, krok)
    html += "<tr>\n"
    html += "<td>" + str(i) + ".</td>"
    html += "<td>" + mapaNaTabeleHTML(mapa, kartaWReku) + "</td>"
    html += "</tr>"

  # Finish
  odkryjCalaMape(mapa, mapaPozycji)
  html += "<tr>\n"
  html += "<td>" + "KONIEC" + "</td>"
  html += "<td>" + mapaNaTabeleHTML(mapa, kartaWReku) + "</td>"
  html += "</tr>"

  html += "</table>\n"
  html += ramyHTMLDol()
  return html

def main():
  listaKrokowStr = open("listaKrokow.txt").read();
  
  rezultat = open("rezultat.txt").read();
  print("aa")
  [czyWygrana, liczbaGier] = rezultat.split(' ')
  listaKrokow = listaKrokowStr.split("\n");
  plik = open("raport\\raport.html", "w", encoding = "utf8").write(generujHTMLa(listaKrokow, czyWygrana, liczbaGier))
  listaKrokowStr.close()
  rezultat.close()
  plik.close()
main()
