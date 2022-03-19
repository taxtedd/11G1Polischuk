from flask import *
from models import *
from datetime import datetime, timedelta
from init import app

@app.route('/')
def first_page():
    resp = make_response(render_template("first_page.html"))
    if not request.cookies.get('test'):
       resp.set_cookie('test', 'testvalue', expires=datetime.now()+timedelta(minutes=30))
    return resp

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
    items = Items.query.all()
    return render_template("catalog.html", items=items)

@app.route('/item/<item>')
def show_item(item):
    item = escape(item)
    return render_template('item.html', item=Items.query.filter_by(name=item).one())

if __name__ == '__main__':
    app.run(debug=True)