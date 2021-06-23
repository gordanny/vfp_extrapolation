def read_vfp(file):
    with open(file, 'r', encoding='utf-8') as inf:
        raw_vfp_table = inf.read().replace('\n','').strip().split('VFPPROD')
        formatted_vfp_table = raw_vfp_table[1].replace('-- ', '').strip().split('/')[:-1]
    return formatted_vfp_table
