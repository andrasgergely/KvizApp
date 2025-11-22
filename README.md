# Focis kvíz

## Hallgató
Ábrahám András

## Feladat leírása
Grafikus kvízprogram, amely véletlenszerű focis kérdéseket jelenít meg.
A felhasználó 10 kérdésre válaszol, a program pedig:
- kiértékeli az eredményt,
- százalékos értékelést ad,
- szöveges minősítést jelenít meg,
- rögzíti a játék időpontját,
- kiszámítja a játék teljes időtartamát.

## Modulok és a modulokban használt függvények

### AA_kviz_modul.py
- **AA_betolt_kerdesek()** – a kérdésbank betöltése  
- **AA_Kviz** osztály:
  - uj()
  - aktualis()
  - valasz()
  - vege()
  - eredmeny()

### Használt külső modulok
- **customtkinter** – grafikus felület  
- **random** – kérdések véletlenszerű kiválasztása  
- **datetime** – játék időpontja és időtartama  

## Osztályok
- **AA_Kviz**

## Futtatás

### Ha még nincs telepítve:
pip install customtkinter

### Indítás:
python main.py

## Funkciók
- 10 véletlenszerű focis kérdés  
- százalékos eredmény  
- szöveges értékelés  
- jól látható, modern GUI  
- játék dátuma és pontos időpontja  
- játék teljes időtartamának mérése  
- „Új játék” funkció időméréssel együtt  

## Fájlok
- **main.py**  
- **AA_kviz_modul.py**  
- **README.md**

