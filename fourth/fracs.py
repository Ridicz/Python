from fractions import gcd


def add_frac(frac1, frac2):
    common_denominator = frac1[1] * frac2[1]
    common_denominator /= gcd(frac1[1], frac2[1])

    common_frac1 = [frac1[0] * common_denominator / frac1[1], frac1[1] * common_denominator / frac1[1]]
    common_frac2 = [frac2[0] * common_denominator / frac2[1], frac2[1] * common_denominator / frac2[1]]

    result_frac = [common_frac1[0] + common_frac2[0], common_denominator]

    wsp = gcd(result_frac[0], result_frac[1])

    result_frac[0] /= wsp
    result_frac[1] /= wsp

    return result_frac


def sub_frac(frac1, frac2):
    minus_frac = list([-frac2[0], frac2[1]])
    return add_frac(frac1, minus_frac)


def mul_frac(frac1, frac2):
    numerator = frac1[0] * frac2[0]
    denumerator = frac1[1] * frac2[1]

    divider = gcd(numerator, denumerator)

    result_frac = [numerator / divider, denumerator / divider]

    return result_frac


def div_frac(frac1, frac2):
    inverted_frac = [frac2[1], frac2[0]]

    return mul_frac(frac1, inverted_frac)


def is_positive(frac):
    return frac[0] * frac[1] > 0


def is_zero(frac):
    return frac[0] == 0


def cmp_frac(frac1, frac2):
    result_frac = sub_frac(frac1, frac2)

    if is_positive(result_frac):
        return 1
    elif is_zero(result_frac):
        return 0
    return -1


def frac2float(frac):
    return float(float(frac[0]) / float(frac[1]))
