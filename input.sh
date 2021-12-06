#!/usr/bin/env bash

day="${1}"

if [[ -z "${day}" ]]; then
    echo "Missing day number"
    exit 0
fi

puzzle_input=$(curl -fsSL --cookie cookies.txt https://adventofcode.com/2021/day/"${day}"/input)

printf -v day_dir "%02d\n" "${day}"
echo "${puzzle_input}" > "${day_dir}"/input
