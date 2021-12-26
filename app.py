from flask import Flask, request
import requests,json,webbrowser
import threading
from tkinter import *

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def callback():
    if request.method == 'POST':
        client_id = "VvpfgpbfsDW1mt5L0p3Ozt"
        redirect_uri = "http://127.0.0.1:5000"
        client_secret = "KsouxvSyExeupzvufUuqz4aV6c5QhtmQu3JsRKTbBdP"
        code = request.form.get('code')
        token_URL = "https://notify-bot.line.me/oauth/token?grant_type=authorization_code&redirect_uri={}&client_id={}&client_secret={}&code={}".format(redirect_uri, client_id, client_secret, code)
        token_r = requests.post(token_URL)
        if token_r.status_code == requests.codes.ok:
            access_token = json.loads(token_r.text)
            lineToken = access_token['access_token']
        print("1....."+lineToken)
        return "申請成功!!"


def get_token():
    client_id = "VvpfgpbfsDW1mt5L0p3Ozt"
    redirect_uri = "http://127.0.0.1:5000"
    code_URL = 'https://notify-bot.line.me/oauth/authorize?response_type=code&scope=notify&response_mode=form_post&state=f094a459&client_id={}&redirect_uri={}'.format(client_id, redirect_uri) 
    webbrowser.open_new(code_URL)



def win1_tk():
    win1 = Tk()
    win1_btn = Button(win1,text="連動",command=lambda:get_token())
    win1_btn.pack()
    win1.mainloop()


if __name__ == '__main__':
    t1 = threading.Thread(target=app.run).start()
    t2 = threading.Thread(target=win1_tk).start()