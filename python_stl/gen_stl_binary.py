import struct
import itertools

from . import util
from . import calc_stl

ut = util.UTIL()
cs = calc_stl.Calc_STL()


class GEN_STL_BINARY():


    def define_header(self, msg):
        ### str >> bytes
        msg_b = msg.encode("utf-8")
        b_header = struct.pack("80s", msg_b)
        return b_header
    

    def define_null(self):
        return struct.pack("2s", b"piko")


    def define_mesh_count(self, count):
        return struct.pack("i", int(count))


    def float3d_to_bin(self, float_3d):

        bb_0 = struct.pack("f", float(float_3d[0]))
        bb_1 = struct.pack("f", float(float_3d[1]))
        bb_2 = struct.pack("f", float(float_3d[2]))

        t = [bb_0, bb_1, bb_2]
        s = b"".join(t)
        
        return s


    def gen_stl_binary(self, mesh_name, pt3_list, export_path):

        export_bin = []

        ### header
        bin_header = self.define_header(mesh_name)
        export_bin.append(bin_header)

        ### count
        count = len(pt3_list)
        bin_count = self.define_mesh_count(count)
        export_bin.append(bin_count)


        ### meshes
        for i in range(count):

            vertex3 = pt3_list[i]
            n_vec = cs.face_normal(vertex3)

            t = [] 
        
            t.append(self.float3d_to_bin(n_vec))
            t.append(self.float3d_to_bin(vertex3[0]))
            t.append(self.float3d_to_bin(vertex3[1]))
            t.append(self.float3d_to_bin(vertex3[2]))
            t.append(self.define_null())

            s = b"".join(t)
            export_bin.append(s)
            
            del(vertex3)
        

        export_bin_join = b"".join(export_bin)


        ### Export
        with open(export_path, 'wb') as f:
            f.write(export_bin_join)


        print("Export (Binary) : {}".format(export_path))

