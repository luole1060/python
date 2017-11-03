#!/usr/bin/python

import os
import requests
import json
import time
import copy
import commands

push_url="http://127.0.0.1:1988/v1/push"
endpoint="Test201"
cmd="su  fwdev -c jps |grep -v grep |grep server_name | wc -l"

def server_report(server_name):
	playload=[]
	cmds=cmd.replace("server_name",server_name)
        status,pnum=commands.getstatusoutput(cmds)
        ts = int(time.time())
        data = {"endpoint": endpoint, "metric": server_name, "timestamp": ts, "step": 60, "value": "","counterType": "GAUGE", "tags": ""}
        if pnum == "1":
		data["value"]=1
        else:
		data["value"]=0
	playload.append(copy.copy(data))
        r=requests.post(push_url,data=json.dumps(playload)) 
      

if __name__ == "__main__":
    while 1:
	server_report("QuorumPeerMain")
	server_report("MDCacheServer")
	server_report("RTPersist")
	server_report("SorSimulatorMain")
	server_report("ExpenseCalcApplication")
	server_report("T2Compliance")
	server_report("CommonApplication")
	server_report("OmsMain")
	server_report("TradeEventReceiver")
	server_report("PKSApplication")
	server_report("PersistentServer")
	server_report("NimbusServer")
	server_report("Supervisor")
	time.sleep(60)
