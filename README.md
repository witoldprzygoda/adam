# Analiza i wizualizacja sieci tramwajowej w Krakowie

Projekt do analizy danych o sieci tramwajowej w Krakowie z wizualizacją na interaktywnej mapie.

## Struktura projektu

```
.
├── linie_tramwajowe.json       # Dane o 17 liniach tramwajowych z GPS
├── ZADANIE_INSTRUKCJA.md       # Szczegółowa instrukcja zadania (PL)
├── zadanie2.py                 # Szablon do uzupełnienia przez studentów
├── zadanie2_rozwiazanie.py     # Przykładowe rozwiązanie (dla instruktora)
├── tests/                      # Testy jednostkowe
│   ├── __init__.py
│   └── test_zadanie2.py        # Testy dla funkcji process_tram_data()
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

### Część 1: Analiza danych (0.75 pkt)
- Wczytanie danych z JSON
- Analiza liczby przystanków dla każdej linii
- Wypisanie statystyk na ekranie (posortowane malejąco)
- Zliczenie unikalnych przystanków
- Zwrócenie: słownika statystyk, liczby unikalnych przystanków

### Część 2: Wizualizacja (0.75 pkt)
- Stworzenie interaktywnej mapy z folium
- Rysowanie tras tramwajowych z różnymi kolorami
- Oznaczanie przystanków z tooltipami
- Zapisanie mapy do pliku HTML

**Łącznie: 1.5 pkt**

## Użycie

### Instalacja zależności

```bash
pip install folium pytest
```

### Uruchomienie przykładowego rozwiązania

```bash
python zadanie2_rozwiazanie.py
```

### Uruchomienie szablonu studenta

```bash
python zadanie2.py
```

### Uruchomienie testów

```bash
pytest tests/test_zadanie2.py -v
```

Lub po prostu:

```bash
pytest -v
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

## Testy

Projekt zawiera 3 testy jednostkowe dla funkcji `process_tram_data()`:

- **test_return_values**: sprawdza typy zwracanych wartości oraz liczby (17 linii, 154 unikalne przystanki)
- **test_specific_line_counts**: weryfikuje poprawność liczby przystanków dla wybranych linii
- **test_output_format**: sprawdza format wydruku i sortowanie malejące

Wszystkie testy przechodzą pomyślnie ✅

```bash
============================= test session starts ==============================
collected 3 items

tests/test_zadanie2.py::test_return_values PASSED                        [ 33%]
tests/test_zadanie2.py::test_specific_line_counts PASSED                 [ 66%]
tests/test_zadanie2.py::test_output_format PASSED                        [100%]

============================== 3 passed in 0.70s ==============================
```

## Technologie

- Python 3.x
- folium (mapy interaktywne)
- json (przetwarzanie danych)
- pytest (testy jednostkowe)

## Pliki wejściowe i wyjściowe

- **Plik wejściowy**: `linie_tramwajowe.json`
- **Plik wyjściowy**: `mapa_tramwaje.html` (jedyny generowany plik)
- **Wydruk na ekranie**: statystyki i analiza danych

## Autor

Projekt utworzony dla celów edukacyjnych.
