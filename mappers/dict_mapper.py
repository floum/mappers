class DictMapper:
    def __init__(self, map_=None, default=None):
        self.map_ = map_ or {}
        self.default = default or (lambda x: x, lambda x: x)
        
    def map(self, dictionary):
        return dict(
            self._map_item((key, value))
            for (key, value) in dictionary.items()
        )

    def _map_item(self, *items):
        mapping = self.map_.get(items[0], self.default)
#        import pdb; pdb.set_trace()
        return (map_(element) for (map_, element) in zip(mapping, items))
