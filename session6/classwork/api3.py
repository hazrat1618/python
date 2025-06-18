import requests
import pprint as p


cookies = {"access_token_cookie": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYXNyaWRkaW5vdnkxNjE4QGdtYWlsLmNvbSIsImV4cCI6MTc1MDE4MjE4NH0.dK_kuLPmiX6URHP1Y9XrhEvs19xb7bCPJPLbiEDrJ6Q"}
url = "https://backend.akumotechnology.com/api/users/me"
about_me = requests.get(url, cookies=cookies)

p.pprint(about_me.json())