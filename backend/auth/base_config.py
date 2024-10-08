from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import JWTStrategy
from fastapi_users.authentication import AuthenticationBackend
from fastapi_users import FastAPIUsers, fastapi_users

from .manager import get_user_manager
from auth.models import User
from core.config import settings


cookie_transport = CookieTransport(cookie_name="bonds", cookie_max_age=3600)

SECRET = settings.auth.secret_key

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int]( #type: ignore
    get_user_manager,
    [auth_backend],
)


current_user = fastapi_users.current_user()