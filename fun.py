import eel

@eel.expose
def value_py(value):
    print(value)
    return