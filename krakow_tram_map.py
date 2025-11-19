import json
import folium

PLIK_DANE = "linie_tramwajowe.json"
PLIK_MAPA = "mapa_tramwaje.html"

def sortuj_linie_po_liczbie_przystankow(dane_linii):
    """Dla danych [{"linia": "1", "przystanki": [...]}, ...] zwróć posortowane [(linia, liczba)]."""
    liczby = [(linia_obj["linia"], len(linia_obj.get("przystanki", []))) for linia_obj in dane_linii]
    return sorted(liczby, key=lambda x: (-x[1], int(x[0]) if x[0].isdigit() else x[0]))

def generuj_tekst_linii(dane_linii) -> str:
    """Zwróć tekst do wypisania: linie posortowane po liczbie przystanków."""
    liczby_posortowane = sortuj_linie_po_liczbie_przystankow(dane_linii)
    return "\n".join(f"linia {nr}: {cnt}" for nr, cnt in liczby_posortowane)

def main():
    # Read data from single JSON file
    with open(PLIK_DANE, encoding="utf-8") as f:
        dane = json.load(f)

    linie_dane = dane["linie"]

    # Build stop dictionary: name -> (lat, lon)
    # Collect all unique stops from all lines
    przystanki = {}
    for linia_obj in linie_dane:
        for przystanek in linia_obj.get("przystanki", []):
            nazwa = przystanek["nazwa"]
            lat = przystanek["lat"]
            lon = przystanek["lon"]
            # Store coordinates (if duplicate names exist, last one wins)
            przystanki[nazwa] = (lat, lon)

    # Count stops per line and print
    print(generuj_tekst_linii(linie_dane))

    # Reverse index: stop -> list of lines
    przystanek_do_linii = {}
    for linia_obj in linie_dane:
        nr = linia_obj["linia"]
        for przystanek in linia_obj.get("przystanki", []):
            nazwa = przystanek["nazwa"]
            przystanek_do_linii.setdefault(nazwa, []).append(nr)

    uzyte_przystanki = set(przystanek_do_linii.keys())

    # Create map
    m = folium.Map(location=[50.0, 20.0], zoom_start=12, tiles="cartodbpositron")

    kolory = [
        "#e41a1c","#377eb8","#4daf4a","#984ea3","#ff7f00",
        "#a65628","#f781bf","#999999","#66c2a5","#fc8d62",
        "#8da0cb","#e78ac3","#a6d854","#ffd92f","#e5c494",
        "#b3b3b3"
    ]

    # Draw lines
    for i, linia_obj in enumerate(linie_dane):
        nr = linia_obj["linia"]
        przystanki_linii = linia_obj.get("przystanki", [])
        wspolrzedne = [(p["lat"], p["lon"]) for p in przystanki_linii]
        if len(wspolrzedne) >= 2:
            folium.PolyLine(
                wspolrzedne,
                color=kolory[i % len(kolory)],
                weight=3,
                opacity=0.9,
                tooltip=f"Linia {nr}"
            ).add_to(m)

    # Draw stop points with tooltips
    for nazwa in sorted(uzyte_przystanki):
        lat, lon = przystanki[nazwa]
        lista_linii = sorted(przystanek_do_linii[nazwa], key=lambda s: int(s) if s.isdigit() else s)
        folium.CircleMarker(
            (lat, lon),
            radius=3,
            color="#333",
            fill=True,
            fill_opacity=0.9,
            weight=1,
            tooltip=f"{nazwa} – linie: {', '.join(lista_linii)}"
        ).add_to(m)

    m.save(PLIK_MAPA)
    print("Mapa ->", PLIK_MAPA)

if __name__ == "__main__":
    main()
