# Author: JD 01/13/2022


def smash(lst):
    sentence = ""
    for i, v in enumerate(lst):
        if i == 0:
            sentence = sentence + v
        else:
            sentence = sentence + " " + v

    return sentence

x = smash(["I", "have", "a", "pen"])
print(x)