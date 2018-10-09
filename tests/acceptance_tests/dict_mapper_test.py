import pytest
from mappers.mapping import Mapping
from mappers.dict_mapper import DictMapper

@pytest.mark.acceptance
def key_dict_mapping_test():
    mapper = DictMapper(default=(lambda x: x.upper(),))

    assert {'HELLO': 'world'} == mapper.map({'hello': 'world'})


@pytest.mark.acceptance
def values_dict_mapping_test():
    mapper = DictMapper(default=(lambda x:x, lambda x: x ** 2,))

    assert {'hello': 4} == mapper.map({'hello': 2})

@pytest.mark.acceptance
def target_specific_key_mapping_test():
    mapper = DictMapper(
      {
        'hello': Mapping(lambda key: key.upper(), lambda value: value.lower()),
      }
    )

    assert {'HELLO': 'world'} == mapper.map({'hello': 'WORLD'})
