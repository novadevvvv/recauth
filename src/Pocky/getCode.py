import requests

"""
Website: https://github.com/novadevvvv
Dependencies: None
"""

def getCode(username: str) -> dict:
    url = "https://pcky.dev/api/recroom/login"

    response = requests.get(url, params={"username": username},verify=False)
    response.raise_for_status()
    data = response.json()

    return {
        "username": data["username"],
        "code": data["code"],
        "expiry": data["expiresAt"],
        "ok": data["ok"]
    }