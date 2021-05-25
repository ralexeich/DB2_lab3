import os
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("postgres", "postgresql")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Team(db.Model):
    name = db.Column(db.String(64), primary_key=True)
    place = db.Column(db.String(64), index=True)


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    year = db.Column(db.Integer)
    team = db.Column(db.String(64), db.ForeignKey('team.name'))


db.create_all()
db.session.commit()


@app.route('/delete_player/<id>')
def delete_player(id):
    dl = db.session.query(Player).get(id)
    db.session.delete(dl)
    db.session.commit()

    return redirect('/index')

@app.route('/delete_team/<name>')
def delete_team(name):
    delete_list = Player.query.filter_by(team=name).all()
    for delete1 in delete_list:
        db.session.query(Player).get(delete1.id)
        db.session.delete(delete1)
        db.session.commit()

    delete = db.session.query(Team).get(name)
    db.session.delete(delete)
    db.session.commit()

    return redirect('/index')


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('start.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
    message = ''
    team_posts = Team.query.all()
    player_posts = Player.query.all()

    if request.method == 'POST':
        name = request.form.get('name_team')
        place = request.form.get('place_team')

        if name and place != '':
            try:
                add = Team(name=name, place=place)
                db.session.add(add)
                db.session.commit()
                return redirect('/index')
            except:
                message = 'TEAM EXISTS!'


        name = request.form.get('name_player')
        year = request.form.get('year_player')
        team = request.form.get('team_player')

        add = Player(name=name, year=year, team=team)

        list_br = []
        all = Team.query.all()
        for br in all:
            list_br.append(br.name)

        if name and year != '':
            if str(team) in list_br:
                db.session.add(add)
                db.session.commit()
                return redirect('/index')
            message = "TEAM DOESN'T EXIST:((("

    return render_template('index.html', team_posts=team_posts, player_posts=player_posts, message=message)


if __name__=="__main__":
    app.run(debug=True)
