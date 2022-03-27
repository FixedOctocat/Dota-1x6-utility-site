let all_heroes = new Array("skeleton_king", "legion_commander", "pudge", "bristleback", "alchemist", "axe", "huskar", "ember_spirit", "troll_warlord", "nevermore", "terrorblade", "phantom_assassin", "hoodwink", "juggernaut", "ogre_magi", "lina", "void_spirit", "puck", "queenofpain")
let marked_heroes = [...all_heroes];

function removeItemOnce(arr, value) {
  var index = arr.indexOf(value);
  if (index > -1) {
    arr.splice(index, 1);
  }
}

function hlimage(e) {
  img = document.getElementById(e.target.id);
  
  if (img.classList.contains('clicked')) {
    marked_heroes.push(e.target.id);
    img.classList.remove('clicked');
  }
  else {
    removeItemOnce(marked_heroes, e.target.id);
    img.classList.add('clicked');
  }
}

function gethero(){
  var hero = marked_heroes[Math.floor(Math.random()*marked_heroes.length)];
  let heroes_profiles = [...all_heroes]
  removeItemOnce(heroes_profiles, hero);
  
  for (var i = 0; i < all_heroes.length; i++) {
    img = document.getElementById(all_heroes[i]);
    img.style["opacity"] = "1"
  }

  for (var i = 0; i < heroes_profiles.length; i++) {
    img = document.getElementById(heroes_profiles[i]);
    img.style["opacity"] = "0.3"
  }
}

function resetheroeslist(){
  for (var i = 0; i < all_heroes.length; i++) {
    img = document.getElementById(all_heroes[i]);
    img.style["opacity"] = "1"
    img.classList.remove('clicked');
  }

  marked_heroes = [...all_heroes];
}