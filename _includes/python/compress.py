
def compress(ar):
    n = len(ar)

    sorted_ar = sorted(set(ar))
    zip = {}
    i = 0
    for x in sorted_ar:
        zip[x] = i
        i += 1



    return [zip[a] for a in ar]
