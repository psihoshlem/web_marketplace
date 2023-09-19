import jwt
from fastapi import HTTPException, Header

JWT_SECRET = "1142b829a5c45e37b6e879ef63d00f29"
JWT_ALGORITHM = "HS256"


def encodeJWT(login: str):
    payload = {
        "login": login
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {
        "token": token
    }


def jwt_bearer(token: str = Header()):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decode_token["login"]
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Token is invalid")