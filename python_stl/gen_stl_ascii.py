import itertools

from . import util
from . import calc_stl

ut = util.UTIL()
cs = calc_stl.Calc_STL()


class GEN_STL_ASCII():


    def pt2stl_vec(self, vector):
        return "facet normal " + str(vector[0]) + " " + str(vector[1]) + " " + str(vector[2])


    def pt2stl_pt(self, point):
        return "vertex " + str(point[0]) + " " + str(point[1]) + " " + str(point[2])


    def format_stl(self, meshes):
        formated = []

        header = "solid nameee"
        formated.append(header)

        for flatten in range(len(meshes)):
            formated.append(meshes[flatten])

        footer = "endsolid nameee"
        formated.append(footer)

        return formated


    def stl_3pt(self, pt3):

        stl = []

        ### calc normal vector
        va = cs.face_normal(pt3)

        stl.append(self.pt2stl_vec(va))
        stl.append("outer loop")
        stl.append(self.pt2stl_pt(pt3[0]))
        stl.append(self.pt2stl_pt(pt3[1]))
        stl.append(self.pt2stl_pt(pt3[2]))
        stl.append("endloop")
        stl.append("endfacet")

        return stl


    def gen_stl_ascii(self, pt3_list, export_path):

        meshes = []

        for num in range(len(pt3_list)):

            # print(num)

            m = self.stl_3pt(pt3_list[num])
            meshes.append(m)


        ### Flatten
        meshes = list(itertools.chain.from_iterable(meshes))
        # print(meshes)

        export = self.format_stl(meshes)

        ### Export File
        with open(export_path, mode='w') as f:
            f.write('\n'.join(export))
    
        print("Export (Ascii) : {}".format(export_path))

