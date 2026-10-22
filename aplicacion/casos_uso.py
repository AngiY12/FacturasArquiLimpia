from aplicacion.puertos import CrearFacturaDTO, ICrearFacturaUseCase, IFacturaRepository
from dominio.factura import Factura


class CrearFacturaUseCase(ICrearFacturaUseCase):
    """Coordina la creación de la factura y su guardado."""

    def __init__(self, repositorio: IFacturaRepository) -> None:
        self._repositorio = repositorio

    def ejecutar(self, dto: CrearFacturaDTO) -> Factura:
        factura = Factura(
            id_factura=dto.id_factura,
            cliente=dto.cliente,
            monto_base=dto.monto_base,
        )
        self._repositorio.guardar(factura)
        return factura
