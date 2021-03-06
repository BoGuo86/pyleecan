# -*- coding: utf-8 -*-
"""Created on Mon Nov 10 15:44:20 2014
@author: pierre_b
"""
import sys
from os.path import dirname, abspath, normpath, join

sys.path.insert(0, normpath(abspath(join(dirname(__file__), "..", ".."))))

from pyleecan.Generator.run_generate_classes import generate_code
from pyleecan.Generator.read_fct import read_all
from pyleecan.definitions import MAIN_DIR, DOC_DIR, INT_DIR

if __name__ == "__main__":
    gen_dict = read_all(DOC_DIR, is_internal=True, in_path=INT_DIR)
    generate_code(MAIN_DIR, gen_dict)
