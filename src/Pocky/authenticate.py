import requests

"""
Website: https://github.com/novadevvvv
Dependencies: None
"""

def checkCode(token: str) -> dict:
    url = "https://pcky.dev/api/recroom/authenticate"

    response = requests.get(url, params={"token": token},verify=False)
    response.raise_for_status()
    data = response.json()

    if data["ok"] is False:
        return {"ok": False, "Reason": "ERR-INVALID_TOKEN"}
    else:
        return {"ok": data["ok"],"username": data["username", "accountId": data["accountId"]], "expiry": data["expiry"]}