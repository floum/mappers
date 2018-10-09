class Mapping:
    def __init__(self, *args):
        self.args = args

    def __getitem__(self, i):
        return self.args[i]

    def __iter__(self):
        return iter(self.args)
