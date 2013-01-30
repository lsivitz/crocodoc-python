#!/bin/bash

rm -rf dist crocodoc.egg-info
python setup.py sdist upload
