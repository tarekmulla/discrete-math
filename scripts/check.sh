#!/bin/sh -eu

run_check() {
    echo "--- $1 Running check for $2"
    shift

    if ! "$@"; then
        printf "^^^ +++\n\e[31mCheck failed for %s\e[0m\n" "$1"
        ret=1
    fi
}

ret=0

run_check ":python:" flake8 ./webapp --config=./.flake8

run_check ":python:" pylint ./webapp --rcfile=./.pylintrc

exit $ret
