def data(name,age,salary):
    print("name : ",name)
    print("age : ",age)
    print("salary : ",salary)

data("nirmit",18,1000000000000000000000000000000)

#named param argumen....

#getUserData(age=23,name="amit",salary=67000)
#getUserData(age=23,name="amit",23000) #error
#getUserData(age=23,name="amit",age=24) #error  keyword argument repeated: age
#getUserData(23,name="amit",salary=34500)
#getUserData(23,"ok",salary=34500) error...
