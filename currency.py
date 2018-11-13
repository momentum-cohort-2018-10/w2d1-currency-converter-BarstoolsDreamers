def convert(rates, value, current, to):
    if current == to:
        return value

    conversion_rate = get_converstion_rate(rates, current, to)
    if conversion_rate is None:
        raise ValueError(f"can't convert from {current} to {to}")


def convert(rates, value, current, to):
    for conversion in rates:
        if current in conversion and to in conversion:
            if current == conversion(0):
                return value * conversion[2]
    return value


def convert(rates, value, current, to):
    for conversion in rates:
        if current == conversion[0] and to == conversion[1]:
            return value * conversion[2]
        if current == conversion[1] and to == conversion[0]:
            return value / conversion[2]


raise ValueError(f"can't convert from {current} to {to}")
