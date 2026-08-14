class greeter:
    def __init__(self,name):
        self.name=name
    def greet(self,loud=False):
        if loud:
            print('HELLO,%s!'%self.name.upper())
        else:
            print('hello,%s'%self.name)
g=greeter('fred')
g.greet()
g.greet(loud=True)
