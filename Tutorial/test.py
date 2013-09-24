import web
from web import form

render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form( 
    form.Textbox("name"), 
    form.Textbox("id", 
        form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        form.Validator('Must be more than 5', lambda x:int(x)>5)),
    form.Textarea('occupation'),
    form.Checkbox('dead'), 
    form.Dropdown('french', ['mustard', 'fries', 'wine']),
    form.Textbox("name2"))

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
            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.
            return "Grrreat success! boe: %s, bax: %s, french: %s" % (form.d.name, form['id'].value, form.d.french)

if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
