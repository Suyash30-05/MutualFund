#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils1 import fetch_reply
from utils1 import ML_pred


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')  
    #print (msg)
    phone=request.form.get('From')
    reply=fetch_reply(msg,phone)
    if  'age' in msg.lower() or 'tenure' in msg.lower() or 'capital' in msg.lower():
        
        #print('ok')
        list_1=msg.split()
        list_2=[]
        for l in list_1:
            if l.isdigit()==True:
                list_2.append(int(l))
            else:
                continue
        reply=ML_pred(list_2)
        #print(reply)
        resp =MessagingResponse()
        resp.message(reply)
        #print('ok3')
        return str(resp)
    else:
        resp = MessagingResponse()
        resp.message(reply)
        return str(resp)
            

    # Create reply
    #resp = MessagingResponse()
    #resp.message(reply)

    #return str(resp)

if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




