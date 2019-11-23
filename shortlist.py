#!/usr/bin/env python3

import json
import requests
import sys

edge = "https://graph.facebook.com/v5.0/716284875084506/feed?"
fields = "fields=message%2Cpermalink_url%2Cfull_picture%2Cmessage_tags"
limit = "&limit=300"
start = "&since="+sys.argv[1]
end = "&until="+sys.argv[2]
token = "&access_token=<your access_token>"
url = edge+fields+start+end+limit+token
filename = sys.argv[1]+sys.argv[2]+".txt"

print (url)
print (filename)

r = requests.get(url)
feed = json.loads(r.content.decode())
feeddata = feed["data"]
for i in feeddata:
	if "message_tags" in i:
		for j in i["message_tags"]:
			if j["name"]=="#stopdowry":
				try:
					text = i["permalink_url"]+","+i["full_picture"]
					with open(filename, "a") as myfile:
						myfile.write(text)
				except:
					print ("No picture in post")
