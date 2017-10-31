
import datetime
import redis
r = redis.Redis(host='127.0.0.0', port=6379, db=1)
def queuerecharge(id,money):
    try:
        keyname = 'id_money_recharge'
        rechargeinfo = {
            'id':str(id),
            'type': '1',
            'money': str(money),
            'time': str(datetime.datetime.now()),
            'info':''
        }
        r.set(keyname,rechargeinfo)
        return '1'
    except:
        return '0'

def queuewithdrawal(id,money):
    try:
        keyname = 'id_money_withdrawal'
        withdrawalinfo = {
            'id':str(id),
            'type': '2',
            'money': str(money),
            'time': str(datetime.datetime.now()),
            'info':''
        }
        r.set(keyname,withdrawalinfo)
        return '1'
    except:
        return '0'

def queuetransfer(id,money,desid):
    try:
        keyname = 'id_money_transfer'
        transferinfo = {
            'id':str(id),
            'desid': str(desid),
            'type': '3',
            'money': str(money),
            'time': str(datetime.datetime.now()),
            'info':''
        }
        r.set(keyname,transferinfo)
        return '1'
    except:
        return '0'

