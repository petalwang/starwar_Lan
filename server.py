
import web, sys, os
from pprint import pprint

urls = (
    '/', 'Index',
    '/login', 'Login',
    '/logout', 'Logout',
    '/sample', 'Sample',
    '/(html)/(.*)', 'Static',
)


web.config.debug = False
app = web.application(urls, locals())
session = web.session.Session(app, web.session.DiskStore('sessions'))

Password = None

class Static:
    
    def GET(self, media, filename):
        if session.get('logged_in', False):
            print filename
            print media
            filepath = os.path.join(os.getcwd(), media, filename)
            print filepath
            try:
                f = open(filepath, 'r')
                return f.read()
            except:
                return 'No such thing' # you can send an 404 error here if you want
        else:
            try:
                f = open(os.path.join(os.getcwd(), 'html', 'login.html'), 'r')
                return f.read()
            except:
                return 'No such thing' # you can send an 404 error here if you want

class Login:

    def POST(self):
        global Password
        password = web.input().password
        if password == Password:
            session.logged_in = True
            raise web.seeother('/')

class Logout:
    def GET(self):
        session.logged_in = False
        raise web.seeother('/')

class Index:

    def GET(self):
        f = open(os.path.join(os.getcwd(), 'html', 'login.html'), 'r')
        return f.read()

class Sample:

    def GET(self):
        if session.get('logged_in', False):
            return '<h1>User is logged in</h1>'
        else:
            return '<h1>User is not logged in</h1>'

app = web.application(urls, globals())

if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'), {'count': 0})
    web.config._session = session
else:
    session = web.config._session

if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) != 3:
        print "python server.py PORT VISITOR_PASSWORD"
        sys.exit(1)
    Password = sys.argv[2]
    print Password
    app.run()
