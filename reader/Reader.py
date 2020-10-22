from OBB import OBB

class Reader():

    def __init__(self, file):

        self.data = list()
        # read and parse the file here

    def print_obb_params(self):

        obb = OBB(self.data)
        result = obb.get()

        print('The obb is:')
        print('Width: {}'.format(result[0]))
        print('Height: {}'.format(result[1]))
        print('Depth: {}'.format(result[2]))
        print('Trafo: {}'.format(' '.join([str(x) for x in result[3]])))


