from rapiclient import RESTAPI

import sys

def get_random_collection():
    import string
    import random
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))


settings = {
    'DOMAIN': 'http://127.0.0.1:8080',
    'PREFIX_PATH': '/',
    'LOGIN_PATH': '/auth/token/login/',
    'LOGOUT_PATH': '/auth/token/logout/',
    'TOKEN_TYPE': 'auth_token',
    'TOKEN_FORMAT': 'Token {token}',
    'HEADERS': {
        'Content-Type': 'application/json'
    }
}

credentials = {
    'email': 'admin@example.com',
    'username': 'admin',
    'password': '<password>',
}

token = "<token>"

api = RESTAPI(settings)

print("==================================")
print("")
print("User Login (credentials)")
response = api.login(credentials)
if response.ok:
    print("Login succeed ...")
else:
    print("Login failed ...")
    sys.exit(-1)
print("Response Ok: %s" % response.ok)
print("Response Status: %s" % response.status)
print("Response Data: %s" % response.data)
print("")
print("")
print("==================================")
print("")
print("User Login (token)")
api = RESTAPI(settings)
api.token = token
print("==================================")
print("")
print("GET api.collections.get()")
print("")
response = api.collections.get()
print("Response Ok: %s" % response.ok)
print("Response Status: %s" % response.status)
print("Response Data: %s" % response.data)
print("")
print("")
print("==================================")
print("")
print("POST api.collections.post({<invalid-doc>})")
print("")
response = api.collections.post({ "sname": get_random_collection() })
print("Response Ok: %s" % response.ok)
print("Response Status: %s" % response.status)
print("Response Data: %s" % response.data)
print("")
print("")
print("==================================")
print("")
print("POST api.collections.post({<valid-doc>})")
print("")
response = api.collections.post({ "name": get_random_collection() })
print("Response Ok: %s" % response.ok)
print("Response Status: %s" % response.status)
print("Response Data: %s" % response.data)
print("")
print("")
print("==================================")
print("")
print("GET api.collections(<valid-key>).get()")
print("")
response = api.collections(response.data["codename"]).get()
print("Response Ok: %s" % response.ok)
print("Response Status: %s" % response.status)
print("Response Data: %s" % response.data)
print("")
print("")
print("==================================")
print("")
print("PATCH api.collections.patch({<valid-doc>})")
print("")
response = api.collections(response.data["codename"]).patch({"name": get_random_collection() })
print("Response Ok: %s" % response.ok)
print("Response Status: %s" % response.status)
print("Response Data: %s" % response.data)
print("")
print("")
print("==================================")
print("")
print("GET api.collections.get(extra={ ... })")
print("")
test = api.collections.get(extra={
    'codename': response.data['codename']
})
print("Response Ok: %s" % test.ok)
print("Response Status: %s" % test.status)
print("Response Data: %s" % test.data)
print("")
print("")
print("==================================")
print("")
print("DELETE api.collections(<valid-key>).delete()")
print("")
response = api.collections(response.data["codename"]).delete()
print("Response Ok: %s" % response.ok)
print("Response Status: %s" % response.status)
print("Response Data: %s" % response.data)
print("")
print("")
print("==================================")
print("")
print("DELETE api.collections(<invalid-key>).delete()")
print("")
response = api.collections("blablalbla").delete()
print("Response Ok: %s" % response.ok)
print("Response Status: %s" % response.status)
print("Response Data: %s" % response.data)
print("")
print("")
print("==================================")
print("")
print("GET api.collections(<invalid-key>).get()")
print("")
response = api.collections("blablalbla").get()
print("Response Ok: %s" % response.ok)
print("Response Status: %s" % response.status)
print("Response Data: %s" % response.data)
print("")
print("")
print("==================================")