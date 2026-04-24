def admission(func):
    def inner(name, **kwargs):
        if "age" not in kwargs or "course" not in kwargs:
            print("Missing required details for", name)
            return

        if kwargs["age"] >= 18 and kwargs["course"] == "CS":
            return func(name, **kwargs)
        else:
            print("Nai Med pde lala..!!")
    return inner

@admission
def apply(name, **kwargs):
    print("Admission is Open For", name)

apply("raj", age=19, course="IT")      # invalid (course not CS)
apply("parth", age=16, course="CS")    # invalid (age <18)
apply("jay", course="IT")              # missing age
apply("amit")                          # missing both
apply("kunal", age=22)                 # missing course
apply("rohit", age=20, course="CS")    # valid
