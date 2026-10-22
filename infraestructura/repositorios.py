from aplicacion.puertos import IFacturaRepository
from dominio.factura import Factura

class PostgresFacturaRepository(IFacturaRepository):
    def __init__(self):
        self.db_en_memoria = []

    def guardar(self, factura: Factura) -> None:
        self.db_en_memoria.append(factura)
        print(f"[PostgreSQL Simulado] Factura {factura.id_factura} de {factura.cliente} guardada.")

class OracleFacturaRepository(IFacturaRepository):
    def __init__(self):
        self.db_en_memoria = []

    def guardar(self, factura: Factura) -> None:
        self.db_en_memoria.append(factura)
        print(f"[Oracle Simulado] Factura {factura.id_factura} de {factura.cliente} guardada.")