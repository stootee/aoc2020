import re

id_keys = {'byr': {'required': True, 'rule': '(^19[2-9][0-9])$|^200[0-2]$'},
           'iyr': {'required': True, 'rule': '(^201[0-9])$|^2020$'},
           'eyr': {'required': True, 'rule': '(^202[0-9])$|^2030$'},
           'hgt': {'required': True, 'rule': '(^(1[5-8][0-9]|19[0-3])cm$)|^(59|6[0-9]|7[0-6])in$'},
           'hcl': {'required': True, 'rule': '^#[0-9a-f]{6}'},
           'ecl': {'required': True, 'rule': '^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$'},
           'pid': {'required': True, 'rule': '^[0-9]{9}$'},
           'cid': {'required': False}
           }


def pair(pair_string):
    return {pair_string.split(':')[0]: pair_string.split(':')[1]}


def is_valid1(id_dict):
    return {k for k in id_keys.keys() if id_keys[k]['required']}.issubset(set(id_dict.keys()))


def is_valid2(id_dict):
    valid_count = 0
    for k in [k for k in id_keys.keys() if id_keys[k]['required']]:
        if k in id_dict.keys():
            if re.search(id_keys[k]['rule'], id_dict[k]):
                valid_count += 1

            id_dict[k] = (id_dict[k], re.search(id_keys[k]['rule'], id_dict[k]))
    return valid_count > 6, id_dict


if __name__ == '__main__':
    with open('day4.txt', 'r') as fl:
        inp = fl.read().replace('\n\n', '|').replace('\n', ' ').split('|')

    dictionaries = []
    for x in inp:
        d = {}
        for ps in x.split():
            d.update(pair(ps))
        dictionaries.append(d)

    # Part 1
    valid_id_list = []
    invalid_id_list = []
    for d in dictionaries:

        vld = is_valid1(d)
        if vld:
            valid_id_list.append(d)
        else:
            invalid_id_list.append(d)

    print(len(valid_id_list))

    # Part 2
    valid_id_list = []
    invalid_id_list = []
    for d in dictionaries:
        vld, dict_with_rules = is_valid2(d)

        if vld:
            valid_id_list.append(d)
        else:
            invalid_id_list.append(dict_with_rules)

    for ky in id_keys:
        for item in invalid_id_list:
            if ky in item.keys() and not ky == 'cid' and not item[ky][1]:
                print(item[ky][0], id_keys[ky]['rule'])

    print(len(valid_id_list))




