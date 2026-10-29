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
# from ..Code.konto import Konto


@pytest.fixture
def service():
    return KontoService()


class TestKontoServiceErstellung:
    """
    Tests für KontoService-Erstellung und Setup
    TODO: Team B - Testet Service-Initialisierung
    """

    def test_placeholder_service_erstellung(self):
        """
        Placeholder-Test - ersetzen Sie diesen durch echte Tests!

        Beispiele für Tests:
        - Service ohne Parameter erstellen
        - Service mit initialen Konten erstellen
        - Service-Zustand nach Erstellung prüfen
        """
        # TODO: Team B - Ersetzen Sie diesen Placeholder durch echte Tests
        assert True, "Placeholder - bitte durch echte Tests ersetzen!"

        # Beispiel-Code (entkommentiert nach Implementierung):
        # service = KontoService()
        # assert len(service.konten_auflisten()) == 0


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


class TestTransaktionen:
    """
    Tests für Transaktions-Funktionen
    TODO: Team B - Testet alle Geldtransaktionen über den Service
    """

    def test_placeholder_einzahlen(self):
        """TODO: Team B - Tests für einzahlen()"""
        # Beispiel-Tests:
        # - Einzahlung auf existierendes Konto
        # - Saldo wird korrekt erhöht
        # - Einzahlung auf nicht-existierendes Konto → Exception?
        # - Ungültiger Betrag → Exception?
        assert True, "TODO: Tests für einzahlen implementieren"

    def test_placeholder_auszahlen(self):
        """TODO: Team B - Tests für auszahlen()"""
        # Beispiel-Tests:
        # - Auszahlung bei ausreichendem Saldo
        # - Saldo wird korrekt reduziert
        # - Auszahlung bei unzureichendem Saldo → Exception?
        # - Auszahlung von nicht-existierendem Konto → Exception?
        assert True, "TODO: Tests für auszahlen implementieren"

    def test_placeholder_ueberweisen(self):
        """TODO: Team B - Tests für ueberweisen()"""
        # Beispiel-Tests:
        # - Überweisung zwischen existierenden Konten
        # - Sender-Saldo wird reduziert
        # - Empfänger-Saldo wird erhöht
        # - Überweisung bei unzureichendem Saldo → Exception?
        # - Überweisung an nicht-existierendes Konto → Exception?
        # - Überweisung von nicht-existierendem Konto → Exception?
        assert True, "TODO: Tests für ueberweisen implementieren"


class TestSaldoFunktionen:
    """
    Tests für Saldo-bezogene Funktionen
    TODO: Team B - Testet Saldo-Abfragen und -Berechnungen
    """

    def test_gesamtsaldo_leer(self, service):
        # Act / Assert
        assert service.gesamtsaldo_berechnen() == Decimal("0.00")


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


class TestKontoServiceIntegration:
    """
    Integration-Tests zwischen Service und Konto-Klassen
    TODO: Team B - Testet das Zusammenspiel aller Komponenten
    """

    def test_placeholder_vollstaendiger_workflow(self):
        """TODO: Team B - Test für kompletten Workflow"""
        # Beispiel-Test:
        # 1. Service erstellen
        # 2. Mehrere Konten erstellen
        # 3. Einzahlungen durchführen
        # 4. Überweisungen durchführen
        # 5. Gesamtsaldo prüfen
        assert True, "TODO: Integration-Test implementieren"
