import cgi
import eel
eel.init("")



eel.start("index.html", size=(1000, 440))

@eel.expose
def ooo():
    our_form = cgi.FieldStorage()
    xxx = our_form.getfirst('Otmetka_verha', 'Не задано...')
    print(xxx)

# ooo()