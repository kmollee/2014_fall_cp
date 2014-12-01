# coding: utf-8
# 上面一行宣告程式內容所採用的編碼(encoding)
# 導入 cherrypy 模組
import cherrypy
# 導入 Python 內建的 os 模組
import os
# 以下為 Guess 類別的設計內容, 其中的 object 使用, 表示 Guess 類別繼承 object 的所有特性, 包括方法與屬性設計


class Guess(object):
    # 以 @ 開頭的 cherrypy.expose 為 decorator, 用來表示隨後的成員方法, 可以直接讓使用者以 URL 連結執行

    @cherrypy.expose
    # index 方法為 CherryPy 各類別成員方法中的內建(default)方法, 當使用者執行時未指定方法, 系統將會優先執行 index 方法
    # 有 self 的方法為類別中的成員方法, Python 程式透過此一 self 在各成員方法間傳遞物件內容
    def index(self, name="John"):
        return "hello, " + name

    @cherrypy.expose
    def saygoodbye(self, name="John"):
        return "goodbye," + name

    @cherrypy.expose
    def sayForm(self):
        # form, action to saygoodbye
        return """
        <html>
            <head>
                <title>sayform</title>
                <meta charset="UTF-8">
            </head>
            <body>
                <h1>say good by to ....</h1>
                <form method="get" action="/saygoodbye">
                    <input type="text" name="name" />
                    <button type="submit">Say it now!</button>
                </form>
            </body>
        </html>
        """


if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示在 OpenSfhit 執行
    application = cherrypy.Application(Guess())
else:
    # 表示在近端執行
    cherrypy.quickstart(Guess())
