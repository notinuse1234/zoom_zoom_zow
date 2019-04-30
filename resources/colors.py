

class Colors():

    @staticmethod
    def get(color):
        return {
            'black': (0, 0, 0),
            'lawn': (86, 176, 0),
            'fairway': (90, 215, 85),
            'flag': (190, 80, 0),
            'green': (0, 169, 0),
            'green_fringe': (36, 168, 33),
            'green_rough': (75, 210, 70),
            'heavy_rough': (0, 99, 3),
            'light_rough': (0, 170, 3),
            'tee_area': (90, 215, 85),
            'tree': (0, 45, 3),
            'white': (255, 255, 255)
        }.get(color)

