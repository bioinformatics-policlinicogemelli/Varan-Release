import os 
import re 


def extract_version_str(foldername):
    version=extract_version_int(foldername)
    versionname="_v"+str(version)
    return versionname

def extract_version_int(foldername):
    version=re.search(r'_v(\d+)$', foldername).group(1)
    return int(version)



def get_newest_version(output_folder):
    old_versions=[file for file in os.listdir() if output_folder+"_v" in file ]
    #if len(old_versions)>0: 
    old_versions_number=list(map(extract_version_int,old_versions))
    version="_v"+str(max(old_versions_number)+1)
    output_folder_version=output_folder+version
    return output_folder_version


def create_newest_version_folder(outputfolder):
    version="_v1"
    output=outputfolder+version
    if not os.path.exists(output):
        os.mkdir(output)
        return output
    else:
        outputfolder_newest_version=get_newest_version(outputfolder)
        os.mkdir(outputfolder_newest_version)
        return outputfolder_newest_version
    
