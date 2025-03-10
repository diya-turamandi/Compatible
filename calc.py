import re

def if_length_two(l1: list):
    for index, value in enumerate(l1):
        if len(str(value)) > 1:
            rem = value % 10
            l1[index] = value // 10
            l1.insert(index + 1, rem)
    return l1



def compCompatibility(name1:str,name2:str):
    name1 : str = name1.lower().strip().replace(" ", "")
    name2 : str = name2.lower().strip().replace(" ", "")

    # name1: str = re.sub(r"\s+", "", name1.lower())
    # name2: str = re.sub(r"\s+", "", name2.lower())

   
    if not (name1.isalpha() and name2.isalpha()):
        raise ValueError
    dict = {}
    for i in name1 + 'loves' + name2 :
        if i not in dict :
            dict[i] = 1
        else:
            dict[i] += 1
    values = list(dict.values())
    values = if_length_two(values)
    values2 = values

    while len(values) > 2:
        values = []
        for i in range(len(values2)//2):
            watch = values2[i]+values2[-(i+1)]
            values.append(values2[i]+values2[-(i+1)])
        if len(values2) % 2 != 0:
            values.append(values2[len(values2)//2])
        values = if_length_two(values)
        values2 = values


    return values[0]*10+values[1]


if __name__ == "__main__": 
    print(compCompatibility(name2=' pooja ',name1='aditya'))


