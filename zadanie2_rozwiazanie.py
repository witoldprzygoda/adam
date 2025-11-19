"""
Zadanie 2: Analiza i wizualizacja sieci tramwajowej w Krakowie
PRZYKŁADOWE ROZWIĄZANIE (dla instruktora)
"""

import json
import folium


def process_tram_data(input_file, output_file):
    """
    Przetwarza dane tramwajowe i zapisuje uproszczony format.

    Args:
        input_file (str): ścieżka do pliku wejściowego JSON
        output_file (str): ścieżka do pliku wyjściowego JSON

    Returns:
        tuple: (słownik {linia: liczba_przystanków}, liczba_unikalnych_przystanków)
    """
    # Wczytaj dane z pliku
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Stwórz słownik w formacie {numer_linii: krotka_przystanków}
    trams_dict = {}

    # Przejdź przez wszystkie linie i przetworz dane
    for line_obj in data['linie']:
        # Zamień numer linii na int
        line_number = int(line_obj['linia'])

        # Wyciągnij nazwy przystanków do listy
        stops = [stop['nazwa'] for stop in line_obj['przystanki']]

        # Dodaj do słownika (konwertuj listę na krotkę)
        trams_dict[line_number] = tuple(stops)

    # Zapisz przetworzone dane do pliku
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(trams_dict, file, ensure_ascii=False, indent=2)

    # Stwórz słownik ze statystykami {linia: liczba_przystanków}
    stats = {line: len(stops) for line, stops in trams_dict.items()}

    # Wypisz statystyki posortowane malejąco po liczbie przystanków
    sorted_stats = sorted(stats.items(), key=lambda x: (-x[1], x[0]))
    for line_num, stop_count in sorted_stats:
        print(f"linia {line_num}: {stop_count}")

    # Znajdź wszystkie unikalne przystanki
    unique_stops = set()
    for stops_tuple in trams_dict.values():
        unique_stops.update(stops_tuple)

    return stats, len(unique_stops)


def create_tram_map(input_file, output_map_file):
    """
    Tworzy interaktywną mapę sieci tramwajowej.

    Args:
        input_file (str): ścieżka do pliku wejściowego JSON
        output_map_file (str): ścieżka do pliku wyjściowego HTML
    """
    # Wczytaj dane
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Stwórz mapę wycentrowaną na Krakowie
    m = folium.Map(
        location=[50.06, 19.95],
        zoom_start=12,
        tiles="cartodbpositron"
    )

    # Paleta kolorów dla różnych linii
    kolory = [
        "#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00",
        "#a65628", "#f781bf", "#999999", "#66c2a5", "#fc8d62",
        "#8da0cb", "#e78ac3", "#a6d854", "#ffd92f", "#e5c494",
        "#b3b3b3"
    ]

    # Narysuj linie tramwajowe
    for i, line_obj in enumerate(data['linie']):
        line_number = line_obj['linia']
        stops = line_obj['przystanki']

        # Przygotuj listę współrzędnych
        coordinates = [(stop['lat'], stop['lon']) for stop in stops]

        # Dodaj PolyLine do mapy
        if len(coordinates) >= 2:
            folium.PolyLine(
                coordinates,
                color=kolory[i % len(kolory)],
                weight=3,
                opacity=0.9,
                tooltip=f"Linia {line_number}"
            ).add_to(m)

    # Stwórz słownik przystanek -> (lat, lon, lista_linii)
    stop_info = {}

    for line_obj in data['linie']:
        line_number = line_obj['linia']
        for stop in line_obj['przystanki']:
            stop_name = stop['nazwa']
            if stop_name not in stop_info:
                stop_info[stop_name] = {
                    'lat': stop['lat'],
                    'lon': stop['lon'],
                    'lines': []
                }
            stop_info[stop_name]['lines'].append(line_number)

    # Dodaj markery dla przystanków
    for stop_name, info in sorted(stop_info.items()):
        # Posortuj numery linii
        lines_sorted = sorted(
            info['lines'],
            key=lambda x: int(x) if x.isdigit() else x
        )

        # Stwórz tooltip
        tooltip = f"{stop_name} – linie: {', '.join(lines_sorted)}"

        # Dodaj marker
        folium.CircleMarker(
            location=(info['lat'], info['lon']),
            radius=3,
            color="#333",
            fill=True,
            fill_color="#333",
            fill_opacity=0.9,
            weight=1,
            tooltip=tooltip
        ).add_to(m)

    # Zapisz mapę do pliku
    m.save(output_map_file)


def main():
    """
    Główna funkcja programu - uruchamia obie części zadania.
    """
    print("=" * 60)
    print("Zadanie 2: Analiza sieci tramwajowej w Krakowie")
    print("=" * 60)
    print()

    # Część 1: Przetwarzanie danych
    print("Część 1: Przetwarzanie danych")
    print("-" * 60)
    stats, unique_stops = process_tram_data(
        'krakow_tram_data.json',
        'tramwaje_out.json'
    )
    print(f"\nLiczba unikalnych przystanków: {unique_stops}")
    print()

    # Część 2: Wizualizacja
    print("Część 2: Tworzenie mapy")
    print("-" * 60)
    create_tram_map('krakow_tram_data.json', 'mapa_tramwaje.html')
    print(f"Pomyślnie wygenerowano mapę: mapa_tramwaje.html")
    print()

    print("=" * 60)
    print("Zadanie zakończone!")
    print("=" * 60)


if __name__ == "__main__":
    main()
