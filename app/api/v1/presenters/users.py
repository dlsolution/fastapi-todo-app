from typing import List

def present_detail(data: dict) -> dict:
    return  {
                "id": data.id,
                "email": data.email,
                "is_active_": data.is_active,
                "items": data.items
            }

def present_list(data: List[dict]) -> List[dict]:
    results = []

    for item in data:
        results.append(present_detail(item))

    return results
