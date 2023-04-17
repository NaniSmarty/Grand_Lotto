def login(string_l):
    x = string_l.split(" ")
    method = x[0]
    params = x[1]
    result = "Method : " + str(method) + " params : " + str(params)
    return result