#!/usr/bin/env perl
use strict;
use warnings;

mkdir 'sac';
system "cp 20080418093658.seed sac";
system "cp event.info sac";

#seed2sac
system "perl rdseed.pl sac";
system "perl eventinfo.pl sac";
system "perl marktime.pl sac";
system "perl transfer.pl sac";
mkdir "sac/seed2sac";
system "cp sac/*.SAC sac/seed2sac";

#rotate
system "perl rotate.pl sac";
mkdir "sac/rotate";
system "cp sac/*.[rtz] sac/rotate";

#resample
system "perl resample.pl sac";
mkdir "sac/resample";
system "cp sac/*.[rtz] sac/resample";
