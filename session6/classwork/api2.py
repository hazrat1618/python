

url = "https://backend.akumotechnology.com/api/users/me"
cookie = {"access_token_cookie": ""}
about_me = request.get(url, cookies=cookie)

print(about_me.json())