"""
Testy dla zadania 2: Analiza i wizualizacja sieci tramwajowej w Krakowie
"""

import pytest
import sys
import os
from io import StringIO

# Dodaj katalog nadrzędny do ścieżki, aby zaimportować zadanie2_rozwiazanie
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from zadanie2_rozwiazanie import process_tram_data


class TestProcessTramData:
    """Testy dla funkcji process_tram_data()"""

    def test_return_type(self):
        """Test czy funkcja zwraca krotkę z dwoma elementami"""
        result = process_tram_data('linie_tramwajowe.json')
        assert isinstance(result, tuple), "Funkcja powinna zwracać krotkę"
        assert len(result) == 2, "Funkcja powinna zwracać krotkę z 2 elementami"

    def test_statistics_dict_type(self):
        """Test czy pierwszy element to słownik"""
        stats, _ = process_tram_data('linie_tramwajowe.json')
        assert isinstance(stats, dict), "Pierwszy element powinien być słownikiem"

    def test_unique_stops_type(self):
        """Test czy drugi element to liczba całkowita"""
        _, unique_stops = process_tram_data('linie_tramwajowe.json')
        assert isinstance(unique_stops, int), "Drugi element powinien być liczbą całkowitą"

    def test_unique_stops_count(self):
        """Test czy liczba unikalnych przystanków jest poprawna"""
        _, unique_stops = process_tram_data('linie_tramwajowe.json')
        assert unique_stops == 154, f"Oczekiwano 154 unikalnych przystanków, otrzymano {unique_stops}"

    def test_number_of_lines(self):
        """Test czy słownik zawiera 17 linii tramwajowych"""
        stats, _ = process_tram_data('linie_tramwajowe.json')
        assert len(stats) == 17, f"Oczekiwano 17 linii, otrzymano {len(stats)}"

    def test_line_numbers_are_int(self):
        """Test czy numery linii są typu int"""
        stats, _ = process_tram_data('linie_tramwajowe.json')
        for line_num in stats.keys():
            assert isinstance(line_num, int), f"Numer linii {line_num} powinien być typu int"

    def test_stop_counts_are_int(self):
        """Test czy liczby przystanków są typu int"""
        stats, _ = process_tram_data('linie_tramwajowe.json')
        for stop_count in stats.values():
            assert isinstance(stop_count, int), f"Liczba przystanków {stop_count} powinna być typu int"

    def test_stop_counts_positive(self):
        """Test czy liczby przystanków są dodatnie"""
        stats, _ = process_tram_data('linie_tramwajowe.json')
        for line_num, stop_count in stats.items():
            assert stop_count > 0, f"Linia {line_num} powinna mieć więcej niż 0 przystanków"

    def test_specific_line_counts(self):
        """Test czy konkretne linie mają poprawną liczbę przystanków"""
        stats, _ = process_tram_data('linie_tramwajowe.json')

        expected_counts = {
            1: 28,
            3: 24,
            4: 33,
            5: 23,
            8: 26,
            9: 28,
            10: 36,
            11: 18,
            13: 24,
            14: 26,
            18: 32,
            20: 20,
            21: 20,
            22: 31,
            24: 28,
            50: 36,
            52: 34
        }

        for line_num, expected_count in expected_counts.items():
            assert line_num in stats, f"Linia {line_num} powinna być w statystykach"
            assert stats[line_num] == expected_count, \
                f"Linia {line_num}: oczekiwano {expected_count} przystanków, otrzymano {stats[line_num]}"

    def test_longest_lines(self):
        """Test czy najdłuższe linie to 10 i 50 (po 36 przystanków)"""
        stats, _ = process_tram_data('linie_tramwajowe.json')
        max_stops = max(stats.values())
        assert max_stops == 36, f"Maksymalna liczba przystanków powinna wynosić 36, otrzymano {max_stops}"

        longest_lines = [line for line, count in stats.items() if count == max_stops]
        assert set(longest_lines) == {10, 50}, \
            f"Najdłuższe linie powinny być 10 i 50, otrzymano {longest_lines}"

    def test_shortest_line(self):
        """Test czy najkrótsza linia to 11 (18 przystanków)"""
        stats, _ = process_tram_data('linie_tramwajowe.json')
        min_stops = min(stats.values())
        assert min_stops == 18, f"Minimalna liczba przystanków powinna wynosić 18, otrzymano {min_stops}"

        shortest_lines = [line for line, count in stats.items() if count == min_stops]
        assert shortest_lines == [11], f"Najkrótsza linia powinna być 11, otrzymano {shortest_lines}"

    def test_prints_output(self, capsys):
        """Test czy funkcja wypisuje coś na ekran"""
        process_tram_data('linie_tramwajowe.json')
        captured = capsys.readouterr()
        assert len(captured.out) > 0, "Funkcja powinna wypisywać wyniki na ekran"

    def test_prints_all_lines(self, capsys):
        """Test czy funkcja wypisuje informacje o wszystkich 17 liniach"""
        process_tram_data('linie_tramwajowe.json')
        captured = capsys.readouterr()

        # Sprawdź czy każda linia jest wypisana
        for line_num in [1, 3, 4, 5, 8, 9, 10, 11, 13, 14, 18, 20, 21, 22, 24, 50, 52]:
            assert f"linia {line_num}:" in captured.out, \
                f"Wydruk powinien zawierać informację o linii {line_num}"

    def test_output_format(self, capsys):
        """Test czy format wydruku jest poprawny (linia X: Y)"""
        process_tram_data('linie_tramwajowe.json')
        captured = capsys.readouterr()

        # Sprawdź czy format jest poprawny dla kilku linii
        assert "linia 1: 28" in captured.out
        assert "linia 10: 36" in captured.out
        assert "linia 11: 18" in captured.out

    def test_output_sorted_descending(self, capsys):
        """Test czy linie są posortowane malejąco po liczbie przystanków"""
        process_tram_data('linie_tramwajowe.json')
        captured = capsys.readouterr()

        lines = captured.out.strip().split('\n')
        # Filtruj tylko linie zaczynające się od "linia"
        tram_lines = [line for line in lines if line.startswith('linia')]

        # Wyciągnij liczby przystanków
        stop_counts = []
        for line in tram_lines:
            # Format: "linia X: Y"
            parts = line.split(': ')
            if len(parts) == 2:
                stop_counts.append(int(parts[1]))

        # Sprawdź czy lista jest posortowana malejąco
        assert stop_counts == sorted(stop_counts, reverse=True), \
            "Linie powinny być posortowane malejąco po liczbie przystanków"

    def test_unique_stops_positive(self):
        """Test czy liczba unikalnych przystanków jest dodatnia"""
        _, unique_stops = process_tram_data('linie_tramwajowe.json')
        assert unique_stops > 0, "Liczba unikalnych przystanków powinna być większa od 0"

    def test_unique_stops_reasonable(self):
        """Test czy liczba unikalnych przystanków jest sensowna"""
        stats, unique_stops = process_tram_data('linie_tramwajowe.json')

        # Minimalna możliwa liczba unikalnych przystanków to długość najdłuższej linii
        max_line_length = max(stats.values())
        assert unique_stops >= max_line_length, \
            f"Liczba unikalnych przystanków ({unique_stops}) powinna być >= {max_line_length}"

        # Maksymalna możliwa liczba to suma wszystkich przystanków (gdyby nie było wspólnych)
        total_stops = sum(stats.values())
        assert unique_stops <= total_stops, \
            f"Liczba unikalnych przystanków ({unique_stops}) nie może przekraczać {total_stops}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
