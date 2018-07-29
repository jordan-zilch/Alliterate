from thesaurus import Word
from flask import Flask, request, render_template

app = Flask(__name__)

def alliterate(foo):
    #only two words for now
    foo = foo.split(" ")
    if len(foo) != 2:
        raise InputError("Fuck")

    f = lambda p: " " not in p
    x = list(filter(f, Word(foo[0]).synonyms()))
    y = list(filter(f, Word(foo[1]).synonyms()))

    
    li = []
    for i in x:
        for j in y:
            if i[0] == j[0]:
                li.append(i + " " + j)

    if len(li) == 0:
        return ["No alliterations found :("]

    return li

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        try:
            res = alliterate(request.form.get("phrase"))
            return render_template('home.html', phrase=request.form.get("phrase"), rows=res)
        except:
            return render_template('home.html', phrase="", rows=["Bad input!"])
    return render_template('home.html', rows=[], phrase="")

if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
