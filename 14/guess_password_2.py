#@+leo-ver=5-thin
#@+node:lee.20141207235250.46: * @file guess_password_2.py
#@@language python
#@@tabwidth -4

#@+<<decorations>>
#@+node:lee.20141207235250.48: ** <<decorations>>
import cherrypy
#@-<<decorations>>

#@+<<secretNumber>>
#@+node:lee.20141207235250.49: ** <<secretNumber>>
secretNumber = '123'
#@-<<secretNumber>>

#@+others
#@+node:lee.20141207235250.50: ** class Guess
class Guess(object):
    #@+others
    #@+node:lee.20141207235250.51: *3* def index
    @cherrypy.expose
    def index(self):
        return "welcome"
    #@+node:lee.20141207235250.52: *3* def form
    @cherrypy.expose
    def form(self):
        return """
        <form action="check">
        <input type="text" value="enter password" name="password">
        <input type="submit" value="Send">
        </form>
        """
    #@+node:lee.20141207235250.53: *3* def check
    @cherrypy.expose
    def check(self, password):
        if password == secretNumber:
            return "you pass it"
        else:
            return "try it again"
    #@-others
#@+node:lee.20141207235250.63: ** run
cherrypy.quickstart(Guess())
#@-others
#@-leo
