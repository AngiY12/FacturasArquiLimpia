class Factura:
    def __init__(self, id_factura: str, cliente: str, monto_base: float):
        self.id_factura = id_factura
        self.cliente = cliente
        self.monto_base = monto_base
        self.monto_total = 0.0
        self.alerta_fraude = False
        
        # Las reglas de negocio críticas se ejecutan al instanciar el objeto[cite: 1]
        self._validar_fraude()
        self._aplicar_politicas_fiscales()

    def _validar_fraude(self) -> None:
        """
        Control de fraude simulado: 
        Si el monto base supera los $10,000, se marca la factura como alerta.
        Esta regla reside exclusivamente en el núcleo del sistema[cite: 1].
        """
        if self.monto_base > 10000:
            self.alerta_fraude = True

    def _aplicar_politicas_fiscales(self) -> None:
        """
        Políticas fiscales simuladas:
        Se calcula un 15% de IVA sobre el monto base para obtener el total.
        Ni la base de datos ni la interfaz web conocen este cálculo[cite: 1].
        """
        iva = self.monto_base * 0.15
        self.monto_total = self.monto_base + iva