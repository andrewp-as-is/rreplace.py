#!/usr/bin/env python
from rreplace import rreplace

"""new_new"""
r = rreplace("old_old", "old", "new")
print(r)

"""old_new"""
r = rreplace("old_old", "old", "new", 1)
print(r)
