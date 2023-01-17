import requests

image_path = "image_classification/test_imgs/banana.jpeg"
url = ' http://172.31.6.218:8000/api'


r = requests.post(url, files={'image': open(image_path, "rb")})

print(r.json())