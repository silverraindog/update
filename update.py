#!/usr/bin/env python3.6
__author__ = "Angus Robinson"
__copyright__ = "Copyright 2019, Sargus Networks"
__credits__ = ["Angus Robinson", "All those that provided answers and docuumentation",
                "on the internet"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Angus Robinson"
__email__ = "angus@sargus.net.za"
__status__ = "Production"

import argparse

from functions import *
from log import get_logger

parser = argparse.ArgumentParser()
parser.add_argument("--update", help="update systems",
                    action="store_true")
parser.add_argument("--list", help="list upgrades on systems",
                    action="store_true")
parser.add_argument("--updatesystem", help="perform the update to systems",
                    action="store_true")
parser.add_argument("--remove", help="remove updates on systems",
                    action="store_true")
parser.add_argument("--centos", help="update centos systems",
                    action="store_true")
parser.add_argument("--all", help="Run all modules",
                    action="store_true")
args = parser.parse_args()
if args.update:
    upodate = get_logger("{}".format(checkupdate()))
    upodate.info('Checking updates on systems running Debian')

if args.list:
    update = get_logger("{}".format(listupgrade()))
    update.info('Checking upgrade list for Debian system')


if args.updatesystem:
    update = get_logger("{}".format(updatesystem()))
    update.info('Installing updates on systems running Debian')


if args.remove:
    update = get_logger("{}".format(removeupdate()))
    update.info('Removing obsolete programs on Debian systems')


if args.centos:
    update = get_logger("{}".format(updatecentos()))
    update.info('Checking update to systems running Centos')
    
 if args.arch:
    update = get_logger("{}".format(archlinux()))
    update.info('Checking update to systems running Arch Linux')   

if args.all:
    upodate = get_logger("{}".format(checkupdate()))
    upodate.info('Checking updates on systems running Debian')
    update = get_logger("{}".format(listupgrade()))
    update.info('Checking upgrade list for Debian system')
    update = get_logger("{}".format(updatesystem()))
    update.info('Installing updates on systems running Debian')
    update = get_logger("{}".format(removeupdate()))
    update.info('Removing obsolete programs on Debian systems')
    update = get_logger("{}".format(updatecentos()))
    update.info('Checking update to systems running Centos')
    update = get_logger("{}".format(archlinux()))
    update.info('Installing updates on systems running Arch Linux')
