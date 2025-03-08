import request

data = requests.get("https://reqres.in/api/users")

print(data.text)