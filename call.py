import requests
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filepath') 
parser.add_argument('-url', '--server_url') 

args = parser.parse_args()


image_path = args.filepath
url = args.server_url + '/api'


r = requests.post(url, files={'image': open(image_path, "rb")})

print(r.json())