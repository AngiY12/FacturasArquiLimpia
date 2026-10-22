import pika
import json
from aplicacion.puertos import ICrearFacturaUseCase, CrearFacturaDTO

class BrokerConsumer:
    def __init__(self, caso_uso: ICrearFacturaUseCase):
        self.caso_uso = caso_uso

    def iniciar(self):
        # Conexión local al contenedor de RabbitMQ
        conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        canal = conexion.channel()
        # Las colas compartidas deben ser durables en RabbitMQ moderno.
        canal.queue_declare(queue='facturas_queue', durable=True)

        def callback(ch, method, properties, body):
            datos = json.loads(body)
            dto = CrearFacturaDTO(
                id_factura=datos['id_factura'],
                cliente=datos['cliente'],
                monto_base=datos['monto_base']
            )
            # El consumidor invoca a la capa de aplicación sin acoplarse a ella[cite: 1]
            self.caso_uso.ejecutar(dto)
            print("[Broker] Mensaje procesado exitosamente.")

        canal.basic_consume(queue='facturas_queue', on_message_callback=callback, auto_ack=True)
        print("Esperando mensajes de RabbitMQ...")
        canal.start_consuming()
