from vfp_extrapolation import extrapolation

a = [[200000, 550, 0.0005, 0.0002], [300000, 500, 0.00001, 0.0003], [250000, 525, 0.00025, 0.00025]]
for i in a:
    print(extrapolation('1.vfp', i))


