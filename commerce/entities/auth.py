from dataclasses import dataclass


@dataclass
class Auth:
    password: str = ""
    access_token: str = ""
    refresh_token: str = ""
