#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_stackadapt import SourceStackadapt

if __name__ == "__main__":
    source = SourceStackadapt()
    launch(source, sys.argv[1:])
