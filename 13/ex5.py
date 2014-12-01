# coding: utf-8
# 上面一行宣告程式內容所採用的編碼(encoding)
# 導入 cherrypy 模組
import cherrypy
# 導入 Python 內建的 os 模組
import os

# all symbol is row 9 col 7
# 1. try use function print out symbol 1, 2, 3
# 2. try get input from user, then loop the input and print out
# 3. use dictionary map function
# 4. try use dict map to function, then use function print out first line
# 5. use row range, print out all line of symbol
# 6. use while loop make game more funny...


def symbolSpace(row):
    s = [
        '■■■■■■■',
        '■■■■■■■',
        '■■■■■■■',
        '■■■■■■■',
        '■■■■■■■',
        '■■■■■■■',
        '■■■■■■■',
        '■■■■■■■',
        '■■■■■■■',
    ]
    return s[row]


def symbol1(row):
    s = [
        '■■■□■■■',
        '■■□□■■■',
        '■■■□■■■',
        '■■■□■■■',
        '■■■□■■■',
        '■■■□■■■',
        '■■■□■■■',
        '■■■□■■■',
        '■□□□□□□',
    ]
    return s[row]


def symbol2(row):
    """
    row is a positive int
    return None
    """
    s = [
        '■□□□□□■',
        '■□■■■■□',
        '■■■■■■□',
        '■■■■■■□',
        '■■■■■■□',
        '■■□□□□□',
        '■□■■■■■',
        '■□■■■■■',
        '■□□□□□□',
    ]
    return s[row]


def symbol3(row):
    s = [
        '■□□□□□■',
        '■■■■■■□',
        '■■■■■■□',
        '■■■■■■□',
        '■□□□□□■',
        '■■■■■■□',
        '■■■■■■□',
        '■■■■■■□',
        '■□□□□□■',
    ]
    return s[row]

'''
# test symbol function is work correctly
symbol1(1)
symbol2(2)
'''

# dict map key:string value:function
# string->function
symbolDict = {"1": symbol1, "2": symbol2, "3": symbol3, "": symbolSpace}


def asciiImage(inp):
    if inp == '':
        return ''
    row = 9
    startString = """
    <html>
        <head>
            <title>asciiImage</title>
            <meta charset="UTF-8">
        </head>
        <body>
    """

    endString = """
        </body>
    </html>
    """
    for r in range(row):
        for c in inp:
            # try get symbol function, if not exist, use symbolSpace as default
            # get the symbol's row
            out_symbol = symbolDict.get(c, symbolDict[""])(r)
            startString += out_symbol
        startString += "<br />"
    outString = startString + endString
    return outString


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
        # output goodbye, name
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

    @cherrypy.expose
    def asciiForm(self):
        # form, action to asciiOutput
        return """
        <html>
            <head>
                <title>asciiForm</title>
                <meta charset="UTF-8">
            </head>
            <body>
                <h1>say something</h1>
                <form method="get" action="/asciiOutput">
                    <input type="text" name="text" />
                    <button type="submit">Say it now!</button>
                </form>
            </body>
        </html>
        """

    @cherrypy.expose
    def asciiOutput(self, text):
        # output asciiImage
        return asciiImage(text)


if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示在 OpenSfhit 執行
    application = cherrypy.Application(Guess())
else:
    # 表示在近端執行
    cherrypy.quickstart(Guess())
