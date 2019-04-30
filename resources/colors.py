

class Colors():

    @staticmethod
    def get(color):
        return {
            'black': (0, 0, 0),
            'lawn': (86, 176, 0),
            'fairway': (90, 215, 85),
            'flag': (255, 215, 0),
            'green': (0, 169, 0),
            'green_fringe': (36, 168, 33),
            'green_rough': (75, 210, 70),
            'heavy_rough': (0, 99, 3),
            'light_rough': (0, 170, 3),
            'sand': (250, 180, 0),
            'tee_area': (90, 215, 85),
            'tree': (34, 139, 34),
            'water': (30, 190, 250),
            'white': (255, 255, 255)
        }.get(color)

