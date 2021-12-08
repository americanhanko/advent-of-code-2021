#!/usr/bin/env bash

day="${1}"
cookie_file=${2}

if [[ -z "${day}" ]]; then
    echo "Missing day number"
    exit 0
fi

printf -v day_dir "%02d" "${day}"
curl -fsSL --cookie ${cookie_file} https://adventofcode.com/2021/day/"${day}"/input --output "${day_dir}"/input
