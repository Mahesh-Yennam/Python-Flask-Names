from flask import *

app = Flask(__name__)

names=[]
@app.route('/')
def home():
    return render_template('home.html', names=names)

@app.route('/add')
def add():
    name=request.args.get('name')
    names.append(name)
    return redirect(url_for('home'))

@app.route('/delete/<int:index>')
def delete(index):
    names.pop(index)
    return redirect(url_for('home'))

@app.route('/edit/<int:index>')
def edit(index):
    name=names[index]
    return render_template('edit.html', name=name, index=index)

@app.route('/update/<int:index>')
def update(index):
    name=request.args.get('name')
    names[index]=name
    return redirect(url_for('home'))


if __name__=="__main__":
    app.run(debug=True)