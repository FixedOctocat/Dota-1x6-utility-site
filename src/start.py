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
    heroes_strength = ["skeleton_king", "legion_commander", "pudge", "bristleback", "alchemist", "axe", "huskar"]
    heroes_agility = ["ember_spirit", "troll_warlord", "nevermore", "terrorblade", "phantom_assassin", "hoodwink", "juggernaut"]
    heroes_intelligence = ["ogre_magi", "lina", "void_spirit", "puck", "queenofpain"]

    return render_template("heroes.html", strength=heroes_strength, agility=heroes_agility, intelligence=heroes_intelligence)


if __name__ == '__main__':
    app.run(debug=True)