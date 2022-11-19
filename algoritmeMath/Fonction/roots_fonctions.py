from collections import Counter

global cte
cte = (int,float,complex)

class allFonction:
    def nb_variable(self):
        result = Counter(x=0)
        for val in self.value:
            if val == 'x': result.update('x')
            elif type(val) in cte:
                continue
            else:
                result.update(val.nb_variable())
        return result


def isConstant(args:list):
    result = []
    for arg in args:
        try:
            result.append(arg.isConstant)
        except:
            if type(arg) in cte: result.append(True)
            else: result.append(False)
    return all(result)