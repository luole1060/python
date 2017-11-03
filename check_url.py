#!/usr/bin/python
import requests
import json
import time
import copy

endpoint = "proxy"
post_url = "http://127.0.0.1:1988/v1/push"

def url_status(server_name,url):
	playload = []
	ts = int(time.time())
	data= {"endpoint": endpoint, "metric": "", "timestamp": ts, "step": 60, "value": "","counterType": "GAUGE", "tags": ""}
	res = requests.get(url, verify=False)
	status = res.status_code
	data["metric"] = server_name
	if status == 200:
		data["value"] = 1
	else:
		data["value"] = 0
	playload.append(copy.copy(data))
	print playload	
	r=requests.post(post_url, data=json.dumps(playload))


if __name__ == "__main__":
    while 1:
	url_status("js_gitlab","http://code.js.iquantex.com")
	url_status("js_svn","http://svn.js.iquantex.com/svnadmin")
	url_status("js_maven","http://maven.js.iquantex.com")
	url_status("js_rap","http://rap.js.iquantex.com:8084/RAP")
	url_status("js_imsui","https://10.16.18.10:8443/")
	time.sleep(60
