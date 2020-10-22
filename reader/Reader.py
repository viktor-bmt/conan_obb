from OBB import OBB

class Reader():

    def __init__(self, file, precision=3):

        self.precision = int(precision)
        if self.precision < 0:
            self.precision = 0
        self.format = '{:.' + str(self.precision) + 'f}'

        self.points = list()
        with open(file,'r') as f:
            eof = False
            while not eof:
                point = f.readline()
                if not point.endswith('\n'):
                    eof = True
                if len(point.strip()) == 0:
                    continue
                point = point.split()
                try:
                    point = [float(coord) for coord in point]
                except:
                    raise RuntimeError('Incorrect input file format. Only numerical values accepted')
                if len(point) != 3:
                    raise RuntimeError('Input points must have the format (X,Y,Z)')
                self.points.append(point)
        if len(self.points) < 2:
            raise RuntimeError('At least 2 points must be present in the input file')


    def print_obb_params(self):

        obb = OBB.build_from_points(self.points)

        print('The obb is:')
        print(('Width: ' + self.format).format(obb.extents[0]))
        print(('Height: ' + self.format).format(obb.extents[1]))
        print(('Depth: ' + self.format).format(obb.extents[2]))
        trafo = list()
        for coord in obb.centroid:
            trafo.append(coord)
        for row in obb.rotation:
            for elem in row:
                trafo.append(elem)
        print('Trafo: {}'.format(' '.join([self.format.format(x) for x in trafo])))


