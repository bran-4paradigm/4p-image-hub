#!/usr/bin/env bash

yum -y install httpie
curl --silent --show-error --retry 5 http://pkg.4paradigm.com/wangyiping/get-pip.py | python