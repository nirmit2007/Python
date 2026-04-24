import numpy as np

fir = np.ones((5,5), dtype=int)
# print(fir)

sec = np.zeros((3,3), dtype=int)
sec[1,1] = 9
# print(sec)

fir[1:4,1:4] = sec
# print(fir)

fir[2, :] = 4
fir[:, 2] = 4

fir[[0,2,4,2],[2,0,2,4]]= 1
print(fir)

sub_arr = fir[1:4,1:4]
#print(sub_arr)

sub_arr[[0,0,2,2],[0,2,0,2]] = 0
print(sub_arr)