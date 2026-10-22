from dominio.control_fraude import ControlFraude

class Factura:
    """
    Entidad central del sistema. 
    """
    def __init__(self, id_factura: str, cliente: str, monto_base: float):
        self.id_factura = id_factura
        self.cliente = cliente
        self.monto_base = monto_base
        self.monto_total = 0.0
        self.alerta_fraude = False
        
        # Ejecución inmediata de reglas de negocio críticas al instanciar[cite: 1]
        self._validar_fraude()
        self._aplicar_politicas_fiscales()

    def _validar_fraude(self) -> None:
        # Delega la responsabilidad de validación a la clase de dominio independiente[cite: 1]
        validador = ControlFraude()
        self.alerta_fraude = validador.evaluar(self.monto_base)

    def _aplicar_politicas_fiscales(self) -> None:
        # Políticas fiscales simuladas (ej. cálculo del 15% de IVA)[cite: 1]
        iva = self.monto_base * 0.15
        self.monto_total = self.monto_base + iva