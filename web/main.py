from flask import *
from models import *
from init import app

@app.route('/')
def first_page():
    return render_template("first_page.html")

@app.route('/about_us', methods=['GET', 'POST'])
def about_page():
    feedback = Feedback.query.all()
    if request.method == 'POST':
        surname = request.form.get('surname')
        name = request.form.get('name')
        email = request.form.get('email')
        text = request.form.get('text')
        if email != '' and text != '':
            f = Feedback(surname=surname, name=name, email=email, text=text)
            db.session.add(f)
            db.session.commit()
            feedback.append(f)
    print(feedback)
    return render_template("about_us.html", feedback=feedback)

@app.route('/catalog')
def catalog_page():
    return render_template("catalog.html")

@app.route('/island_spa')
def island_spa_page():
    return render_template("island_spa.html")

@app.route('/mixed_berry')
def mixed_bery_page():
    return render_template("mixed_berry.html")

@app.route('/pure_lilen')
def pure_lilen_page():
    return render_template("pure_lilen.html")

@app.route('/white_jasmine')
def white_jasmine_page():
    return render_template("white_jasmine.html")

if __name__ == '__main__':
    app.run(debug=True)