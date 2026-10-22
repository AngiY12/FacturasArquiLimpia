from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class ControlFraude:
    """Política de dominio que marca montos que requieren revisión."""

    limite_alerta: Decimal = Decimal("10000")

    def __post_init__(self) -> None:
        limite = Decimal(str(self.limite_alerta))
        if not limite.is_finite() or limite < 0:
            raise ValueError("El límite de alerta debe ser no negativo y finito.")
        object.__setattr__(self, "limite_alerta", limite)

    def es_sospechosa(self, monto_base: Decimal) -> bool:
        return Decimal(str(monto_base)) > self.limite_alerta

    # Se conserva este nombre para código que use la versión anterior del dominio.
    def evaluar(self, monto_base: Decimal) -> bool:
        return self.es_sospechosa(monto_base)
