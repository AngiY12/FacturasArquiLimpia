from aplicacion.casos_uso import CrearFacturaUseCase
from infraestructura.repositorios import FacturaEnMemoriaRepository
from presentacion.api_rest import crear_app


# Composition Root: aquí se conectan los componentes concretos.
repositorio = FacturaEnMemoriaRepository()
caso_uso = CrearFacturaUseCase(repositorio)
app = crear_app(caso_uso)
