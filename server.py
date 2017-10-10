from aiohttp import web
import json


async def handle_hello(request):
    name = request.match_info.get('username', "Anonymous")
    text = "Hello, " + name
    print(u"text = %s" % str(text))
    return web.Response(text=json.dumps({"message": text}))


app = web.Application()
app.router.add_get('/v2/hello/{username}', handle_hello)

web.run_app(app, port=8888)
