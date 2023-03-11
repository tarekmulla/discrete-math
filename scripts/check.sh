#!/bin/sh -eu

run_check() {
    printf "=========================================\n"
    printf "$1 Running check for $2\n"
    shift

    if ! "$@"; then
        printf "^^^ +++\n\e[31mCheck failed for %s\e[0m\n" "$1"
        ret=1
    fi
    printf "=========================================\n\n\n\n\n"
}

ret=0

cd ./webapp

run_check "🔧 flake8: linting - " flake8 . --config=./.flake8

run_check "🐼 black: code formatter - " black --check --diff --color .

run_check "🐉 isort: check imports sorting - " isort --check --diff --color --settings-path=./pyproject.toml .

run_check "🔐 bandit: security linter - " bandit -r . -c=./pyproject.toml

run_check "🎯 mypy: static type checker - " mypy . --config-file=./pyproject.toml

run_check "🔩 pylint: static code analysis - " pylint . --rcfile=./pyproject.toml

# todo: increase the fail rate
run_check "🐍" pytest \
    --cov=app \
    --cov-fail-under=10 \
    --cov-report term-missing \
    --cov-report xml:reports/coverage.xml \
    --junitxml=reports/test-results.xml \
    tests

exit $ret
