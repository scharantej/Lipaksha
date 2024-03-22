
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    return render_template('lessons.html')

@app.route('/lesson/<lesson_number>')
def lesson(lesson_number):
    return render_template('lesson{}.html'.format(lesson_number))

@app.route('/practice')
def practice():
    return render_template('practice.html')

@app.route('/quizzes')
def quizzes():
    return render_template('quizzes.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run()
