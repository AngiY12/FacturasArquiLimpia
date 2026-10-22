from decimal import Decimal
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from aplicacion.puertos import CrearFacturaDTO, ICrearFacturaUseCase


class CrearFacturaRequest(BaseModel):
    cliente: str = Field(min_length=1, description="Nombre del cliente")
    monto_base: Decimal = Field(gt=0, description="Monto antes de impuestos")
    id_factura: str | None = Field(default=None, min_length=1)


class FacturaResponse(BaseModel):
    id_factura: str
    cliente: str
    monto_base: Decimal
    monto_total: Decimal
    alerta_fraude: bool


def crear_app(caso_uso: ICrearFacturaUseCase) -> FastAPI:
    """Construye el adaptador HTTP recibiendo el puerto de entrada."""
    app = FastAPI(title="API de Facturas", version="1.0.0")

    @app.post("/facturas", response_model=FacturaResponse, status_code=201)
    def crear_factura(solicitud: CrearFacturaRequest) -> FacturaResponse:
        try:
            factura = caso_uso.ejecutar(
                CrearFacturaDTO(
                    id_factura=solicitud.id_factura or str(uuid4()),
                    cliente=solicitud.cliente.strip(),
                    monto_base=solicitud.monto_base,
                )
            )
        except ValueError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

        return FacturaResponse(
            id_factura=factura.id_factura,
            cliente=factura.cliente,
            monto_base=factura.monto_base,
            monto_total=factura.monto_total,
            alerta_fraude=factura.alerta_fraude,
        )

    return app
