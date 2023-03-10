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

run_check ":python:" black --check --diff --color ./webapp

run_check ":python:" isort --check --diff --color ./webapp

run_check ":python:" bandit -r ./webapp

run_check ":python:" mypy ./webapp

run_check ":python:" pylint ./webapp --rcfile=./.pylintrc

# todo: increase the fail rate
run_check ":python:" pytest \
    --cov=webapp \
    --cov-fail-under=10 \
    --cov-report term-missing \
    --cov-report xml:reports/coverage.xml \
    --junitxml=reports/test-results.xml \
    tests

exit $ret
