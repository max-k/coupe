def _merge_multiple_values(attribute):
    attribute.value = ' '.join(attribute.values)


OBJECT_PROCESSORS = {'FlagList': _merge_multiple_values}
