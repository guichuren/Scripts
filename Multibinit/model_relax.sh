'''
This script is used for relax a batch of structures with a model.
'''
#!/bin/bash

# ==== some input for the calculation ====
name_model='fit2_4'
ncpu=10
#=========================================

mkdir ${name_model}

for i in Fm-3m P-43m P42nmc Pbca Pca21 Pmn21 R3 P21c # Here specifies the structures
do
        mkdir ${name_model}/${i}

        cp input_files/* ${name_model}/${i}
        sed -i -r "s/fit_coeffs/${name_model}/g" ${name_model}/${i}/model_relax.files

        cp ${i}/model_relax.abo_HIST.nc ${name_model}/${i}

        cd ${name_model}/${i}
        mpirun -np ${ncpu} multibinit < model_relax.files > log &
        cd ../..
done

#dir ${name_model} # Show the results fold if wanted
