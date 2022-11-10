RUNDIR=run/nmlcc

rm -fr "${RUNDIR}"
mkdir -p "${RUNDIR}"

(
    time nmlcc bundle NeuroML/TestL5PC.net.nml "${RUNDIR}"
    cd "${RUNDIR}"
    time python3 main.py
) 2>&1 | tee > "${RUNDIR}/log"


