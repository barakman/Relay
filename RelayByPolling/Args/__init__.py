from sys import argv


Args = {}


if len(argv) > 0:
    with open(argv[1]) as file:
        for line in file:
            words = line.split()
            if len(words) > 1:
                Args[words[0]] = words[1]
