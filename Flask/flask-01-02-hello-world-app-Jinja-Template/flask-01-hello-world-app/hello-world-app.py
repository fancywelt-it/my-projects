from flask import Flask

app = Flask(__name__)

@app.route('/')  # ekorete ediliyor route / anasayfa demek, bu yaziyi karsima cikar
def hello():
    return "Hello World from Flask!!!"

@app.route('/second')
def second():
    return 'Bize Her Yer Trabzon!!!!'

@app.route('/third/subthird')
def third():
    return 'This is the subpage of third page'

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'



if __name__ == '__main__':
    app.run(debug=True, port=2000)  # burada port=2000 yazmadan calistirinca http://127.0.0.1:5000 de calistirir yani localhost:5000, yoksa burasi app.run(debug=True) seklimde calistirip devam ediyoruz 