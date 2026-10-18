# Implementiert von: [JSOS], [TNKR]

"""Tests für die Konto-Klasse."""

import pytest
from decimal import Decimal

from Uebung3.Code.konto import Konto


class TestKontoErstellung:
    def test_konto_wird_mit_id_und_saldo_erstellt(self):
        konto = Konto(1, Decimal("100.00"))

        assert konto.konto_id == 1
        assert konto.saldo == Decimal("100.00")

    def test_konto_hat_standardmaessig_einen_saldo_von_null(self):
        konto = Konto(2)

        assert konto.saldo == Decimal("0.00")

    @pytest.mark.parametrize("ungueltige_id", [0, -1, "1", None, True])
    def test_ungueltige_id_wirft_value_error(self, ungueltige_id):
        with pytest.raises(ValueError):
            Konto(ungueltige_id)

    @pytest.mark.parametrize("ungueltiger_saldo", [Decimal("-0.01"), "100.00", None])
    def test_ungueltiger_saldo_wirft_value_error(self, ungueltiger_saldo):
        with pytest.raises(ValueError):
            Konto(1, ungueltiger_saldo)


class TestKontoEigenschaften:
    def test_properties_sind_nur_lesbar(self):
        konto = Konto(1, Decimal("10.00"))

        with pytest.raises(AttributeError):
            konto.konto_id = 2
        with pytest.raises(AttributeError):
            konto.saldo = Decimal("20.00")


class TestEinzahlung:
    def test_einzahlung_erhoeht_den_saldo(self):
        konto = Konto(1, Decimal("100.00"))

        konto.einzahlen(Decimal("25.50"))

        assert konto.saldo == Decimal("125.50")

    @pytest.mark.parametrize("ungueltiger_betrag", [Decimal("0"), Decimal("-1.00"), "10.00", None])
    def test_ungueltige_einzahlung_wirft_value_error(self, ungueltiger_betrag):
        konto = Konto(1, Decimal("100.00"))

        with pytest.raises(ValueError):
            konto.einzahlen(ungueltiger_betrag)

        assert konto.saldo == Decimal("100.00")


class TestAuszahlung:
    def test_auszahlung_reduziert_den_saldo(self):
        konto = Konto(1, Decimal("100.00"))

        konto.auszahlen(Decimal("25.50"))

        assert konto.saldo == Decimal("74.50")

    def test_auszahlung_des_gesamten_saldos_ist_erlaubt(self):
        konto = Konto(1, Decimal("100.00"))

        konto.auszahlen(Decimal("100.00"))

        assert konto.saldo == Decimal("0.00")

    def test_ueberziehung_wirft_runtime_error_und_aendert_saldo_nicht(self):
        konto = Konto(1, Decimal("100.00"))

        with pytest.raises(RuntimeError):
            konto.auszahlen(Decimal("100.01"))

        assert konto.saldo == Decimal("100.00")

    @pytest.mark.parametrize("ungueltiger_betrag", [Decimal("0"), Decimal("-1.00"), "10.00", None])
    def test_ungueltige_auszahlung_wirft_value_error(self, ungueltiger_betrag):
        konto = Konto(1, Decimal("100.00"))

        with pytest.raises(ValueError):
            konto.auszahlen(ungueltiger_betrag)

        assert konto.saldo == Decimal("100.00")


class TestKontoGrenzfaelle:
    def test_kleinster_gueltiger_betrag_wird_korrekt_verarbeitet(self):
        konto = Konto(1)

        konto.einzahlen(Decimal("0.01"))

        assert konto.saldo == Decimal("0.01")

    def test_decimal_praezision_bleibt_erhalten(self):
        konto = Konto(1, Decimal("0.10"))

        konto.einzahlen(Decimal("0.20"))
        konto.auszahlen(Decimal("0.10"))

        assert konto.saldo == Decimal("0.20")