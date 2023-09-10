version = "1.0"
# ===============================================

import os 
import sys
import argparse
from loguru import logger 
from configparser import ConfigParser
from walk import walk_folder 
from filter_clinvar import filter_main
from concatenate import concatenate_main
from ValidateFolder import validateFolderlog
from Make_meta_and_cases import meta_case_main
from Update_script import update_main 
from Delete_script import delete_main 
from ExtractSamples_script import extract_main

def varan(args):
    
    logger.info(f"Varan args [input:{args.input}, output_folder:{args.output_folder}, filter_snv:{args.filter_snv}, cancer:{args.Cancer}, \
                            vcf_type:{args.vcf_type}, overwrite_output:{args.overWrite}, vus:{args.vus}], \
                            update:{args.Update}, extract:{args.Extract}, remove:{args.Remove}")

    if not any([args.Update ,args.Extract , args.Remove]) :       
            
            ###########################
            #        1.  WALK         #
            ###########################
            
            logger.info("Starting preparation study folder")
            walk_folder(args.input, args.output_folder, args.overWrite, args.vcf_type,args.filter_snv)

            ###########################
            #       2. FILTER         #
            ###########################
        
            logger.info("Starting filter")    
            filter_main(args.output_folder, args.output_folder, args.vus,args.overWrite)

            ############################
            #      3. CONCATENATE      #
            ############################

            logger.info("Concatenate mutation file")
            folders=["NoBenign"]
            if args.vus:
                folders.append("NoVus")
            
            for folder in folders:
                input_folder=os.path.join(args.output_folder,folder)
                output_file=os.path.join(input_folder,"data_mutations_extended.txt")
                concatenate_main(input_folder,"maf",output_file)
        
            if args.vus:
                logger.info("Extracting data_mutations_extended from NoVUS folder") 
                os.system("cp "+os.path.join(args.output_folder,os.path.join("NoVus","data_mutations_extended.txt"))+" "+ args.output_folder )
            else:
                logger.info("Extracting data_mutations_extended from NoBenign folder") 
                os.system("cp "+os.path.join(args.output_folder,os.path.join("NoBenign","data_mutations_extended.txt"))+" "+ args.output_folder )
            
            
            ###########################################
            #      4. MAKE AND POPULATE TABLES        #
            ###########################################

            logger.info("It's time to create tables!")
            meta_case_main(args.Cancer,args.vus,args.output_folder)

            
            ############################
            #      5. VALIDATION       #
            ############################
            logger.info("Starting Validation Folder")
            validateFolderlog(args.output_folder)
            logger.success("The end! The study is ready to be uploaded on cBioportal")
        
    ############################
    #         UPDATE           #
    ############################

    elif args.Update: 
        logger.info("Starting Update study")
        update_main(args.Path,args.NewPath,args.output_folder)

    ############################
    #         DELETE           #
    ############################

    elif args.Remove:
        logger.info("Starting Delete samples from study")  
        delete_main(args.Path,args.SampleList,args.output_folder)

    ############################
    #         EXTRACT          #
    ############################

    elif args.Extract:
        logger.info("Starting Extract samples from study")
        extract_main(args.Path,args.SampleList,args.output_folder)

#################################################################################################################

class MyArgumentParser(argparse.ArgumentParser):
  """An argument parser that raises an error, instead of quits"""
  def error(self, message):
    raise ValueError(message)

if __name__ == '__main__':
	
    logger.remove()
    logfile="Varan_{time:YYYY-MM-DD_HH-mm-ss.SS}.log"
    logger.level("INFO", color="<green>")
    logger.add(sys.stderr, format="{time:YYYY-MM-DD_HH-mm-ss.SS} | <lvl>{level} </lvl>| {message}",colorize=True, catch=True)
    logger.add(os.path.join('Logs',logfile),format="{time:YYYY-MM-DD_HH-mm-ss.SS} | <lvl>{level} </lvl>| {message}",mode="w")
    logger.info("Welcome to VARAN")

    parser = MyArgumentParser(add_help=False, exit_on_error=False, usage=None, description='Argument of Varan script')
    
    # WALK BLOCK
    parser.add_argument('-c', '--Cancer', required=False,help='Cancer Name')
    parser.add_argument('-i', '--input', required=False, help='input folder tsv with data or tsv with path of data')
    parser.add_argument('-f', '--filter_snv', required=False,action='store_true',help='Filter out from the vcf the variants wit dot (.) in Alt column')
    parser.add_argument('-t', '--vcf_type', required=False, choices=['snv', 'cnv'],help='Select the vcf file to parse')
    parser.add_argument('-w', '--overWrite', required=False,action='store_true',help='Overwrite output folder if it exists')

    # FILTER_CLINVAR BLOCK
    parser.add_argument('-v', '--vus', required=False,action='store_true', help='Filter out VUS variants')
    # UPDATE BLOCK
    parser.add_argument('-u', '--Update', required=False,action='store_true',help='Add this argument if you want to concatenate two studies')
    parser.add_argument('-n', '--NewPath', required=False,help='Path of new study folder to add')  
    # DELETE BLOCK
    parser.add_argument('-r', '--Remove', required=False,action='store_true',help='Add this argument if you want to remove samples from a study')
    # EXTRACT BLOCK
    parser.add_argument('-e', '--Extract', required=False,action='store_true', help='Add this argument if you want to extract samples from a study')
    
    # COMMON BLOCK 
    parser.add_argument('-o', '--output_folder', required=True,help='Output folder')
    parser.add_argument('-s', '--SampleList', required=False,help='Path of file with list of SampleIDs')
    parser.add_argument('-p', '--Path', required=False,help='Path of original study folder')
    

    args = parser.parse_args()
    if args.Update and not all([args.Path,args.NewPath]):
        logger.critical("To update a study, you need to specify both original and new folder paths")
        raise argparse.ArgumentError("To update a study, you need to specify both old and new paths")

    if args.Extract and not all([args.Path,args.SampleList]):
        logger.critical("To extract samples from a study, you need to specify both original folder path and list samples")
        raise argparse.ArgumentError("To extract samples from a study, you need to specify both original folder path and list samples")
    
    if args.Remove and not all([args.Path,args.SampleList]):
        logger.critical("To remove samples from a study, you need to specify both original folder path and list samples")
        raise argparse.ArgumentError("To remove samples from a study, you need to specify both original folder path and list samples")
    
    if not any([args.Update ,args.Extract , args.Remove]) and args.Cancer==None:
            logger.critical("Error Argument: Cancer name is required")
            raise argparse.ArgumentError("Cancer is required")  
    if not any([args.Update ,args.Extract , args.Remove]) and args.input==None:
            logger.critical("Error Argument: Input is required")
            raise argparse.ArgumentError("Input is required")

    varan(args)