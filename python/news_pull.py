# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
import urllib
import json

app = Flask(__name__)

@app.route('/rock', methods=['GET', 'POST'])

def baojin():
    data = json.loads(request.get_data())
    ttt  = json.dumps(data)
    print (ttt)
    for num in data['alerts']:
        mess = num['annotations'].get('summary')
        chat =  num['annotations'].get('chid')
        if chat is None or mess is None:
            return "None"
        else:
            send_url = 'http://ip/QywxInterface/SendChatHandler.ashx'
            send_values = {
                "receiver":
                {
                    "type": "group",
                    "id": chat
                },
                "sender": "mailname",
                "msgtype": "text",
                "text":
                {
                    "content": mess
                }
            }
            header = 'msg='
            send_data = header+json.dumps(send_values, ensure_ascii=False)
            print (send_data)        
            send_request = urllib.request.Request(send_url, send_data.encode(encoding='UTF8'))
            print (mess)
            response = json.loads(urllib.request.urlopen(send_request).read())
            print (chat)

    #return "200"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)