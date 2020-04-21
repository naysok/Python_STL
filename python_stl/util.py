import datetime
import math
import random


class UTIL():


    def get_current_time(self):
        return str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))


    def remap_number(self, src, old_min, old_max, new_min, new_max):
        return ((src - old_min) / (old_max - old_min) * (new_max - new_min) + new_min)


    def test_generate_grid(self, u, v):
        pts = []
        for i in range(u):
            sub = []
            for j in range(v):
                x = j
                y = i
                z = random.random() * 2
                sub.append((x,y,z))
            pts.append(sub)
        return pts


    def test_grid_to_3pt3pt(self, u, v):
        grid = self.test_generate_grid(u, v)

        pt3s = []

        for i in range(len(grid) - 1):
            for j in range(len(grid[i]) - 1):
                
                p0 = grid[i][j]
                p1 = grid[i][j+1]
                p2 = grid[i+1][j+1]
                p3 = grid[i+1][j]

                pt3_a = [p0, p1, p2]
                pt3_b = [p0, p2, p3]

                pt3s.append(pt3_a)
                pt3s.append(pt3_b)
        
        return pt3s
