import urllib.request
import requests

# opener = urllib.request.build_opener()
#
# response = opener.open("https://httpbin.org/get")
#
# print (response.read())

#
# res = requests.post("https://httpbin.org/get", data = "Test data hello world", headers = {"h1": "My title"})
#
# response = requests.get("https://httpbin.org/get")
# print(response.text)


coin_list = []

response = requests.get("https://bank.gov.ua/")
response_text = response.text

response_parse = response_text.split("<span>")

for parse_elem1 in response_parse:
    if not parse_elem1.startswith("₴"):
        continue
    for parse_elem2 in parse_elem1.split("</span>"):
        if parse_elem2.startswith("₴") and parse_elem2[1].isdigit():
            coin_list.append(parse_elem2)

hrivnya = coin_list[0]
print("hrivnya =", hrivnya)
