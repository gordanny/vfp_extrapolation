def get_extrapolation_range(data, parameters):
    parameters_dict = {
        'FLO': parameters[0],
        'THP': parameters[1],
        'WFR': parameters[2],
        'GFR': parameters[3]
    }
    parameters_range = dict()
    for parameter in parameters_dict:
        if (
                parameters_dict[parameter] < data['parameters'][parameter]['values'][0]
                or
                parameters_dict[parameter] > data['parameters'][parameter]['values'][-1]
        ):
            parameters_range[parameter] = {
                'type': 'single',
                'min': data['parameters'][parameter]['values'][0],
                'max': data['parameters'][parameter]['values'][-1]
            }
            continue

        for value in data['parameters'][parameter]['values'][1:]:

            if parameters_dict[parameter] == value:
                parameters_range[parameter] = {
                    'type': 'known',
                    'value': value
                }
                break

            if parameters_dict[parameter] < value:
                value_index = data['parameters'][parameter]['values'].index(value)
                if value_index == 1:
                    parameters_range[parameter] = {
                        'type': 'single',
                        'min': data['parameters'][parameter]['values'][1],
                        'max': data['parameters'][parameter]['values'][-1]
                    }
                    break
                if value_index == len(data['parameters'][parameter]['values']) - 2:
                    parameters_range[parameter] = {
                        'type': 'single',
                        'min': data['parameters'][parameter]['values'][1],
                        'max': data['parameters'][parameter]['values'][-2]
                    }
                    break
                parameters_range[parameter] = {
                    'type': 'double',
                    'min': data['parameters'][parameter]['values'][0],
                    'low_mid': data['parameters'][parameter]['values'][value_index-1],
                    'high_mid': data['parameters'][parameter]['values'][value_index],
                    'max': data['parameters'][parameter]['values'][-1]
                }
                break

    print(parameters_dict, parameters_range)
    return parameters_range
