import requests

# requests.get()

url = "http://www.example.com/downloads/sample.pdf"

new = url[-1:-4:-1]
new2 = url.split(".")

# print(new)
if "pdf" not in new2:
    print("pass")
    print(new[-1::-1])

r = requests.head(url)