from get_data import get_data
from get_extrapolation_range import get_extrapolation_range


def extrapolation(file, input_parameters):
    data = get_data(file)
    parameters_string = '|'.join([str(float(parameter)) for parameter in input_parameters])
    if parameters_string in data['data']:
        return data['data'][parameters_string]
    er = get_extrapolation_range(data, input_parameters)
    par = ['FLO', 'THP', 'WFR', 'GFR']
    term1 = []
    term2 = []
    ex = []
    for p in par:
        term1.append(er[p]['value'] if er[p]['type'] == 'known' else er[p]['min'])
        term2.append(er[p]['value'] if er[p]['type'] == 'known' else er[p]['max'])

    y1 = data['data']['|'.join(map(str, term1))]
    y2 = data['data']['|'.join(map(str, term2))]
    for i in range(len(par)):
        print(i, er[par[i]]['type'], er[par[i]])
        if er[par[i]]['type'] != 'known':
            ex.append(y1 + (y2 - y1)/(term2[i] - term1[i])*(input_parameters[i]-term1[i]))

    print("***", ex, '***')
    total_ex = sum(ex)/len(ex)

    print('*',total_ex,'*')
