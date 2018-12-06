#Lay du lieu tu web ve python
from urllib.request import urlopen
import json #chuyen kieu du lieu

url = "https://wind.waqi.info/nsearch/full/hanoi?n=4"

#1. Open connection
conn = urlopen(url)

#2. Read date
raw_data = conn.read()

#3. Decode data
text = raw_data.decode("utf-8")

#4. Convert data from str to dict
data = json.loads(text)


results = data["results"]
result = results[0]
for i in results:
    print(i["n"], i["s"]["a"])