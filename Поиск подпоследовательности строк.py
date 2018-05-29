from functools import lru_cache


# lru_cache is needed for optimisation.
@lru_cache(maxsize=None)
def common(first, second):
    # Returning '' if one of the strings is emptyrt.
    if not (len(first) and len(second)):
            return ''
    result = ''
    # Checking if the last symbols of both strings are equal.
    while first[-1] == second[-1]:
        result = first[-1] + result
        first, second = first[:-1], second[:-1]
        # Returning result if one of the strings is empty
        if not first or not second:
            return result
    # Getting results of common with both strings without theit\r last symbol.
    result1 = common(first[:-1], second).split(',')
    result2 = common(first, second[:-1]).split(',')
    final = []
    # Appending the biggest string(strings) to final.
    if len(result1[0]) >= len(result2[0]):
        for item in result1:
            final += [item + result]
    if len(result1[0]) <= len(result2[0]):
        for item in result2:
            final += [item + result]
    # Returning final result.
    return ','.join(sorted(list(set(final))))
print(common("GTCGCTGTGCAGGTCCGGGTTCA",
             "GCGACCCGAATCCAGCTATAGGTATATGTCAGTCGGCCGTTAGGT"))