global cte
cte = (int,float,complex)

def isConstant(args: list):
    result = []
    for arg in args:
        try:
            result.append(arg.isConstant)
        except:
            if type(arg) in cte: result.append(True)
            else: result.append(False)
    return all(result)