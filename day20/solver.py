LOW = 0
HIGH = 1
from math import gcd

def parse_modules(input_data):
    modules_configuration = {}
    modules_state = {}
    
    for line in input_data:
        label,destinations = line.replace(" ","").split("->")
        module_type = None
        if label[0] == '%' or label[0] == "&":
            module_type = label[0]
            label = label[1:]
        modules_configuration[label] = (module_type,destinations.split(","))
        
        if module_type == '%':
            modules_state[label] = False
        elif module_type == '&':
            modules_state[label] = {}
        pass
    
    for config in modules_configuration:
        for destination in modules_configuration[config][1]:
            if destination not in modules_state:
                continue
            if modules_configuration[destination][0] == '&':
                modules_state[destination][config] = LOW
                pass
            pass
        pass
    return modules_configuration, modules_state

def hash_state(state):
    hash = ""
    for key in state:
        hash += f"{key} {state[key]}"

def press_button(configuration,state,n,history={}):
    signals = []
    lows = 1
    highs = 0
    initial_state = {}
    for b in configuration["broadcaster"][1]:
        signals.append((b,LOW,None))
    while len(signals) != 0:
        label,level,sender = signals.pop(0)
        #print(f"{sender} {level} -> {label} | {state}")
        if level == LOW:
            lows += 1
        else:
            highs += 1
        if label not in configuration:
            continue
        if configuration[label][0] == '%':
            if level == HIGH:
                continue
            else:
                pulse = LOW
                if not state[label]:
                    pulse = HIGH
                    if label not in history:
                        history[label] = n
                state[label] = not state[label]
                for destination in configuration[label][1]:
                    signals.append((destination,pulse,label))
                    pass
                pass
        elif configuration[label][0] == '&':
            state[label][sender] = level
            pulse = LOW
            for other_sender in state[label]:
                if state[label][other_sender] == LOW:
                    pulse = HIGH
                    if label not in history:
                        history[label] = n
                    break
            
            for destination in configuration[label][1]:
                signals.append((destination,pulse,label))
                pass
        pass
    #print(f"highs : {highs} lows : {lows}")
    return highs,lows

def part1(input_data):
    modules_configuration,modules_state = parse_modules(input_data)
    print(modules_configuration)
    print(modules_state)
    highs = 0
    lows = 0
    for i in range(1000):
        result = press_button(modules_configuration,modules_state)
        #print(modules_state)
        highs += result[0]
        lows += result[1]
    return highs * lows

def find_when(label,configuration, history):
    lcm = 1
    for sender in configuration:
        if configuration[sender][1] == None:
            print(f"{label} {sender} {configuration[sender]}")
        if label in configuration[sender][1]:
            print(f"{sender} -> {label}")
            when_label = history[sender]
            lcm = lcm*when_label//gcd(lcm, when_label)
    return lcm

def part2(input_data):
    modules_configuration,modules_state = parse_modules(input_data)
    print(modules_configuration)
    print(modules_state)
    modules_configuration["rx"] = ("%",[])
    modules_state["rx"] = False
    history = {}
    for i in range(100000):
        press_button(modules_configuration,modules_state,i+1,history=history)
    for key in history:
        print(f"{key} {history[key]}")
    final = find_when("hj",modules_configuration,history)
    return final
    
