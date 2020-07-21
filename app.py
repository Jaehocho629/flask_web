from flask import Flask ,render_template
from data import Articles

app = Flask(__name__)
app.debug=True

@app.route('/')
def index():
    print("Success")
    # return "TEST"
    return render_template('home.html',hello="jhch")

@app.route('/about')
def about():
    print("Success")
    # return "TEST"
    return render_template('about.html',hello="jhch")

@app.route('/articles' , methods=['GET','POST'])
def articles():
    print("Success")
    # return "TEST"
    articles = Articles()
    print(len(articles))
    return render_template('articles.html',articles=articles)

@app.route('/test')
def show_image():
    return render_template('image.html')

@app.route('/article/<id>')
def article(id):
    print(id)
    articles = Articles()[id-1]
    print(articles)
    return render_template('article.html',data = [articles,id])
    # return "Success"



if __name__ == "__main__":
    # app.run(host = '0.0.0.0',port='8080')
    app.run()

    