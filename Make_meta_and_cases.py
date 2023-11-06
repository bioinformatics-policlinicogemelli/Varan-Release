# cBioportal metafile
import os
from configparser import ConfigParser
from populate_case_lists import populate_cases_cna,populate_cases_sequenced,populate_cases_sv
from loguru import logger
from versioning import extract_version_str
import pandas as pd


def create_meta_study(cancer, project_name,vus, description, output_dir,version):
    """
        Function to create meta_study_file
    Args:
        cancer : cancer type
        vus : Flag to select Vus inclusion
        description : optional description to overwrite default description
        output_dir : path of output dir
    """
    
    if vus:
        study_id = cancer+"_"+project_name+version+"_NoVus"
    else:
        study_id = cancer+"_"+project_name+version

    if vus:
        name = cancer.capitalize()+" Cancer ("+project_name.upper()+")"+version+ "_NoVus"
    else:
        name = cancer.capitalize()+" Cancer ("+project_name.upper()+")"+version
    add_global_case_list = "true"

    if description == " ":
        if vus:
            description = "Comprehensive profiling of "+cancer.capitalize() + \
                " cancer samples including VUS variants. Generated by the Fondazione Policlinico Universitario Agostino Gemelli IRCCS."
        else:
            description = "Comprehensive profiling of "+cancer.capitalize() + \
                " cancer samples. Generated by the Fondazione Policlinico Universitario Agostino Gemelli IRCCS."

    dictionary_file = {
        "type_of_cancer": cancer, 
        "cancer_study_identifier": study_id,
        "name": name, 
        "add_global_case_list": add_global_case_list,
        "description": description
        }

    meta_file = open(f"{output_dir}/meta_study.txt", "w")
    logger.info("Writing meta_study.txt file...")
    
    for key, value in dictionary_file.items():
        logger.info(f"{key}: {value}", file=meta_file)
        print(f"{key}: {value}", file=meta_file)
    meta_file.close()


def create_meta_clinical_patient(cancer,project_name, vus, output_dir,version):
    """
        Function to create meta_clinical_patient
    Args:
        cancer : cancer type
        vus : Flag to select Vus inclusion
        output_dir : path of output dir
    """

    if vus:
        study_id = cancer+project_name+version+"_NoVus"
    else:
        study_id = cancer+project_name+version

    alteration_type = "CLINICAL"
    datatype = "PATIENT_ATTRIBUTES"
    data_filename = "data_clinical_patient.txt"
    dictionary_file = {
        "cancer_study_identifier": study_id,
        "genetic_alteration_type": alteration_type,
        "datatype": datatype,
        "data_filename": data_filename,
    }
    meta_file = open(f"{output_dir}/meta_clinical_patient.txt", "w")
    logger.info("Writing meta_clinical_patient.txt file...")
    for key, value in dictionary_file.items():
        logger.info(f"{key}: {value}", file=meta_file)
        print(f"{key}: {value}", file=meta_file)
    meta_file.close()


def create_meta_clinical_sample(cancer,project_name, vus, output_dir,version):
    """
        Function to create meta_clinical_sample
    Args:
        cancer : cancer type
        vus : Flag to select Vus inclusion
        output_dir : path of output dir
    """

    if vus:
        study_id = cancer+project_name+version+"_NoVus"
    else:
        study_id = cancer+project_name+version

    alteration_type = "CLINICAL"
    datatype = "SAMPLE_ATTRIBUTES"
    data_filename = "data_clinical_sample.txt"
    dictionary_file = {
        "cancer_study_identifier": study_id,
        "genetic_alteration_type": alteration_type,
        "datatype": datatype,
        "data_filename": data_filename,
    }
    meta_file = open(f"{output_dir}/meta_clinical_sample.txt", "w")
    logger.info("Writing meta_clinical_sample.txt file...")
    for key, value in dictionary_file.items():
        logger.info(f"{key}: {value}", file=meta_file)
        print(f"{key}: {value}", file=meta_file)
    meta_file.close()


def create_meta_mutations(cancer, project_name,vus, profile, output_dir,version):
    """
        Function to create meta_mutations
    Args:
        cancer : cancer type
        vus : Flag to select Vus inclusion
        profile: Description to overwrite default description
        output_dir : path of output dir
    """

    if vus:
        study_id = cancer+project_name+version+"_NoVus"
    else:
        study_id = cancer+project_name+version

    alteration_type = "MUTATION_EXTENDED"
    datatype = "MAF"
    stable_id = "mutations"
    profile_in_analysis_tab = "TRUE"
    profile_name = "Mutations"

    if profile == " ":
        profile = "Sequencing of "+cancer.capitalize() + \
            " tumor via TruSight Oncology 500 High Throughput panel (TSO500HT) on Illumina NovaSeq6000 sequencers"

    data_filename = "data_mutations_extended.txt"

    dictionary_file = {
        "cancer_study_identifier": study_id,
        "genetic_alteration_type": alteration_type,
        "datatype": datatype,
        "stable_id": stable_id,
        "show_profile_in_analysis_tab": profile_in_analysis_tab,
        "profile_name": profile_name,
        "profile_description": profile,
        "data_filename": data_filename,
    }
    meta_file = open(f"{output_dir}/meta_mutations_extended.txt", "w")
    logger.info("Writing meta_mutations_extended.txt file...")
    for key, value in dictionary_file.items():
        logger.info(f"{key}: {value}", file=meta_file)
        print(f"{key}: {value}", file=meta_file)
    meta_file.close()


def create_meta_sv(cancer,project_name, vus, output_dir,version):
    """
        Function to create meta_sv
    Args:
        cancer : cancer type
        vus : Flag to select Vus inclusion
        output_dir : path of output dir
    """
    
    if vus:
        study_id = cancer+project_name+version+"_NoVus"
    else:
        study_id = cancer+project_name+version

    alteration_type = "STRUCTURAL_VARIANT"
    datatype = "SV"
    stable_id = "structural_variants"
    profile_in_analysis_tab = "false"
    profile_name = "Structural variants"

    profile = "Structural Variant Data for "+study_id

    data_filename = "data_sv.txt"

    dictionary_file = {
        "cancer_study_identifier": study_id,
        "genetic_alteration_type": alteration_type,
        "datatype": datatype,
        "stable_id": stable_id,
        "show_profile_in_analysis_tab": profile_in_analysis_tab,
        "profile_name": profile_name,
        "profile_description": profile,
        "data_filename": data_filename,
    }

    meta_file = open(f"{output_dir}/meta_sv.txt", "w")
    logger.info("Writing meta_sv.txt file...")
    for key, value in dictionary_file.items():
        logger.info(f"{key}: {value}", file=meta_file)
        print(f"{key}: {value}", file=meta_file)
    meta_file.close()


def create_meta_cna(cancer,project_name, vus, output_dir,version):
    """
        Function to create meta_cna
    Args:
        cancer : cancer type
        vus : Flag to select Vus inclusion
        output_dir : path of output dir
    """

    if vus:
        study_id = cancer+project_name+version+"_NoVus"
    else:
        study_id = cancer+project_name+version

    alteration_type = "COPY_NUMBER_ALTERATION"
    datatype = "DISCRETE"
    stable_id = "cna"
    profile_in_analysis_tab = "true"
    profile_name = "Putative copy-number alterations from GISTIC of "+cancer+" tumor FPG500"

    profile = "Putative copy-number from GISTIC 2.0. Values:  -2 = hemizygous deletion; 0 = neutral / no change; 2 = gain."

    data_filename = "data_cna.txt"

    dictionary_file = {
        "cancer_study_identifier": study_id,
        "genetic_alteration_type": alteration_type,
        "datatype": datatype,
        "stable_id": stable_id,
        "show_profile_in_analysis_tab": profile_in_analysis_tab,
        "profile_name": profile_name,
        "profile_description": profile,
        "data_filename": data_filename,
    }

    meta_file = open(f"{output_dir}/meta_cna.txt", "w")
    logger.info("Writing meta_cna.txt file...")
    for key, value in dictionary_file.items():
        logger.info(f"{key}: {value}", file=meta_file)
        print(f"{key}: {value}", file=meta_file)
    meta_file.close()


def create_meta_cna_hg19(cancer,project_name, vus, output_dir,version):
    """
        Function to create meta_cna_hg19
    Args:
        cancer : cancer type
        vus : Flag to select Vus inclusion
        output_dir : path of output dir
    """
    
    if vus:
        study_id = cancer+project_name+version+"_NoVus"
    else:
        study_id = cancer+project_name+version

    alteration_type = "COPY_NUMBER_ALTERATION"
    datatype = "SEG"
    genome_id = "hg19"
    profile = "Somatic CNA data (copy number ratio from tumor samples minus ratio from matched normals) from FPG500."
    data_filename = "data_cna_hg19.seg"

    dictionary_file = {
        "cancer_study_identifier": study_id,
        "genetic_alteration_type": alteration_type,
        "datatype": datatype,
        "reference_genome_id": genome_id,
        "description": profile,
        "data_filename": data_filename,
    }

    meta_file = open(f"{output_dir}/meta_cna_hg19_seg.txt", "w")
    logger.info("Writing meta_cna_hg19_seg.txt file...")
    for key, value in dictionary_file.items():
        logger.info(f"{key}: {value}", file=meta_file)
        print(f"{key}: {value}", file=meta_file)
    meta_file.close()


def meta_case_main(cancer,vus,output_folder):
    
    logger.info("Starting meta_case_main script:")
    logger.info(f"meta_case_main args [cancer:{cancer}, vus:{vus}, output_file:{output_folder}]")
    
    config = ConfigParser()
    configFile = config.read("conf.ini")
    project=config.get("Project","PROJECT_NAME")
    project_name="_"+project
    
    description=config.get("Project","DESCRIPTION")
    profile=config.get("Project","PROFILE")

    logger.info("Creating case list folder...")
    cases_list_dir = os.path.join(output_folder, "case_lists")
    if os.path.exists(cases_list_dir):
        logger.info("It seemps that this folder already exists")
        pass
    else:
        os.mkdir(cases_list_dir)

    version=extract_version_str(output_folder)
    ###########  METAFILE FUNCTIONS ###########
    
    create_meta_study(cancer,project, vus, description, output_folder,version)
    
    if os.path.exists(os.path.join(output_folder,"data_clinical_patient.txt")):
        create_meta_clinical_patient(cancer, project_name,vus, output_folder,version)
        logger.info("meta_clinical_patient.txt created!")
    if os.path.exists(os.path.join(output_folder,"data_clinical_sample.txt")):
        create_meta_clinical_sample(cancer,project_name, vus, output_folder,version)
        logger.info("meta_clinical_sample.txt created!")
    if os.path.exists(os.path.join(os.path.join(output_folder,"data_mutations_extended.txt"))):
        create_meta_mutations(cancer,project_name, vus, profile, output_folder,version)
        logger.info("meta_mutations_extended.txt created!")
    if os.path.exists(os.path.join(os.path.join(output_folder,"data_sv.txt"))):
        create_meta_sv(cancer,project_name, vus, output_folder,version)
        logger.info("meta_sv.txt created!")
    if os.path.exists(os.path.join(output_folder,"data_cna.txt")):
        create_meta_cna(cancer,project_name, vus, output_folder,version)
        logger.info("meta_cna.txt created!")
    if os.path.exists(os.path.join(output_folder,"data_cna_hg19.seg")):
        create_meta_cna_hg19(cancer, project_name,vus, output_folder,version)
        logger.info("meta_cna_hg19.txt created!")

    ########### CASE LIST FUNCTION ###########

    if os.path.exists(os.path.join(output_folder,"data_mutations_extended.txt")):
        file_extended=pd.read_csv(os.path.join(output_folder,"data_mutations_extended.txt"),sep="\t")
        if file_extended.shape[0]>1:
            populate_cases_sequenced(cancer,project_name, vus, output_folder,cases_list_dir,version,logger)
        else:
            os.remove(os.path.join(output_folder,"data_mutations_extended.txt"))
            os.remove(os.path.join(output_folder,"meta_mutations_extended.txt"))
    else: logger.warning("data_mutations_extended.txt file not found!")
    
    if os.path.exists(os.path.join(output_folder,"data_cna.txt")):
        file_cna=pd.read_csv(os.path.join(output_folder,"data_cna.txt"),sep="\t")
        if file_cna.shape[0]>1:
            populate_cases_cna(cancer, project_name,vus,output_folder, cases_list_dir,version,logger)
        else:
            os.remove(os.path.join(output_folder,"data_cna.txt"))
            os.remove(os.path.join(output_folder,"meta_cna.txt"))
    else: logger.warning("data_cna.txt file not found!")
    
    if os.path.exists(os.path.join(output_folder,"data_sv.txt")):
        file_sv=pd.read_csv(os.path.join(output_folder,"data_sv.txt"),sep="\t")
        if file_sv.shape[0]>1:
            populate_cases_sv(cancer,project_name, vus, output_folder,cases_list_dir,version,logger)
        else:
            os.remove(os.path.join(output_folder,"data_sv.txt"))
            os.remove(os.path.join(output_folder,"meta_sv.txt"))
    else: logger.warning("data_sv.txt file not found!")

    logger.success("Make_meta_and_cases script completed!")

