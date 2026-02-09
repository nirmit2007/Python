units=[190,100,200,300,334,70,50,400,450,10,110]
#give 20 % discount if unit us above 200 else 10% disaocunt give  after discount list
#["171","90",160]....

new = [i//1.2 if i>200 else i//1.1 for i in units]
print(new)