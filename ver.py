import requests

url_input = input("请输入网站链接:")

url = url_input + "/data/admin/ver.txt"

print (url)

response = requests.get(url);

print ("此网站织梦系统版本为:"+response.text);
