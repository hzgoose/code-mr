from extensions import sanic,asyncio,uvloop,LOGGING,Queue, redis, MongoClient
from queue import queuerecharge,queuewithdrawal,queuetransfer
q = Queue(connection=redis.Redis())
LOGGING['loggers']['network']['handlers'] = ['errorStream']
app = sanic.Sanic(__name__)
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
mcon = MongoClient('127.0.0.1', 27017,connect=False,maxPoolSize=None)

@app.route("/money/recharge/<id>/<money>")
async def recharge (request,id,money):
    q.enqueue(queuerecharge,id,money)
    return json({ "result": "1" })

@app.route("/money/withdrawal/<id>/<money>")
async def Withdrawal (request,id,money):
    q.enqueue(queuewithdrawal,id,money)
    return json({ "result": "1" })

@app.route("/money/transfer/<id>/<money>/<desid>")
async def transfer (request,id,money,desid):
    q.enqueue(queuetransfer,id,money,desid)
    return json({ "result": "1" })

@app.route("/money/info/<id>")
async def info (request,id):
    result = mcon.customers.info.find({'id':str(id)})
    return json(result)

if __name__ == '__main__':
    #app.config['DEBUG'] = True
    app.run(host="0.0.0.0", port=5551)
    # app.run(host='0.0.0.0', port=5501, workers=5,debug=False, log_config=LOGGING)