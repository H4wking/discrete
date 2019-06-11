def grammar_type(rules):
    """
    Determine the type of given ruleset in Chomsky hierarchy. Start symbol is S. Empty word(lambda) is L.

    >>> grammar_type([("S", "aA"), ("A", "a"), ("A", "b")])
    3

    :param rules: list of rules
    :return: int representing grammar type
    """
    for rule in rules:
        if len(rule[0]) > len(rule[1]):
            return 0
    for rule in rules:
        if len(rule[0]) != 1 or rule[0] != rule[0].upper():
            return 1
    for rule in rules:
        if rule != ("S", "L") and \
           (len(rule[1]) > 2 or
           (len(rule[1]) == 2 and (rule[1][0] != rule[1][0].lower() or rule[1][1] != rule[1][1].upper())) or
           (len(rule[1]) == 1 and rule[1] != rule[1].lower())):
            return 2
    return 3


if __name__ == "__main__":
    rules = []
    while True:
        lhs = str(input("Enter left-hand-side of the rule or press Enter to finish: "))
        if lhs == "":
            break
        rhs = str(input("Enter right-hand-side of the rule: "))
        rules.append((lhs, rhs))
    print("Given ruleset is type {} in Chomsky hierarchy.".format(grammar_type(rules)))
