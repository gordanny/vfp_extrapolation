from read_vfp import read_vfp


def get_sample_parameters(vfp_table):
    sample_parameters = {}
    for row in vfp_table[1:6]:
        splitted_row = row.strip().replace(':', '').split()
        if splitted_row[0] != 'THP':
            sample_parameters[splitted_row[0]] = [float(value) for value in splitted_row[2:]]
        else:
            sample_parameters[splitted_row[0]] = [float(value) for value in splitted_row[1:]]
    return sample_parameters


def get_sample_values(sample_parameters, vfp_table):
    sample_values = {}
    vfp_table[6] = ' '.join(vfp_table[6].strip().split()[5:])
    for row in vfp_table[6:]:
        splitted_row = row.strip().split()
        for i in range(len(splitted_row[4:])):
            input_data = (
                str(sample_parameters['FLO'][i]) + '|'
                + str(sample_parameters['THP'][int(splitted_row[0])-1]) + '|'
                + str(sample_parameters['WFR'][int(splitted_row[1])-1]) + '|'
                + str(sample_parameters['GFR'][int(splitted_row[2])-1])
            )
            sample_values.update({input_data: float(splitted_row[i+4])})
    return {'value': sample_values, 'parameters': sample_parameters}
