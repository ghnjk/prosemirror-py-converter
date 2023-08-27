#!/usr/bin/env bash

pep8_cmd="autopep8 --in-place  --ignore-local-config  --aggressive --aggressive --ignore E402 "
${pep8_cmd} -r pmconverter
${pep8_cmd} -r tests
