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
from config import *
from fabric import Connection


def pacmanupdate():
    for host in arch:
        print("Going to check updates on {}".format(host))
        result = Connection(host).run('yes | pacman -Suy', pty=True)
        print("{}: {}".format(host, result.stdout.strip()))


def aptcheckupdate ():
        for host in debian:
            print("Going to check updates on {}".format(host))
            result = Connection(host).run('apt update', pty=True)
            print("{}: {}".format(host, result.stdout.strip()))




def aptlistupgrade ():
        for host in debian:
            print("Going to list updates on {}".format(host))
            result = Connection(host).run('apt list --upgradable', pty=True)
            print("{}: {}".format(host, result.stdout.strip()))



def aptupdatesystem ():
        for host in debian:
            print("Going to update on {}".format(host))
            result = Connection(host).run('apt -y dist-upgrade', pty=True)
            print("{}: {}".format(host, result.stdout.strip()))


def aptremoveupdate():
        for host in debian:
            print("Going to remove updates on {}".format(host))
            result = Connection(host).run('apt autoremove -y', pty=True)
            print("{}: {}".format(host, result.stdout.strip()))

def updatecentos():
        for host in centos:
            print("Going to install updates on {}".format(host))
            result = Connection(host).run('yum update -y', pty=True)
            print("{}: {}".format(host, result.stdout.strip()))

def iparemove():
        for host in ipaclients:
            print("Going to remove ipa on {}".format(host))
            result = Connection(host).run('ipa-client-install --uninstall', pty=True)
            print("{}: {}".format(host, result.stdout.strip()))

def ipainstall():
        for host in ipaclients:
            print("Going to join {} to SARGUS.NET.ZA".format(host))
            result = Connection(host).run('ipa-client-install --mkhomedir --realm=SARGUS.NET.ZA --domain=sargus.net.za --server=ipa.sargus.net.za --hostname=$(hostname)', pty=True)
            print("{}: {}".format(host, result.stdout.strip()))
