import os
from aplicacion.casos_uso import CrearFacturaUseCase
from infraestructura.repositorios import PostgresFacturaRepository, OracleFacturaRepository
from presentacion.broker_amqp import BrokerConsumer

def configurar_sistema():
    # El intercambio entre proveedores se resuelve por configuración[cite: 2]
    proveedor_bd = os.getenv("PROVEEDOR_BD", "Postgres")

    if proveedor_bd == "Oracle":
        repositorio = OracleFacturaRepository()
    else:
        repositorio = PostgresFacturaRepository()

    # Inyección de dependencias
    caso_uso = CrearFacturaUseCase(repositorio)
    
    # Iniciar el consumidor pasándole el caso de uso
    consumidor = BrokerConsumer(caso_uso)
    consumidor.iniciar()

if __name__ == "__main__":
    configurar_sistema()