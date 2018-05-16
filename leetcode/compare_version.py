# given version1 and version 2 compare which one is a later version


def compare_version(version1, version2):
    v1 = version1.split(".")
    v2 = version2.split(".")

    length = min(len(v1), len(v2))
    i = 0
    while i < length:
        if int(v1[i]) < int(v2[i]):
            return -1
        elif int(v1[i]) > int(v2[i]):
            return 1
        else:
            i += 1
    if len(v1) > len(v2) and convert(v1[i:]):
        return 1
    elif len(v1) < len(v2) and convert(v2[i:]):
        return -1
    else:
        return 0

def convert(version):
    count = 0
    for num in version:
        count += int(num)
    return count > 0 

