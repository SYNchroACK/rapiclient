DEFAULT_OPTIONS = {
    'DOMAIN': 'http://127.0.0.1',
    'PREFIX_PATH': '/',
    'LOGIN_PATH': '/auth/token/login/',
    'LOGOUT_PATH': '/auth/token/logout/',
    'TOKEN_KEY': 'auth_token',
    'TOKEN_FORMAT': 'Token {token}',
    'HEADERS': {
        'Content-Type': 'application/json'
    },
    'VERIFY_SSL': True
}

# This import MUST be in the end of the file
from rapiclient.connection import RESTAPI