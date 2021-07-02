from read_vfp import read_vfp
from get_data import get_sample_parameters, get_sample_values
from get_ranges import get_parameters_range


def extrapolate_params(input_parameters, file):
    vfp_table = read_vfp(file)
    sampling_points = get_sample_parameters(vfp_table)
    sampling_values = get_sample_values(sampling_points, vfp_table)

    parameters_string = '|'.join([str(float(parameter)) for parameter in input_parameters])
    if parameters_string in sampling_values['value']:
        return sampling_values['value'][parameters_string]

    parameters_range = get_parameters_range(input_parameters, sampling_points)


