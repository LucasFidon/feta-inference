# feta-inference
Inference pipeline for our participation in the FeTA challenge 2021.

Team name: TRABIT

A description of our fetal brain 3D MRI segmentation pipeline can be found in [our paper][feta2021].

## Installation

Download the two folders in
https://drive.google.com/drive/folders/1V5PBETb89GEA3oSNidTpQRtNADjcdp_0?usp=sharing

Move them to ```feta-inference/data```

Build the docker image by running
```bash
cd feta-inference
sh build_docker.sh
```
The tag for the docker image should be ```feta_challenge/trabit:latest```

Note that you have to rebuild the docker image for changes in the code 
to be taken into account.

## Compute automatic fetal brain MRI segmentation using docker
After you have built the docker image, you can create a docker container 
and obtain the predicted fetal brain segmentation by running the command
```bash
sh example_docker_inference.sh
```
The script ```example_docker_inference.sh``` is based on the instructions found at
https://feta-2021.grand-challenge.org/Submission/

You can adapt the script ```example_docker_inference.sh``` to segment your fetal brain 3D MRI by 
changing the following paths at the beginning of the script: 
* ```TEST_INPUT_IMG```: path to the folder containing the 3D MRI to be segmented
* ```TEST_INPUT_META```: path to the folder containing meta data about the fetal brain 3D MRI to be segmented
* ```RESULT_LOCATION```: path to the location where to save the output of the segmentation pipeline

The folders ```TEST_INPUT_IMG``` and ```TEST_INPUT_META``` and the data therein are assumed to use the same 
structure as for the testing phase of the FeTA challenge 2021.

```TEST_INPUT_IMG``` must contain a folder called ```\anat``` containing the 3D MRI to be segmented.
The 3D MRI needs to use the file format extension ```.nii.gz``` and the naming convention ```<study-name>_T2w.nii.gz```.

In addition, if you already have a brain mask you can put it in the folder ```TEST_INPUT_IMG``` with the file name ```mask.nii.gz```.
Otherwise, the brain mask will be estimated automatically.

```TEST_INPUT_META``` must contain a file ```meta.json``` with the fields ```Pathology``` and ```Gestational age```.
```Pathology``` can be either ```Neurotypical``` or ```Pathological```.
```Gestational age``` is the gestational age of the fetus at the time of imaging in weeks.

## How to cite
If you find this repository useful in your work,
please cite our work
* L. Fidon, M. Aertsen, S. Shit, P. Demaerel, S. Ourselin, J. Deprest, T. Vercauteren.
[Partial supervision for the FeTA challenge 2021.][feta2021]
MICCAI 2021 Perinatal, Preterm and Paediatric Image Analysis (PIPPI) workshop.
* L. Fidon, M. Aertsen, D. Emam, N. Mufti, F. Guffens, T. Deprest, P. Demaerel, A. L. David,
A. Melbourne, S. Ourselin, J. Deprest, T. Vercauteren.
[Label-Set Loss Functions for Partial Supervision: Application to Fetal Brain 3D MRI Parcellation][partialsup]
MICCAI 2021.

BibTeX:
```
@article{fidon2021partial,
  title={Partial supervision for the FeTA challenge 2021},
  author={Fidon, Lucas and Aertsen, Michael and Shit, Suprosanna and Demaerel, Philippe and Ourselin, S{\'e}bastien and Deprest, Jan and Vercauteren, Tom},
  journal={arXiv preprint arXiv:2111.02408},
  year={2021}
}
@inproceedings{fidon2021label,
  title={Label-set loss functions for partial supervision: application to fetal brain 3D MRI parcellation},
  author={Fidon, Lucas and Aertsen, Michael and Emam, Doaa and Mufti, Nada and Guffens, Fr{\'e}d{\'e}ric and Deprest, Thomas and Demaerel, Philippe and David, Anna L and Melbourne, Andrew and Ourselin, S{\'e}bastien and others},
  booktitle={International Conference on Medical Image Computing and Computer-Assisted Intervention},
  pages={647--657},
  year={2021},
  organization={Springer}
}
```

[feta2021]: https://arxiv.org/abs/2111.02408
[partialsup]: https://link.springer.com/chapter/10.1007/978-3-030-87196-3_60
