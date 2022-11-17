RUNDIR=run/neuron

which pynml
which nrn

rm -fr "${RUNDIR}"
mkdir -p "${RUNDIR}"

(
    time pynml ./NeuroML/LEMS_TestL5PC.xml -neuron -nogui -outputdir "${RUNDIR}"
    cd "${RUNDIR}"
    python LEMS_TestL5PC_nrn.py
) 2>&1 | tee "${RUNDIR}/log"
