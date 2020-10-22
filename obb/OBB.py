class OBB():

    def __init__(self, data):

        self.data = list()
        for point in data:
            if len(point) != 3:
                raise RuntimeError("A point must have the format (X,Y,Z)")
            self.data.append(point)

    def get(self):
        width = 0
        height = 0
        depth = 0
        trafo = [None]

        return (width, height, depth, trafo)