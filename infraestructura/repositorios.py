from aplicacion.puertos import IFacturaRepository
from dominio.factura import Factura


class PostgresFacturaRepository(IFacturaRepository):
    """Repositorio simulado de PostgreSQL con almacenamiento en memoria."""

    def __init__(self) -> None:
        self.db_en_memoria: list[Factura] = []

    def guardar(self, factura: Factura) -> None:
        self.db_en_memoria.append(factura)


class OracleFacturaRepository(IFacturaRepository):
    """Repositorio simulado de Oracle con almacenamiento en memoria."""

    def __init__(self) -> None:
        self.db_en_memoria: list[Factura] = []

    def guardar(self, factura: Factura) -> None:
        self.db_en_memoria.append(factura)
