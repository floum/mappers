# Mappers

Mappers is intended to provide seamless operations on data structure to pass them to other interfaces.

## Features

## Basic Usage

```
mapper = Mapper(map)
mapper.map(params)
```

### DictMapper

```
mapper = Mapper(lambda x: x)
mapped_params = mapper.map(params)
assert mapped_params == params
```
