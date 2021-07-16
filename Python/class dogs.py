class dog :
    def __init__(self,owner,breed) :
        self.owner=owner
        self.breed=breed
        self.name=[]
    def add_name(self,name) :
        self.name.append(name)
d=dog(input('enter the owners name'),input('enter the breed name'))

      
