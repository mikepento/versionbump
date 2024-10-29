# Copyright (C) 2024 Mike Pento
#
# This file is part of Versionbump.
#
# Versionbump is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# Versionbump is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this Versionbump.  If not, see <http://www.gnu.org/licenses/>.

import sys
import argparse
import logging
from pathlib import Path
from versionbump.process import Process
from versionbump.config import Config

from versionbump import (
    __title__,
    __version__,
    __author__,
    __copyright__
    )

def _is_scm_installed():
    scm_info = {}
    for scm in Config.get_scm_list():
        if scm.is_installed():
            scm_info.update()

def main():
    parser = argparse.ArgumentParser(prog=__title__)

    parser.add_argument('-p', '--path', nargs='?',
                        help='Path to search. (Default=\'.\')', default='.',
                        type=Path)
    parser.add_argument('-c', '--current-version', nargs='?',
                        help='Current version to bump. (Required)',
                        required=True)
    parser.add_argument('-r', '--replace-version', nargs='?',
                        help='Replace current version with specified \
                            version. (Optional)',
                            default=None)
    parser.add_argument('-i', '--increment-by', nargs='?',
                        help='Increment by value. (Default=1)',
                        const=1, type=int, default=1)
    parser.add_argument('field', choices=['major', 'minor', 'patch'],
                        nargs='?',
                        help='Version field to increment.')
    parser.add_argument('-v', '--version', action='version',
                        version=f'%(prog)s {__version__} - \
                            {__copyright__}, {__author__}')

    try:
        args = parser.parse_args(None if sys.argv[1:] else ['-h'])
    except ValueError as ex:
        raise ValueError from ex

    # configure logging
    logging.root.handlers = []

    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )

    # instance of the process class
    p = Process(args.path,
                args.current_version,
                args.replace_version,
                args.field,
                args.increment_by)

    # do processing ..
    p.do_process()


if __name__ == "__main__":
    main()
