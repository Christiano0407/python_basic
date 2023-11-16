#####
#Fast API & Uvicorn
####
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
#HomePage
@app.get('/', response_class=HTMLResponse)
async def get_home():
  html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
            <meta charset="utf-8" />
        </head>
        <body>
            <h1>Hello Dev! HTML & Python!</h1>
            <h2>Python Backend </h2>
            <p>Developer Web Content</p>
        </body>
    </html>
    """
  return HTMLResponse(content=html_content, status_code=200)

#Content
@app.get('/content', response_class=HTMLResponse)
async def get_content():
  html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
            <meta charset="utf-8" />
        </head>
        <body>
            <h1>Content Page</h1>
            <p>Hello World! Python In Backend!!! Amazing Content</p>
        </body>
    </html>
   """
  return HTMLResponse(content=html_content, status_code=200)