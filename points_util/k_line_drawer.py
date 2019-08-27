import random


class k_line_drawer:
    def __init__(self, vir_down, true_down, true_up, vir_up, is_start_from_up, ticks):
        assert vir_down <= true_down <= true_up <= vir_up

        self.vir_up = vir_up
        self.vir_down = vir_down
        self.true_up = true_up
        self.true_down = true_down
        self.is_start_from_up = is_start_from_up
        self.ticks = ticks
        self.point_gen = self.get_points()

    def get_virtual_tops_show_time(self):
        t = self.ticks - 2
        virtual_point_down_time = 0
        virtual_point_up_time = random.randint(0, t - 1)  # 0,1,2,...t-1
        down_temp = random.randint(0, t - 2)  # 0,1,2..t-2
        choose = 0
        for i in range(t):
            if i == virtual_point_up_time:
                continue
            elif choose == down_temp:
                virtual_point_down_time = i
            choose += 1
        assert virtual_point_up_time != virtual_point_down_time
        return virtual_point_up_time + 1, virtual_point_down_time + 1

    def get_points(self):
        tick = 0
        # 第0个tick是true,第n个tick是true
        virtual_point_up_time, virtual_point_down_time = self.get_virtual_tops_show_time()
        while tick < self.ticks:
            if tick == 0:
                yield self.true_up if self.is_start_from_up else self.true_down
            elif tick == self.ticks - 1:
                yield self.true_down if self.is_start_from_up else self.true_up
            elif tick == virtual_point_down_time:
                yield self.vir_down
            elif tick == virtual_point_up_time:
                yield self.vir_up
            else:
                yield random.randint(self.vir_down, self.vir_up)
            tick += 1

    def __str__(self):
        ret = "vir_down:" + str(self.vir_down) + "," + "true_down:" + str(self.true_down) + "," + "true_up:" + str(
            self.true_up) + "," + "vir_up:" + str(self.vir_up)
        return ret


if __name__ == '__main__':
    d = k_line_drawer(60, 30, 40, 35, True, 6)
    for each in d.point_gen:
        print(each)
