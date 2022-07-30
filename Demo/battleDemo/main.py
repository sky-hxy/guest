from termios import TIOCPKT_DOSTOP
from common import Common

comm = Common('http://127.0.0.1:12356')

def getStart():
    uri = '/'
    response_index = comm.get(uri)
    print("Response内容：" + response_index.text)

getStart()

def postStart():
    uri = '/login'
    username = "criss"
    password = "criss"
    payload = "username=" + username + "&password=" + password
    response_index = comm.post(uri)
    print("Response内容：" + response_index.text)

postStart()

def selectStart():
    uri = '/selectEq'
    equipmentid = '10003'
    payload = "equipmentid=" + equipmentid
    response_index = comm.post(uri, prams=payload)
    print("Response内容：" + response_index.text)

selectStart()

def killStart():
    uri = '/kill'
    enemyid = '20001'
    equipmentid = '10003'
    payload = "enemyid=" + enemyid + "&equipmentid=" + equipmentid
    response_index = comm.post(uri, prams=payload)
    print("Response内容：" + response_index.text)

killStart()

#TODO 下载清单，和POSTMAN
comm.put()