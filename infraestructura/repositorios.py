from dominio.factura import Factura
from aplicacion.puertos import IFacturaRepository


class FacturaEnMemoriaRepository(IFacturaRepository):
    """Persistencia volátil para ejecutar y probar la API sin una base de datos."""

    def __init__(self) -> None:
        self._facturas: list[Factura] = []

    def guardar(self, factura: Factura) -> None:
        self._facturas.append(factura)

    def listar(self) -> list[Factura]:
        return list(self._facturas)
