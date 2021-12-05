#!/usr/bin/env bash

day="${1}"

if [[ -z "${day}" ]]; then
    echo "Missing day number"
    exit 0
fi

puzzle_input=$(curl --silent --cookie cookies.txt https://adventofcode.com/2021/day/"${day}"/input)

echo "${puzzle_input}"
