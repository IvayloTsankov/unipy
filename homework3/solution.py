
nacci():
    current_number, next_number = 1, 1

    while True:
        yield current_number
        current_number, next_number = next_number, current_number + next_number


def primes():
    def is_prime(n):
        if n <= 3:
            return n >= 2
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    number = 0
    while True:
        number += 1
        if is_prime(number):
            yield number


def alphabet(code=None, letters=None):
    if letters:
        for letter in letters:
            yield letter

        # if both letters and code are defined this will ignore code
        return StopIteration
    else:
        lower_bound = 0x61 if code == "lat" else 0x430  # else "bg"
        upper_bound = 0x7B if code == "lat" else 0x450  # else "bg"

        for letter_hex in range(lower_bound, upper_bound):
            # 0x44D and 0x44B are from russian alphabet
            if letter_hex != 0x44D or letter_hex != 0x44B:
                yield chr(letter_hex)

        return StopIteration


def intertwined_sequences(configurations, generator_definitions=[]):
    def get_generator(name):
        return globals()[name]

    generators = {}
    for config in configurations:
        name = config["sequence"]
        length = config["length"]
        del(config["sequence"])
        del(config["length"])

        # create generator from definition on the fly
        if name in generator_definitions and name not in generators:
            if len(config) == 0:
                generators[name] = iter(generator_definitions[name]())
            else:
                generators[name] = iter(
                    generator_definitions[name](*config.values()))

        # create generator if not exists
        if name not in generators:
            if len(config) == 0:
                generators[name] = get_generator(name)()
            else:
                generators[name] = get_generator(name)(config_params)

        generator = generators[name]

        for i in range(length):
            yield(next(generator))

    return StopIteration
