from typing import List

def present_detail(data: dict) -> dict:
    return  {
                "id": data.id,
                "title": data.title,
                "description": data.description,
                "owner_id": data.owner_id
            }


def present_list(data: List[dict]) -> List[dict]:
    results = []

    for item in data:
        results.append(present_detail(item))

    return results
