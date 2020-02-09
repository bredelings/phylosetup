from atom.api import Atom, Str, Range, Bool, Value, Int, Tuple, observe, ContainerList, ForwardTyped, Typed

class GenericModel(Atom):
    func = Str()

    args = ContainerList(ForwardTyped(lambda:GenericModel))

    def as_string(self):
        if len(self.args) > 0:
            arg_strings = list()
            for arg in self.args:
                arg_strings.append(arg.as_string())
            return "{}[{}]".format(self.func,",".join(arg_strings))
        else:
            return self.func

