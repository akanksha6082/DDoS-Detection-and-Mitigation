#!/usr/bin/env python
import requests
import json
import signal

rt = 'http://127.0.0.1:8008'
name = 'icmp'

def sig_handler(signal,frame):
  requests.delete(rt + '/flow/' + name + '/json')
  exit(0)

signal.signal(signal.SIGINT, sig_handler)

flow = {'keys':'ipsource,ipdestination,macsource,macdestination',
        'value':'frames',
        'log':True}
        
r = requests.put(rt + '/flow/' + name + '/json',data=json.dumps(flow))

flowurl = rt + '/flows/json?name=' + name + '&maxFlows=10&timeout=20'
flowID = -1

while 1 == 1:
  r = requests.get(flowurl + "&flowID=" + str(flowID))
  if r.status_code != 200: break
  flows = r.json()
  if len(flows) == 0: continue
  flowID = flows[0]["flowID"]
  flows.reverse()
  for f in flows:
    print(str(f['flowID']) + "," + str(f['flowKeys']) + ',' + str(int(f['value'])) + ',' + str(f['end'] - f['start']) + ',' + f['agent'] + ',' + str(f['dataSource']))
