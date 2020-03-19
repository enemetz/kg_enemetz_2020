import sys


def isMappable(string1, string2):
    dict = {}

    # Only mappable if string1 is shorter than string2
    if len(string1) > len(string2):
        return False

    # iterate through string1, place character in dict. If in dictionary, return false
    for i in range(len(string1)):
        if string1[i] not in dict:
            dict[string1[i]] = string2[i]
        else:
            return False
    return True


if __name__ == "__main__":
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    print(isMappable(str1, str2))
