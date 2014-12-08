#@+leo-ver=5-thin
#@+node:lee.20141207235250.46: * @file guess_password_2.py
#@@language python
#@@tabwidth -4




secretNumber = '123'

class Guess(object):
    @cherrypy.expose
    def index(self):
        return "welcome"
    @cherrypy.expose
    def form(self):
        return """
        <form action="check">
        <input type="text" name="password">
        <input type="submit">
        </form>
        """
    @cherrypy.expose
    def check(self, password):
        if password == serectNumber:
            return "you pass it"
        else:
            return "try it again"



if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 在 openshift
    application = cherrypy.Application(Guess())
else:
    # 在其他環境下執行
    cherrypy.quickstart(Guess())
#@-leo
