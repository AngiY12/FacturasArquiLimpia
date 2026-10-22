from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation

from dominio.control_fraude import ControlFraude


@dataclass(frozen=True)
class Factura:
    """Entidad de dominio: valida una factura y calcula sus importes fiscales."""

    id_factura: str
    cliente: str
    monto_base: Decimal
    tasa_iva: Decimal = Decimal("0.15")
    control_fraude: ControlFraude = field(default_factory=ControlFraude, repr=False)
    monto_total: Decimal = field(init=False)
    alerta_fraude: bool = field(init=False)

    def __post_init__(self) -> None:
        if not self.id_factura or not self.id_factura.strip():
            raise ValueError("El id de la factura es obligatorio.")
        if not self.cliente or not self.cliente.strip():
            raise ValueError("El cliente es obligatorio.")

        try:
            base = Decimal(str(self.monto_base))
            tasa = Decimal(str(self.tasa_iva))
        except (InvalidOperation, TypeError, ValueError) as exc:
            raise ValueError("El monto base y la tasa de IVA deben ser números válidos.") from exc

        if not base.is_finite() or base <= 0:
            raise ValueError("El monto base debe ser un número positivo y finito.")
        if not tasa.is_finite() or tasa < 0:
            raise ValueError("La tasa de IVA debe ser un número no negativo y finito.")

        object.__setattr__(self, "monto_base", base)
        object.__setattr__(self, "tasa_iva", tasa)
        object.__setattr__(self, "monto_total", base * (Decimal("1") + tasa))
        object.__setattr__(self, "alerta_fraude", self.control_fraude.es_sospechosa(base))
