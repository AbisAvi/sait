from dataclasses import asdict
from flask import Flask, render_template
from forms.SignUpForm import SignUpForm

users = []


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def signUp():
    form = SignUpForm()

    if form.validate_on_submit():
        name = form.name.data
        rassa = form.rassa.data

        if rassa == "Э":
            return render_template("classes_elf.html", name=name)

        elif rassa == "Д":
            return render_template("classes_dvorf.html", name=name)

        elif rassa == "Пэ":
            return render_template("classes_poluelf.html", name=name)

        elif rassa == "Т":
            return render_template("classes_tifling.html", name=name)

        elif rassa == "Г":
            return render_template("classes_gnom.html", name=name)

        elif rassa == "П":
            return render_template("classes_poluroslik.html", name=name)

        elif rassa == "Др":
            return render_template("classes_drakonorogden.html", name=name)

        elif rassa == "Пр":
            return render_template("classes_poluork.html", name=name)

        return render_template("classes.html", name=name)
    else:
        return render_template("formTemplate.html", form=form,  btn_name="Регистрация!")


@app.route("/users", methods=['GET', 'POST'])
def getUsers():
    return users


@app.route("/users/<int:user_id>")
def getUser(user_id: int):
    for user in users:
        if user.id == user_id:
            return asdict(user)

    return str(None)


@app.route("/delUser/<int:user_id>")
def delUser(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return asdict(user)

    return str(None)


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    app.run(debug=True, port = 1029)
