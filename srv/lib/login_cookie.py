from datetime import datetime
from fastapi import Response, Request, HTTPException
import hashlib

class LoginCookie:
    COOKIE_PARAMS = dict(httponly=True, samesite="none", secure=True)

    def __init__(self, secret_key: str, timeout: int=3600, cookie_name: str='login'):
        self.cookie_name = cookie_name
        self.secret_key = secret_key
        self.timeout = timeout
        self.cookie_params = self.COOKIE_PARAMS
        self.cookie_params["key"] = self.cookie_name

    def get_cookie_value(self):
        timeout = int(datetime.timestamp(datetime.now()) + self.timeout)
        unhashed = f"{self.secret_key} + {timeout}"
        hashed = hashlib.sha256(unhashed.encode()).hexdigest()
        return f"{timeout}|{hashed}"
    
    def get_cookie_params(self):
        return self.cookie_params
    
    def delete_cookie(self, response:Response):
        response.delete_cookie(**self.get_cookie_params())

    def set_login_cookie(self, response:Response):
        value = self.get_cookie_value()
        response.set_cookie(value=value, **self.get_cookie_params())
        response.set_cookie(key="MyInsecureCookie", value="NotASecret") # this line is designed to show how to extract cookie via JS


    def check_login_cookie(self, request: Request) -> dict[str, str]:
        cookie_value = request.cookies.get(self.cookie_name)
        if not cookie_value:
            raise HTTPException(status_code=401, detail="Login cookie missing")
        timeout_str, hashed = cookie_value.split("|")
        timeout = int(timeout_str)
        if timeout < datetime.now().timestamp():
            raise HTTPException(status_code=401, detail="Login cookie expired")
        unhashed = f"{self.secret_key} + {timeout}"
        new_hashed = hashlib.sha256(unhashed.encode()).hexdigest()
        if hashed != new_hashed:
            raise HTTPException(status_code=401, detail="Login cookie tampered")
        return {"username": "Not Secure"}

cookieChecker = LoginCookie(secret_key="secret_key", timeout=3600, cookie_name="login")