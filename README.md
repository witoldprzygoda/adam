# Analiza i wizualizacja sieci tramwajowej w Krakowie

Projekt do analizy danych o sieci tramwajowej w Krakowie z wizualizacją na interaktywnej mapie.

## Struktura projektu

```
.
├── linie_tramwajowe.json       # Dane o 17 liniach tramwajowych z GPS
├── ZADANIE_INSTRUKCJA.md       # Szczegółowa instrukcja zadania (PL)
├── zadanie2.py                 # Szablon do uzupełnienia przez studentów
├── zadanie2_rozwiazanie.py     # Przykładowe rozwiązanie (dla instruktora)
└── mapa_tramwaje.html          # Mapa interaktywna (generowana)
```

## Dane

Plik `linie_tramwajowe.json` zawiera:
- 17 linii tramwajowych
- 154 unikalne przystanki
- Współrzędne GPS dla każdego przystanku (lat, lon)
- Aktualne na 2025 rok

## Zadanie dla studentów

Studenci mają zaimplementować dwie funkcje:

### Część 1: Przetwarzanie i analiza danych (0.75 pkt)
- Wczytanie danych z JSON
- Konwersja do uproszczonego formatu (słownik: linia → krotka przystanków)
- Wypisanie statystyk na ekranie (posortowane malejąco)
- Zwrócenie: słownika linii, słownika statystyk, liczby unikalnych przystanków

### Część 2: Wizualizacja (0.75 pkt)
- Stworzenie interaktywnej mapy z folium
- Rysowanie tras tramwajowych z różnymi kolorami
- Oznaczanie przystanków z tooltipami
- Zapisanie mapy do pliku HTML

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
- **TYLKO** `mapa_tramwaje.html` - interaktywną mapę HTML
- Wyniki drukowane na ekranie (statystyki linii, liczba unikalnych przystanków)

Statystyki linii (top 5):
```
linia 10: 36 przystanków
linia 50: 36 przystanków
linia 52: 34 przystanki
linia 4:  33 przystanki
linia 18: 32 przystanki
```

Liczba unikalnych przystanków: **154**

## Technologie

- Python 3.x
- folium (mapy interaktywne)
- json (przetwarzanie danych)

## Pliki wejściowe i wyjściowe

- **Plik wejściowy**: `linie_tramwajowe.json`
- **Plik wyjściowy**: `mapa_tramwaje.html` (jedyny generowany plik)
- **Wydruk na ekranie**: statystyki i analiza danych

## Autor

Projekt utworzony dla celów edukacyjnych.
