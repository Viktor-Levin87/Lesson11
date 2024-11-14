from pprint import pprint
import inspect


def introspection_info(obj):
    type_of_obj = type(obj)
    attributes = dir(obj)
    methods = [i for i in dir(obj) if callable(getattr(obj, i))]
    module = inspect.getmodule(introspection_info)

    return {'type': type_of_obj.__name__, 'attributes': attributes, 'methods': methods, 'module': module}


number_info = introspection_info(42)
print(number_info)
number_info = introspection_info(pprint)
pprint(number_info)
