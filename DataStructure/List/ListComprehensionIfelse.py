names = ["ram","shyam","amit","sumit","geeta","jaya","rama"]
inm = ['yes' if i.endswith('m') else 'no' for i in names]
print(inm)

filtUsers2 = ["yes" if i == i[::-1] else "No" for i in names]
print(filtUsers2)

numbers = [-100,100,0,20,0,-90,98,97,67,-32]
n2 = ["+" if i>0 else ("0" if i ==0 else "-") for i in numbers]
print(n2)