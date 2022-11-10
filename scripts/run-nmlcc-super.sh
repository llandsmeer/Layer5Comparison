RUNDIR=run/nmlcc-super

which nmlcc
python3 -c 'import arbor; print(arbor.__path__)'

rm -fr "${RUNDIR}"
mkdir -p "${RUNDIR}"

(
    time nmlcc bundle -s NeuroML/TestL5PC.net.nml "${RUNDIR}"
    cd "${RUNDIR}"
    time python3 main.py
) 2>&1 | tee > "${RUNDIR}/log"


