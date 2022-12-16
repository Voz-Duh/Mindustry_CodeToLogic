import fileinput as fi

file = fi.FileInput(input('Compile file path: '))


class Result:
    result = ''
    next = ''
    code: list[str] = []
    lines: list[str] = []
    var_id = 0
    cont_i = -1
    lines_counter = 0
    current_code = 0
    old = []
    special_brackets_counter = []


labels: dict[str, int] = {}
variables: list[str] = []
macroses: dict[str, str] = {}
classes: dict[str, list[str, list[list[str, str]]]] = {}


def add(token: str, args: list[str]):
    Result.lines_counter += 1
    _in = ''
    for arg in args:
        _in += ' ' + str(arg)
    Result.result = token + _in  # + '\n'
    Result.lines.append(Result.result)


def find(string: str, it: list[str]):
    is_inside = False
    brackets_count = 0

    for i in range(0, len(string)):
        current = string[i]

        if current == '(': brackets_count += 1
        if current == ')': brackets_count -= 1

        if current == '"': is_inside = not is_inside

        if not is_inside and brackets_count <= 0:
            for s in it:
                if i + len(s) <= len(string) and string[slice(i, i + len(s))] == s:
                    Result.cont_i = i
                    return s
    Result.cont_i = -1
    return ''


def find_inversed(string: str, it: list[str]):
    is_inside = False
    brackets_count = 0

    for i in range(len(string), 0):
        current = string[i]

        if current == '(': brackets_count += 1
        if current == ')': brackets_count -= 1

        if current == '"': is_inside = not is_inside

        if not is_inside and brackets_count <= 0:
            for s in it:
                if i + len(s) <= len(string) and string[slice(i, i + len(s))] == s:
                    Result.cont_i = i
                    return s
    Result.cont_i = -1
    return ''


def split_istr(string: str, it: str, _max: int = -1):
    is_inside = False
    brackets_count = 0
    count = 0
    last = 0
    result: list[str] = []

    for i in range(0, len(string)):
        current = string[i]

        if current == '(': brackets_count += 1
        if current == ')': brackets_count -= 1

        if current == '"': is_inside = not is_inside

        if not is_inside and brackets_count <= 0:
            if i + len(it) <= len(string) and string[slice(i, i + len(it))] == it:
                result.append(string[slice(last, i)])
                count += 1
                last = i + len(it)
                if _max != -1 and count == _max: break

    result.append(string[slice(last, len(string))])
    return result


err_value_op = '__op_err__'


def functions(value: str, name: str):
    if startswith(value, 'get_flag'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]

        add('getflag', [name, get_value(_inside)])
        return name

    if startswith(value, 'get_block'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        x, y = split_istr(_inside, ',')

        add('getblock', ['block', name, get_value(x), get_value(y)])
        return name

    if startswith(value, 'get_building'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        x, y = split_istr(_inside, ',')

        add('getblock', ['building', name, get_value(x), get_value(y)])
        return name

    if startswith(value, 'get_ore'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        x, y = split_istr(_inside, ',')

        add('getblock', ['ore', name, get_value(x), get_value(y)])
        return name

    if startswith(value, 'get_floor'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        x, y = split_istr(_inside, ',')

        add('getblock', ['floor', name, get_value(x), get_value(y)])
        return name

    if startswith(value, 'spawn'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        team, unit, x, y, rot = split_istr(_inside, ',')

        add('spawn', [get_value(unit), get_value(x), get_value(y), get_value(rot), get_value(team), name])
        return name

    if startswith(value, 'fetch_build'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        team, block, link = split_istr(_inside, ',')

        add('fetch', ['build', name, get_value(team), get_value(link), get_value(block)])
        return name

    if startswith(value, 'fetch_core'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        team, link = split_istr(_inside, ',')

        add('fetch', ['core', name, get_value(team), get_value(link), '0'])
        return name

    if startswith(value, 'fetch_player'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        team, link = split_istr(_inside, ',')

        add('fetch', ['player', name, get_value(team), get_value(link), '0'])
        return name

    if startswith(value, 'fetch_unit'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        team, link = split_istr(_inside, ',')

        add('fetch', ['unit', name, get_value(team), get_value(link), '0'])
        return name

    if startswith(value, 'fetch_build_count'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        team, block = split_istr(_inside, ',')

        add('fetch', ['buildCount', name, get_value(team), '0', get_value(block)])
        return name

    if startswith(value, 'fetch_core_count'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]

        add('fetch', ['coreCount', name, get_value(_inside), '0', '0'])
        return name

    if startswith(value, 'fetch_player_count'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]

        add('fetch', ['playerCount', name, get_value(_inside), '0'])
        return name

    if startswith(value, 'fetch_unit_count'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]

        add('fetch', ['unitCount', name, get_value(_inside), '0'])
        return name

    if startswith(value, 'color'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        r, g, b, a = split_istr(_inside, ',')

        add('packcolor', [name, get_value(r), get_value(g), get_value(b), get_value(a)])
        return name

    if startswith(value, 'distance_radar'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        _from, order, type0, type1, type2 = split_istr(_inside, ',')

        add('radar', [get_value(type0), get_value(type1), get_value(type2), 'distance', get_value(_from), get_value(order), name])
        return name

    if startswith(value, 'health_radar'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        _from, order, type0, type1, type2 = split_istr(_inside, ',')

        add('radar', [get_value(type0), get_value(type1), get_value(type2), 'health', get_value(_from), get_value(order), name])
        return name

    if startswith(value, 'shield_radar'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        _from, order, type0, type1, type2 = split_istr(_inside, ',')

        add('radar', [get_value(type0), get_value(type1), get_value(type2), 'shield', get_value(_from), get_value(order), name])
        return name

    if startswith(value, 'armor_radar'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        _from, order, type0, type1, type2 = split_istr(_inside, ',')

        add('radar', [get_value(type0), get_value(type1), get_value(type2), 'armor', get_value(_from), get_value(order), name])
        return name

    if startswith(value, 'max_health_radar'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        _from, order, type0, type1, type2 = split_istr(_inside, ',')

        add('radar', [get_value(type0), get_value(type1), get_value(type2), 'maxHealth', get_value(_from), get_value(order), name])
        return name

    if startswith(value, 'unit_distance_radar'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        order, type0, type1, type2 = split_istr(_inside, ',')

        add('uradar', [get_value(type0), get_value(type1), get_value(type2), 'distance', '0', get_value(order), name])
        return name

    if startswith(value, 'unit_health_radar'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        order, type0, type1, type2 = split_istr(_inside, ',')

        add('uradar', [get_value(type0), get_value(type1), get_value(type2), 'health', '0', get_value(order), name])
        return name

    if startswith(value, 'unit_shield_radar'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        order, type0, type1, type2 = split_istr(_inside, ',')

        add('uradar', [get_value(type0), get_value(type1), get_value(type2), 'shield', '0', get_value(order), name])
        return name

    if startswith(value, 'unit_armor_radar'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        order, type0, type1, type2 = split_istr(_inside, ',')

        add('uradar', [get_value(type0), get_value(type1), get_value(type2), 'armor', '0', get_value(order), name])
        return name

    if startswith(value, 'unit_max_health_radar'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        order, type0, type1, type2 = split_istr(_inside, ',')

        add('uradar', [get_value(type0), get_value(type1), get_value(type2), 'maxHealth', '0', get_value(order), name])
        return name

    if startswith(value, 'unit_get_block'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        x, y, _type, floor = split_istr(_inside, ',')

        add('ucontrol', ['getBlock', get_value(x), get_value(y), _type.strip(), name, floor.strip()])
        return name

    if startswith(value, 'unit_inside'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        x, y, radius = split_istr(_inside, ',')

        add('ucontrol', ['getBlock', get_value(x), get_value(y), get_value(radius), name, '0'])
        return name

    if startswith(value, 'unit_locate_ore'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        ore, outx, outy = split_istr(_inside, ',')

        add('ulocate', ['ore', '0', '0', '0', get_value(ore), outx.strip(), outy.strip(), name, '0'])
        return name

    if startswith(value, 'unit_locate_build'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        _type, enemy, outx, outy, found = split_istr(_inside, ',')

        add('ulocate',
            ['building', get_value(_type), get_value(enemy), '0', outx.strip(), outy.strip(), found.strip(), name])
        return name

    if startswith(value, 'unit_locate_spawn'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        outx, outy, found = split_istr(_inside, ',')

        add('ulocate', ['spawn', '0', '0', '0', outx.strip(), outy.strip(), found, name])
        return name

    if startswith(value, 'unit_locate_damaged'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        outx, outy, found = split_istr(_inside, ',')

        add('ulocate', ['damaged', '0', '0', '0', outx.strip(), outy.strip(), found, name])
        return name

    if startswith(value, 'not'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]

        add('op', ['not', name, get_value(_inside), '0'])
        return name

    if startswith(value, 'max'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)
        _inside = _inside[1]
        _inside = _inside.rsplit(')', 1)[0]
        a, b = split_istr(_inside, ',')

        add('op', ['max', name, get_value(a), get_value(b)])
        return name

    if startswith(value, 'min'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        a, b = split_istr(_inside, ',')

        add('op', ['min', name, get_value(a), get_value(b)])
        return name

    if startswith(value, 'angle'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        a, b = split_istr(_inside, ',')

        add('op', ['angle', name, get_value(a), get_value(b)])
        return name

    if startswith(value, 'len'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        a, b = split_istr(_inside, ',')

        add('op', ['len', name, get_value(a), get_value(b)])
        return name

    if startswith(value, 'noise'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]
        a, b = split_istr(_inside, ',')

        add('op', ['noise', name, get_value(a), get_value(b)])
        return name

    if startswith(value, 'abs'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]

        add('op', ['abs', name, get_value(_inside), '0'])
        return name

    if startswith(value, 'log'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]

        add('op', ['log', name, get_value(_inside), '0'])
        return name

    if startswith(value, 'log10'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]

        add('op', ['log10', name, get_value(_inside), '0'])
        return name

    if startswith(value, 'floor'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]

        add('op', ['floor', name, get_value(_inside), '0'])
        return name

    if startswith(value, 'ceil'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]

        add('op', ['ceil', name, get_value(_inside), '0'])
        return name

    if startswith(value, 'sqrt'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]

        add('op', ['sqrt', name, get_value(_inside), '0'])
        return name

    if startswith(value, 'rand'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]

        add('op', ['rand', name, get_value(_inside), '0'])
        return name

    if startswith(value, 'sin'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]

        add('op', ['sin', name, get_value(_inside), '0'])
        return name

    if startswith(value, 'cos'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]

        add('op', ['cos', name, get_value(_inside), '0'])
        return name

    if startswith(value, 'tan'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]

        add('op', ['tan', name, get_value(_inside), '0'])
        return name

    if startswith(value, 'asin'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]

        add('op', ['asin', name, get_value(_inside), '0'])
        return name

    if startswith(value, 'acos'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]

        add('op', ['acos', name, get_value(_inside), '0'])
        return name

    if startswith(value, 'atan'):
        if name != err_value_op: Result.var_id += 1
        _inside = value.split('(', 1)[1].rsplit(')', 1)[0]

        add('op', ['atan', name, get_value(_inside), '0'])
        return name

    return value


def get_value(value: str):
    value = str(value).strip()

    name = '__op_' + str(Result.var_id) + '__'

    if value.startswith('(') and value.endswith(')'):
        return get_value(value[slice(1, len(value) - 1)])

    contains_word = find(value, ['=>', '<<<', '<<'])  # find math operators in val
    if Result.cont_i != -1:  # check contains
        Result.var_id += 1
        left, right = split_istr(value, contains_word, 1)
        left, right = get_value(left), get_value(right)

        if contains_word == '=>':
            add('lookup', [left, name, right])
            return name
        if contains_word == '<<':
            add('sensor', [name, right, left])
            return name
        if contains_word == '<<<':
            add('read', [name, right, left])
            return name

    contains0 = find(value, ["&&", '&', "||", "===", "==", "!==", "!=", "<=", ">=", "<", ">"])  # find boolean operators in val
    if Result.cont_i != -1:  # check contains
        Result.var_id += 1
        left, right = split_istr(value, contains0, 1)
        left, right = get_value(left), get_value(right)

        if contains0 == "&&":
            add('op', ['land', name, left, right])
            return name
        if contains0 == "&":
            add('op', ['and', name, left, right])
            return name
        if contains0 == "||":
            add('op', ['or', name, left, right])
            return name
        if contains0 == "!==":
            add('op', ['strictEqual', name, left, right])
            add('op', ['xor', name, name, '0'])
            return name
        if contains0 == "===":
            add('op', ['strictEqual', name, left, right])
            return name
        if contains0 == "==":
            add('op', ['equal', name, left, right])
            return name
        if contains0 == "!=":
            add('op', ['notEqual', name, left, right])
            return name
        if contains0 == "<=":
            add('op', ['lessThanEq', name, left, right])
            return name
        if contains0 == ">=":
            add('op', ['greaterThanEq', name, left, right])
            return name
        if contains0 == "<":
            add('op', ['lessThan', name, left, right])
            return name
        if contains0 == ">":
            add('op', ['greaterThan', name, left, right])
            return name

    contains1 = find(value, ["+", '-'])  # find basic math operators in val
    if Result.cont_i != -1:  # check contains
        Result.var_id += 1

        left, right = split_istr(value, contains1, 1)
        left, right = get_value(left), get_value(right)

        if contains1 == "+":
            add('op', ['add', name, left, right])
            return name
        if contains1 == "-":
            add('op', ['sub', name, left, right])
            return name

    contains = find(value, ["*", "//", "/", "^", "%"])  # find math operators in val
    if Result.cont_i != -1:  # check contains
        Result.var_id += 1
        left, right = split_istr(value, contains, 1)
        left, right = get_value(left), get_value(right)

        if contains == "*":
            add('op', ['mul', name, left, right])
            return name
        if contains == "/":
            add('op', ['div', name, left, right])
            return name
        if contains == "//":
            add('op', ['idiv', name, left, right])
            return name
        if contains == "^":
            add('op', ['pow', name, left, right])
            return name
        if contains == "%":
            add('op', ['mod', name, left, right])
            return name

    if value.startswith('#inv'):
        add('op', ['sub', name, '0', get_value(value.removeprefix('#inv'))])
        return name

    if value.startswith('!'):  # check contains
        value = value.removeprefix('!').lstrip()
        Result.var_id += 1

        add('op', ['xor', name, get_value(value), '1'])
        return name

    if value.startswith('#'):  # check contains
        value = value.removeprefix('#').lstrip()
        if value == 'mind_code_lines': return str(Result.lines_counter)

        Result.var_id += 1

        add('getlink', [name, get_value(value)])
        return name

    if value.startswith('$'):  # check contains
        value = value.removeprefix('$').lstrip()

        return value

    if value.startswith('@'):  # check @
        return value.replace('_', '-')

    # no math in val
    if macroses.__contains__(value):
        return get_value(macroses[value])
    else:
        return functions(value, name)


def startswith(string: str, prefix: str):
    return string[slice(0, len(prefix) + 1)].rstrip().rstrip('(').rstrip('=').rstrip('+').rstrip('-').rstrip(
        '*').rstrip('/').rstrip('%').rstrip('^') == prefix


def parse_line(line: str):
    line = line.strip()

    if startswith(line, 'var'):
        line = line.removeprefix('var')
        _inside = line.removeprefix('var')
        name, inside = _inside.split('=', 1)

        add('set', [name.strip(), get_value(inside)])
        variables.append(name.strip())

    if startswith(line, 'draw_flush'):
        line = line.removeprefix('draw_flush')

        add('drawflush', [get_value(line)])

    if startswith(line, 'print_flush'):
        line = line.removeprefix('print_flush')

        add('printflush', [get_value(line)])

    if startswith(line, 'print'):
        line = line.removeprefix('print')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        _inside = split_istr(_inside, ',')

        for out in _inside:
            add('print', [get_value(out)])

    if startswith(line, 'write'):
        line = line.removeprefix('write')
        it, cell, _id = split_istr(line, '>>')

        add('write', [get_value(it), get_value(cell), get_value(_id)])

    if startswith(line, 'wait'):
        line = line.removeprefix('wait')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]

        add('wait', [get_value(_inside)])

    if startswith(line, 'set_color'):
        line = line.removeprefix('set_color')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        unit, color = split_istr(_inside, ',')

        add('control', ['color', get_value(unit), get_value(color), '0', '0', '0'])

    if startswith(line, 'set_config'):
        line = line.removeprefix('set_config')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        unit, b = split_istr(_inside, ',')

        add('control', ['config', get_value(unit), get_value(b), '0', '0', '0'])

    if startswith(line, 'set_enabled'):
        line = line.removeprefix('set_enabled')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        unit, b = split_istr(_inside, ',')

        add('control', ['enabled', get_value(unit), get_value(b), '0', '0', '0'])

    if startswith(line, 'shoot_to'):
        line = line.removeprefix('shoot_to')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        unit, x, y, b = split_istr(_inside, ',')

        add('control', ['shoot', get_value(unit), get_value(x), get_value(y), get_value(b), '0'])

    if startswith(line, 'shoot_unit'):
        line = line.removeprefix('shoot_unit')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        unit, to, b = split_istr(_inside, ',')

        add('control', ['shootp', get_value(unit), get_value(to), get_value(b), '0', '0'])

    if startswith(line, 'draw_clear'):
        line = line.removeprefix('draw_clear')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        r, g, b = split_istr(_inside, ',')

        add('draw', ['clear', get_value(r), get_value(g), get_value(b), '0', '0', '0'])

    if startswith(line, 'draw_rgba'):
        line = line.removeprefix('draw_rgba')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        r, g, b, a = split_istr(_inside, ',')

        add('draw', ['color', get_value(r), get_value(g), get_value(b), get_value(a), '0', '0'])

    if startswith(line, 'draw_color'):
        line = line.removeprefix('draw_color')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]

        add('draw', ['col', get_value(_inside), '0', '0', '0', '0', '0'])

    if startswith(line, 'draw_stroke'):
        line = line.removeprefix('draw_stroke')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]

        add('draw', ['stroke', get_value(_inside), '0', '0', '0', '0', '0'])

    if startswith(line, 'draw_line'):
        line = line.removeprefix('draw_line')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        x1, y1, x2, y2 = split_istr(_inside, ',')

        add('draw', ['line', get_value(x1), get_value(y1), get_value(x2), get_value(y2), '0', '0'])

    if startswith(line, 'draw_rect'):
        line = line.removeprefix('draw_rect')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        x, y, x_size, y_size = split_istr(_inside, ',')

        add('draw', ['rect', get_value(x), get_value(y), get_value(x_size), get_value(y_size), '0', '0'])

    if startswith(line, 'draw_line_poly'):
        line = line.removeprefix('draw_line_poly')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        x, y, sides, radius, rotation = split_istr(_inside, ',')

        add('draw',
            ['linePoly', get_value(x), get_value(y), get_value(sides), get_value(radius), get_value(rotation), '0'])

    if startswith(line, 'draw_poly'):
        line = line.removeprefix('draw_poly')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        x, y, sides, radius, rotation = split_istr(_inside, ',')

        add('draw', ['poly', get_value(x), get_value(y), get_value(sides), get_value(radius), get_value(rotation), '0'])

    if startswith(line, 'draw_line_rect'):
        line = line.removeprefix('draw_line_rect')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        x, y, x_size, y_size = split_istr(_inside, ',')

        add('draw', ['lineRect', get_value(x), get_value(y), get_value(x_size), get_value(y_size), '0', '0'])

    if startswith(line, 'draw_triangle'):
        line = line.removeprefix('draw_triangle')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        x1, y1, x2, y2, x3, y3 = split_istr(_inside, ',')

        add('draw',
            ['triangle', get_value(x1), get_value(y1), get_value(x2), get_value(y2), get_value(x3), get_value(y3)])

    if startswith(line, 'draw_image'):
        line = line.removeprefix('draw_image')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        x, y, texture, size, rotation = split_istr(_inside, ',')

        add('draw',
            ['image', get_value(x), get_value(y), get_value(texture), get_value(size), get_value(rotation), '0'])

    if startswith(line, 'unit_bind'):
        line = line.removeprefix('unit_bind')

        add('ubind', [get_value(line)])

    if startswith(line, 'unit_idle'):
        line = line.removeprefix('unit_idle')

        add('ucontrol', ['idle', '0', '0', '0', '0', '0'])

    if startswith(line, 'unit_stop'):
        line = line.removeprefix('unit_stop')

        add('ucontrol', ['stop', '0', '0', '0', '0', '0'])

    if startswith(line, 'unit_move'):
        line = line.removeprefix('unit_move')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        args = split_istr(_inside, ',')
        x, y = args[0], args[1]

        if len(args) == 3:
            add('ucontrol', ['approach', get_value(x), get_value(y), get_value(args[2]), '0', '0'])
        else:
            add('ucontrol', ['move', get_value(x), get_value(y), '0', '0', '0'])

    if startswith(line, 'unit_boost'):
        line = line.removeprefix('unit_boost')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]

        add('ucontrol', ['boost', get_value(_inside), '0', '0', '0', '0'])

    if startswith(line, 'unit_shoot_to'):
        line = line.removeprefix('unit_shoot_to')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        x, y, b = split_istr(_inside, ',')

        add('ucontrol', ['target', get_value(x), get_value(y), get_value(b), '0', '0'])

    if startswith(line, 'unit_shoot_unit'):
        line = line.removeprefix('unit_shoot_unit')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        unit, b = split_istr(_inside, ',')

        add('ucontrol', ['target', get_value(unit), get_value(b), '0', '0', '0'])

    if startswith(line, 'unit_item_drop'):
        line = line.removeprefix('unit_item_drop')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        to, amount = split_istr(_inside, ',')

        add('ucontrol', ['target', get_value(to), get_value(amount), '0', '0', '0'])

    if startswith(line, 'unit_item_take'):
        line = line.removeprefix('unit_item_take')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        _from, item, amount = split_istr(_inside, ',')

        add('ucontrol', ['target', get_value(_from), get_value(item), get_value(amount), '0', '0'])

    if startswith(line, 'unit_pay_drop'):
        line = line.removeprefix('unit_pay_drop')

        add('ucontrol', ['payDrop', '0', '0', '0', '0', '0'])

    if startswith(line, 'unit_pay_take'):
        line = line.removeprefix('unit_pay_take')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]

        add('ucontrol', ['payTake', get_value(_inside), '0', '0', '0', '0'])

    if startswith(line, 'unit_pay_enter'):
        line = line.removeprefix('unit_pay_take')

        add('ucontrol', ['payEnter', '0', '0', '0', '0', '0'])

    if startswith(line, 'unit_mine'):
        line = line.removeprefix('unit_mine')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        x, y = split_istr(_inside, ',')

        add('ucontrol', ['mine', get_value(x), get_value(y), '0', '0', '0'])

    if startswith(line, 'unit_flag'):
        line = line.removeprefix('unit_flag')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]

        add('ucontrol', ['flag', get_value(_inside), '0', '0', '0', '0'])

    if startswith(line, 'unit_build'):
        line = line.removeprefix('unit_build')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        x, y, block, rot, config = split_istr(_inside, ',')

        add('ucontrol', ['mine', get_value(x), get_value(y), get_value(block), get_value(rot), get_value(config)])

    if startswith(line, 'unit_unbind'):
        line = line.removeprefix('unit_unbind')

        add('ucontrol', ['unbind', '0', '0', '0', '0', '0'])

    if startswith(line, 'set_block'):
        line = line.removeprefix('set_block')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        team, block, x, y, rot = split_istr(_inside, ',')

        add('setblock', ['block', get_value(block), get_value(x), get_value(y), get_value(team), get_value(rot)])

    if startswith(line, 'set_ore'):
        line = line.removeprefix('set_ore')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        block, x, y = split_istr(_inside, ',')

        add('setblock', ['ore', get_value(block), get_value(x), get_value(y), '0', '0'])

    if startswith(line, 'shock_unit'):
        line = line.removeprefix('shock_unit')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]

        add('status', ['false', 'shocked', get_value(_inside), '0'])

    if startswith(line, 'boss_unit'):
        line = line.removeprefix('boss_unit')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]

        add('status', ['false', 'boss', get_value(_inside), '0'])

    if startswith(line, 'apply_status'):
        line = line.removeprefix('apply_status')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        status, unit = split_istr(_inside, ',')

        add('status', ['false', get_value(status), get_value(unit), '0'])

    if startswith(line, 'remove_status'):
        line = line.removeprefix('remove_status')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        status, unit = split_istr(_inside, ',')

        add('status', ['true', get_value(status), get_value(unit), '0'])

    if startswith(line, 'spawn_wave'):
        line = line.removeprefix('spawn_wave')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        x, y, nat = split_istr(_inside, ',')

        add('spawnwave', [get_value(x), get_value(y), get_value(nat)])

    if startswith(line, 'set_map_area'):
        line = line.removeprefix('set_map_area')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        x, y, w, h = split_istr(_inside, ',')

        add('setrule', ['mapArea', get_value(x), get_value(y), get_value(w), get_value(h)])

    if startswith(line, 'set_rule'):
        line = line.removeprefix('set_rule')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        rule, x = split_istr(_inside, ',')

        add('setrule', [get_value(rule), get_value(x), '0', '0', '0'])

    if startswith(line, 'set_team_rule'):
        line = line.removeprefix('set_team_rule')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        team, rule, x = split_istr(_inside, ',')

        add('setrule', [get_value(rule), get_value(x), get_value(team), '0', '0'])

    if startswith(line, 'cutscene_pan'):
        line = line.removeprefix('cutscene_pan')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        x, y, speed = split_istr(_inside, ',')

        add('cutscene', ['pan', get_value(x), get_value(y), get_value(speed), '0'])

    if startswith(line, 'cutscene_zoom'):
        line = line.removeprefix('cutscene_zoom')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]

        add('cutscene', ['zoom', get_value(_inside), '0', '0', '0'])

    if startswith(line, 'cutscene_stop'):
        line = line.removeprefix('cutscene_stop')

        add('cutscene', ['stop', '0', '0', '0', '0'])

    if startswith(line, 'explosion'):
        line = line.removeprefix('explosion')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        team, x, y, radius, damage, flying, ground, pierce = split_istr(_inside, ',')

        add('explosion', [get_value(team), get_value(x), get_value(y), get_value(radius), get_value(damage), get_value(flying), get_value(ground), get_value(pierce)])

    if startswith(line, 'set_rate'):
        line = line.removeprefix('set_rate')

        add('setrate', [get_value(line)])

    if startswith(line, 'set_flag'):
        line = line.removeprefix('set_flag')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        flag, b = split_istr(_inside, ',')

        add('setflag', [get_value(flag), get_value(b)])

    if startswith(line, 'flush_notify'):
        line = line.removeprefix('flush_notify')

        add('message', ['notify', '0'])

    if startswith(line, 'flush_mission'):
        line = line.removeprefix('flush_mission')

        add('message', ['mission', '0'])

    if startswith(line, 'flush_announce'):
        line = line.removeprefix('flush_announce')

        add('message', ['announce', get_value(line)])

    if startswith(line, 'flush_toast'):
        line = line.removeprefix('flush_toast')

        add('message', ['toast', get_value(line)])

    if startswith(line, 'goto'):
        line = line.removeprefix('goto')
        _inside = line.lstrip().rstrip()

        if labels.__contains__(_inside):
            add('jump', [labels[_inside], 'always', '0', '0'])
        else:
            add('jump', ['__' + _inside + '_change_label__', 'always', '0', '0'])

    if startswith(line, '#macro'):
        line = line.removeprefix('#macro')
        name, _inside = line.split(':', 1)

        macroses[name.strip()] = _inside.strip()

    if startswith(line, 'class'):
        line = line.removeprefix('class')
        name, _inside = line.split('(', 1)
        _inside = _inside.rsplit(')', 1)[0]
        _vars = split_istr(line.split('{', 1)[1].rsplit('}', 1)[0], ',')

        _list: list[list[str, str]] = []
        for var in _vars:
            vname, vid = split_istr(var, ':')
            add('read', [name.strip() + '_' + vname.strip(), _inside.strip(), vid.strip()])
            _list.append([vname.strip(), vid.strip()])
        classes[name] = [_inside.strip(), _list]

    # if startswith(line, 'continue'):
    #     Result.special_brackets_counter.reverse()
    #     for spec in Result.special_brackets_counter:
    #         if spec[2] and spec[1] == 0:
    #             if spec[0] == 'for':
    #                 parse_line(spec[5])
    #                 add('jump', [str(spec[3]), 'equal', str(get_value(spec[4])), 'true'])
    #                 break
    #
    #     Result.special_brackets_counter.reverse()

    if startswith(line, 'if'):
        line = line.removeprefix('if')
        _inside, _line = line.split('(', 1)[1].rsplit(')', 1)

        val = get_value(_inside)

        Result.special_brackets_counter.append(['if', 0, True, Result.lines_counter, val])
        add('jump', ['', 'equal', val, 'false'])

    if startswith(line, 'for'):
        line = line.removeprefix('for')
        _inside = line.split('(', 1)[1].rsplit(')', 1)[0]
        v, b, a = split_istr(_inside, ';')

        parse_line(v)
        Result.special_brackets_counter.append(['for', 0, True, Result.lines_counter, b, a])

    if startswith(line, 'stop'):
        line = line.removeprefix('stop')
        add('stop', [])
    if startswith(line, 'end'):
        line = line.removeprefix('end')
        add('end', [])

    if line.startswith(':'):
        line = line.removeprefix(':')
        labels[line] = Result.lines_counter
        i = 0
        for l in Result.lines:
            Result.lines[i] = l.replace('__' + line + '_change_label__', str(Result.lines_counter))
            i += 1

    while line.startswith('}'):
        result = []
        for spec in Result.special_brackets_counter:
            spec[1] -= 1
            if spec[2] and spec[1] == 0:
                #def as_if():
                if spec[0] == 'if':
                    i = spec[3]
                    Result.lines[i] = Result.lines[i][slice(0, 5)] + str(Result.lines_counter) + Result.lines[i][
                        slice(5, len(Result.lines[i]))]

                    check = line.removeprefix('}').lstrip()
                    if startswith(check, 'else'):
                        result.append(['else', 0, True, Result.lines_counter])
                        add('jump', ['', 'notEqual', get_value(spec[4]), 'false'])
                if spec[0] == 'else':
                    i = spec[3]
                    Result.lines[i] = Result.lines[i][slice(0, 5)] + str(Result.lines_counter) + Result.lines[i][
                        slice(5, len(Result.lines[i]))]

                if spec[0] == 'for':
                    parse_line(spec[5])
                    add('jump', [str(spec[3]), 'equal', str(get_value(spec[4])), 'true'])
            else: result.append(spec)
        Result.special_brackets_counter = result
        line = line.removeprefix('}')

    if line.endswith('{'):
        for spec in Result.special_brackets_counter:
            spec[1] += 1

    for var in variables:
        if startswith(line, var):
            contains = find(line, ['=', '++', '--', '+=', '-=', '*=', '/=', '//=', '%=', '^='])
            name = line[slice(Result.cont_i)].strip()  # get all left
            inside = '1'
            if contains != '++' and contains != '--':
                inside = get_value(line[slice(Result.cont_i + len(contains), len(line))])  # get all right
            else:
                if contains == '++':
                    contains = '+='
                if contains == '--':
                    contains = '-='

            if contains == '=':
                add('set', [name, get_value(inside)])
            else:
                if contains == "+=":
                    add('op', ['add', name, name, inside])
                if contains == "-=":
                    add('op', ['sub', name, name, inside])
                if contains == "*=":
                    add('op', ['mul', name, name, inside])
                if contains == "/=":
                    add('op', ['div', name, name, inside])
                if contains == "//=":
                    add('op', ['idiv', name, name, inside])
                if contains == "^=":
                    add('op', ['pow', name, name, inside])
                if contains == "%=":
                    add('op', ['mod', name, name, inside])
            line = line.removeprefix(var)

    for n_class in classes.keys():
        _class = classes[n_class]
        for arg in _class[1]:
            n = n_class + '.' + arg[0]
            if startswith(line, n):
                line = line.removeprefix(n)
                _inside = line.split('<<', 1)[1]
                add('write', [get_value(_inside), get_value(_class[0]), get_value(arg[1])])
                break

    for macro in macroses.keys():
        if line.startswith(macro):
            _inside = split_istr(macroses[macro], '~')

            _inside = _inside

            for __l in _inside: parse_line(__l)

    functions(line, err_value_op)


code = ''
for file_line in file:
    if file_line.lstrip().startswith('//'): continue
    for l in split_istr(file_line, '->'):
        if l.strip() == '': continue
        if l.lstrip().startswith('<-'):
            code = code.removesuffix('\n')
            l = l.split('<-', 1)[1]

        if l.endswith('\n'): code += l
        else: code += l + '\n'

code = split_istr(code, '\n')
Result.code = code

__i = 0
for value in code:
    Result.current_code = __i
    Result.next = code[min(__i+1, len(code)-1)]
    parse_line(value)
    Result.old = value
    __i += 1

add('end', [])

for res in Result.lines: print(res)
