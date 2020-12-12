# --coding: utf-8 --

import  requests

#response = requests.get("https://api.xdclass.net/pub/api/v1/web/all_category")

# https://api.xdclass.net/pub/api/v1/web/video_detail?video_id=53
# data = {"video_id":53}
# response = requests.get("https://api.xdclass.net/pub/api/v1/web/video_detail", data)

# data = {"phone":"18668091423","pwd":"yb85119850"}
# response = requests.post("https://api.xdclass.net//pub/api/v1/web/web_login", data=data)


headers = {"token":"xdclasseyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4ZGNsYXNzIiwicm9sZXMiOiIxIiwiaW1nIjoiaHR0cHM6Ly94ZC12aWRlby1wYy1pbWcub3NzLWNuLWJlaWppbmcuYWxpeXVuY3MuY29tL3hkY2xhc3NfcHJvL2RlZmF1bHQvaGVhZF9pbWcvNy5qcGVnIiwiaWQiOjY3ODA2ODgsIm5hbWUiOiLljaHljaHlk6UiLCJpYXQiOjE2MDcxNDg3NzEsImV4cCI6MTYwNzc1MzU3MX0.Qro1NQY7KAma4qc80QYunHPG61o4V6zz8cYQGY5UZdk"}
response =  requests.get("https://api.xdclass.net/pub/api/v1/web/user_info", headers=headers)



print(response.status_code)
# print(response.text)
# print(response.content)
print(response.json())



    




