#!/usr/bin/env python
import glob
import os

from obspy import read
from ucap.data2stream import seed2stream
from ucap.processing import marktime, resample, rotate, write_to_sac


seed = '20080418093658.seed'
sampling_rate = 5
os.system('mkdir obspy')
os.system('cp 20080418093658.seed obspy')
os.chdir("obspy")

# seed2sac
st, inv = seed2stream(seed, pre_filt=(0.005, 0.01, 1.0, 1.3))
st = marktime(st)
for tr in st:
    tr.stats.azimuth = -12345
    tr.stats.back_azimuth = -12345
write_to_sac(st)
os.system('mkdir seed2sac')
os.system('mv *.[enz] seed2sac')

# rotate
st = rotate(st, inventory=inv, method="NE->RT")
write_to_sac(st)
os.system('mkdir rotate')
os.system('mv *.[rtz] rotate')

# resample
st = resample(st, sampling_rate=sampling_rate)
write_to_sac(st)
os.system('mkdir resample')
os.system('mv *.[rtz] resample')

# write to sac files
write_to_sac(st)
