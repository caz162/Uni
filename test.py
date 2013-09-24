import web
          
urls = ('/working/(.*)', 'working',
        '/(.*)', 'hello')

app = web.application(urls, globals())
  
class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

class working:
    def GET(self, name):
        if not name:
            name = 'This'
        return name + ' Sucks' +'!'    
  
if __name__ == "__main__":
    app.run()
