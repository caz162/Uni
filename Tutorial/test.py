import web, os
import sqlite3
from web import form

USER_DATA_DIR = "userData"
render = web.template.render('templates/')


urls = ('/', 'index',
        '/count', 'count',
        '/trackPieceAdd', 'trackPieceAdd',
        '/routeAdd', 'routeAdd'
        )


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


def generate():
    potential = db.select('TrackPiece')
    

db=loadDB("main")
#pointTypes = db.select("PointType").list()

class count:
    def GET(self):
        form = myform()
        print "Pieces: " +  str(db.query("SELECT count(*) FROM TrackPiece").list())
        print "Routes: " +  str(db.query("SELECT count(*) FROM Route").list())
        return render.formtest(form)
    
        
class trackPieceAdd:
    def GET(self):
        print db.query("SELECT * FROM TrackPiece").list()
    def POST(self):
        db.insert("TrackPiece",name=form.d.name, difficulty=form.d.difficulty, terrain=form.d.terrain)



class routeAdd:
    def GET(self):
        print db.query("SELECT * FROM Route").list()
    def POST(self):
        db.insert("Route", name=form.d.name)

    

class index: 
    def GET(self): 
        form = myform()

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


        db.query("""CREATE TABLE Route(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)""")
        
        db.query("""CREATE TABLE TrackPiece(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, startPointLat REAL, startPointLon REAL, endPointLat REAL, endPointlon REAL, difficulty TEXT, terrain TEXT )""")


    web.internalerror = web.debugerror
    app = web.application(urls, globals())
    app.run()
