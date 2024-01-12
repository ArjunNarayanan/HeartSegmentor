import SimpleITK as sitk
import numpy as np
import os
import argparse


def make_output_dir(dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)


cardiac_structures = [
    "aorta",
    "heart_atrium_left",
    "heart_atrium_right",
    "heart_myocardium",
    "heart_ventricle_left",
    "heart_ventricle_right",
    "pulmonary_artery"
]

structure2label = {
    "aorta": 820,
    "heart_atrium_left": 420,
    "heart_atrium_right": 550,
    "heart_myocardium": 205,
    "heart_ventricle_left": 500,
    "heart_ventricle_right": 600,
    "pulmonary_artery": 850,
}


def combine_segmentations_of_sample(sample):
    structure = cardiac_structures[0]

    input_file = os.path.join(input_dir, sample, structure + ".nii.gz")
    # print("Processing : ", input_file)
    img = sitk.ReadImage(input_file)
    img_arr = sitk.GetArrayFromImage(img)

    output_arr = np.zeros_like(img_arr, dtype=output_dtype)
    mask = img_arr == 1
    output_arr[mask] = structure2label[structure]

    for structure in cardiac_structures[1:]:
        input_file = os.path.join(input_dir, sample, structure + ".nii.gz")
        # print("Processing : ", input_file)
        img = sitk.ReadImage(input_file)
        img_arr = sitk.GetArrayFromImage(img)
        mask = img_arr == 1
        output_arr[mask] = structure2label[structure]

    output_img = sitk.GetImageFromArray(output_arr)
    output_img.CopyInformation(img)

    output_file = os.path.join(output_dir, sample + ".nii.gz")
    sitk.WriteImage(output_img, output_file)
    # print("\nWriting output file : ", output_file)


def list_subdirs(path):
    for f in os.listdir(path):
        f_path = os.path.join(path, f)
        if not f.startswith('.') and os.path.isdir(f_path):
            yield f


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-input", required=True)
    parser.add_argument("-output", required=True)
    parser.add_argument("-dtype", default="uint16")
    args = parser.parse_args()

    output_dtype = args.dtype
    input_dir = args.input
    output_dir = args.output
    make_output_dir(output_dir)
    subfolders = list(list_subdirs(input_dir))

    for folder in subfolders:
        sample = os.path.basename(folder)
        print("Processing sample : ", sample)
        combine_segmentations_of_sample(sample)
