from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

# Route for About page


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/thoughts')
def thoughts():
    return render_template('thoughts.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

if __name__ == "__main__":
    app.run()
