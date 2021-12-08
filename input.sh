#!/usr/bin/env bash

day="${1}"

if [[ -z "${day}" ]]; then
    echo "Missing day number"
    exit 0
fi

printf -v day_dir "%02d" "${day}"
curl -fsSL --cookie cookies.txt https://adventofcode.com/2021/day/"${day}"/input --output "${day_dir}"/input
