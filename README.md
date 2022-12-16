
<details><summary>Operators</summary>
<p>

<details><summary><-</summary>
<p>

Move line to end of last line.

<details><summary>Example</summary>
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

<details><summary>-></summary>
<p>

Line separator.

<details><summary>Example</summary>
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

<details><summary><< and <<<</summary>
<p>

Read.

<details><summary>Example</summary>
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

<details><summary>=></summary>
<p>

Read.

<details><summary>Example</summary>
<p>

```js
    var y = (@type << wall1) => @copper_wall

    //y = wall1 is copper_wall
```

</p>
</details>

</p>
</details>

<details><summary>#inv</summary>
<p>

Read.

<details><summary>Example</summary>
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
    
    Basic if.
    
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
    
    Basic java for.
    
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
    
    Basic variable definition.
    
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
    
    Class definition.
    
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
    
    Macro definition.
    
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
    
    Print flush.
    
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
    
    Draw flush.
    
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
    
    Write value to cell index.
    
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
    
    <details><summary>wait</summary>
    <p>
    
    Processor wait.
    
        <details><summary>Example</summary>
        <p>
        
        ```js
            wait 1
            //Now processor waiting 1 second
        ```
        
        </p>
        </details>
    
    </p>
    </details>
    
    <details><summary>unit_bind</summary>
    <p>
    
    Bind unit to processor.
    
        <details><summary>Example</summary>
        <p>
        
        ```js
            unit_bind @dagger
            //Now all daggers binded to processor
        ```
        
        </p>
        </details>
    
    </p>
    </details>
    
    <details><summary>unit_idle</summary>
    <p>
    
    Set binded unit to idle.
    
        <details><summary>Example</summary>
        <p>
        
        ```js
            unit_idle
        ```
        
        </p>
        </details>
    
    </p>
    </details>
    
    <details><summary>unit_idle</summary>
    <p>
    
    Stop binded unit.
    
        <details><summary>Example</summary>
        <p>
        
        ```js
            unit_stop
        ```
        
        </p>
        </details>
    
    </p>
    </details>
    
    <details><summary>unit_pay_drop</summary>
    <p>
    
    Binded unit drop payload.
    
        <details><summary>Example</summary>
        <p>
        
        ```js
            unit_pay_drop
        ```
        
        </p>
        </details>
    
    </p>
    </details>
    
    <details><summary>unit_pay_enter</summary>
    <p>
    
    Binded unit enter.
    
        <details><summary>Example</summary>
        <p>
        
        ```js
            unit_pay_enter
        ```
        
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



</p>
</details>

</p>
</details>