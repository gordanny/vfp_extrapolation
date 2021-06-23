from vfp_extrapolation import extrapolation

a = [[5, 200, 0.001, 0.00065], [5000, 5, 0, 0], [200000, 400, 0.00001, 0.0008]]
for i in a:
    print(extrapolation('1.vfp', i))


