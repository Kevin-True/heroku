from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/about')
def about():
    return render_template('About.html')

if  __name__ == '__main__':
    #para correr y editar
    app.run(debug = False)
    
