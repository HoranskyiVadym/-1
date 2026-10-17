import requests

def test_requests():
    response = requests.get("https://api.ipify.org?format=json")
    print(f"[Requests] Твоя публічна IP адреса: {response.json().get('ip')}")