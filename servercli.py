import asyncio
import json
import pymongo
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers

async def run(loop):
    await nc.connect(servers=["http://35.223.171.148:4222"])
    future = asyncio.Future()

    async def message_handler(msg):
        data = json.loads(msg.data.decode())
        #aca se empizan a enviar los datos a las bases de datos
        con=pymongo.MongoClient('34.70.196.45',27017)
        try:
            db=con.proyecto2
            db.casos.insert({"name":data["name"],"depto":data["depto"],"age":10,"form":data["form"],"state":data["state"]})
            print("datos enviados a mongo")
        except Exception as e:
            print(e)
            print("problemas con la conexion de mongo")
        finally:
            con.close()
        print(data)

    await nc.subscribe("updates", cb=message_handler)

if __name__ == '__main__':
    nc = NATS()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    try:
        loop.run_forever()
    finally:
        loop.close()
