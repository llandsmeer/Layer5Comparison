OUT=generated/nmlcc-super

which nmlcc
python3 -c 'import arbor; print(arbor.__path__)'

rm -fr "${OUT}"
mkdir -p "${OUT}"

(
    time nmlcc bundle -s NeuroML/TestL5PC.net.nml "${OUT}"
) 2>&1 | tee "${OUT}/log"


