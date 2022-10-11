from typing import Dict, List

def orderEntity(item) -> Dict:
    return {
        "id": str(item["_id"]),
    }


def ordersEntity(entity) -> List[Dict]:
    return [orderEntity(i) for i in entity]