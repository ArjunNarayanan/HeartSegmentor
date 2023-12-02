import subprocess
import glob
import argparse
import os
import sys


def make_folder_if_missing(dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)


def segment_all_files():
    for filename in input_files:
        sample_name = (os.path.basename(filename)).split(".")[0]
        sample_output_folder = os.path.join(output_folder, sample_name)
        make_folder_if_missing(sample_output_folder)
        print("Processing file : ", filename)

        subprocess.run(
            ["TotalSegmentator -i " + filename + " -o " + sample_output_folder + " -ta heartchambers_highres"],
            shell=True
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-input", help="input folder", required=True)
    parser.add_argument("-output", help="output folder", required=True)
    parser.add_argument("-extension", help="input file extension", default=".nii.gz")
    args = parser.parse_args()

    input_folder = args.input
    output_folder = args.output

    input_files = glob.glob(os.path.join(input_folder, "*" + args.ext))
