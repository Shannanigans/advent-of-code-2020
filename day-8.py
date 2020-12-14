def get_data(filename="day-8-data.txt"):
    for line in open(filename, "r"):
        yield line.strip()


def clean(dirty_string):
    op, value = dirty_string.split(" ")
    return (op, int(value))


get_instructions = lambda data: [clean(x) for x in data]


def get_new_index(op, value, index, accumulator):
    if op == "nop":
        return index + 1, accumulator
    if op == "acc":
        return index + 1, accumulator + value
    if op == "jmp":
        return index + value, accumulator


def process_instructions(instructions, index=0, accumulator=0, index_history=[]):
    if index in index_history:
        return (accumulator, False)

    if index >= len(instructions):
        return (accumulator, True)

    index_history += [index]
    op, value = instructions[index]
    new_index, accumulator = get_new_index(op, value, index, accumulator)
    accumulator, status = process_instructions(
        instructions, new_index, accumulator, index_history
    )
    return (accumulator, status)


def mod_instructions(instructions):
    for index, instruction in enumerate(instructions):
        op, value = instruction
        new_instruction = instruction
        if op == "jmp":
            new_instruction = ("nop", value)
        if op == "nop":
            new_instruction = ("jmp", value)
        if new_instruction != instruction:
            new_instructions = [*instructions]
            new_instructions[index] = new_instruction
            yield new_instructions


# PART 1
# print(process_instructions(get_instructions(get_data())))

# PART 2
instructions = get_instructions(get_data())
mod_instructions_generator = mod_instructions(instructions)
for new_instructions in mod_instructions_generator:
    accumulator, status = process_instructions(
        new_instructions, index=0, accumulator=0, index_history=[]
    )
    if status:
        print(accumulator)
