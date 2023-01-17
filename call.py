import requests

image_path = "image_classification/test_imgs/banana.jpeg"
url = 'http://localhost:5000/api'


r = requests.post(url, files={'image': open(image_path, "rb")})

print(r.json())