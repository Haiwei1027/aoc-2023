
def test(solver, test_filepath, id=None):
    #get input and expected results
    tests = {}
    
    with open(test_filepath,"r") as tests_file:
        lines = [l.replace("\n","") for l in tests_file.readlines()]
        markers = [i for i,l in enumerate(lines) if l.strip() == "[test]"]
        for i,marker in enumerate(markers):
            if i == len(markers)-1:
                tests[lines[marker+1]] = lines[marker+2:]
            else:
                tests[lines[marker+1]] = lines[marker+2:markers[i+1]]
                pass
            pass
        pass
    print(f"loaded {len(tests)} tests")
    #run tests and print outcome
    for expected in tests:
        if id != None:
            if expected != str(id):
                continue
        result = str(solver(tests[expected]))
        if result == expected:
            print(f"{expected} passed")
        else:
            print(f"{expected} failed, got {result} instead")
    pass

def testp1(solver, day, id=None):
    test(solver, f"day{day}/test1.txt", id=id)
    pass

def testp2(solver, day, id=None):
    test(solver, f"day{day}/test2.txt", id=id)
    pass