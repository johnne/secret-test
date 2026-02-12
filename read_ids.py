#!/usr/bin/env python

import polars as pl

df = pl.read_csv("ids.txt", separator="\t", has_header=False)
assert(df.height==2)
assert(df.width==3)