import eel
from rich import print

@eel.expose
def value_py(value):
    print(value)
    return