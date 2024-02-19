from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse
from requests_html import AsyncHTMLSession, HTMLSession

app = FastAPI()


@app.post('/tasks/')
async def run_task(payload=Body(...)):
    try:
        user_agent = {
            'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'
        }
        proxies = {
            'http': 'http://username:password@1.111.111.111:8080',
            'https': 'http://username:password@1.111.111.111:8080',
        }
        if (payload['render']):
            asession = AsyncHTMLSession()
            response = await asession.get(payload['url'], proxies=proxies, headers = user_agent)
            await response.html.arender()
            return response.html.html
        else:
            session = HTMLSession()
            response = session.get(payload['url'], proxies=proxies, headers = user_agent)
            return response.content
    except Exception as ex:
        return ex


print('ok')