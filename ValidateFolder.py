import os
from os import walk
import argparse
from loguru import logger
import sys

def validateFolderlog(folder, log=False):
    """
    Validates the contents of the folder against required files for cBioPortal data upload.
    
    This function checks the contents of the folder against a set of required files for different categories
    (e.g., Patient, Study, CNA, Fusion, SNV) that are necessary for uploading data to cBioPortal. It logs any
    missing files and provides a success message if all required files are present.

    Args:
        folder (str): Path to the folder to be validated.
        logfile (str): Path to the log file where validation messages will be logged.

    Notes:
        - The function checks the presence of required files within the specified 'folder' and its subdirectories.
        - Required file paths are defined for each category in the 'required_files' dictionary.
        - If any required file is missing, a warning message is logged along with the missing file names.
        - If all required files are present for all categories, a success message is logged.

    Example:
        >>> validateFolderlog('data_folder/', 'validation_log.txt')
    """
    list_files=[]
    for file in os.listdir(folder):
        if os.path.isdir(os.path.join(folder,file)):
            subdir=file
            sudbirfiles=os.listdir(os.path.join(folder,subdir))
            for subdirfile in sudbirfiles:
                list_files.append(os.path.join(subdir,subdirfile))
        else:
            list_files.append(file)

 
    # Define required files for each category
    required_files = {
        "Patient": [
            "data_clinical_patient.txt",
            "meta_clinical_patient.txt",
        ],
        "Study": [
            "data_clinical_sample.txt",
            "meta_study.txt",
            "meta_clinical_sample.txt",
        ],
        "CNA": [
            "case_lists/cases_cna.txt",
            "data_cna.txt",
            "data_cna_hg19.seg",
            "meta_cna.txt",
            "meta_cna_hg19_seg.txt",
        ],
        "Fusion": [
            "case_lists/cases_sv.txt",
            "data_sv.txt",
            "meta_sv.txt",
        ],
        "SNV": [
            "case_lists/cases_sequenced.txt",
            "data_mutations_extended.txt",
            "meta_mutations_extended.txt",
        ],
    }
    
    result_all = {}
    for category, required_files_list in required_files.items():
        missing_files = [elem for elem in required_files_list if elem not in list_files]
        result_all[category] = len(missing_files) == 0
    
        
        if not result_all[category]:
            logger.warning("Missing required files for "+ category)
            logger.warning("Missing files:")
            for missing in missing_files:
                logger.warning("* "+missing)
        
            
    if all(result_all.values()):
        logger.success("Folder contains all required files for cBioportal")



def validateFolder(folder,log=False):
    """
    Validates the contents of a folder against required files for cBioPortal data upload.

    This function checks the contents of a folder against a set of required files for different categories
    (e.g., Patient, Study, CNA, Fusion, SNV) that are necessary for uploading data to cBioPortal. It prints
    any missing files and associated warnings.

    Args:
        folder (str): Path to the folder to be validated.

    Returns:
        None

    Notes:
        - The function checks the presence of required files within the specified 'folder' and its subdirectories.
        - Required file paths are defined for each category in the 'required_files' dictionary.
        - If any required file is missing, a warning message is printed along with the missing file names.

    Example:
        >>> validateFolder('data_folder/')
        
    """
    
    if not log:
        logger.remove()
        logfile="validateFolder_{time:HH-mm-ss.SS}.log"
        logger.level("INFO", color="<green>")
        logger.add(sys.stderr, format="{time:HH-mm-ss.SS} | <lvl>{level} </lvl>| {message}",colorize=True)
        logger.add(os.path.join('Logs',logfile),format="{time:HH-mm-ss.SS} | <lvl>{level} </lvl>| {message}")#,mode="w")
	
    logger.info("Starting validateFolder script:")
    logger.info(f"validateFolder args [folder:{folder}]")
    
    list_files=[]
    for file in os.listdir(folder):
        if os.path.isdir(os.path.join(folder,file)):
            subdir=file
            sudbirfiles=os.listdir(os.path.join(folder,subdir))
            for subdirfile in sudbirfiles:
                list_files.append(os.path.join(subdir,subdirfile))
        else:
            list_files.append(file)

 
    # Define required files for each category
    required_files = {
        "Patient": [
            "data_clinical_patient.txt",
            "meta_clinical_patient.txt",
        ],
        "Study": [
            "data_clinical_sample.txt",
            "meta_study.txt",
            "meta_clinical_sample.txt",
        ],
        "CNA": [
            "case_lists/cases_cna.txt",
            "data_cna.txt",
            "data_cna_hg19.seg",
            "meta_cna.txt",
            "meta_cna_hg19_seg.txt",
        ],
        "Fusion": [
            "case_lists/cases_sv.txt",
            "data_sv.txt",
            "meta_sv.txt",
        ],
        "SNV": [
            "case_lists/cases_sequenced.txt",
            "data_mutations_extended.txt",
            "meta_mutations_extended.txt",
        ],
    }
    
    result_all = {}
    for category, required_files_list in required_files.items():
        missing_files = [elem for elem in required_files_list if elem not in list_files]
        result_all[category] = len(missing_files) == 0
    
        
        if not result_all[category]:
            print("[WARNING] Missing required files for",category)
            print("Missing files:")
            for missing in missing_files:
                print("* ", missing)
        
            
class MyArgumentParser(argparse.ArgumentParser):
  """An argument parser that raises an error, instead of quits"""
  def error(self, message):
    raise ValueError(message)  

if __name__ == '__main__':

    parser = MyArgumentParser(add_help=False, exit_on_error=False, usage=None, description='Parser of Update script for cBioportal')

    parser.add_argument('-f', '--Folder', required=True,
						help='Folder path to check')

    try:
        args = parser.parse_args()
    except Exception as err:
        logger.remove()
        logfile="validate_folder_{time:HH-mm-ss.SS}.log"
        logger.level("INFO", color="<green>")
        logger.add(sys.stderr, format="{time:HH-mm-ss.SS} | <lvl>{level} </lvl>| {message}",colorize=True,catch=True)
        logger.add(os.path.join('Logs',logfile),format="{time:HH-mm-ss.SS} | <lvl>{level} </lvl>| {message}",mode="w")
        logger.critical(f"error: {err}", file=sys.stderr)
    
    folder=args.Folder
    
    if not os.path.exists(folder):
        print(["[WARNING] Folder not found"])
    else:
        validateFolder(folder,log=False)   