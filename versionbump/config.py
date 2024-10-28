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

import os
import json


class Config:
    """
    This is a class that provides methods and functions for
    managing settings from a configuration file.

    NOTE: Config file hard-coded as '_config.json'
    """

    def __init__(self):
        with open(os.path.join(os.path.dirname(__file__),
                               '_config.json'), 'r') as fp:
            self.config = json.load(fp)

    def get_patterns(self):
        ''' Returns a list of file search patterns from config file. '''
        return [k for i, k in enumerate(self.config['search-patterns'])]
    
    def get_scm_list(self):
        ''' Returns a list if source control tools from config file. '''
        return [k for i, k in enumerate(self.config['source-control-mgmt'])]
