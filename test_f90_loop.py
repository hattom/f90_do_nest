#!/usr/bin/env python

nest_level = 1024
two_level = 100

var_names = [f'i{i}' for i in range(nest_level)]
var_loops = [1 for var in var_names]
for i in range(nest_level):
    if i%two_level == 0:
        var_loops[i] = 2

def write_header(f):
    f.write('program test_loops\n')
    f.write('  implicit none\n')
    f.write('\n')

def write_footer(f):
    f.write('end program test_loops\n')

def write_decl(f, var_names):
    for var in var_names:
        f.write(f'  integer :: {var}\n')

def write_decl_pretty(f, var_names):
    for var in var_names:
        f.write(f'  integer :: {var}\n')

def write_do_nest(f, var_names, var_loops, do_indent=False):
    indent=""
    for var, loop_count in zip(var_names, var_loops):
        f.write(f'  {indent}do {var}=1,{loop_count}\n')
        if do_indent:
            indent=indent+'  '
    f.write(f'  {indent}print*, {var}\n')
    for var, loop_count in zip(var_names[::-1], var_loops[::-1]):
        if do_indent:
            indent=indent[:-2]
        f.write(f'  {indent}enddo\n')

def write_doconc_nest(f, var_names, var_loops):
    f.write(f'  do concurrent(&\n')
    for ivar, (var, loop_count) in enumerate(zip(var_names, var_loops)):
        if ivar != len(var_names) - 1:
            f.write(f'    {var}=1:{loop_count}, &\n')
        else:
            f.write(f'    {var}=1:{loop_count} &\n')
    f.write(f'  )\n')
    f.write(f'    print*, {var}\n')
    f.write(f'  enddo\n')

with open('f90code.F90', 'w') as f:
    write_header(f)
    write_decl(f, var_names)
    write_do_nest(f, var_names, var_loops)
    write_footer(f)

with open('f90code_conc.F90', 'w') as f:
    write_header(f)
    write_decl(f, var_names)
    write_doconc_nest(f, var_names, var_loops)
    write_footer(f)