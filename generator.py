"""
the format is a python dict.
{
    "functions": [
        {
            "mangled_function_name_to_hook" : xxx(string),
            "mangled_function_name_to_listen": xxx(string),
            "parameters" : xxx(int),
        },
    ],
}
and this script but a binding between the hooked function and
the listener function.
The listener function will receive the original function as the
first parameter.
"""
class ParseError(Exception):
    pass

def build_paramter_string(parameters):
    ret = []
    for i in range(parameters):
        ret.append('void* p%d' % i)
    return ', '.join(ret)

def build_call_string(mangled_function_name_to_hook, mangled_function_name_to_listen, parameters):
    s = "    return %s(&__real_%s, " % (mangled_function_name_to_listen, mangled_function_name_to_hook)
    ret = []
    for i in range(parameters):
        ret.append('p%d' % i)
    return s + ', '.join(ret) + ");"

class Writer(object):
    def __init__(self):
        self.file_ = open("hook_output.c", "w")
        f = self.file_
        print >> f, '#include <stdint.h>'
        print >> f, ''
        print >> f, ''

    def one_element(self, mangled_function_name_to_hook, mangled_function_name_to_listen, parameters):
        f = self.file_
        parameter_string = build_paramter_string(parameters)
        print >> f, 'extern void __real_%s();' % mangled_function_name_to_hook
        print >> f, 'extern void* %s(%s, %s);' % (mangled_function_name_to_listen, 'void* func', parameter_string)
        print >> f, 'void* __wrap_%s(%s)' % (mangled_function_name_to_hook, parameter_string)
        print >> f, '{'
        print >> f, build_call_string(mangled_function_name_to_hook, mangled_function_name_to_listen, parameters)   
        print >> f, '}'
        print >> f, ''

    def close(self):
        f = self.file_
        f.close();

def parse(file_name, parsed_one_element):
    with open(file_name, 'r') as f:
        _my_dict = eval(f.read())

    if "functions" not in _my_dict:
        raise ParseError("no functions in hook_desc");

    for function_dict in _my_dict["functions"]:
        mangled_function_name_to_hook = function_dict["mangled_function_name_to_hook"]
        mangled_function_name_to_listen = function_dict["mangled_function_name_to_listen"]
        parameters = function_dict["parameters"]
        parsed_one_element(mangled_function_name_to_hook, mangled_function_name_to_listen, parameters)

def main():
    w = Writer()
    parse('hook_desc', w.one_element)
    w.close()

if __name__ == '__main__':
    main()
