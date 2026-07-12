from dataclasses import dataclass

@dataclass
class OrderFilledEvent:
    """Emitted to topic 'order.filled' when an order is matched."""
    order_id: str
    user_id: str
    symbol: str
    exec_qty: float  # renamed from filled_qty
    exec_price: float  # renamed from filled_price
    order_side: str  # renamed from side; values now "BUY"/"SELL" (uppercase)
    timestamp_ms: int
    fee_asset: str  # new required field
    fee_amount: float  # new required field
