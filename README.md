
<details><summary>## Operators</summary>
<p>

<details><summary>## <-</summary>
<p>

Move line to end of last line.

<details><summary>## Example</summary>
<p>

```js
    var x = 2
    <- * 2

    //x = 4
```

<p>
<details>

<p>
<details>

<details><summary>## -></summary>
<p>

Line separator.

<details><summary>## Example</summary>
<p>

```js
    var x = 2 ->var y = 1

    //x = 2
    //y = 1
```

<p>
<details>

<p>
<details>

<details><summary>## <<</summary>
<p>

Read.

<details><summary>## Example</summary>
<p>

```js
    var x = @shooting << duo1

    //x = is duo1 shooting
```

<p>
<details>

<p>
<details>

<p>
<details>

<details><summary>## Keywords</summary>
<p>



<p>
<details>

<details><summary>## Functions</summary>
<p>

<details><summary>## World</summary>
<p>

get_flag(name)

get_block(x, y)

get_building(x, y)

get_ore(x, y)

get_floor(x, y)

spawn(team, unit, x, y, rot)

fetch_build(team, block, link)

fetch_core(team, link)

fetch_player(team, link)

fetch_unit(team, link)

fetch_build_count(team, block)

fetch_core_count(team)

fetch_player_count(team)

fetch_unit_count(team)

<p>
<details>

color(r, g, b, a)

distance_radar(from, order, type0, type1, type2)

health_radar(from, order, type0, type1, type2)

shield_radar(from, order, type0, type1, type2)

armor_radar(from, order, type0, type1, type2)

max_health_radar(from, order, type0, type1, type2)

unit_distance_radar(order, type0, type1, type2)

unit_health_radar(order, type0, type1, type2)

unit_shield_radar(order, type0, type1, type2)

unit_armor_radar(order, type0, type1, type2)

unit_max_health_radar(order, type0, type1, type2)

unit_get_block(x, y, type, floor)

unit_inside(x, y, radius)

unit_locate_ore(ore, out x, out y)

unit_locate_build(type, enemy, out x, out y, found)

unit_locate_spawn(out x, out y, found)

unit_locate_damaged(out x, out y, found)

not(bool)

<details><summary>## Math</summary>
<p>

max(a, b)

min(a, b)

angle(x, y)

len(x, y)

noise(x, y)

abs(number)

log(number)

log10(number)

floor(number)

ceil(number)

sqrt(number)

rand(number)

sin(angle)

cos(angle)

tan(angle)

asin(angle)

acos(angle)

atan(angle)

<p>
<details>

<p>
<details>