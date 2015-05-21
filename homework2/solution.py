ct_type(zipped_symbols, extract_type):
    extracted = ""

    for zipped_info in zipped_symbols:
        if type(zipped_info[0]) is extract_type:
            extracted += str(zipped_info[0]) * zipped_info[1]

    return extracted


def reversed_dict(dictionary):
    return {value: key for key, value in dictionary.items()}


def flatten_dict_rec(dictionary, flatten, parrent):
    for key, value in dictionary.items():
        if type(value) is dict:
            flatten_dict_rec(value, flatten, parrent + key + ".")
        else:
            flatten[parrent + key] = value


def flatten_dict(dictionary):
    flatten = {}
    flatten_dict_rec(dictionary, flatten, "")
    return flatten


def unflatten_dict(dictionary):
    unflatten = {}

    for key, value in dictionary.items():
        key_parts = key.split(".")

        # this loop starts with the root dictionary
        d = unflatten

        # add new dictionary and go deep in child
        # dict if needed
        for part in key_parts[:-1]:
            if part not in d:
                d[part] = dict()
            d = d[part]

        d[key_parts[-1]] = value

    return unflatten


def reps(sequence):
    return tuple(
        [element for element in sequence if sequence.count(element) > 1]
    )
