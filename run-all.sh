#!/usr/bin/env bash


. env/bin/activate

set -x

bash scripts/run-eden.sh
bash scripts/run-nmlcc.sh
bash scripts/run-nmlcc-super.sh
