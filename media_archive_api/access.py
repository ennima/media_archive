import requests
endpoint = "http://127.0.0.1:3000/private"
data = {}
headers = {"Authorization":"Bearer ayJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEyMywiaWF0IjoxNTQ2MDUwMTU4LCJleHAiOjE1NDYwNjYxNTh9.ezByMvap7zVgoRGRoh15wSu32xMi_gldCXx8KLIsuoI"}

try:
	req = requests.get(endpoint,data=data,headers=headers).json()
except Exception as e:
	print(e)
	# raise e
else:
	print(req)


