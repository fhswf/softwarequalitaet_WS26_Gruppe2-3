# Implementiert von: [JSOS], [TNKR]

"""
Hier sollen Sie Ihre Implementierung der Konto-Klasse erstellen.

TODO: Implementieren Sie die Konto-Klasse basierend auf dem KontoInterface
"""

from decimal import Decimal
from .interfaces import KontoInterface

class Konto(KontoInterface):
    """
    TODO: Implementieren Sie diese Klasse
    
    Regeln:
    - ID wird bei Erstellung mitgegeben (numerisch, darf nicht leer sein)
    - Konto darf nicht überzogen werden (Saldo < 0)
    - Fehler bei inkorrekter Nutzung werfen
    """
    
    def __init__(self, konto_id: int, saldo: Decimal = Decimal('0.00')):
        if isinstance(konto_id, bool) or not isinstance(konto_id, int) or konto_id <= 0:
            raise ValueError("konto_id muss eine positive Ganzzahl sein")
        if not isinstance(saldo, Decimal) or saldo < 0:
            raise ValueError("saldo muss ein nichtnegativer Decimal-Wert sein")

        self._konto_id = konto_id
        self._saldo = saldo
    
    @property
    def konto_id(self) -> int:
        return self._konto_id
    
    @property
    def saldo(self) -> Decimal:
        return self._saldo
    
    def einzahlen(self, betrag: Decimal) -> None:
        self._validiere_betrag(betrag)
        self._saldo += betrag
    
    def auszahlen(self, betrag: Decimal) -> None:
        self._validiere_betrag(betrag)
        if self._saldo - betrag < 0:
            raise RuntimeError("Das Konto darf nicht überzogen werden")
        self._saldo -= betrag

    @staticmethod
    def _validiere_betrag(betrag: Decimal) -> None:
        if not isinstance(betrag, Decimal) or betrag <= 0:
            raise ValueError("betrag muss ein positiver Decimal-Wert sein")
