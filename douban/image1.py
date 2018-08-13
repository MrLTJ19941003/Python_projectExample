class test:
    def remove_noise(slef,img,frame, window=1):
        """ 中值滤波移除噪点
        """
        if window == 1:
            # 十字窗口
            window_x = [1, 0, 0, -1, 0]
            window_y = [0, 1, 0, 0, -1]
        elif window == 2:
            # 3*3矩形窗口
            window_x = [-1, 0, 1, -1, 0, 1, 1, -1, 0]
            window_y = [-1, -1, -1, 1, 1, 1, 0, 0, 0]

        width, height = img.size
        for i in range(width):
            for j in range(height):
                box = []
                black_count, white_count = 0, 0
                for k in range(len(window_x)):
                    d_x = i + window_x[k]
                    d_y = j + window_y[k]
                    try:
                        d_point = frame[d_x, d_y]
                        if d_point == 0:#BLACK:
                            box.append(1)
                        else:
                            box.append(0)
                    except IndexError:
                        frame[i, j] = 255
                        continue
                box.sort()
                if len(box) == len(window_x):
                    mid = box[len(box) // 2]
                    if mid == 1:
                        frame[i, j] = 0#BLACK
                    else:
                        frame[i, j] = 255#WHITE