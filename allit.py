from nltk.corpus import wordnet
from flask import Flask, request, render_template

app = Flask(__name__)

def alliterate(foo):
    #only two words for now
    foo = foo.split(" ")
    if len(foo) != 2:
        raise InputError("Fuck")

    f = lambda p: " " not in p
    syns_first = [x.lemmas()[0].name() for x in wordnet.synsets(foo[0])]
    syns_second = [x.lemmas()[0].name() for x in wordnet.synsets(foo[1])]
    print(syns_first)
    print(syns_second)
    x = list(filter(f, syns_first))
    y = list(filter(f, syns_second))

    
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
        except BaseException as err:
            return render_template('home.html', phrase="", rows=[f"{err}"])
    return render_template('home.html', rows=[], phrase="")

if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
