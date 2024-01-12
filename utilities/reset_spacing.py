import SimpleITK as sitk


filename = "/Users/arjun/Documents/Research/SimCardio/Datasets/CardiacAndVascular/nifti/0174_0000.nii.gz"
outputfile = "/Users/arjun/Documents/Research/SimCardio/Datasets/CardiacAndVascular/respaced-nifti/0174_0000.nii.gz"
img = sitk.ReadImage(filename)