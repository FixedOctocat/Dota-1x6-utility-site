from flask import Flask, request, render_template, url_for

import utils.statistic as stat

app = Flask(__name__)


@app.route("/leaderboard")
def leaderboard():
    data = stat.heroes_leaderbord()
    
    hero_names = [hero.name for hero in data]
    hero_fav = [hero.fav_rating for hero in data]
    hero_avg = [hero.avg_rating for hero in data]

    return render_template("leaderboard.html", labels=hero_names, hero_fav=hero_fav, hero_avg=hero_avg)

@app.route("/heroes")
def heroes():
    return render_template("heroes.html")


if __name__ == '__main__':
    app.run(debug=True)