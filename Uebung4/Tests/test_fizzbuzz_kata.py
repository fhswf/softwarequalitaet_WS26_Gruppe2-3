"""
TDD-Template für FizzBuzz Kata
==============================

TODO: Team A - Entwickelt FizzBuzz mit TDD!

FizzBuzz-Regeln:
- Zahl durch 3 teilbar → "Fizz"  
- Zahl durch 5 teilbar → "Buzz"
- Zahl durch 3 UND 5 teilbar → "FizzBuzz"
- Sonst → Zahl als String

TDD-Prozess: RED → GREEN → REFACTOR → wiederholen!

Autorschaft dokumentieren: Wer hat welchen TDD-Schritt gemacht?
"""

import pytest

# TODO: Team A - Import nach erster Implementierung:
from ..Code.fizzbuzz_kata import fizzbuzz


class TestFizzBuzzTDD:
    """
    TODO: Team A - Entwickelt FizzBuzz mit TDD!

    Tipps:
    - Startet mit dem einfachsten Test
    - Schreibt minimalen Code zum Bestehen
    - Refaktoriert wenn nötig
    - Ein Test nach dem anderen!
    """

    def test_placeholder_start_here(self):
        # TDD-Autor: Torben Krüger 31.10.2026 13:10 Uhr

        assert fizzbuzz(1) == "1"
        assert fizzbuzz(3) == "Fizz"
        assert fizzbuzz(5) == "Buzz"
        assert fizzbuzz(15) == "FizzBuzz"
        

class TestFizzBuzzErweitert:
    # TDD-Autor: Torben Krüger 31.10.2026 13:15 Uhr
    @pytest.mark.parametrize(
        ("number", "expected"),
        [
            (1, "1"),
            (2, "2"),
            (3, "Fizz"),
            (6, "Fizz"),
            (9, "Fizz"),
            (5, "Buzz"),
            (10, "Buzz"),
            (20, "Buzz"),
            (15, "FizzBuzz"),
            (30, "FizzBuzz"),
            (45, "FizzBuzz"),
        ],
    )
    def test_multiple_numbers(self, number, expected):
        assert fizzbuzz(number) == expected

    @pytest.mark.parametrize(
        ("number", "expected"),
        [
            (0, "FizzBuzz"),
            (-3, "Fizz"),
            (-5, "Buzz"),
            (-15, "FizzBuzz"),
        ],
    )
    def test_edge_cases(self, number, expected):
        assert fizzbuzz(number) == expected

    def test_large_number(self):
        assert fizzbuzz(1_000_000_005) == "FizzBuzz"

    def test_string_input_raises_type_error(self):
        with pytest.raises(TypeError):
            fizzbuzz("3")

"""
TDD-Fortschritt dokumentieren:

Test 1: Fizzbuzz Happy path - Autor: Torben Krüger - 31.10.2026 13:10 Uhr Zeit: 5 Minuten
Implementation 1: [Minimale Lösung] - Zeit: 3 Min
1. Zahl 1 übergeben -> erawrtete Ausgabe "1", weil die Zahl nicht durch 3 oder 5 teilbar ist
2. Zahl 3 übergebne -> erwartete Ausgabe "Fizz", weil 3 durch 3 teilbar ist
3. Zahl 5 übergeben -> erwartete Ausgabe "Buzz", weil 5 durch 5 teilbar ist
4. Zahl 15 übergeben -> erwartete Ausgabe "FizzBuzz", weil 15 durch 3 und 5 teilbar ist

Test 2: Edgecase - Autor: Jonas Oberste-Berghaus - 31.10.2026 13:15 Uhr Zeit: 5 Minuten  
- Normale Zahlen (1, 2): Ausgabe ist die Zahl als String ("1", "2").
- Vielfache von 3 (3, 6, 9): Ausgabe ist "Fizz".
- Vielfache von 5 (5, 10, 20): Ausgabe ist "Buzz".
- Vielfache von 3 und 5 (15, 30, 45): Ausgabe ist "FizzBuzz".
- Randfälle (0, -3, -5, -15): Ausgabe ist "FizzBuzz", "Fizz", "Buzz", "FizzBuzz".
- Große Zahl (1_000_000_005): Ausgabe ist "FizzBuzz".
- Zahl als string ("3"): TypeError 

Refactoring: [Was geändert] - Zeit: [Zeit]

[Weiter dokumentieren...]

Erkenntnisse:
- Was war überraschend?
- Wo musstet ihr refaktorieren?
- Welche Tests brachten neue Herausforderungen?
"""
