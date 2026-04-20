def getFullName(**kwargs):
    
    def find():
        #return kwargs['name'].lower() + "-" + kwargs['lname'].lower()
        return "-".join(list(kwargs.values())) 
    
    return find()

fullName = getFullName(name="MahendraSingh", lname="Dhoni")
print(fullName)