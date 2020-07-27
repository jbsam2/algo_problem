def count_blood(blood_infos):
    ret = {}
    for blood_info in blood_infos:
        if blood_info in ret:
            ret[blood_info] += 1
        else:
            ret[blood_info] = 1
    return ret

info = [
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB'
]
print(count_blood(info))