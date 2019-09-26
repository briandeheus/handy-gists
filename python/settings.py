"""
Only requires pyyaml
"""

import yaml
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str, default='settings.yaml')
args = parser.parse_args()

__settings = yaml.safe_load(open(args.config, 'r'))


def get(name, default=None):
    keys = name.split('.')
    val = __settings

    for key in keys:

        val = val.get(key)

        if val is None:
            return default

    return val
