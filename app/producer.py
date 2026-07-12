import json
from dataclasses import asdict
from app.events import OrderFilledEvent

TOPIC_ORDER_FILLED = "order.filled"

def publish_order_filled(producer, event: OrderFilledEvent) -> None:
    """Publish OrderFilledEvent to Kafka."""
    producer.send(TOPIC_ORDER_FILLED, json.dumps(asdict(event)).encode())
