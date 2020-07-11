data = '1234567833333333123456789abc000031313131'
'''1234 5678 3333 3333 1234 5678 9abc 0000 3131 3131'''

angle_data = data[0:8]
angle_data_direction = data[8:16]

corner_data = data[16:28]
corner_data_direction = data[28:31]

print(angle_data)
print(angle_data_direction)

print(corner_data)
print(corner_data_direction)

block = '▩'

# orange
print("\033[31m{}\033[0m".format(block))

# red
print("\033[35m{}\033[0m".format(block))

# green
print("\033[32m{}\033[0m".format(block))

# blue
print("\033[34m{}\033[0m".format(block))

# white
print("\033[37m{}\033[0m".format(block))

# yellow
print("\033[33m{}\033[0m".format(block))

# print(block)

# 颜色不太够，凑合用吧，35当红色好了，31当作橙色

ORANGE = 31
RED = 35
GREEN = 32
BLUE = 34
WHITE = 37
YELLOW = 33

LEVEL_HIGH = 3
LEVEL_MID = 2
LEVEL_LOW = 1


# 这里似乎是棱块的，角块的坐标系不同
# def get_level(color):
#     if color == ORANGE or color == RED:
#         return LEVEL_HIGH
#
#     if color == WHITE or color == YELLOW:
#         return LEVEL_MID
#
#     if color == BLUE or color == GREEN:
#         return LEVEL_LOW
def get_angle_color_level(color):
    if color == BLUE or color == GREEN:
        return LEVEL_HIGH

    if color == ORANGE or color == RED:
        return LEVEL_MID

    if color == WHITE or color == YELLOW:
        return LEVEL_LOW


def get_edges_color_level(color):
    if color == ORANGE or color == RED:
        return LEVEL_HIGH

    if color == WHITE or color == YELLOW:
        return LEVEL_MID

    if color == BLUE or color == GREEN:
        return LEVEL_LOW


def get_max_level_color(color1, color2, color3):
    center_color1_level = get_angle_color_level(color1)
    center_color2_level = get_angle_color_level(color2)
    center_color3_level = get_angle_color_level(color3)

    if center_color1_level > center_color2_level and center_color1_level > center_color3_level:
        return color1

    if center_color2_level > center_color1_level and center_color2_level > center_color3_level:
        return color2

    if center_color3_level > center_color1_level and center_color3_level > center_color2_level:
        return color3


# 基本思路使用快来标示数据

class edge_block_color:
    def __init__(self, color1, color2):
        self.color1 = color1
        self.color2 = color2


class angle_block_color:
    # def __init__(self, color_main, color_left, color_right):
    #     self.color_main = color_main
    #     self.color_left = color_left
    #     self.color_right = color_right
    def __init__(self, color1, color2, color3):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3


def edge_poistion_max_color_level(position):
    '''
    绿黄 1
    绿红 2
    绿白 3
    橙绿 4
    红黄 5
    红白 6
    橙白 7
    橙黄 8
    蓝黄 9
    蓝红 a
    蓝白 b
    橙蓝 c
    '''

    if position == 1:
        return LEVEL_MID
    if position == 2:
        return LEVEL_HIGH
    if position == 3:
        return LEVEL_MID
    if position == 4:
        return LEVEL_HIGH
    if position == 5:
        return LEVEL_HIGH
    if position == 6:
        return LEVEL_HIGH
    if position == 7:
        return LEVEL_HIGH
    if position == 8:
        return LEVEL_HIGH
    if position == 9:
        return LEVEL_MID
    if position == 10:
        return LEVEL_HIGH
    if position == 11:
        return LEVEL_MID
    if position == 12:
        return LEVEL_HIGH

    pass


def init_edge_data(edge_index):
    '''
    高级色 橙色 红色
    中级色 白色 黄色
    低级色 蓝色 绿色

    绿黄 1
    绿红 2
    绿白 3
    橙绿 4
    红黄 5
    红白 6
    橙白 7
    橙黄 8
    蓝黄 9
    蓝红 a
    蓝白 b
    橙蓝 c
    '''

    if edge_index == '1':
        return edge_block_color(YELLOW, GREEN)
    if edge_index == '2':
        return edge_block_color(RED, GREEN)
    if edge_index == '3':
        return edge_block_color(WHITE, GREEN)
    if edge_index == '4':
        return edge_block_color(ORANGE, GREEN)
    if edge_index == '5':
        return edge_block_color(RED, YELLOW)
    if edge_index == '6':
        return edge_block_color(RED, WHITE)
    if edge_index == '7':
        return edge_block_color(ORANGE, WHITE)
    if edge_index == '8':
        return edge_block_color(ORANGE, YELLOW)
    if edge_index == '9':
        return edge_block_color(YELLOW, BLUE)
    if edge_index == 'a':
        return edge_block_color(RED, BLUE)
    if edge_index == 'b':
        return edge_block_color(WHITE, BLUE)
    if edge_index == 'c':
        return edge_block_color(ORANGE, BLUE)


def init_angle_data(angle_index):
    '''
    黄绿红 1
    红绿白 2
    白橙绿 3
    黄绿橙 4
    黄蓝红 5
    红蓝白 6
    白橙蓝 7
    黄蓝橙 8
    '''

    # 目前内部顺时针逆时针数据未定，可能也不需要吧，不好说

    if angle_index == 1:
        # return angle_block_color(GREEN, RED, YELLOW)
        return angle_block_color(GREEN, RED, YELLOW)
    elif angle_index == 2:
        return angle_block_color(GREEN, RED, WHITE)
    elif angle_index == 3:
        # return angle_block_color(GREEN, ORANGE, WHITE)
        return angle_block_color(GREEN, ORANGE, WHITE)
    elif angle_index == 4:
        return angle_block_color(GREEN, ORANGE, YELLOW)
    elif angle_index == 5:
        return angle_block_color(BLUE, RED, YELLOW)
    elif angle_index == 6:
        # return angle_block_color(BLUE, RED, WHITE)
        return angle_block_color(BLUE, RED, WHITE)
    elif angle_index == 7:
        return angle_block_color(BLUE, ORANGE, WHITE)
    elif angle_index == 8:
        return angle_block_color(BLUE, ORANGE, YELLOW)
    # return angle_block_color(BLUE, ORANGE, YELLOW)

    # if angle_index == 1:
    #     # return angle_block_color(GREEN, RED, YELLOW)
    #     return angle_block_color(GREEN, YELLOW, RED)
    # elif angle_index == 2:
    #     return angle_block_color(GREEN, RED, WHITE)
    # elif angle_index == 3:
    #     # return angle_block_color(GREEN, ORANGE, WHITE)
    #     return angle_block_color(GREEN, WHITE, ORANGE)
    # elif angle_index == 4:
    #     return angle_block_color(GREEN, ORANGE, YELLOW)
    # elif angle_index == 5:
    #     return angle_block_color(BLUE, RED, YELLOW)
    # elif angle_index == 6:
    #     # return angle_block_color(BLUE, RED, WHITE)
    #     return angle_block_color(BLUE, WHITE, RED)
    # elif angle_index == 7:
    #     return angle_block_color(BLUE, ORANGE, WHITE)
    # elif angle_index == 8:
    #     return angle_block_color(BLUE, YELLOW, ORANGE)


def get_edge_color(block_index, position, edge_data_direction, center_color):
    edge_block = init_edge_data(block_index)

    center_color_level = get_edges_color_level(center_color)

    higher_color_level = get_edges_color_level(edge_block.color1)
    position_max_color_level = edge_poistion_max_color_level(position)

    '''
    高级色 橙色 红色
    中级色 白色 黄色
    低级色 蓝色 绿色
    '''

    if edge_data_direction == '0':
        if center_color_level == LEVEL_HIGH:
            return edge_block.color1
        if center_color_level == LEVEL_MID:
            if position_max_color_level == LEVEL_MID:
                return edge_block.color1
            else:
                return edge_block.color2
                # if higher_color_level == LEVEL_MID or higher_color_level == LEVEL_HIGH:
                #     return edge_block.color2
                # else:
                #     return edge_block.color1
        if center_color_level == LEVEL_LOW:
            return edge_block.color2
    else:
        if center_color_level == LEVEL_HIGH:
            return edge_block.color2
        if center_color_level == LEVEL_MID:
            if position_max_color_level == LEVEL_MID:
            #if higher_color_level == LEVEL_MID:  # or higher_color_level == LEVEL_HIGH:
                return edge_block.color2
            else:
                return edge_block.color1
        if center_color_level == LEVEL_LOW:
            return edge_block.color1


def get_angle_color(block_index, position_index, angle_data_direction, center_color):
    # angle_high_level_plane_color = get_max_level_color(angle_block_color_obj.color1, angle_block_color_obj.color2,
    #                                                    angle_block_color_obj.color3)
    block_index = int(block_index)
    angle_block = init_angle_data(block_index)
    direction = int(angle_data_direction)

    center_color_level = get_angle_color_level(center_color)

    same_plane = False
    if (position_index <= 4 and block_index >= 5) or (position_index >= 5 and block_index <= 4):
        # if abs(position_index - int_block_index) <= 3:
        index_right = (position_index + 1) % 2 == block_index % 2
    else:
        index_right = position_index % 2 == block_index % 2
        same_plane = True

    if direction == 3:
        if index_right:
            if center_color_level == LEVEL_HIGH:
                return angle_block.color1
            if center_color_level == LEVEL_MID:
                return angle_block.color2
            if center_color_level == LEVEL_LOW:
                return angle_block.color3

        if same_plane:
            if center_color_level == LEVEL_HIGH:
                return angle_block.color1
            if center_color_level == LEVEL_MID:
                return angle_block.color3
            if center_color_level == LEVEL_LOW:
                return angle_block.color2
        else:
            if center_color_level == LEVEL_HIGH:
                return angle_block.color1
            if center_color_level == LEVEL_MID:
                return angle_block.color3
            if center_color_level == LEVEL_LOW:
                return angle_block.color2

    if direction == 2:
        if index_right:
            if center_color_level == LEVEL_HIGH:
                return angle_block.color3
            if center_color_level == LEVEL_MID:
                return angle_block.color1
            if center_color_level == LEVEL_LOW:
                return angle_block.color2
        if same_plane:
            if center_color_level == LEVEL_HIGH:
                return angle_block.color2
            if center_color_level == LEVEL_MID:
                return angle_block.color1
            if center_color_level == LEVEL_LOW:
                return angle_block.color3
        else:
            if center_color_level == LEVEL_HIGH:
                return angle_block.color2
            if center_color_level == LEVEL_MID:
                return angle_block.color1
            if center_color_level == LEVEL_LOW:
                return angle_block.color3

    if direction == 1:
        if index_right:
            if center_color_level == LEVEL_HIGH:
                return angle_block.color2
            if center_color_level == LEVEL_MID:
                return angle_block.color3
            if center_color_level == LEVEL_LOW:
                return angle_block.color1
        if same_plane:
            if center_color_level == LEVEL_HIGH:
                return angle_block.color3
            if center_color_level == LEVEL_MID:
                return angle_block.color2
            if center_color_level == LEVEL_LOW:
                return angle_block.color1
        else:
            if center_color_level == LEVEL_HIGH:
                return angle_block.color3
            if center_color_level == LEVEL_MID:
                return angle_block.color2
            if center_color_level == LEVEL_LOW:
                return angle_block.color1


def set_data(data):
    print(data)
    # 整体采用这样的坐标系 第一个块为 block_1_1,最后一个块为 block_9_1
    # ▩ ▩ ▩
    # ▩ ▩ ▩
    # ▩ ▩ ▩
    # ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩
    # ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩
    # ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩ ▩
    # ▩ ▩ ▩
    # ▩ ▩ ▩
    # ▩ ▩ ▩

    angle_data = data[0:8]
    angle_data_direction = data[8:16]

    corner_data = data[16:28]
    corner_data_direction = data[28:31]
    # print(corner_data_direction)
    corner_data_direction = str('{:04b}'.format(int(corner_data_direction[0],16))) + str(
        '{:04b}'.format(int(corner_data_direction[1],16))) + str('{:04b}'.format(int(corner_data_direction[2],16)))

    # print(corner_data_direction)
    # 棱快
    block_1_2 = get_edge_color(corner_data[11], 12, corner_data_direction[11], ORANGE)
    block_2_1 = get_edge_color(corner_data[7], 8, corner_data_direction[7], ORANGE)
    block_2_3 = get_edge_color(corner_data[6], 7, corner_data_direction[6], ORANGE)
    block_3_2 = get_edge_color(corner_data[3], 4, corner_data_direction[3], ORANGE)

    block_4_2 = get_edge_color(corner_data[3], 4, corner_data_direction[3], GREEN)
    block_4_5 = get_edge_color(corner_data[6], 7, corner_data_direction[6], WHITE)
    block_4_8 = get_edge_color(corner_data[11], 12, corner_data_direction[11], BLUE)
    block_4_11 = get_edge_color(corner_data[7], 8, corner_data_direction[7], YELLOW)

    block_5_1 = get_edge_color(corner_data[0], 1, corner_data_direction[0], GREEN)
    block_5_3 = get_edge_color(corner_data[2], 3, corner_data_direction[2], GREEN)
    block_5_4 = get_edge_color(corner_data[2], 3, corner_data_direction[2], WHITE)
    block_5_6 = get_edge_color(corner_data[10], 11, corner_data_direction[10], WHITE)
    block_5_7 = get_edge_color(corner_data[10], 11, corner_data_direction[10], BLUE)
    block_5_9 = get_edge_color(corner_data[8], 9, corner_data_direction[8], BLUE)
    block_5_10 = get_edge_color(corner_data[8], 9, corner_data_direction[8], YELLOW)
    block_5_12 = get_edge_color(corner_data[0], 1, corner_data_direction[0], YELLOW)

    block_6_2 = get_edge_color(corner_data[1], 2, corner_data_direction[1], GREEN)
    block_6_5 = get_edge_color(corner_data[5], 6, corner_data_direction[5], WHITE)
    block_6_8 = get_edge_color(corner_data[9], 10, corner_data_direction[9], BLUE)
    block_6_11 = get_edge_color(corner_data[4], 5, corner_data_direction[4], YELLOW)

    block_7_2 = get_edge_color(corner_data[1], 2, corner_data_direction[1], RED)
    block_8_1 = get_edge_color(corner_data[4], 5, corner_data_direction[4], RED)
    block_8_3 = get_edge_color(corner_data[5], 6, corner_data_direction[5], RED)
    block_9_2 = get_edge_color(corner_data[9], 10, corner_data_direction[9], RED)

    # 角块
    block_1_1 = get_angle_color(angle_data[7], 8, angle_data_direction[7], ORANGE)
    block_1_3 = get_angle_color(angle_data[6], 7, angle_data_direction[6], ORANGE)

    block_3_1 = get_angle_color(angle_data[3], 4, angle_data_direction[3], ORANGE)
    block_3_3 = get_angle_color(angle_data[2], 3, angle_data_direction[2], ORANGE)

    block_4_1 = get_angle_color(angle_data[3], 4, angle_data_direction[3], GREEN)
    block_4_3 = get_angle_color(angle_data[2], 3, angle_data_direction[2], GREEN)

    block_4_4 = get_angle_color(angle_data[2], 3, angle_data_direction[2], WHITE)
    block_4_6 = get_angle_color(angle_data[6], 7, angle_data_direction[6], WHITE)

    block_4_7 = get_angle_color(angle_data[6], 7, angle_data_direction[6], BLUE)
    block_4_9 = get_angle_color(angle_data[7], 8, angle_data_direction[7], BLUE)

    block_4_10 = get_angle_color(angle_data[7], 8, angle_data_direction[7], YELLOW)
    block_4_12 = get_angle_color(angle_data[3], 4, angle_data_direction[3], YELLOW)

    block_6_1 = get_angle_color(angle_data[0], 1, angle_data_direction[0], GREEN)
    block_6_3 = get_angle_color(angle_data[1], 2, angle_data_direction[1], GREEN)

    block_6_4 = get_angle_color(angle_data[1], 2, angle_data_direction[1], WHITE)
    block_6_6 = get_angle_color(angle_data[5], 6, angle_data_direction[5], WHITE)

    block_6_7 = get_angle_color(angle_data[5], 6, angle_data_direction[5], BLUE)
    block_6_9 = get_angle_color(angle_data[4], 5, angle_data_direction[4], BLUE)

    block_6_10 = get_angle_color(angle_data[4], 5, angle_data_direction[4], YELLOW)
    block_6_12 = get_angle_color(angle_data[0], 1, angle_data_direction[0], YELLOW)

    block_7_1 = get_angle_color(angle_data[0], 1, angle_data_direction[0], RED)
    block_7_3 = get_angle_color(angle_data[1], 2, angle_data_direction[1], RED)

    block_9_1 = get_angle_color(angle_data[4], 5, angle_data_direction[4], RED)
    block_9_3 = get_angle_color(angle_data[5], 6, angle_data_direction[5], RED)

    print("\033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m ".format(block_1_1, block_1_2, block_1_3))
    print("\033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m ".format(block_2_1, ORANGE, block_2_3))
    print("\033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m ".format(block_3_1, block_3_2, block_3_3))

    print(
        "\033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m ".format(
            block_4_1, block_4_2, block_4_3, block_4_4, block_4_5, block_4_6, block_4_7, block_4_8, block_4_9,
            block_4_10, block_4_11,
            block_4_12))
    print(
        "\033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m ".format(
            block_5_1, GREEN, block_5_3, block_5_4, WHITE, block_5_6, block_5_7, BLUE, block_5_9, block_5_10, YELLOW,
            block_5_12))
    print(
        "\033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m ".format(
            block_6_1, block_6_2, block_6_3, block_6_4, block_6_5, block_6_6, block_6_7, block_6_8, block_6_9,
            block_6_10, block_6_11,
            block_6_12))

    print("\033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m ".format(block_7_1, block_7_2, block_7_3))
    print("\033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m ".format(block_8_1, RED, block_8_3))
    print("\033[{}m▩\033[0m \033[{}m▩\033[0m \033[{}m▩\033[0m ".format(block_9_1, block_9_2, block_9_3))


set_data('1273568433113311123756c49ab8000031535133')
print('-----')
set_data('123485673333333312345678c9ab000011131123')
print('-----')
set_data('1234567833333333123456789abc000041414141')
print('-----')
set_data('1287564333333333123c56879ab4000033333131')
print('-----')
set_data('162457383223322312645b389a7c262041313133')
print('-----')
set_data('4238167523322332382416795abc498021232163')
print('-----')
set_data('4378126522222222387412b95a6c6fa043313321')
