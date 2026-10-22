import os

from aplicacion.casos_uso import CrearFacturaUseCase
from infraestructura.repositorios import OracleFacturaRepository, PostgresFacturaRepository
from presentacion.api_rest import crear_app


def crear_repositorio():
    proveedor = os.getenv("PROVEEDOR_BD", "Postgres").strip().lower()
    if proveedor == "oracle":
        return OracleFacturaRepository()
    return PostgresFacturaRepository()


# Composition Root: la API y RabbitMQ comparten el mismo caso de uso.
repositorio = crear_repositorio()
caso_uso = CrearFacturaUseCase(repositorio)
app = crear_app(caso_uso)


if __name__ == "__main__":
    from presentacion.broker_amqp import BrokerConsumer

    BrokerConsumer(caso_uso).iniciar()
