import random
from datetime import datetime
from typing import List, Dict, Optional

import pandas as pd


def parse_end_time(value: str) -> datetime:
    """Parse end_time strings from CSV into a timezone-naive datetime.
    Assumes input like 'YYYY-MM-DD HH:MM:SS'.
    """
    return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")


def auto_bid(
    auction_data: pd.DataFrame,
    max_budget: float = 1000.0,
    max_bid_per_item: Optional[float] = None,
    snipe_minutes: int = 5,
) -> List[Dict[str, object]]:
    """Simulate auto-bidding based on simple rules.

    Rules:
    - Only bid if the current price is below both the total max budget and per-item cap (if set)
    - If the auction is ending within `snipe_minutes`, increase aggressiveness slightly
    - Bid is current_price + min_increment
    - Status is mocked as Winning/Outbid at random
    """
    results: List[Dict[str, object]] = []
    current_time = datetime.now()

    for _, row in auction_data.iterrows():
        try:
            end_time_raw = row["end_time"]
            end_time = parse_end_time(end_time_raw) if isinstance(end_time_raw, str) else end_time_raw
        except Exception:
            end_time = current_time

        current_price = float(row["current_price"]) if pd.notna(row["current_price"]) else 0.0
        min_increment = float(row["min_increment"]) if pd.notna(row["min_increment"]) else 1.0
        item_name = str(row["item_name"]) if pd.notna(row["item_name"]) else "Unknown Item"

        if current_price > max_budget:
            continue

        if max_bid_per_item is not None and current_price > max_bid_per_item:
            continue

        minutes_left = max((end_time - current_time).total_seconds() / 60.0, 0)
        aggressiveness = 1.0
        if minutes_left <= snipe_minutes:
            aggressiveness = 1.25

        base_bid = current_price + min_increment
        bid_amount = round(base_bid * aggressiveness, 2)

        if max_bid_per_item is not None:
            bid_amount = min(bid_amount, max_bid_per_item)

        status = random.choice(["Winning", "Outbid"])  # mocked outcome

        results.append(
            {
                "item_name": item_name,
                "current_price": current_price,
                "bid_amount": bid_amount,
                "status": status,
                "minutes_left": round(minutes_left, 1),
                "timestamp": current_time.strftime("%Y-%m-%d %H:%M:%S"),
            }
        )

    return results
