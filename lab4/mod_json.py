import json

def test_json():
    data = {"status": "success", "code": 200}
    json_str = json.dumps(data)
    print(f"[JSON] Серіалізований рядок: {json_str}")