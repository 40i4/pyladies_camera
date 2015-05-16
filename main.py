from flask import Flask, render_template, request
from wtforms import (
    Form,
    SelectField,
)

app = Flask(__name__)


@app.route('/')
def hello_world():
    to_jest_fajna_zmienna = "ala ma aids"
    return render_template("index.html", zmienna=to_jest_fajna_zmienna)

class HandChooseForm(Form):
    """
    Choose a hand
    """
    hand_choice = SelectField(
        'hand_choice',
        choices=[
            ('small', 'small'),
            ('big', 'big'),
        ]
    )


def cpu_choice():
    pass


@app.route('/play', methods=['GET', 'POST'])
def play():
    form = HandChooseForm()
    print(request.method, form.validate())

    if request.method == 'POST':
        player_choice = request.form.get('hand_choice')
        import pdb; pdb.set_trace()
        outcome = "lost"
        cpu_choice = "cpu"
        how = "kick"
        print("test")
        return "You {}, your {} was {} by {}".format(
            outcome, player_choice, how, cpu_choice
        )
    return render_template("play.html", form=form)

if __name__ == '__main__':
    app.run()
