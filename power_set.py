def power_set(param_set):
    if len(param_set) <= 1:
        return param_set
    else:
        to_return = []
        for item in power_set(param_set[1:]):
            to_return.append([param_set[0]] + [item])
        return to_return
print (power_set([1,2,3]))
