import os
# COMPUTER_NAME = os.environ['COMPUTERNAME']
# print("Computer: ", COMPUTER_NAME)

TARGET_VOXEL_MM = 1.00
MEAN_PIXEL_VALUE_NODULE = 41
LUNA_SUBSET_START_INDEX = 1
SEGMENTER_IMG_SIZE = 320

BASE_DIR_SSD = "/data/"  #"C:/werkdata/kaggle/ndsb3/"
BASE_DIR = "/data/" # "D:/werkdata/kaggle/ndsb3/"
EXTRA_DATA_DIR = "resources/"
# NDSB3_RAW_SRC_DIR = BASE_DIR + "ndsb_raw/stage12/"
NDSB3_RAW_SRC_DIR = BASE_DIR + "kaggle/stage12/stage1/"
# LUNA16_RAW_SRC_DIR = BASE_DIR + "luna_raw/"
LUNA16_RAW_SRC_DIR = BASE_DIR + "LUNA16/"

NDSB3_EXTRACTED_IMAGE_DIR = BASE_DIR + "ndsb3_extracted_images/"
LUNA16_EXTRACTED_IMAGE_DIR = BASE_DIR + "luna16_extracted_images/"
NDSB3_NODULE_DETECTION_DIR = BASE_DIR + "ndsb3_nodule_predictions/"

