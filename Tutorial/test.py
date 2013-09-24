import web, os
from web import form


render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form( 
    form.Textbox("name"), 
    form.Textarea('description'),
    form.Checkbox('pref1',value="some value"),
    form.Checkbox('pref2',value="some value"),
    form.Checkbox('pref3',value="some value"), 
    form.Dropdown('difficulty', ['All_Mountain', 'All_Mountain_Plus', 'XC']),
    form.Dropdown('terrain', ['Rock', 'Grass', 'Road']))

class index: 
    def GET(self): 
        form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        return render.formtest(form)

    def POST(self): 
        form = myform() 
        if not form.validates(): 
            return render.formtest(form)
        else:
            os.system("dir")
            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.
            return "Worked name: %s, pref1: %s, pref2: %s, pref3: %s, difficulty: %s, terrain: %s" % (form.d.name,form['pref1'].checked,form['pref2'].checked,form['pref3'].checked, form['difficulty'].value, form.d.terrain)

if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
