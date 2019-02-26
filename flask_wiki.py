from flask import Flask, render_template, url_for, request
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/study', methods=['GET','POST'])
def study():
    if request.method == 'POST':
        word = request.form['word']

        return render_template('study.html',word=word)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)