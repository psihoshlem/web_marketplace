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
        "access token": token
    }


def jwt_bearer(authorization: str = Header()):
    print(authorization)
    try:
        if not authorization.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Invalid Authorization header format")
        
        token = authorization.split("Bearer ")[1]
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decode_token.login
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Token is invalid")