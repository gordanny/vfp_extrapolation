def get_parameters_range(input_parameters, sampling_points):

    parameters_range = dict()

    for parameter in input_parameters:
        if input_parameters[parameter] in sampling_points[parameter]:
            parameters_range[parameter] = {
                'type': 'known',
                'value': input_parameters[parameter]
            }

        elif input_parameters[parameter] < sampling_points[parameter][1]:
            start, end = [0, 1] if input_parameters[parameter] < sampling_points[parameter][0] else [1, 2]
            parameters_range[parameter] = {
                'type': 'single',
                'min': sampling_points[parameter][start],
                'max': sampling_points[parameter][end]
            }

        elif input_parameters[parameter] > sampling_points[parameter][-2]:
            start, end = [-2, -1] if input_parameters[parameter] > sampling_points[parameter][-1] else [-2, -3]
            parameters_range[parameter] = {
                'type': 'single',
                'min': sampling_points[parameter][start],
                'max': sampling_points[parameter][end]
            }

        else:
            for value in sampling_points[parameter][2:-1]:
                value_index = sampling_points[parameter].index(value)
                parameters_range[parameter] = {
                    'type': 'double',
                    'min': sampling_points[parameter][value_index],
                    'low_mid': sampling_points[parameter][value_index-1],
                    'high_mid': sampling_points[parameter][value_index],
                    'max': sampling_points[parameter][value_index-1]
                }
                break

    return parameters_range


def get_values_range(parameters_range):
    min_parameters = []
    max_parameters = []
    ex = []
    for parameter in parameters_range:
        min_parameters.append(parameters_range[p]['value'] if parameters_range[p]['type'] == 'known' else parameters_range[p]['min'])
        max_parameters.append(parameters_range[p]['value'] if parameters_range[p]['type'] == 'known' else parameters_range[p]['max'])

    y1 = data['data']['|'.join(map(str, term1))]
    y2 = data['data']['|'.join(map(str, term2))]
    for i in range(len(par)):
        print(i, er[par[i]]['type'], er[par[i]])
        if er[par[i]]['type'] != 'known':
            ex.append(y1 + (y2 - y1)/(term2[i] - term1[i])*(input_parameters[i]-term1[i]))
