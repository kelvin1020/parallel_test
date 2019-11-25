#BSUB -J testsc
#BSUB -q gold2
#BSUB -n 16
#BSUB -o %J.out
#BSUB -e %J.err
#BSUB -a python 
#BSUB -R span[ptile=16]
python ./testsc.py
