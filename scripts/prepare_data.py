import requests
import os
from zipfile import ZipFile
import hashlib

directory = 'data'

if not os.path.exists(directory):
    os.makedirs(directory)
    
wine_quality = os.path.join(directory, 'wine_quality')
if not os.path.exists(wine_quality):
    os.makedirs(wine_quality)
    

url = 'https://archive.ics.uci.edu/static/public/186/wine+quality.zip'

response = requests.get(url)
if response.status_code == 200:
    file_name = url.split('/')[-1]
    with open(os.path.join(wine_quality, file_name), "wb") as f:
        f.write(response.content)

    with ZipFile(os.path.join(wine_quality, file_name), "r") as zr:
        zr.extractall(wine_quality)
        
    os.remove(os.path.join(wine_quality,"wine+quality.zip"))
        
    print(f"Download Successful: {file_name}")

else:
    print(f"Download Unsuccessful: {url}")
    

red_csv = '4a402cf041b025d4566d954c3b9ba8635a3a8a01e039005d97d6a710278cf05e'
white_csv = '76c3f809815c17c07212622f776311faeb31e87610d52c26d87d6e361b169836'
names = '15d215e73b39105952380fd487e4ce1bf5a6b83a425abb285c2ec55193d3ca92'


with open('data/wine_quality/winequality-red.csv', mode = 'rb') as f:
    data=f.read()
    red_sha256 = hashlib.sha256(data).hexdigest()
    
with open('data/wine_quality/winequality-white.csv', mode = 'rb') as f:
    data=f.read()
    white_sha256 = hashlib.sha256(data).hexdigest()
    
with open('data/wine_quality/winequality.names', mode = 'rb') as f:
    data=f.read()
    name_sha256 = hashlib.sha256(data).hexdigest()
    
    
if red_csv == red_sha256:
    if white_csv == white_sha256:
        if names == name_sha256:
            print("Computer hash matches expected hash")
        else:
            print("Computer hash does not match expected hash")
