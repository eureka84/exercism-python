def slices(series, length):
    if len(series) < length:
        raise ValueError("cannot extract slices of length {} from series {}".format(length, series))
    if length < 1:
        raise ValueError("slices length cannot be less than 1")
    candidates = [series[i:i+length] for i in range(0, len(series))]
    return filter(lambda c: len(c) == length, candidates)
