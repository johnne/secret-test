#!/usr/bin/env python

import polars as pl

df = pl.read_csv("ids.txt", separator=" ", has_header=False).filter(pl.col("column_1").is_not_null())
assert(df.height==2)
assert(df.width==3)
df.write_csv("ids.csv", separator=",")