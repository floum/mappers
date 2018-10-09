class DictMapper:
    def __init__(self, map_=None, keys=lambda x: x, values=lambda x: x):
        self.map_ = map_ or {}
        self.keys = keys
        self.values = values

    def map(self, dictionary):
        return dict(
            self._map_item(key, value)
            for key, value in dictionary.items()
        )

    def _map_item(self, key, value):
        mapping = self.map_.get(key, (self.keys, self.values))
        return (mapping[0](key), mapping[1](value))
