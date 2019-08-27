import cv2
import numpy as np
from points_util.k_line_drawer import k_line_drawer
import random


# image = cv2.imread("a.png")
# image = cv2.resize(image, (100, 100))
# img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# this_row = img_gray[:, 55]  # 这一列
# index_diff = np.where(np.diff(this_row) != 0)[0]
# cv2.imshow("fgh", img_gray)
# cv2.waitKey(0)


class pointers_getter:
    def __init__(self, k_line_amount, img):
        self.all_k_lines_list = []
        self.k_line_amout = k_line_amount

        self.img = img
        self.height = int(self.img.shape[0])
        self.width = int(self.img.shape[1])

        self.step = int(self.width / self.k_line_amout)
        print(self.width, self.height, self.step)

    def get_all_pointers(self):
        last_end = 0
        for i in range(0, self.width, self.step):
            this_row = self.img[:, i]  # 这一列
            print(len(this_row))
            index_diff = list(np.where(np.diff(this_row) != 0)[0])
            if 0 in index_diff:
                index_diff.pop(0)
            if self.height - 1 in index_diff:
                index_diff.pop(self.height - 1)

            # if len(index_diff) == 2:
            #     assert index_diff[0] < index_diff[-1]
            #     print(index_diff)
            #     a = random.randint(0, index_diff[0] - 1)
            #     b = index_diff[0]
            #     c = random.randint(index_diff[0], index_diff[-1])
            #     d = index_diff[-1]
            #     print("2", a, b, c, d)
            #     new_point = k_line_drawer(a, b, c, d, i % 2, 7)
            if len(index_diff) >= 2:
                assert index_diff[0] < index_diff[-1]
                print(index_diff)
                a = index_diff[0]

                c = index_diff[-1]
                b = random.randint(a, c - 1)
                d = random.randint(c, self.height - 1)

                print(">2", a, b, c, d)
                new_point = k_line_drawer(a, b, c, d, i % 2, 7)
            else:
                # x = random.sample(range(0, self.height), 4)  # 一次性取出两个不相同的随机数,但它的柱子长度很短
                dir = random.randint(0, 1)
                a = last_end - random.randint(1, 4) if dir == 0 else last_end + random.randint(1, 4)
                d = a + random.randint(1, 4)
                x = random.sample((a, d), 2)
                x.sort()
                b, c = x
                # b = b if b > 1 else 1
                # c = c if c < self.height - 1 else self.height - 1
                # a = random.randint(0, b - 1)
                # d = random.randint(c, self.height - 1)

                print("0", a, b, c, d)
                new_point = k_line_drawer(a, b, c, d, i % 2, 7)
            last_end = b if i % 2 else c
            self.all_k_lines_list.append(new_point)


if __name__ == '__main__':
    image = cv2.imread("a.png")
    image = cv2.resize(image, (100, 100))
    img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    pg = pointers_getter(10, img_gray)
    pg.get_all_pointers()
    print([str(a) for a in pg.all_k_lines_list])
