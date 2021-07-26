# feta-inference
Inference pipeline for our participation in the FeTA challenge 2021.

Team name: TRABIT

## Installation
To build the docker image run
```bash
cd feta-inference
sh build_docker.sh
```
The tag for the docker image should be ```feta_challenge/trabit:latest```.

## Run inference using docker
After you have built the docker image, you can create a docker container 
and obtain the predicted fetal brain segmentation by running
```bash
sh example_docker_inference.sh
```
The script ```example_docker_inference.sh``` is based on the instructions found at
https://feta-2021.grand-challenge.org/Submission/

Note that you have to rebuild the docker image for changes in the code 
to be taken into account.
