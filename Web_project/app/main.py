from flask import Flask, render_template, redirect, request, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from data import db_session
from data.news import News
from data.users import User
from forms.user import RegisterForm, LoginForm

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    db_session.global_init("db/blogs.db")
    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        news = db_sess.query(News).filter((News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/profile')
def profile():
    return render_template("profile.html")


@app.route('/Bird')
def Bird():
    return render_template("design/Bird.html")


@app.route('/Meet')
def Meet():
    return render_template("design/Meet.html")


@app.route('/Fish')
def Fish():
    return render_template("design/Fish.html")


@app.route('/Soups')
def Soups():
    return render_template("design/Soups.html")


@app.route('/Salads')
def Salads():
    return render_template("design/Salats.html")


@app.route('/Desserts')
def Desserts():
    return render_template("design/Desserts.html")


@app.route('/Cocktail')
def Cocktails():
    return render_template("design/Cocktails.html")


@app.route('/meet1')
def Meet1():
    return render_template("meet/meet_res_1.html")


@app.route('/meet2')
def Meet2():
    return render_template("meet/meet_res_2.html")


@app.route('/meet3')
def Meet3():
    return render_template("meet/meet_res_3.html")


@app.route('/meet4')
def Meet4():
    return render_template("meet/meet_res_4.html")


@app.route('/meet5')
def Meet5():
    return render_template("meet/meet_res_5.html")


@app.route('/meet6')
def Meet6():
    return render_template("meet/meet_res_6.html")


@app.route('/bird1')
def Bird1():
    return render_template("bird/bird_res_1.html")


@app.route('/bird2')
def Bird2():
    return render_template("bird/bird_res_2.html")


@app.route('/bird3')
def Bird3():
    return render_template("bird/bird_res_3.html")


@app.route('/bird4')
def Bird4():
    return render_template("bird/bird_res_4.html")


@app.route('/bird5')
def Bird5():
    return render_template("bird/bird_res_5.html")


@app.route('/bird6')
def Bird6():
    return render_template("bird/bird_res_6.html")


@app.route('/fish1')
def Fish1():
    return render_template("fish/fish_res_1.html")


@app.route('/fish2')
def Fish2():
    return render_template("fish/fish_res_2.html")


@app.route('/fish3')
def Fish3():
    return render_template("fish/fish_res_3.html")


@app.route('/fish4')
def Fish4():
    return render_template("fish/fish_res_4.html")


@app.route('/fish5')
def Fish5():
    return render_template("fish/fish_res_5.html")


@app.route('/fish6')
def Fish6():
    return render_template("fish/fish_res_6.html")


@app.route('/soup1')
def soup1():
    return render_template("soup/soup_res_1.html")


@app.route('/soup2')
def soup2():
    return render_template("soup/soup_res_2.html")


@app.route('/soup3')
def soup3():
    return render_template("soup/soup_res_3.html")


@app.route('/soup4')
def soup4():
    return render_template("soup/soup_res_4.html")


@app.route('/soup5')
def soup5():
    return render_template("soup/soup_res_5.html")


@app.route('/soup6')
def soup6():
    return render_template("soup/soup_res_6.html")


@app.route('/salad1')
def salad1():
    return render_template("salad/salad_res_1.html")


@app.route('/salad2')
def salad2():
    return render_template("salad/salad_res_2.html")


@app.route('/salad3')
def salad3():
    return render_template("salad/salad_res_3.html")


@app.route('/salad4')
def salad4():
    return render_template("salad/salad_res_4.html")


@app.route('/salad5')
def salad5():
    return render_template("salad/salad_res_5.html")


@app.route('/salad6')
def salad6():
    return render_template("salad/salad_res_6.html")


@app.route('/dessert1')
def dessert1():
    return render_template("dessert/dessert_res_1.html")


@app.route('/dessert2')
def dessert2():
    return render_template("dessert/dessert_res_2.html")


@app.route('/dessert3')
def dessert3():
    return render_template("dessert/dessert_res_3.html")


@app.route('/dessert4')
def dessert4():
    return render_template("dessert/dessert_res_4.html")


@app.route('/dessert5')
def dessert5():
    return render_template("dessert/dessert_res_5.html")


@app.route('/dessert6')
def dessert6():
    return render_template("dessert/dessert_res_6.html")


@app.route('/cocktail1')
def cocktail1():
    return render_template("cocktail/cocktail_res_1.html")


@app.route('/cocktail2')
def cocktail2():
    return render_template("cocktail/cocktail_res_2.html")


@app.route('/cocktail3')
def cocktail3():
    return render_template("cocktail/cocktail_res_3.html")


@app.route('/cocktail4')
def cocktail4():
    return render_template("cocktail/cocktail_res_4.html")


@app.route('/cocktail5')
def cocktail5():
    return render_template("cocktail/cocktail_res_5.html")


@app.route('/cocktail6')
def cocktail6():
    return render_template("cocktail/cocktail_res_6.html")


if __name__ == '__main__':
    main()
