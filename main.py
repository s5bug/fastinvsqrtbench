import ieee754
import struct


def bitstr_to_float(N):  # ieee-745 bits (max 32 bit)
    a = int(N[0])  # sign,     1 bit
    b = int(N[1:9], 2)  # exponent, 8 bits
    c = int("1" + N[9:], 2)  # fraction, len(N)-9 bits

    return (-1) ** a * c / (1 << (len(N) - 9 - (b - 127)))


def bitstr_inv_sqrt(x):
    x_half = 0.5 * x
    i = int(ieee754.single(x).hex()[0], 16)  # store floating-point bits in integer
    i = 0x5f3759df - (i >> 1)  # initial guess for Newton's method
    x = bitstr_to_float("{0:032b}".format(i))  # convert new bits into float
    x = x * (1.5 - x_half * x * x)  # One round of Newton's method
    return x

def struct_inv_sqrt(x):
    x_half = 0.5 * x
    i = struct.unpack(">I", struct.pack(">f", x))[0]
    i = 0x5f3759df - (i >> 1)
    x = struct.unpack(">f", struct.pack(">I", i))[0]
    x = x * (1.5 - x_half * x * x)
    return x
