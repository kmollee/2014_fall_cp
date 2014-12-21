#@+leo-ver=5-thin
#@+node:lee.20141215164031.46: * @file application.py
#@@language python
#@@tabwidth -4

#@+<<decorations>>
#@+node:lee.20141215164031.47: ** <<decorations>>
import cherrypy
import os
from symbol import *
import random
from jinja2 import Environment, FileSystemLoader
#@-<<decorations>>

#@+others
#@+node:lee.20141215164031.48: ** folder setting
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))

if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示程式在雲端執行
    data_dir = os.environ['OPENSHIFT_DATA_DIR']
    tmp_dir = data_dir + 'tmp'
    templates_dir = os.environ['OPENSHIFT_REPO_DIR'] + 'templates'
    static_dir = os.environ['OPENSHIFT_REPO_DIR'] + 'static'
    std_dir = os.environ['OPENSHIFT_REPO_DIR'] + 'std/'
else:
    # 表示程式在近端執行
    data_dir = _curdir + "/local_data/"
    templates_dir = _curdir + "/templates"
    tmp_dir = data_dir + '/tmp'
    static_dir = _curdir + '/static'
    std_dir = _curdir + '/std/'

env = Environment(loader=FileSystemLoader(templates_dir))

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

if not os.path.exists(tmp_dir):
    os.makedirs(tmp_dir)
#@+node:lee.20141215164031.50: ** class Final
class Final(object):
    #@+others
    #@+node:lee.20141215164031.51: *3* _cp_config
    _cp_config = {

        'tools.encode.encoding': 'utf-8',    
        'tools.sessions.on' : True,
        'tools.sessions.storage_type' : 'file',
        'tools.sessions.locking' : 'early',
        'tools.sessions.storage_path' : tmp_dir,
        'tools.sessions.timeout' : 60,
    }
    #@+node:lee.20141215164031.52: *3* def index
    @cherrypy.expose
    def index(self):
        # get template
        tmpl = env.get_template('index.html')
        # student list 40323101 - 40323157
        # use 40323100 to demonstrate example
        std_list = ["403231{0:02d}".format(s) for s in range(0, 58)]
        return tmpl.render(title='index', students=std_list)
    #@-others
#@+node:lee.20141215164031.86: ** def error_page_404
# handle page 404
def error_page_404(status, message, traceback, version):
    tmpl = env.get_template('404.html')
    return tmpl.render(title='404')

cherrypy.config.update({'error_page.404': error_page_404})
#@+node:lee.20141221203113.43: ** import std module to root
root = Final()

import imp

# import all std module, if not import success, pass
# use student numbert to be sub path
# e.g. 127.0.0.1/40323100/
# if visitor visit not exsit page, raise 404
# 40323100 - 57, 40323100 is an example page.
for i in range(0, 58):
    try:
        mod = imp.load_source(
            'a403231%02d' % i, std_dir + 'a403231%02d.py' % i)
        setattr(root, '403231%02d' % i, mod.Application())
    except:
        pass
#@+node:lee.20141221203113.44: ** application_conf
# set up app conf
application_conf = {
    '/static': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': static_dir
    },
}
#@+node:lee.20141215164031.60: ** run env
if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 在 openshift
    application = cherrypy.Application(root, config = application_conf)
else:
    # 在其他環境下執行
    cherrypy.quickstart(root, config = application_conf)
#@-others
#@-leo
