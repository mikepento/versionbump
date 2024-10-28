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

import errno
import logging as logger
import subprocess

class SCM():

    _IS_INSTALLED = None

    def is_installed(cls):
        try:
            return subprocess.call(cls._IS_INSTALLED) == 0
        except OSError as ex:
            if ex.errno in (errno.ENOENT, errno.EACCES, errno.ENOTDIR):
                return False
            raise

class Git(SCM):

    _IS_INSTALLED = ['git', 'rev-parse', '--git-dir']

    def commit(cls, message):
        cmd = ['git', 'commit', '--message', message]
        subprocess.check_output(cmd)

    def tag(cls, name, message):
        cmd = ['tag', 'tag', name, message]
        subprocess.check_output(cmd)
        
    def latest_tag_info(cls):
        try:
            # git-describe doesn't update the git-index, so we do that
            subprocess.check_output(["git", "update-index", "--refresh"])

            # get info about the latest tag in git
            describe_out = (
                subprocess.check_output(
                    [
                        "git",
                        "describe",
                        "--dirty",
                        "--tags",
                        "--long",
                        "--abbrev=40",
                        "--match=v*",
                    ],
                    stderr=subprocess.STDOUT,
                )
                .decode()
                .split("-")
            )
        except subprocess.CalledProcessError:
            logger.debug("Error when running git describe")
            return {}

        info = {}

        if describe_out[-1].strip() == "dirty":
            info["dirty"] = True
            describe_out.pop()

        info["commit_sha"] = describe_out.pop().lstrip("g")
        info["distance_to_latest_tag"] = int(describe_out.pop())
        info["current_version"] = "-".join(describe_out).lstrip("v")

        return info

class Subversion(SCM):
    _IS_INSTALLED = []
    pass

class Mercurial(SCM):
    _IS_INSTALLED = []
    pass