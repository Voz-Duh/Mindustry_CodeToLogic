
<details><summary>Constants</summary>
<p>

<details><summary>#mind_code_lines</summary>
<p>

Current number of mindustry processors code lines.

</p>
</details>

</p>
</details>

<details><summary>Operators</summary>
<p>

<details><summary>  <-</summary>
<p>

####    Move line to end of last line.

<details><summary>      Example</summary>
<p>

```js
    var x = 2
    <- * 2

    //x = 4
```

</p>
</details>

</p>
</details>

<details><summary>  -></summary>
<p>

####    Line separator.

<details><summary>      Example</summary>
<p>

```js
    var x = 2 ->var y = 1

    //x = 2
    //y = 1
```

</p>
</details>

</p>
</details>

<details><summary>  << and <<<</summary>
<p>

####    Read.

<details><summary>      Example</summary>
<p>

```js
    var x = @shooting << duo1
    var y = 0 <<< cell1

    //x = is duo1 shooting
    //y = 0 index from cell1
```

</p>
</details>

</p>
</details>

<details><summary>  =></summary>
<p>

####    Read.

<details><summary>      Example</summary>
<p>

```js
    var y = (@type << wall1) => @copper_wall

    //y = wall1 is copper_wall
```

</p>
</details>

</p>
</details>

<details><summary>  #inv</summary>
<p>

####    Inverse number.

<details><summary>      Example</summary>
<p>

```js
    var x = #inv 10

    //x = -10
```

</p>
</details>

</p>
</details>

</p>
</details>

<details><summary>Keywords</summary>
<p>

<details><summary>if</summary>
<p>

####    Basic if.
    
<details><summary>Example</summary>
<p>
        
```js
            if(true){
                //if
            }else->if(){
                //else if
            }else{
                //else
            }
```
        
</p>
</details>
    
</p>
</details>

<details><summary>for</summary>
<p>

####    Basic Java/C#/C++ for.
    
<details><summary>Example</summary>
<p>
        
```js
            for(var i = 0; i < 2; i++){
                //code
            }
```
        
</p>
</details>
    
</p>
</details>

<details><summary>var</summary>
<p>

####    Basic variable definition.
    
<details><summary>Example</summary>
<p>
        
```js
            var x = 0
        
            //x = 0
```
        
</p>
</details>
    
</p>
</details>

<details><summary>class</summary>
<p>

####    Class definition.
    
<details><summary>Example</summary>
<p>
        
```js
            class x(cell1) = { x: 0, y: 1 }
            //x_x = 0 index from cell1
            //x_y = 1 index from cell1
        
            x.x = 10
            //write 10 to 0 index in cell1
```
        
</p>
</details>
    
</p>
</details>

<details><summary>#macro</summary>
<p>

####    Macro definition.
    
<details><summary>Example</summary>
<p>
        
```js
            #macro setx: var x = 0
        
            setx
            //x = 0
            #macro setx: var x = 2
            setx
            //x = 2
```
        
</p>
</details>
    
</p>
</details>

<details><summary>print_flush</summary>
<p>

####    Print flush.
    
<details><summary>Example</summary>
<p>
        
```js
            print("Hello!")
            print_flush message1
            //Now we have "Hello!" in message1
```
        
</p>
</details>
    
</p>
</details>

<details><summary>draw_flush</summary>
<p>

####    Draw flush.
    
<details><summary>Example</summary>
<p>
        
```js
            draw_clear(0, 0, 0)
            draw_flush display1
            //Now we have black display1
```
        
</p>
</details>
    
</p>
</details>

<details><summary>write</summary>
<p>

####    Write value to cell index.
    
<details><summary>Example</summary>
<p>
        
```js
            write 10 >> cell1 >> 0
            //Now cell1 have 10 on 0 index
```
        
</p>
</details>
    
</p>
</details>

<details><summary>  wait</summary>
<p>

####   Processor wait.

<details><summary>      Example</summary>
<p>

```js
            wait 1
            //Now processor waiting 1 second
```

</p>
</details>

</p>
</details>

<details><summary>  flush_notify</summary>
<p>

####   Flush notify.

<details><summary>      Example</summary>
<p>

```js
            flush_notify
```

</p>
</details>

</p>
</details>

<details><summary>  flush_mission</summary>
<p>

####   Flush mission.

<details><summary>      Example</summary>
<p>

```js
            flush_mission
```

</p>
</details>

</p>
</details>

<details><summary>  flush_announce</summary>
<p>

####   Flush announce.

<details><summary>      Example</summary>
<p>

```js
            flush_announce 1
            //Flush announce to 1 second
```

</p>
</details>

</p>
</details>

<details><summary>  flush_toast</summary>
<p>

####   Flush toast.

<details><summary>      Example</summary>
<p>

```js
            flush_toast 1
            //Flush toast to 1 second
```

</p>
</details>

</p>
</details>

<details><summary>  unit_bind</summary>
<p>

####    Bind unit to processor.
    
<details><summary>      Example</summary>
<p>
        
```js
            unit_bind @dagger
            //Now all daggers binded to processor
```
        
</p>
</details>
    
</p>
</details>

<details><summary>  unit_unbind</summary>
<p>

####    Unbind unit from processor.

<details><summary>      Example</summary>
<p>

```js
            unit_unbind
```

</p>
</details>

</p>
</details>

<details><summary>  unit_idle</summary>
<p>

####    Set binded unit to idle.
    
<details><summary>      Example</summary>
<p>
        
```js
            unit_idle
```
        
</p>
</details>
    
</p>
</details>

<details><summary>  unit_stop</summary>
<p>

####    Stop binded unit.
    
<details><summary>      Example</summary>
<p>
        
```js
            unit_stop
```
        
</p>
</details>
    
</p>
</details>

<details><summary>  unit_pay_drop</summary>
<p>

<details><summary>  unit_pay_drop</summary>
<p>

####    Binded unit drop payload.
    
<details><summary>      Example</summary>
<p>
        
```js
            unit_pay_drop
```
        
</p>
</details>
    
</p>
</details>

<details><summary>  unit_pay_enter</summary>
<p>

####    Binded unit enter.
    
<details><summary>      Example</summary>
<p>
        
```js
            unit_pay_enter
```
        
</p>
</details>
    
</p>
</details>

<details><summary>  cutscene_stop</summary>
<p>

####    Stop cutscene.

<details><summary>      Example</summary>
<p>

```js
            cutscene_stop
```

</p>
</details>

</p>
</details>

<details><summary>  cutscene_zoom</summary>
<p>

####    Cutscene zoom.

<details><summary>      Example</summary>
<p>

```js
            cutscene_zoom 10
```

</p>
</details>

</p>
</details>

<details><summary>  stop</summary>
<p>

####    Stop processor.

<details><summary>      Example</summary>
<p>

```js
            stop
```

</p>
</details>

</p>
</details>

<details><summary>  end</summary>
<p>

####    End processor.

<details><summary>      Example</summary>
<p>

```js
            end
```

</p>
</details>

</p>
</details>

<details><summary>  goto</summary>
<p>

####    go to label.

<details><summary>      Example</summary>
<p>

```js
            :test
            
            goto test
```

</p>
</details>

</p>
</details>

<details><summary>  Label</summary>
<p>

####    Definition of label.

<details><summary>      Example</summary>
<p>

```js
            :test
```

</p>
</details>

</p>
</details>

</p>
</details>

</p>
</details>

<details><summary>Functions</summary>
<p>

<details><summary>World</summary>
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

</p>
</details>

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

<details><summary>Math</summary>
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

</p>
</details>

<details><summary>Operations</summary>
<p>

print(values...)

set_color(unit, color)

set_config(unit, b)

set_enabled(unit, bool)

shoot_to(unit, x, y, bool)

shoot_unit(unit, to, bool)

draw_clear(r, g, b)

draw_rgba(r, g, b, a)

draw_color(color)

draw_stroke(value)

draw_line(x1, y1, x2, y2)

draw_rect(x, y, x_size, y_size)

draw_line_poly(x, y, sides, radius, rotation)

draw_poly(x, y, sides, radius, rotation)

draw_line_rect(x, y, x_size, y_size)

draw_triangle(x1, y1, x2, y2, x3, y3)

draw_image(x, y, texture, size, rotation)

unit_move(x, y, [range])

unit_boost(bool)

unit_shoot_to(x, y, b)

unit_shoot_unit(unit, b)

unit_item_drop(to, amount)

unit_item_take(from, item, amount)

unit_pay_take(block)

unit_mine(x, y)

unit_flag(flag)

unit_build(x, y, block, rot, config)

set_block(team, block, x, y, rot)

set_ore(block, x, y)

shock_unit(unit)

boss_unit(unit)

apply_status(status, unit)

remove_status(status, unit)

spawn_wave(x, y, nat)

set_map_area((x, y, w, h)

set_rule(rule, value)

set_team_rule(team, rule, x)

cutscene_pan(x, y, speed)

explosion(team, x, y, radius, damage, flying, ground, pierce)

set_flag(flag, b)

</p>
</details>

</p>
</details>
