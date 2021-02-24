

def cutting_string1(w1,w2):
    return w1.replace(w2 , "").strip()

def cutting_string2(w1,w2):
    list1 = w1.split(" ")
    list2 = w2.split(" ")
    list3 = []
    for item in list1:
        if item not in list2:
            list3.append(item)

    return list3

def list_to_string(list1):

    return " ".join(list1)


# MAIN

word1 = "first example cefi nesto kako hehe maco"
word2 = "first cefi"

final1 = cutting_string1(word1,word2)
final2 = cutting_string2(word1,word2)
final3 = list_to_string(final2)
print(final1)
print(final2)
print(final3)
