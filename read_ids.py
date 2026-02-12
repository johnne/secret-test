#!/usr/bin/env python

import polars as pl

df = pl.read_csv("ids.txt", separator=" ", has_header=False)
assert(df.height==2)
assert(df.width==3)
df.write_csv("ids.csv", separator=",")