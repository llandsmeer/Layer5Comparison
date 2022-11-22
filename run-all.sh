#!/usr/bin/env bash


# . env/bin/activate

if [ ! -d generated ]
then
    bash scripts/generate-all.sh
fi

run () {
    echo "################################################################################"
    echo "# Running $@ #"
    echo "################################################################################"
    (
    cd scripts
    $@ | python3 miniterm.py
    )
    echo
    echo
}

run python3 run-nmlcc.py 4a
run python3 run-nmlcc.py 4b
run python3 run-nmlcc.py 5a
run python3 run-nmlcc-super.py

# run scripts/run-neuron.sh
# run scripts/run-eden.sh

