import math


from . import util, transform

ut = util.UTIL()
tr = transform.Transform()


class Calc_STL():
    
    
    def face_normal(self, pt3):
        va = tr.pt_pt_subtract(pt3[1], pt3[0])
        vb = tr.pt_pt_subtract(pt3[2], pt3[0])
        
        # ベクトル同士の外積
        n0 = va[1] * vb[2] - va[2] * vb[1]
        n1 = va[2] * vb[0] - va[0] * vb[2]
        n2 = va[0] * vb[1] - va[1] * vb[0]

        vec_u = tr.vector_unitize([n0, n1, n2])

        return vec_u
