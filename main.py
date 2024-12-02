import glob
import os

# Get all the day_<int>.py files and import them.
DAY_PYTHON_FILES = glob.glob('./day_*.py')
DAY_MODULE_NAMES = [os.path.splitext(os.path.basename(x))[0] for x in DAY_PYTHON_FILES]
for day_module_name in DAY_MODULE_NAMES:
    exec(f'import {day_module_name}')


if __name__ == '__main__':
    # Run each day solver to view the output and timings.
    for day_module_name in DAY_MODULE_NAMES:
        eval(f'{day_module_name}.run()')
