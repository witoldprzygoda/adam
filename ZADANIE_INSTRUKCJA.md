# Zadanie: Analiza i wizualizacja sieci tramwajowej w Krakowie

## Cel zadania

Zadanie polega na przetworzeniu danych o liniach tramwajowych w Krakowie, wykonaniu analizy statystycznej oraz stworzeniu interaktywnej mapy sieci tramwajowej za pomocą biblioteki `folium`.

## Dane wejściowe

W pliku `krakow_tram_data.json` znajdują się dane o 17 liniach tramwajowych w Krakowie wraz z przystankami i ich współrzędnymi GPS (stan: 2025). Struktura danych:

```json
{
  "opis": "Linie tramwajowe w Krakowie z przystankami i współrzędnymi GPS (stan: 2025)",
  "liczba_linii": 17,
  "linie": [
    {
      "linia": "1",
      "przystanki": [
        {"nazwa": "Wzgórza Krzesławickie", "lat": 50.094815, "lon": 20.065271},
        {"nazwa": "Jarzębiny", "lat": 50.0920145, "lon": 20.0611215},
        ...
      ]
    },
    ...
  ]
}
```

## Wczytywanie danych

W języku Python czytanie danych w formacie JSON wykonywane jest z pomocą modułu `json`:

```python
import json

with open('krakow_tram_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
```

Dostęp do danych:
- `data['linie']` - lista wszystkich linii tramwajowych
- `data['linie'][0]['linia']` - numer pierwszej linii (np. "1")
- `data['linie'][0]['przystanki']` - lista przystanków dla pierwszej linii
- `data['linie'][0]['przystanki'][0]['nazwa']` - nazwa pierwszego przystanku
- `data['linie'][0]['przystanki'][0]['lat']` - szerokość geograficzna przystanku
- `data['linie'][0]['przystanki'][0]['lon']` - długość geograficzna przystanku

## Zadanie do wykonania

### Część 1: Przetwarzanie danych (0.75 pkt)

Napisz funkcję `process_tram_data(input_file, output_file)`, która:

1. **Wczytuje dane** z pliku `input_file` (np. `krakow_tram_data.json`)

2. **Przetwarza dane** do uproszczonego formatu - słownika, gdzie:
   - **Klucz**: numer linii tramwajowej (jako `int`, np. 1, 3, 4, ...)
   - **Wartość**: krotka (`tuple`) zawierająca wszystkie nazwy przystanków danej linii

   Przykład oczekiwanego formatu dla linii nr 1:
   ```python
   {
       1: ('Wzgórza Krzesławickie', 'Jarzębiny', 'Darwina', 'Wańkowicza', ...),
       3: ('Nowy Bieżanów P+R', 'Ćwiklińskiej', ...),
       ...
   }
   ```

3. **Zapisuje wynik** do pliku `output_file` w formacie JSON:
   ```python
   with open(output_file, 'w', encoding='utf-8') as file:
       json.dump(trams_dict, file, ensure_ascii=False, indent=2)
   ```

4. **Wypisuje na ekranie**:
   - Informacje w formacie: `linia X: Y przystanków`
   - Posortowane po liczbie przystanków (malejąco)
   - Na końcu: całkowitą liczbę **unikalnych** przystanków (przystanki mogą być współdzielone przez różne linie)

5. **Zwraca**:
   - Słownik: `{numer_linii: liczba_przystanków}` (np. `{1: 28, 3: 24, ...}`)
   - Liczbę unikalnych przystanków (jako `int`)

### Część 2: Wizualizacja na mapie (0.75 pkt)

Napisz funkcję `create_tram_map(input_file, output_map_file)`, która:

1. **Wczytuje dane** z pliku `input_file`

2. **Tworzy interaktywną mapę** używając biblioteki `folium`:
   ```python
   import folium

   # Stwórz mapę wycentrowaną na Krakowie
   m = folium.Map(location=[50.0, 20.0], zoom_start=12, tiles="cartodbpositron")
   ```

3. **Rysuje trasy tramwajowe** jako linie (`PolyLine`):
   - Każda linia ma inny kolor (użyj listy kolorów)
   - Dodaj tooltip z numerem linii
   - Przykład:
   ```python
   folium.PolyLine(
       coordinates,  # lista krotek (lat, lon)
       color=color,
       weight=3,
       opacity=0.9,
       tooltip=f"Linia {line_number}"
   ).add_to(m)
   ```

4. **Oznacza przystanki** jako punkty (`CircleMarker`):
   - Tooltip zawierający nazwę przystanku i listę linii, które przez niego przejeżdżają
   - Przykład: `"Rondo Mogilskie – linie: 3, 4, 5, 9, 10, 14, 20, 50, 52"`

5. **Zapisuje mapę** do pliku HTML:
   ```python
   m.save(output_map_file)
   ```

## Wymagania techniczne

### Instalacja wymaganych bibliotek

```bash
pip install folium
```

### Struktura plików

```
ZADANIE2/
├── krakow_tram_data.json        # Plik wejściowy (dostarczony)
├── zadanie2.py                   # Twój kod (do uzupełnienia)
├── tramwaje_out.json            # Plik wyjściowy (generowany)
└── mapa_tramwaje.html           # Mapa HTML (generowana)
```

### Kod do uzupełnienia w `zadanie2.py`

```python
import json
import folium

def process_tram_data(input_file, output_file):
    """
    Przetwarza dane tramwajowe i zapisuje uproszczony format.

    Args:
        input_file: ścieżka do pliku wejściowego JSON
        output_file: ścieżka do pliku wyjściowego JSON

    Returns:
        tuple: (słownik {linia: liczba_przystanków}, liczba_unikalnych_przystanków)
    """
    # TODO: Implementacja
    pass

def create_tram_map(input_file, output_map_file):
    """
    Tworzy interaktywną mapę sieci tramwajowej.

    Args:
        input_file: ścieżka do pliku wejściowego JSON
        output_map_file: ścieżka do pliku wyjściowego HTML
    """
    # TODO: Implementacja
    pass

if __name__ == "__main__":
    # Część 1: Przetwarzanie danych
    stats, unique_stops = process_tram_data('krakow_tram_data.json', 'tramwaje_out.json')

    # Część 2: Wizualizacja
    create_tram_map('krakow_tram_data.json', 'mapa_tramwaje.html')

    print(f"\nPomyślnie wygenerowano mapę: mapa_tramwaje.html")
```

## Przykładowe wyjście programu

```
linia 10: 36
linia 50: 36
linia 52: 34
linia 4: 33
linia 18: 32
linia 22: 31
linia 1: 28
linia 9: 28
linia 24: 28
linia 8: 26
linia 14: 26
linia 3: 24
linia 13: 24
linia 5: 23
linia 20: 20
linia 21: 20
linia 11: 18

Liczba unikalnych przystanków: 142

Pomyślnie wygenerowano mapę: mapa_tramwaje.html
```

## Wskazówki

### Konwersja numeru linii na int

```python
line_number = int(line_obj['linia'])
```

### Wyodrębnienie unikalnych przystanków

```python
# Użyj set() do znalezienia unikalnych nazw
all_stops = set()
for line in lines:
    for stop in line['przystanki']:
        all_stops.add(stop['nazwa'])

unique_count = len(all_stops)
```

### Sortowanie słownika po wartościach

```python
sorted_items = sorted(stats.items(), key=lambda x: -x[1])  # malejąco
```

### Paleta kolorów dla linii

```python
kolory = [
    "#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00",
    "#a65628", "#f781bf", "#999999", "#66c2a5", "#fc8d62",
    "#8da0cb", "#e78ac3", "#a6d854", "#ffd92f", "#e5c494",
    "#b3b3b3"
]

# Użyj modulo do cyklicznego wyboru koloru
color = kolory[i % len(kolory)]
```

### Budowanie tooltipa dla przystanku

```python
# Zbierz wszystkie linie przechodzące przez dany przystanek
stop_to_lines = {}
for line_obj in data['linie']:
    line_num = line_obj['linia']
    for stop in line_obj['przystanki']:
        stop_name = stop['nazwa']
        stop_to_lines.setdefault(stop_name, []).append(line_num)

# Posortuj numery linii
lines_list = sorted(stop_to_lines[stop_name],
                   key=lambda x: int(x) if x.isdigit() else x)
tooltip = f"{stop_name} – linie: {', '.join(lines_list)}"
```

## Punktacja

- **Część 1** (przetwarzanie danych): 0.75 pkt
  - Poprawne wczytanie i przetworzenie danych
  - Zapisanie do pliku wyjściowego
  - Wypisanie statystyk
  - Zwrócenie poprawnych wartości

- **Część 2** (wizualizacja): 0.75 pkt
  - Stworzenie mapy z folium
  - Narysowanie tras tramwajowych
  - Oznaczenie przystanków z tooltipami
  - Zapisanie mapy HTML

**Razem: 1.5 pkt**

## Termin oddania

Uzupełniony plik `zadanie2.py` należy umieścić w repozytorium GitHub Classroom.

---

**Powodzenia!**
