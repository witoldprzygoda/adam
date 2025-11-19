"""
Zadanie 2: Analiza i wizualizacja sieci tramwajowej w Krakowie
Autor: [Imię Nazwisko]
Data: [Data]
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

    Przykład:
        stats, unique = process_tram_data('krakow_tram_data.json', 'tramwaje_out.json')
        # stats = {1: 28, 3: 24, ...}
        # unique = 142
    """
    # TODO: Wczytaj dane z pliku input_file
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # TODO: Stwórz słownik w formacie {numer_linii: krotka_przystanków}
    trams_dict = {}

    # TODO: Przejdź przez wszystkie linie i przetworz dane
    for line_obj in data['linie']:
        line_number = None  # TODO: Zamień numer linii na int
        stops = []  # TODO: Wyciągnij nazwy przystanków do listy

        # TODO: Dodaj do słownika (pamiętaj o konwersji listy na krotkę)
        pass

    # TODO: Zapisz przetworzone dane do pliku output_file

    # TODO: Stwórz słownik ze statystykami {linia: liczba_przystanków}
    stats = {}

    # TODO: Wypisz statystyki posortowane malejąco po liczbie przystanków
    # Format: "linia X: Y"

    # TODO: Znajdź wszystkie unikalne przystanki (użyj set)
    unique_stops = set()

    # TODO: Wypisz liczbę unikalnych przystanków

    # Zwróć wyniki
    return stats, len(unique_stops)


def create_tram_map(input_file, output_map_file):
    """
    Tworzy interaktywną mapę sieci tramwajowej.

    Args:
        input_file (str): ścieżka do pliku wejściowego JSON
        output_map_file (str): ścieżka do pliku wyjściowego HTML

    Przykład:
        create_tram_map('krakow_tram_data.json', 'mapa_tramwaje.html')
    """
    # TODO: Wczytaj dane
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # TODO: Stwórz mapę wycentrowaną na Krakowie [50.0, 20.0], zoom=12
    m = None  # TODO

    # Paleta kolorów dla różnych linii
    kolory = [
        "#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00",
        "#a65628", "#f781bf", "#999999", "#66c2a5", "#fc8d62",
        "#8da0cb", "#e78ac3", "#a6d854", "#ffd92f", "#e5c494",
        "#b3b3b3"
    ]

    # TODO: Narysuj linie tramwajowe
    for i, line_obj in enumerate(data['linie']):
        line_number = line_obj['linia']
        stops = line_obj['przystanki']

        # TODO: Przygotuj listę współrzędnych [(lat, lon), ...]
        coordinates = []

        # TODO: Dodaj PolyLine do mapy z odpowiednim kolorem i tooltipem
        if len(coordinates) >= 2:
            pass  # TODO: folium.PolyLine(...)

    # TODO: Stwórz słownik przystanek -> lista linii
    stop_to_lines = {}

    # TODO: Dodaj markery dla przystanków
    # Dla każdego unikalnego przystanku:
    #   - Stwórz CircleMarker
    #   - Dodaj tooltip z nazwą i listą linii

    # TODO: Zapisz mapę do pliku
    # m.save(output_map_file)

    pass


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
