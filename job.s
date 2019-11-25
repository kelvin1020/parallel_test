#BSUB -J testsc
#BSUB -q gold2
#BSUB -n 8
#BSUB -o %J.out
#BSUB -e %J.err
#BSUB -a python 
#BSUB -R span[ptile=8]
python ./testsc.py
