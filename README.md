# f90 do nest
Ever wanted to generated deeply nested do loops in Fortran?

No? Nevermind, maybe this is not the repository for you.


## How To

`test_f90_loop.py` is a python script which will generate nested loops in Fortran.
It will generate "classical" nested `do/enddo` in `f90code.F90` and also a `do concurrent` version in `f90code_conc.F90`.

`nest_level` sets the total number of loops, the majority of which will have 1 iteration.

In order to make it slightly less trivial, every k-th loop will have 2 trips instead of 1.
Change `two_level` in the python code to choose k.

The resulting scripts have been tested by compiling with `gfortran` `v10.3.0` up to a `nest_level` of 1024. It is not known what the maximum `nest_level` is for gfortran.

Note: Because of line length limits, and crazy levels of nesting, loop indentation defaults to false. `do_indent` can be set to true to turn this on.