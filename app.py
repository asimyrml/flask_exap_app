from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import csv
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exam_app.db'
db = SQLAlchemy(app)


questions_list = [
    {
        "question": "Discord.py ne için kullanılır?",
        "options": ["Sohbet botu", "Veri analizi", "Oyun motoru", "Veri tabanı"],
        "answer": "Sohbet botu"
    },
    {
        "question": "Flask hangi tür projede kullanılır?",
        "options": ["Web sitesi", "Mobil oyun", "Resim düzenleme", "Donanım kontrolü"],
        "answer": "Web sitesi"
    },
    {
        "question": "TensorFlow en çok hangi alanda kullanılır?",
        "options": ["Yapay zeka", "Web tasarım", "Veritabanı yönetimi", "Ses kaydı"],
        "answer": "Yapay zeka"
    },
    {
        "question": "ImageAI ile hangi alan ilgilidir?",
        "options": ["Bilgisayar Görüşü", "Veri tabanı", "Metin madenciliği", "Ses analizi"],
        "answer": "Bilgisayar Görüşü"
    },
    {
        "question": "BeautifulSoup hangi amaçla kullanılır?",
        "options": ["Web scraping", "Oyun geliştirme", "Makine öğrenmesi", "Veri tabanı"],
        "answer": "Web scraping"
    },
    {
        "question": "NLTK hangi amaçla kullanılır?",
        "options": ["Doğal Dil İşleme", "Web geliştirme", "Görüntü işleme", "Oyun geliştirme"],
        "answer": "Doğal Dil İşleme"
    },
    {
        "question": "Keras hangi tür projede yaygın?",
        "options": ["Yapay zeka", "Web sitesi", "Veritabanı", "Donanım kontrolü"],
        "answer": "Yapay zeka"
    },
    {
        "question": "PyTorch genellikle hangi alanda kullanılır?",
        "options": ["Makine öğrenmesi", "Web geliştirme", "Veritabanı", "Ses kaydı"],
        "answer": "Makine öğrenmesi"
    },
    {
        "question": "FastAPI hangi amaçla kullanılır?",
        "options": ["Web API", "Resim işleme", "Oyun", "Veri tabanı"],
        "answer": "Web API"
    },
    {
        "question": "OpenCV ile hangi alan ilgilidir?",
        "options": ["Bilgisayar Görüşü", "Veri analizi", "Web sitesi", "Yapay zeka"],
        "answer": "Bilgisayar Görüşü"
    },
    {
        "question": "Matplotlib ne için kullanılır?",
        "options": ["Veri görselleştirme", "Metin analizi", "Veritabanı", "Yapay zeka"],
        "answer": "Veri görselleştirme"
    },
    {
        "question": "Scikit-learn hangi alanda öne çıkar?",
        "options": ["Makine öğrenmesi", "Web geliştirme", "Donanım", "Resim düzenleme"],
        "answer": "Makine öğrenmesi"
    },
    {
        "question": "Django ile hangi tür uygulama yapılır?",
        "options": ["Web sitesi", "Ses kaydı", "Görsel işleme", "Veri analizi"],
        "answer": "Web sitesi"
    },
    {
        "question": "Requests kütüphanesi ne için kullanılır?",
        "options": ["HTTP istekleri", "Veri tabanı", "Resim işleme", "Oyun motoru"],
        "answer": "HTTP istekleri"
    },
    {
        "question": "Pandas genellikle hangi amaçla kullanılır?",
        "options": ["Veri analizi", "Donanım kontrolü", "Ses işleme", "Oyun"],
        "answer": "Veri analizi"
    },
    {
        "question": "SpeechRecognition kütüphanesi neyi işler?",
        "options": ["Ses", "Sayı", "Resim", "Video"],
        "answer": "Ses"
    },
    {
        "question": "SQLAlchemy neyle ilgilidir?",
        "options": ["Veri tabanı", "Görsel işleme", "Ses analizi", "Oyun motoru"],
        "answer": "Veri tabanı"
    },
    {
        "question": "Transformers kütüphanesi hangi alanla ilgili?",
        "options": ["Doğal Dil İşleme", "Donanım", "Ses kaydı", "Oyun"],
        "answer": "Doğal Dil İşleme"
    },
    {
        "question": "Flask hangi programlama diliyle yazılır?",
        "options": ["Python", "JavaScript", "Java", "C++"],
        "answer": "Python"
    },
    {
        "question": "Pillow neyle ilgilidir?",
        "options": ["Resim işleme", "Web API", "Donanım", "Veri tabanı"],
        "answer": "Resim işleme"
    }
]


# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    highest_score = db.Column(db.Integer, default=0)

class ExamResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)


def load_questions(num_questions=5):
    selected_questions = random.sample(questions_list, num_questions)
    shuffled_questions = []
    for q in selected_questions:
        
        options = q["options"][:]
        random.shuffle(options)
        
        answer = q["answer"]
        shuffled_questions.append({
            "question": q["question"],
            "options": options,
            "answer": answer
        })
    return shuffled_questions



@app.route('/')
def home():
    if 'username' in session:
        user = User.query.filter_by(username=session['username']).first()
        highest_score = user.highest_score if user else 0
    else:
        highest_score = 0

    all_time_high = db.session.query(db.func.max(User.highest_score)).scalar() or 0

    return render_template('index.html', highest_score=highest_score, all_time_high=all_time_high)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    if not user:
        user = User(username=username)
        db.session.add(user)
        db.session.commit()

    session['username'] = user.username
    return redirect(url_for('exam'))

@app.route('/exam')
def exam():
    questions = load_questions(num_questions=5)
    session['questions'] = questions
    return render_template('exam.html', questions=questions)


@app.route('/submit', methods=['POST'])
def submit_exam():
    if 'username' not in session or 'questions' not in session:
        return redirect(url_for('home'))

    user = User.query.filter_by(username=session['username']).first()
    questions = session['questions']
    total_questions = len(questions)

    score = 0
    for i, q in enumerate(questions):
        user_answer = request.form.get(f'answer{i}')
        if user_answer == q['answer']:
            score += 1

    user_percent = int((score / total_questions) * 100)

    prev_highest = user.highest_score
    if score > prev_highest:
        user.highest_score = score

    db.session.add(ExamResult(user_id=user.id, score=score))
    db.session.commit()

    all_time_high_score = db.session.query(db.func.max(User.highest_score)).scalar() or 0
    all_time_high_percent = int((all_time_high_score / total_questions) * 100) if total_questions > 0 else 0

    user_highest_percent = int((user.highest_score / total_questions) * 100) if total_questions > 0 else 0

    session.pop('questions', None)

    return render_template(
        'result.html',
        score=score,
        user_percent=user_percent,
        user_highest_percent=user_highest_percent if prev_highest > 0 or score > 0 else None,
        all_time_high_percent=all_time_high_percent,
        total_questions=total_questions
    )


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)


