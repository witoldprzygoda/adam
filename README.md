# Analiza i wizualizacja sieci tramwajowej w Krakowie

Projekt do analizy danych o sieci tramwajowej w Krakowie z wizualizacją na interaktywnej mapie.

## Struktura projektu

```
.
├── krakow_tram_data.json        # Dane o 17 liniach tramwajowych z GPS
├── krakow_tram_map.py          # Skrypt demonstracyjny
├── ZADANIE_INSTRUKCJA.md       # Szczegółowa instrukcja zadania (PL)
├── zadanie2.py                 # Szablon do uzupełnienia przez studentów
├── zadanie2_rozwiazanie.py     # Przykładowe rozwiązanie (dla instruktora)
├── tramwaje_out.json           # Plik wyjściowy (generowany)
└── mapa_tramwaje.html          # Mapa interaktywna (generowana)
```

## Dane

Plik `krakow_tram_data.json` zawiera:
- 17 linii tramwajowych
- 154 unikalne przystanki
- Współrzędne GPS dla każdego przystanku (lat, lon)
- Aktualne na 2025 rok

## Zadanie dla studentów

Studenci mają zaimplementować dwie funkcje:

### Część 1: Przetwarzanie danych (0.75 pkt)
- Wczytanie danych z JSON
- Konwersja do uproszczonego formatu
- Analiza statystyczna (liczba przystanków na linię)
- Zliczenie unikalnych przystanków

### Część 2: Wizualizacja (0.75 pkt)
- Stworzenie interaktywnej mapy z folium
- Rysowanie tras tramwajowych
- Oznaczanie przystanków z tooltipami

**Łącznie: 1.5 pkt**

## Użycie

### Instalacja zależności

```bash
pip install folium
```

### Uruchomienie przykładowego rozwiązania

```bash
python zadanie2_rozwiazanie.py
```

### Uruchomienie szablonu studenta

```bash
python zadanie2.py
```

## Wyniki

Program generuje:
- `tramwaje_out.json` - przetworzone dane w formacie słownika
- `mapa_tramwaje.html` - interaktywną mapę HTML

Statystyki linii (top 5):
```
linia 10: 36 przystanków
linia 50: 36 przystanków
linia 52: 34 przystanki
linia 4:  33 przystanki
linia 18: 32 przystanki
```

## Technologie

- Python 3.x
- folium (mapy interaktywne)
- json (przetwarzanie danych)

## Autor

Projekt utworzony dla celów edukacyjnych.
