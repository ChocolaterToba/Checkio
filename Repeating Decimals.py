def convert(numerator, denominator):
    result = str(numerator // denominator) + '.'
    remainders = [numerator % denominator]
    while 0 not in remainders:
        numerator = numerator % denominator * 10
        result += str(numerator // denominator)
        if numerator % denominator in remainders:
            i = remainders.index(numerator % denominator)
            return result[:i + 2] + '(' + result[i + 2:] + ')'
        remainders += [numerator % denominator]
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"
