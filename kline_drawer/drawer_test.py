import pygame, sys
from points_util.pointers_getter import pointers_getter
from points_util.k_line_drawer import k_line_drawer
import cv2
import time

image = cv2.imread("d.jpg")
img_height = int(image.shape[0])
img_width = int(image.shape[1])
true_img_height = 100
true_img_width = int(img_width * 100 / img_height)
scale = 2

image = cv2.resize(image, (true_img_width, true_img_height))
img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
img_out = cv2.resize(img_gray, (true_img_width * scale, true_img_height * scale))
cv2.imwrite("temp.jpg", img_out)
background = pygame.image.load("temp.jpg")
pg = pointers_getter(80, img_gray)
pg.get_all_pointers()
# print([str(a) for a in pg.all_k_lines_list])
print(len(pg.all_k_lines_list))
pygame.init()

screen = pygame.display.set_mode([true_img_width * scale, true_img_height * scale])
screen.blit(background, (0, 0))

# screen.fill([255, 255, 255])  # fill screen with white
k_line_index = 0
last_point = (0, 0)
last_y_point = 0
lasy_k_line_y_point = 0
thick_line_width = pg.step * scale
thin_line_width = 1 * scale
up_color = 0, 255, 0
down_color = 255, 0, 0
background_color = 255, 255, 255
for each_k_line in pg.all_k_lines_list:
    # each_k_line = k_line_drawer()  # TODO
    x_axis = k_line_index * thick_line_width
    up = lasy_k_line_y_point
    down = lasy_k_line_y_point
    for index, each_y_point in enumerate(each_k_line.point_gen):
        # print(index, each_y_point)
        each_y_point *= scale
        pygame.draw.line(screen, background_color,
                         (x_axis, lasy_k_line_y_point),
                         (x_axis, up), thick_line_width)
        pygame.draw.line(screen, up_color,
                         (x_axis, lasy_k_line_y_point),
                         (x_axis, up), thin_line_width)
        pygame.draw.line(screen, background_color,
                         (x_axis, lasy_k_line_y_point),
                         (x_axis, down), thick_line_width)
        pygame.draw.line(screen, down_color,
                         (x_axis, lasy_k_line_y_point),
                         (x_axis, down), thin_line_width)
        if each_y_point > lasy_k_line_y_point:
            pygame.draw.line(screen, up_color,
                             (x_axis, lasy_k_line_y_point),
                             (x_axis, each_y_point), thick_line_width)
        else:
            pygame.draw.line(screen, down_color,
                             (x_axis, lasy_k_line_y_point),
                             (x_axis, each_y_point), thick_line_width)
        if each_y_point > up:
            up = each_y_point
        if each_y_point < down:
            down = each_y_point

        last_y_point = each_y_point
        time.sleep(0.05)
        pygame.display.flip()
    lasy_k_line_y_point = last_y_point
    k_line_index += 1
