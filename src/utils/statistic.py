import utils.api as api
from utils.structures import Hero

def heroes_leaderbord():
    profiles = api.leaderboard()

    heroes = [profile["favorHero"] for profile in profiles]
    heroes_games_played = dict(zip(list(heroes), [list(heroes).count(i) for i in list(heroes)]))

    heroes_rating = dict.fromkeys(set(heroes), 0)
    for profile in profiles:
        heroes_rating[profile['favorHero']] += int(profile["rating"]/heroes_games_played[profile['favorHero']])
    heroes_rating = dict(sorted(heroes_rating.items(), key=lambda item: item[1]))
    
    heroes = [Hero(hero.replace("npc_dota_hero_", ""), heroes_games_played[hero], heroes_rating[hero]) for hero in set(heroes)]
    sort_heroes = sorted(heroes, key=lambda hero: hero.avg_rating)
    return sort_heroes