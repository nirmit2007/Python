def grade(func):
    def inner(name, **kwargs):
        # if no subjects → directly grade C
        if not kwargs:
            func(name, **kwargs)
            print(name, "gets grade C")
            return
        
        avg = sum(kwargs.values()) / len(kwargs)

        if avg >= 90:
            g = "A"
        elif avg >= 80:
            g = "B"
        elif avg >= 70:
            g = "C"
        else:
            g = "D"

        func(name, **kwargs)
        print(name, "gets grade", g)

    return inner


@grade
def grade_report(name, **kwargs):
    print("Calculating grade for", name)

grade_report("amit", maths=80, science=90, english=70)
grade_report("amit")