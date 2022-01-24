@echo off
:menu
cls
echo ======================
echo 	Menu		
echo ======================
echo 1. program
echo 2. program z wejsciem
echo 3. opis programu
echo 4. backup
echo 5. exit
set /p wybor=Wybierz opcje: 
if %wybor% EQU 1 GOTO start
if %wybor% EQU 2 GOTO inputer
if %wybor% EQU 3 GOTO info
if %wybor% EQU 4 GOTO backup
if %wybor% EQU 5 exit 
goto menu

:start
start main.py
start createSite.py
start raport\raport.html
goto menu

:inputer
start playFromInputDeck.py
start createSite.py
start raport\raport.html
goto menu

:info
cls
echo Program rozgrywa partie pasjansa na specjalnych zasadach.
echo W pasjansie tym, po przetasowaniu talii 24 krat, ukladamy (koszulkami do gory) 
echo cztery rzedy krat po szesc - z wyjatkiem rzedu czwartego, w ktorym ostatnia karte zatrzymujemy w dloni.
echo Celem gry jest ulozenie kart we wlasciwej kolejnosci: 
echo - w pierwszym rzedzie kiery (9, 10, walet, dama, krol i as), 
echo - w kolejnych odpowiednie kolory to: karo, trefl i pik (kolejnosc figur jak w kierach).
echo Gra konczy sie, gdy w dloni miec bedziemy asa pik. Jesli karta w dloni nie jest as pik,
echo to kladziemy ja (obrazkiem do gory) na odpowiadajace jej miejsce (np. gdyby byla to dama
echo tref, to odlozylibysmy ja do rzedu trzeciego do czwartej kolumny), biorac w dlon lezaca tam karte. 
echo Jesli natrafimy ostatecznie na asa pik, to (o ile bedzie taka potrzeba) odslaniamy,
echo nie zmieniajac ich polozen w ukladzie, pozostale nieodsloniete (lezace koszulkami do gory) dotychczas karty. 
echo Jezeli wszystkie karty lezec beda we wlasciwej kolejnosci - wygralismy, jesli nie - przegralismy.
echo
echo W momencie zwyciestwa, pokazuje za ktorym razem trafil na zwycieska rozgrywke oraz pokazuje kazdy jej etap.
pause
goto menu

:backup
if not exist backup (
mkdir backup
)
cls
set date=%date:~-0,4%%date:~4,2%%date:~6,4%
if exist backup\%date% (
echo "Robiles juz dzisiaj backup. Usun ja aby stworzyc nowa"

pause
goto menu
) else (
mkdir backup\%date%
xcopy *.* backup\%date%
pause
)
goto menu