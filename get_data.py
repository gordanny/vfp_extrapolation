from read_vfp import read_vfp


def get_parameters(table):
    parameters ={}
    for row in table[1:6]:
        splitted_row = row.strip().replace(':', '').split()
        if splitted_row[0] != 'THP':
            parameters[splitted_row[0]] = {'type': splitted_row[1], 'values': [float(value) for value in splitted_row[2:]]}
        else:
            parameters[splitted_row[0]] = {'type': '', 'values': [float(value) for value in splitted_row[1:]]}
    return parameters


def get_data(file):
    data = {}
    table = read_vfp(file)
    parameters = get_parameters(table)
    table[6] = ' '.join(table[6].strip().split()[5:])
    for row in table[6:]:
        splitted_row = row.strip().split()
        for i in range(len(splitted_row[4:])):
            input_data = (
                str(parameters['FLO']['values'][i]) + '|'
                + str(parameters['THP']['values'][int(splitted_row[0])-1]) + '|'
                + str(parameters['WFR']['values'][int(splitted_row[1])-1]) + '|'
                + str(parameters['GFR']['values'][int(splitted_row[2])-1])
            )
            data.update({input_data: float(splitted_row[i+4])})
    return {'data':data, 'parameters': parameters}
