class ControlFraude:
    """
    Encapsula exclusivamente las reglas para detectar fraudes.
    Si la complejidad crece, se modifica aquí sin afectar a la entidad Factura.
    """
    def evaluar(self, monto_base: float) -> bool:
        # Lógica simulada: transacciones mayores a $10,000 son marcadas como sospechosas[cite: 1]
        return monto_base > 10000