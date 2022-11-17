RUNDIR=run/eden

which eden

rm -fr "${RUNDIR}"
mkdir -p "${RUNDIR}"

(
    cd "${RUNDIR}"
    time eden nml ../../NeuroML/LEMS_TestL5PC.xml
) 2>&1 | tee "${RUNDIR}/log"
