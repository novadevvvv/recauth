import requests

"""
Website: https://github.com/novadevvvv
Dependencies: None
"""

def verifyAccount(username: str) -> dict:
    url = "https://pcky.dev/api/recroom/validate"

    response = requests.get(url, params={"username": username},verify=False)
    response.raise_for_status()
    data = response.json()

    if data["ok"] is False:
        return {"ok": False, "Reason": "ERR-NO_BIO_CODE"}
    else:
        return {"ok": data["ok"],"username": data["username", "sessionToken": data["sessionToken"]], "expiry": data["expiry"]}