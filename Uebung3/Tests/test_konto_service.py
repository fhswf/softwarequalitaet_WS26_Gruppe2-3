# BNFT, TMMH

"""
Test-Template für die KontoService-Klasse (Test-After Approach)
===============================================================

TODO: Team B - Implementieren Sie hier Ihre Tests NACH der KontoService-Implementierung!

Arbeitsablauf:
1. Implementieren Sie zuerst die KontoService-Klasse in Code/konto_service.py
2. Schreiben Sie dann hier umfassende Tests für Ihren Service
3. Testen Sie alle Service-Methoden gründlich
4. Dokumentieren Sie Ihre Autorschaft in den Tests

Tipps für Service-Tests:
- Nutzen Sie pytest fixtures für Setup/Teardown
- Testen Sie Integration zwischen Service und Konto-Klasse
- Testen Sie sowohl normale als auch Grenzfälle
- Testen Sie Validierungslogik im Service
"""

import pytest
from decimal import Decimal

# TODO: Team B - Entkommentieren Sie nach Ihrer Implementierung:
from ..Code.konto_service import KontoService
from ..Code.konto import Konto


@pytest.fixture
def service():
    return KontoService()


@pytest.fixture
def service_mit_konten(service):
    a = service.konto_erstellen(Decimal("100.00"))
    b = service.konto_erstellen(Decimal("50.00"))
    return service, a, b


# -------- Helper function
def saldo_von(service, konto_id):
    """Hilfsfunktion: Saldo eines Kontos über den Service lesen."""
    return next(k["saldo"] for k in service.konten_auflisten() if k["konto_id"] == konto_id)


class TestKontoServiceErstellung:
    """
    Tests für KontoService-Erstellung und Setup
    TODO: Team B - Testet Service-Initialisierung
    """

    def test_placeholder_service_erstellung(self):
        def test_service_startet_leer(self):
            # Arrange / Act
            service = KontoService()
            # Assert
            assert service.konten_auflisten() == []
            assert service.get_max_konto_id() == 0


class TestKontoVerwaltung:
    """
    Tests für Konto-Erstellung und -Verwaltung
    TODO: Team B - Testet alle Konto-Verwaltungs-Funktionen
    """

    def test_erstes_konto_bekommt_id_1(self, service):
        # Act
        konto_id = service.konto_erstellen(Decimal("10.00"))
        # Assert
        assert konto_id == 1

    def test_zweites_konto_bekommt_id_2(self, service):
        # Arrange
        service.konto_erstellen()
        # Act
        konto_id = service.konto_erstellen()
        # Assert
        assert konto_id == 2

    def test_konto_erstellen_negativer_saldo(self, service):
        # Act / Assert
        with pytest.raises(ValueError):
            service.konto_erstellen(Decimal("-1.00"))
        assert service.konten_auflisten() == []

    def test_konto_erstellen_falscher_typ(self, service):
        # Act / Assert
        with pytest.raises(ValueError):
            service.konto_erstellen(10)

    def test_konten_auflisten_anzahl(self, service):
        # Arrange
        service.konto_erstellen()
        service.konto_erstellen()
        # Act
        konten = service.konten_auflisten()
        # Assert
        assert len(konten) == 2

    def test_konten_auflisten_enthaelt_id_und_saldo(self, service):
        # Arrange
        service.konto_erstellen(Decimal("10.00"))
        # Act
        eintrag = service.konten_auflisten()[0]
        # Assert
        assert set(eintrag.keys()) == {"konto_id", "saldo"}

    def test_konto_erstellen_mit_saldo(self, service):
        konto_id = service.konto_erstellen(Decimal("10.00"))
        assert saldo_von(service, konto_id) == Decimal("10.00")

    def test_konto_erstellen_default_saldo(self, service):
        konto_id = service.konto_erstellen()
        assert saldo_von(service, konto_id) == Decimal("0.00")

    def test_konto_ids_fortlaufend_und_eindeutig(self, service):
        ids = [service.konto_erstellen() for _ in range(3)]
        assert ids == [1, 2, 3]

    def test_konten_auflisten_inhalt(self, service_mit_konten):
        service, a, b = service_mit_konten
        assert service.konten_auflisten() == [
            {"konto_id": a, "saldo": Decimal("100.00")},
            {"konto_id": b, "saldo": Decimal("50.00")},
        ]


class TestTransaktionen:
    @pytest.mark.parametrize("betrag", [Decimal("0"), Decimal("-5.00")])
    def test_ueberweisen_ungueltiger_betrag(self, service_mit_konten, betrag):
        # Arrange
        service, a, b = service_mit_konten
        # Act / Assert
        with pytest.raises(ValueError):
            service.ueberweisen(a, b, betrag)

    def test_ueberweisen_falscher_typ(self, service_mit_konten):
        service, a, b = service_mit_konten
        with pytest.raises(ValueError):
            service.ueberweisen(a, b, 10)

    def test_ueberweisen_unbekanntes_quellkonto(self, service_mit_konten):
        service, _, b = service_mit_konten
        with pytest.raises(ValueError):
            service.ueberweisen(99, b, Decimal("1.00"))

    def test_ueberweisen_gleiches_konto(self, service_mit_konten):
        service, a, _ = service_mit_konten
        with pytest.raises(ValueError):
            service.ueberweisen(a, a, Decimal("1.00"))

    def test_einziehen_ungueltiger_betrag(self, service_mit_konten):
        service, a, b = service_mit_konten
        with pytest.raises(ValueError):
            service.einziehen(b, a, Decimal("0"))

    def test_ueberweisen_erfolgreich(self, service_mit_konten):
        service, a, b = service_mit_konten
        service.ueberweisen(a, b, Decimal("30.00"))
        assert saldo_von(service, a) == Decimal("70.00")
        assert saldo_von(service, b) == Decimal("80.00")

    def test_ueberweisen_ganzer_saldo(self, service_mit_konten):
        service, a, b = service_mit_konten
        service.ueberweisen(a, b, Decimal("100.00"))
        assert saldo_von(service, a) == Decimal("0.00")

    def test_ueberweisen_ueberziehung(self, service_mit_konten):
        service, a, b = service_mit_konten
        with pytest.raises(RuntimeError):
            service.ueberweisen(a, b, Decimal("100.01"))
        assert saldo_von(service, a) == Decimal("100.00")
        assert saldo_von(service, b) == Decimal("50.00")

    def test_ueberweisen_unbekanntes_zielkonto(self, service_mit_konten):
        service, a, _ = service_mit_konten
        with pytest.raises(ValueError):
            service.ueberweisen(a, 99, Decimal("1.00"))
        assert saldo_von(service, a) == Decimal("100.00")

    def test_einziehen_erfolgreich(self, service_mit_konten):
        service, a, b = service_mit_konten
        service.einziehen(b, a, Decimal("20.00"))  # a zieht von b ein
        assert saldo_von(service, a) == Decimal("120.00")
        assert saldo_von(service, b) == Decimal("30.00")

    def test_einziehen_ueberziehung(self, service_mit_konten):
        service, a, b = service_mit_konten
        with pytest.raises(RuntimeError):
            service.einziehen(b, a, Decimal("50.01"))


class TestSaldoFunktionen:
    def test_gesamtsaldo_ein_konto(self, service):
        service.konto_erstellen(Decimal("42.50"))
        assert service.gesamtsaldo_berechnen() == Decimal("42.50")

    def test_gesamtsaldo_mehrere_konten(self, service_mit_konten):
        service, _, _ = service_mit_konten
        assert service.gesamtsaldo_berechnen() == Decimal("150.00")

    def test_gesamtsaldo_nach_ueberweisung_unveraendert(self, service_mit_konten):
        service, a, b = service_mit_konten
        service.ueberweisen(a, b, Decimal("40.00"))
        assert service.gesamtsaldo_berechnen() == Decimal("150.00")


class TestUtilityFunktionen:
    """
    Tests für Hilfsfunktionen
    TODO: Team B - Testet ID-Verwaltung und Export-Funktionen
    """

    def test_max_id_leer(self, service):
        # Act / Assert
        assert service.get_max_konto_id() == 0

    def test_max_id_nach_erstellung(self, service):
        # Arrange
        service.konto_erstellen()
        # Act / Assert
        assert service.get_max_konto_id() == 1

    def test_max_id_nach_mehreren_konten(self, service):
        service.konto_erstellen()
        service.konto_erstellen()
        assert service.get_max_konto_id() == 2


class TestKontoServiceIntegration:
    def test_vollstaendiger_workflow(self, service):
        # Arrange
        a = service.konto_erstellen(Decimal("100.00"))
        b = service.konto_erstellen()
        c = service.konto_erstellen(Decimal("25.00"))
        # Act
        service.ueberweisen(a, b, Decimal("60.00"))
        service.einziehen(c, b, Decimal("10.00"))
        # Assert
        assert saldo_von(service, a) == Decimal("40.00")
        assert saldo_von(service, b) == Decimal("70.00")
        assert saldo_von(service, c) == Decimal("15.00")
        assert service.gesamtsaldo_berechnen() == Decimal("125.00")

    def test_service_erzeugt_echte_konten(self, service):
        # Arrange
        service.konto_erstellen(Decimal("10.00"))
        # Act
        konto = service._konten[0]
        # Assert
        assert isinstance(konto, Konto)
