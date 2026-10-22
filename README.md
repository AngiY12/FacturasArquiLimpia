# Sistema de Facturación - Arquitectura Limpia
**Universidad de las Fuerzas Armadas - ESPE** | Trabajo Práctico 8vo Semestre de Ingeniería de Software

Evolución de un sistema monolítico hacia una Arquitectura Limpia. El sistema procesa facturas provenientes de dos fuentes distintas (API REST y broker asíncrono) reutilizando la misma lógica de negocio y permitiendo el intercambio de persistencia (PostgreSQL/Oracle) mediante configuración.

## Requisitos Previos
- Python 3.10+
- Docker (para el contenedor de RabbitMQ)
- Postman (para pruebas HTTP)

## Instalación
1. Clonar el repositorio:
   `git clone <URL_DEL_REPOSITORIO>`
2. Crear e iniciar el entorno virtual:
   `python -m venv venv`
   `source venv/bin/activate` (En Windows: `venv\Scripts\activate`)
3. Instalar dependencias:
   `pip install -r requirements.txt`

## Ejecución del Entorno Asíncrono (RabbitMQ)
Levantar el broker de mensajería en Docker:
`docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management`

## Uso y Configuración
El sistema utiliza repositorios simulados en memoria para aislar el dominio de la persistencia real.
Para cambiar entre PostgreSQL y Oracle, define la variable de entorno antes de ejecutar:


**En Windows (PowerShell):**
`$env:PROVEEDOR_BD="Postgres"`
`python main.py`

## Estructura del Proyecto
- `dominio/`: Núcleo puro (Entidad Factura, reglas de fraude y políticas fiscales).
- `aplicacion/`: Casos de uso y contratos (Interfaces abstractas).
- `infraestructura/`: Implementaciones concretas (Repositorios simulados en memoria).
- `presentacion/`: Adaptadores simétricos (API REST con FastAPI y Consumidor AMQP).