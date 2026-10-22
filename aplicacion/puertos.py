from abc import ABC, abstractmethod
from dataclasses import dataclass
from dominio.factura import Factura

# Objeto de transferencia de datos puro (DTO) para desacoplar la entrada
@dataclass
class CrearFacturaDTO:
    id_factura: str
    cliente: str
    monto_base: float

# Contrato de entrada (Puerto primario)
class ICrearFacturaUseCase(ABC):
    """
    Este es el contrato que ambos adaptadores (API REST y RabbitMQ)
    van a invocar de forma simétrica[cite: 1].
    """
    @abstractmethod
    def ejecutar(self, dto: CrearFacturaDTO) -> None:
        pass

# Contrato de salida (Puerto secundario)
class IFacturaRepository(ABC):
    """
    El dominio define el contrato de persistencia que necesita,
    las implementaciones concretas de PostgreSQL u Oracle deberán cumplirlo[cite: 2].
    """
    @abstractmethod
    def guardar(self, factura: Factura) -> None:
        pass