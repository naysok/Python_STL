import time
from python_stl import gen_stl_ascii, gen_stl_binary, util


gsa = gen_stl_ascii.GEN_STL_ASCII()
gsb = gen_stl_binary.GEN_STL_BINARY()
ut = util.UTIL()




### =============== Case 1 ===============
# p0 = [0, 0, 0]
# p1 = [1, 0, 0]
# p2 = [1, 1, 4]
# p3 = [0, 1, 0]

# pts = [[p0, p1, p3], [p1, p2, p3]]
### =============== Case 1 ===============


### =============== Case 2 ===============
pts = ut.test_grid_to_3pt3pt(100, 200)
### =============== Case 2 ===============




time1 = time.time()


### Ascii
# path_current_time = "./STL/" + ut.get_current_time() + ".stl"
# gsa.gen_stl_ascii(pts, path_current_time)
### Ascii



### Binary
path_current_time = "./STL/" + ut.get_current_time() + ".stl"
gsb.gen_stl_binary("bin_stl_test", pts, path_current_time)
### Binary


time2 = time.time()
print("time : {} sec".format(time2 - time1))