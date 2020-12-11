import sys

def accumulate(state, arg):
    state[1] += arg
    state[0] += 1

def jump(state, arg):
    state[0] += arg

def incindex(state, arg):
    state[0] += 1

instructions = {
    'acc': accumulate,
    'jmp': jump,
    'nop': incindex,
}

def run(program):
    visited = [False] * len(program)
    # state is [current instruction number, accumulator value, loop detected]
    state = [0, 0, False]
    while state[0] < len(program):
        # print(f'idx {state[0]} acc {state[1]}')
        if visited[state[0]]: 
            state[2] = True
            break
        visited[state[0]] = True
        instr = program[state[0]][:3]
        arg = int(program[state[0]][4:])
        instructions[instr](state, arg)
    return state

input = [line.strip() for line in sys.stdin]

# part 1 - 1137
state = run(input)
print(state[1])

# part 2 - 1125
for i,line in enumerate(input):
    if line[:3] == 'nop' or line[:3] == 'jmp':
        newinstr = 'nop' if line[:3] == 'jmp' else 'jmp'
        modified = list(input)
        modified[i] = newinstr + line[3:]
        st = run(modified)
        if not st[2]:
            print(f'changing {line} at {i} completed with acc {st[1]}')
            break
