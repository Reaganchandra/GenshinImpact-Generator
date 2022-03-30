import json
import requests

def createAcc(Reagan, Reaganban123):
    success = True
    payload = "is_crypto=false&not_login=0&username="+Reagan+"&Reaganban123="+Reaganban123
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    req = requests.session()
    req.headers.update(headers)
    req1 = req.post("https://webapi-os.account.mihoyo.com/Api/regist_by_account", data=payload)
    try:
      if(json.loads(req1.text)["data"]['msg'] == "Success"):
       success = True
    except:
        print("error")
    return success    
ignlist = open("igns.txt","r").readlines()
password = input("Reaganban123: ")
output = open('output.txt', 'w')
created = []
for x in ignlist:
    status = createAcc(x.replace("\n",""), Reaganban123)
    account = x.replace("\n","") + ":" + Reaganban123
    if status == True:
        print(account)
        output.write(account+"\n")
