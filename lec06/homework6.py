import numpy as np

def minimum_Fs(f):
    Fs = 2 * f  
    return Fs
    
import math
def omega(f, Fs):
    omega = 2 * math.pi * f / Fs
    return omega

def pure_tone(omega, N):
    x = np.cos(omega * np.arange(N))
    return x

