#!/usr/bin/env python
import yaml
yaml_file = 'yaml1.yml'
with open(yaml_file) as f:
    output = yaml.load(f)
print output
