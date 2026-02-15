![Banner](src/git/banner.png)
![Dynamic JSON Badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fnovadevvvv%2Frecauth%2Frefs%2Fheads%2Fmain%2Fsrc%2Fdata.json&query=lastUpdate&style=flat&label=Last%20Update)

# RecAuth

> A lightweight verification utility for securely confirming user ownership via profile bio validation.

Credit to **[@pckydev](https://github.com/pckydev)** for the API endpoints utilised in this project.

---

## Overview

RecAuth provides a minimal, dependency-light method for verifying account ownership without requiring OAuth, passwords, or sensitive credentials.

### Verification Model

1. Generate a unique verification code.
2. Instruct the user to place the code in their profile bio.
3. Confirm ownership by validating the presence of the code.

This ensures the user has control over the account while maintaining a simple integration flow.

---

## Installation

```bash
git clone https://github.com/novadevvvv/recauth.git
cd recauth
```

---

## Usage

### Import

```python
from src.Pocky.authenticate import checkCode
from src.Pocky.getCode import getCode
from src.Pocky.verifyAccount import verifyAccount
```

---

## API Reference

### `getCode(username: str) -> dict`

Generates a unique verification code for a given username.

#### Example

```python
response = getCode("username")
print(response)
```

#### Example Response

```json
{
  "success": true,
  "code": "ABC123"
}
```

---

### `verifyAccount(username: str) -> dict`

Checks whether the generated verification code exists in the user's bio.

#### Example

```python
response = verifyAccount("username")
print(response)
```

#### Example Response

```json
{
  "verified": true
}
```

---

### `checkCode(code: str) -> dict`

Retrieves the account associated with a verification code.

#### Example

```python
response = checkCode("ABC123")
print(response)
```

#### Example Response

```json
{
  "username": "exampleUser",
  "valid": true
}
```

---

## End-to-End Example

```python
username = "exampleUser"

# Step 1: Generate verification code
code_data = getCode(username)
code = code_data["code"]

print("Verification code:", code)
print("Ask the user to place this code in their bio.")

# Step 2: After user updates bio, verify ownership
verification = verifyAccount(username)

if verification.get("verified"):
    print("User successfully verified.")
else:
    print("Verification failed.")
```

---

## Security Considerations

- No passwords or authentication tokens are collected.
- Verification relies solely on user-controlled profile metadata.
- Codes should be treated as temporary and rotated appropriately.
- Avoid storing verification codes indefinitely.

