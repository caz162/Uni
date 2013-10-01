import web, os
import sqlite3
from web import form

USER_DATA_DIR = "userData"
render = web.template.render('templates/')

db = web.database(dbn='sqlite', db='testdb.sqlite')

urls = ('/', 'index')


myform = form.Form( 
    form.Textbox("name"), 
    form.Textarea('description'),
    form.Checkbox('pref1',value="some value"),
    form.Checkbox('pref2',value="some value"),
    form.Checkbox('pref3',value="some value"), 
    form.Dropdown('difficulty', ['All_Mountain', 'All_Mountain_Plus', 'XC']),
    form.Dropdown('terrain', ['Rock', 'Grass', 'Road']))

def loadDB(name):
    return web.database(dbn="sqlite", db=os.path.join(USER_DATA_DIR,"{}.sqlite".format(name)))


class index: 
    def GET(self): 
        form = myform()

        print "hello"
        todos = db.select('todo')
        #return render.index('todo')
        return render.formtest(form)

    def POST(self): 
        form = myform() 
        if not form.validates(): 
            return render.formtest(form)
        else:

            return "Worked name: %s, pref1: %s, pref2: %s, pref3: %s, difficulty: %s, terrain: %s" % (form.d.name,form['pref1'].checked,form['pref2'].checked,form['pref3'].checked, form['difficulty'].value, form.d.terrain)

if __name__=="__main__":
    if not os.path.exists(USER_DATA_DIR) and not os.path.isdir(USER_DATA_DIR):
        os.mkdir(USER_DATA_DIR)
    if not os.path.exists(os.path.join(USER_DATA_DIR,"main.sqlite")):
        db = loadDB("main")

        db.query("CREATE TABLE PointType(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")


        #db.query("INSERT INTO PointType(name, icon) VALUES ('{}', x'{}')".format(n,d))

        # Points table represents knowledge about an area such as an eatery, a good sight or a rest spot.
        db.query("""CREATE TABLE Point(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, desc TEXT, lat NUMERIC, lon NUMERIC, type INTEGER REFERENCES pointType(id))""")

        # Route is just here to help maintain a list of routes
        db.query("""CREATE TABLE Route(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)""")

        # RoutePoint joins route and point together
        db.query("""CREATE TABLE RoutePoint(route_id INTEGER REFERENCES Route(id), point_id INTEGER REFERENCES Point(id), PRIMARY KEY (route_id, point_id))""")

        
    web.internalerror = web.debugerror
    app = web.application(urls, globals())
    app.run()
