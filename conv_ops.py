# conv_ops.py
#
# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p
# This script calculates the output shape and operation count of a convolution layer.
#
# Parameters:
#  c_in: input channel count
#  h_in: input height count
#  w_in: input width count
#  n_filt: number of filters in the convolution layer
#  h_filt: filter height count
#  w_filt: filter width count
#  s: stride of convolution filters
#  p: amount of padding on each of the four input map sides
#
# Output:
#  Prints the output channel count, output height count, output width count, 
#  and the number of additions, multiplications, and divisions performed.
#
# Written by Nick Davis
# Other contributors: None
#
# This work is licensed under CC BY-SA 4.0

# Import necessary modules
import sys
# import math

# Helper function to calculate the output dimensions of the convolution layer
def calc_conv_output(c_in, h_in, w_in, n_filt, h_filt, w_filt, s, p):
    # Output dimensions after convolution
    h_out = (h_in - h_filt + 2 * p) / s + 1
    w_out = (w_in - w_filt + 2 * p) / s + 1
    c_out = n_filt

    # Calculate the number of operations
    # Each filter performs one multiplication per element in the filter
    muls_per_filter = c_in * h_filt * w_filt
    muls = muls_per_filter * h_out * w_out * n_filt

    # Each multiplication is followed by an addition (except the first one)
    adds_per_filter = (muls_per_filter - 1)
    adds = adds_per_filter * h_out * w_out * n_filt

    # Divisions are not generally part of the basic convolution operations
    divs = 0

    return c_out, h_out, w_out, adds, muls, divs

# Parse script arguments
if len(sys.argv) == 9:
    c_in = int(sys.argv[1])
    h_in = int(sys.argv[2])
    w_in = int(sys.argv[3])
    n_filt = int(sys.argv[4])
    h_filt = int(sys.argv[5])
    w_filt = int(sys.argv[6])
    s = int(sys.argv[7])
    p = int(sys.argv[8])
else:
    print('Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p')
    exit()

# Calculate the output dimensions and operation counts
c_out, h_out, w_out, adds, muls, divs = calc_conv_output(c_in, h_in, w_in, n_filt, h_filt, w_filt, s, p)

# Print the results
print(int(c_out))  # Output channel count
print(int(h_out))  # Output height count
print(int(w_out))  # Output width count
print(int(adds))   # Number of additions performed
print(int(muls))   # Number of multiplications performed
print(int(divs))   # Number of divisions performed