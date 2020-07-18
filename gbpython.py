import subprocess

gb_imports = ["(scheme repl)" "(scheme base)" "(srfi 69)"]
#SRFI 69 for Gauche

def gb_conv(python_object,in_qq=False):
    global gb_imports
    if python_object is True:
        return "#t"
    elif python_object is False:
        return "#f"
    elif type(python_object) == int or type(python_object) == float:
        return str(python_object)
    elif type(python_object) == str:
        return "\"" + python_object + "\""
    elif type(python_object) == list:
        if in_qq:
            res = "("
        else:
            res = "`("
        for o in python_object:
            _r = gb_conv(o,True)
            if _r is None:
                return None
            res += " " + _r
        res += ")"
        return res
    elif type(python_object) == dict:
        if in_qq:
            res = ","
        else:
            res = ""

        alist = "`("
        for key,val in python_object.items():
            _key = gb_conv(key)
            _val = gb_conv(val)
            if _key is None or _val is None:
                return None
            alist += "(" + _key + " . " + _val + ")"
        alist += ")"
        res += "(alist->hash-table " + alist + " equal?)"
        return res
    return None

def goodbye_repl():
    gbals = filter(lambda x:x[0][0] != "_"
                        and x[0] != "gb_imports"
                        and x[0] != "gb_conv"
                        and x[0] != "goodbye_repl"
                        ,globals().items())

    import_expression = "(import " + " ".join(gb_imports) + ")"
    contents = ""
    for key,val in gbals:
        _val = gb_conv(val)
        if _val is not None:
            contents += ("(define " + key + " " + _val + " ) ")
    subprocess.run(["gosh","-e","(begin " + import_expression + contents + ")"])
    exit()
