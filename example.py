# -*- coding: utf-8 -*-

"""
@author Lucas Fidon (lucas.fidon@kcl.ac.uk)
"""

import os
import glob
import ast
import json
import sys
sys.path.insert(1, os.path.join(sys.path[0], '.'))
sys.stdout.flush()
from src.deep_learning.inference.inference import pred_softmax


# Important directories
input_img_dir = '/input_img'
input_meta_dir = '/input_meta'
outputDir = '/output'
repo_dir = '/feta_seg'
outputDirTemplateSpace = os.path.join(outputDir, 'template_space')


# Get SRR path and subject name
T2wImagePath = glob.glob(os.path.join(input_img_dir, 'anat', '*_T2w.nii.gz'))[0]
sub = os.path.split(T2wImagePath)[1].split('_')[0] # to split the input directory and to obtain the subject name


# Read GA and Pathology
jsonPath = os.path.join(input_meta_dir, 'meta.json')
with open(jsonPath) as jsonFile:
    jsonData = json.dumps(json.load(jsonFile))
    jsonFile.close()
jsonData = ast.literal_eval(jsonData)
pathology = jsonData['Pathology']
GA = jsonData['Gestational age']
print('Subject:', sub)
print('pathological info:', pathology)
print('GA:', GA)
GA_ROUNDED = max(min(int(round(float(GA))), 38), 21)  # clip the GA to [21, 38]
print('GA used:', GA_ROUNDED)


# PRE-PROCESSING
print('\n** Create the brain mask (mask.nii.gz saved in outputDir)')
cmd_brain_extraction = 'python %s/src/preprocessing/brain_extraction.py --input_img %s --output_folder %s --ga %d' % \
    (repo_dir, T2wImagePath, outputDir, GA_ROUNDED)
os.system(cmd_brain_extraction)
maskPath = os.path.join(outputDir, 'mask.nii.gz')

print('\n** Put the SRR and mask in the template space')
cmd_put_in_template_space = 'python %s/src/preprocessing/put_srr_in_template_space.py --input_img %s --input_mask %s --output_folder %s --ga %d' % \
    (repo_dir, T2wImagePath, maskPath, outputDirTemplateSpace, GA_ROUNDED)
os.system(cmd_put_in_template_space)
T2wImageTemplateSpacePath = os.path.join(outputDirTemplateSpace, 'srr.nii.gz')
maskTemplateSpacePath = os.path.join(outputDirTemplateSpace, 'mask.nii.gz')

# INFERENCE
print('\n** Run the deep learning ensemble on the SRR in the template space')
pred_softmax(
    img_path=T2wImageTemplateSpacePath,
    mask_path=maskTemplateSpacePath,
    save_folder=outputDirTemplateSpace,
)

# POSTPROCESSING
#todo

##
# your logic here. Below we do binary thresholding as a demo
##

# # using SimpleITK to do binary thresholding between 100 - 10000
# T2wImage = sitk.ReadImage(T2wImagePath)
# resultImage = sitk.BinaryThreshold(T2wImage, lowerThreshold=100, upperThreshold=10000)
#
# # Save the segmentation mask
# save_path = os.path.join(outputDir, sub + '_seg_result.nii.gz')
# sitk.WriteImage(resultImage, save_path)
# print('\nPredicted segmentation saved as %s' % save_path)
