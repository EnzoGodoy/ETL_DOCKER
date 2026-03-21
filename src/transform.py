from typing import List, Dict, Any, Optional

def safe_str(value: Any)-> Optional[str]:
    if value is None:
        return None
    text = str(value).strip()
    return text if text else None


def safe_float(value: Any) -> Optional[float]:
    try:
        return float(value)
    except (ValueError, TypeError):
        return None
    
def transform_record(record: dict[str,Any]) -> Dict[str, Any]:
    return{
        "brewery_id": safe_str(record.get('brewery_id')),
        "name": safe_str(record.get('name')),
        "brewery_type": safe_str(record.get('brewery_type')),
        "street": safe_str(record.get('street')),
        "city": safe_str(record.get('city')),
        "state": safe_str(record.get('state')),
        "postal_code": safe_str(record.get('postal_code')),
        "country": safe_str(record.get('country')),
        "phone": safe_str(record.get('phone')),
        "website_url": safe_str(record.get('website_url')),
        "updated_at": safe_str(record.get('updated_at')),
        "latitude": safe_float(record.get('latitude')), 
        "longitude": safe_float(record.get('longitude')),
        "state_province": safe_str(record.get('state_province'))    
    }

def transform_all(raw_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    transformed = []
    skipped = 0
    for record in raw_data:
        item = transform_record(record)
        if item['brewery_id'] or not item['name']:
            skipped += 1
            continue
        transformed.append(item)

    print(f"[trasform] Transformed {len(transformed)} records, skipped {skipped} ")
    print(f"[trasform]  records, skipped {skipped} ")

    return transformed
    
    
          