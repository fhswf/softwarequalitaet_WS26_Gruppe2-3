"""
TDD-Template für Weather-API Service
====================================

TODO: Team A - Implementiert get_weather_category() testgetrieben!

Aufgabe:
- Funktion ruft Weather-API auf (mocken!)
- Extrahiert Temperatur aus JSON
- Gibt Kategorie zurück basierend auf Temperatur

Temperatur-Kategorien:
- < 0°C:      "frostgefahr"
- 0-10°C:     "kalt"
- 11-15°C:    "kühl"
- 16-24°C:    "angenehm"
- 25-30°C:    "warm"
- > 30°C:     "heiß"

TDD-Prozess: RED → GREEN → REFACTOR → wiederholen!

Dokumentiert eure Autorschaft: Wer hat welchen TDD-Schritt gemacht?
"""

import pytest
from unittest.mock import patch

from ..Code.weather_service import get_weather_category


class TestWeatherService:
    """
    Tests für Weather-API Service
    
    TDD-Vorgehen:
    1. Test schreiben (RED)
    2. Minimale Implementierung (GREEN)
    3. Refactoring
    """
    
    def test_angenehm(self):
        """TDD-Zyklus 1: RED von JSOS um 10:18 Uhr
        Temperatur 20 °C wird als angenehm eingestuft."""
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = {"temperature": 20}

            result = get_weather_category("Berlin")

            assert result == "angenehm"
            mock_get.assert_called_once_with(
                "https://api.weather.com/current?city=Berlin",
                timeout=5,
            )

    # TODO: Team A - Weitere Tests für alle Temperaturkategorien hinzufügen!


    @pytest.mark.parametrize(
        ("temperature", "expected_category"),
        [
            (-5, "frostgefahr"),
            (5, "kalt"),
            (13, "kühl"),
            (20, "angenehm"),
            (28, "warm"),
            (35, "heiß"),
        ],
    )
    def test_all_temperature_categories(self, temperature, expected_category):
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = {
                "temperature": temperature
            }

            result = get_weather_category("Berlin")

            assert result == expected_category
            mock_get.assert_called_once_with(
                "https://api.weather.com/current?city=Berlin",
                timeout=5,
            )
