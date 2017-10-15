print('Apriori Algorithm')

ds = []
item_list = {}

with open('adata.txt', 'r') as f:
    for l in f:
        temp = l.replace('\n','').split(sep=' ')
        ds.append(temp)
        for item in temp:
            if item in list(item_list.keys()):
                item_list[item] += 1
            else:
                item_list[item] = 1

print(item_list)

support = int(input('Enter the support value: '))

def delete_from_list():
    temp = []
    for item in item_list:
        if item_list[item] < support:
            temp.append(item)

    for t in temp:
        del item_list[t]


def get_new_keys(i):
    keys = []
    for key in item_list:
        if type(key) is str:
            keys.append(key)
        else:
            keys += key
    from itertools import combinations
    keys = list(combinations(list(set(keys)), i))
    return keys


def get_new_list(new_keys):
    temp_list = {}
    for trans in ds:
        for key in new_keys:
            if set(key).issubset(set(trans)):
                if key in temp_list.keys():
                    temp_list[key] += 1
                else:
                    temp_list[key] = 1
    return temp_list


i = 1
prev_list = {}
while len(item_list) > 1:
    delete_from_list()
    print(item_list)
    print('\n')
    if len(set(prev_list.items())) == len(set(item_list.items())):
        break
    i += 1
    new_keys = get_new_keys(i)
    item_list = get_new_list(new_keys)
    prev_list = dict(item_list)
