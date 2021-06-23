from get_data import get_data
from get_extrapolation_range import get_extrapolation_range


def extrapolation(file, input_parameters):
    data = get_data(file)
    parameters_string = '|'.join([str(float(parameter)) for parameter in input_parameters])
    if parameters_string in data['data']:
        return data['data'][parameters_string]
    extrapolation_range = get_extrapolation_range(data, input_parameters)

