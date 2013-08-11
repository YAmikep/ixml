#!/usr/bin/env bash
#
# Auto discovers and runs all the tests (doctests and unittests).
#
# On the command line, just pass the tests to run as additional arguments to shut down auto discovering.
# Usage: http://nose.readthedocs.org/en/latest/usage.html
# Common options:
# -v --verbose 

nosetests -v --nocapture --with-doctest --doctest-extension=rst -s $@
