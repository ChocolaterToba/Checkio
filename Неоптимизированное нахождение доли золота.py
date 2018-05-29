from fractions import Fraction


METALS = ('gold', 'tin', 'iron', 'copper')


def checkio(alloys):
    result = 0
    for metal in METALS:
        if all(metal + '-' + another_metal in alloys or
               another_metal + '-' + metal in alloys
               for another_metal in METALS if another_metal != metal):
            for i in range(4):
                if METALS[i] != metal:
                    if metal + '-' + METALS[i] in alloys:
                        result += alloys[metal + '-' + METALS[i]]
                    else:
                        result += alloys[METALS[i] + '-' + metal]
            amount = Fraction((result - 1) / 2)
            if metal != 'gold':
                if metal + '-gold' in alloys:
                    return Fraction(alloys[metal + '-gold'] - amount)
                else:
                    return Fraction(alloys['gold-' + metal] - amount)
                return amount
    else:
        for i in METALS:
            for k in METALS:
                for n in METALS:
                    if i != k and k != n and result == 0:
                        if ((i + '-' + k in alloys or k + '-' + i in alloys) and
                        (i + '-' + n in alloys or n + '-' + i in alloys) and
                        (n + '-' + k in alloys or k + '-' + n in alloys)):
                                if i + '-' + k in alloys:
                                    result += alloys[i + '-' + k]
                                else:
                                    result += alloys[k + '-' + i]
                                if i + '-' + n in alloys:
                                    result += alloys[i + '-' + n]
                                else:
                                    result += alloys[n + '-' + i]
                                if n + '-' + k in alloys:
                                    result += alloys[n + '-' + k]
                                else:
                                    result += alloys[k + '-' + n]
                                amount = Fraction(1 - result / 2)
                                for a in METALS:
                                    if a != n and a != k and a != i:
                                        metal = a
                                if i == 'gold':
                                    if n + '-' + k in alloys:
                                        final_result = alloys[n + '-' + k]
                                    else:
                                        final_result = alloys[k + '-' + n]
                                elif n == 'gold':
                                    if i + '-' + k in alloys:
                                        final_result = alloys[i + '-' + k]
                                    else:
                                        final_result = alloys[k + '-' + i]
                                elif k == 'gold':
                                    if n + '-' + i in alloys:
                                        final_result = alloys[n + '-' + i]
                                    else:
                                        final_result = alloys[i + '-' + n]
                                if metal != 'gold':
                                    return Fraction(1 - final_result - amount)
                                return amount
