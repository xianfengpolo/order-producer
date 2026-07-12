from dataclasses import dataclass

@dataclass
class OrderFilledEvent:
    """Emitted to topic 'order.filled' when an order is matched."""
    order_id: str
    user_id: str
    symbol: str
    filled_qty: float
    filled_price: float
    side: str  # "buy" | "sell"
    timestamp_ms: int
