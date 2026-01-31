def nested_dict_from_strings(words):
    result = {}

    for w in words:
        length = len(w)
        parity = "even" if length % 2 == 0 else "odd"
        result[w] = {"length": length, "parity": parity}

    return result


"""

This is an example run 



"""

strings = ["data", "science"]
print(nested_dict_from_strings(strings))

