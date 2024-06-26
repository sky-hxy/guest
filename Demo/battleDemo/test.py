import requests


class Test(object):
    def __init__(self, url):
        self.url = url

    def get(url):
        re = requests.get(url)
        print(re.text)

# t = Test("http://127.0.0.1:12356/")



# re = requests.get("http://127.0.0.1:12356/")
# print(re.text)

url_login = "http://127.0.0.1:12356/login"
username = "criss"
password = "criss"
payload = "username=" + username + "&password=" + password
res_login = requests.post(url_login, data=payload)
print(res_login.text)