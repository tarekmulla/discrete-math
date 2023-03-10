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

run_check ":python:" flake8 ./webapp
run_check ":python: :test_tube:" flake8 tests
run_check ":python: :toolbox:" flake8 tools

run_check ":python:" pylint ./webapp
run_check ":python: :test_tube:" pylint --disable=line-too-long,use-implicit-booleaness-not-comparison,too-many-public-methods,duplicate-code tests
run_check ":python: :toolbox:" pylint tools

exit $ret
