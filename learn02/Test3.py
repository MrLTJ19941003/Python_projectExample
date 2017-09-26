import asyncio,datetime

async def show_operation(num,loop):
    end_time=loop.time()+10.0
    while True:
        print('loop:{} time:{}'.format(num,datetime.datetime.now()))
        if loop.time()+2.0>=end_time:
            break
        await asyncio.sleep(1)

loop=asyncio.get_event_loop()
tasks=[show_operation(1,loop),show_operation(2,loop)]
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()