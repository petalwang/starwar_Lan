""" Basic todo list using webpy 0.3 """
import web, sys

urls = (
    '/', 'Index',
    '/login', 'Login',
    '/logout', 'Logout',
    '/sample', 'Sample',
)


web.config.debug = False
app = web.application(urls, locals())
session = web.session.Session(app, web.session.DiskStore('sessions'))

Password = None

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
        if session.get('logged_in', False):
            return 'Display user logged in content'
        else:
            return '<html><form action="login" method="POST">password<input type="text" name="password" value="1234"><br><br><input type="submit" value="submit"></form></html>'

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
