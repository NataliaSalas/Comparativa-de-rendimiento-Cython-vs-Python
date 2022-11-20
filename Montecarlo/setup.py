from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("montecarlo_cy.pyx"))
setup(ext_modules = exts)