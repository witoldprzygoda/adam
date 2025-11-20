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

Projekt zawiera 17 testów jednostkowych dla funkcji `process_tram_data()`:

- **Testy typu zwracanego**: sprawdzają czy funkcja zwraca poprawne typy danych
- **Testy wartości**: weryfikują poprawność liczby unikalnych przystanków (154) i liczby linii (17)
- **Testy konkretnych linii**: sprawdzają poprawność liczby przystanków dla każdej linii
- **Testy formatowania**: weryfikują poprawność wydruku na ekranie
- **Testy sortowania**: sprawdzają czy wyniki są posortowane malejąco

Wszystkie testy przechodzą pomyślnie ✅

```bash
============================= test session starts ==============================
collected 17 items

tests/test_zadanie2.py::TestProcessTramData::test_return_type PASSED     [  5%]
tests/test_zadanie2.py::TestProcessTramData::test_statistics_dict_type PASSED [ 11%]
tests/test_zadanie2.py::TestProcessTramData::test_unique_stops_type PASSED [ 17%]
tests/test_zadanie2.py::TestProcessTramData::test_unique_stops_count PASSED [ 23%]
tests/test_zadanie2.py::TestProcessTramData::test_number_of_lines PASSED [ 29%]
tests/test_zadanie2.py::TestProcessTramData::test_line_numbers_are_int PASSED [ 35%]
tests/test_zadanie2.py::TestProcessTramData::test_stop_counts_are_int PASSED [ 41%]
tests/test_zadanie2.py::TestProcessTramData::test_stop_counts_positive PASSED [ 47%]
tests/test_zadanie2.py::TestProcessTramData::test_specific_line_counts PASSED [ 52%]
tests/test_zadanie2.py::TestProcessTramData::test_longest_lines PASSED   [ 58%]
tests/test_zadanie2.py::TestProcessTramData::test_shortest_line PASSED   [ 64%]
tests/test_zadanie2.py::TestProcessTramData::test_prints_output PASSED   [ 70%]
tests/test_zadanie2.py::TestProcessTramData::test_prints_all_lines PASSED [ 76%]
tests/test_zadanie2.py::TestProcessTramData::test_output_format PASSED   [ 82%]
tests/test_zadanie2.py::TestProcessTramData::test_output_sorted_descending PASSED [ 88%]
tests/test_zadanie2.py::TestProcessTramData::test_unique_stops_positive PASSED [ 94%]
tests/test_zadanie2.py::TestProcessTramData::test_unique_stops_reasonable PASSED [100%]

============================== 17 passed in 0.78s ==============================
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
