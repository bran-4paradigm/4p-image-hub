#!/usr/bin/env bash

check_opts() {
    if [ -z "$REGISTRY" ]; then
        echo "REGISTRY not set" && exit
    fi

    if [ -z "$USERNAME" ]; then
        echo "USERNAME not set"  && exit
    fi

    if [ -z "$PASSWORD" ]; then
        echo "PASSWORD not set"  && exit
    fi
}

check_opts

pecan serve /app/etc/pecan/config.py

