
# In-depth functions

### Block One: Create Study Folder ex-Novo

<p align="justify">Below are reported and explained the functions called by the main `varan.py`. These functions can also be called separetely by giving their specific input.

* **walk.py**<br><p align="justify">The `walk.py`  function is a Python script that processes Variant Call Format (VCF) files containing genetic information about Single Nucleotide Polymorphism (SNP) and Copy Number Variation (CNV) variants. Once the `walk` is executed, you will have an output containing the Minor Allele Frequencies (MAF).

	*Options*
	`-d` input is a folder
	`-i` path to input
	`-t` snv or cnv
	`-f` filter snv
	`-o` path to output
	`-w` rewrite study folder

	*Example:*
	- file input
	```
	python3 walk.py  -i <path_to_input_file> -f -t <cnv or snv> -o <path_output_folder> -w
	```
	- folder input
	```
	python3 walk.py  -i <path_to_input_directory> -d -f -o <path_ output_ folder> -w
	```

* **filter_clinvar.py**<br><p align="justify">The `filter_clinvar.py` function is a Python script to filter mutations according to ClinVar annotation and/or mutation consequence.

	-  **VUS option**:

		Through this filter all mutations that **aren't annotated as *benign* or *likely benign*** will be maintained.

  

	-  **NO_VUS option**:

		The first step is the elimination of all mutations annotated as *benign* or *likely benign*.

		Next, the script retaines variants annotated in **Clinvar** such as

		-  *risk_factor*

		-  *pathogenic*

		-  *likely_pathogenic*

		-  *drug_response*.

		
		or mutations that have terms in the Consequence column such as

  

		-  *splice_region_variant*,

		-  *frameshift_variant*,

		-  *splice_donor_variant*,

		-  *stop_gained*,

		-  *splice_acceptor_variant*,

		-  *start_lost*,

		-  *inframe_insertion*,

		-  *inframe_deletion*

	*Options*
	`-f` path folder containing the maf files
	`-o` output folder
	`-v` filter out VUS variants

	*Example:*
	```
	python3 filter_clinvar.py  -f <path_ folder_ maf_ files> -o <path_ output_ folder> -v
	```



  
* **Concatenate.py**<p align="justify"> The `concatenate.py` is a Python script that can be used to merge the MAF files of single 	patients, into a unique file<br> *Options*<br> `-f` path folder containing the maf files<br> `-e` extensionofthefilestoconcatenate (eg. .maf) <br> `-o` output file<br>
 *Example*:
	```
	python3 concatenate.py -f <path_folder_maf_files> -e <extension_of_the_files_to_concatenate> - o <outputfile>
	```

  
* **Make_meta_and_cases.py**<br><p align="justify"> The `Make_meta_and_cases.py` function is a Python script that creates all the required metafiles
	* meta_study.txt
	* meta_clinical_patient.txt
	* meta_clinical_sample.txt
	* data_mutations_extended.txt
	* meta_sv.txt
	* meta_cna.txt
	* meta_cna_hg19_seg.txt

	It also create the case list files:
	* cases_sequenced.txt
	* cases_cna.txt
	* cases_sv.txt		

	*Options* <br>`-c`cancer_type <br>`-v` filter out VUS variants<br>`-o` output folder<br>
*Example*:
```
python3 Make_meta_and_cases_to_study_ -c <cancer_type> -v -o <path_output_to_study_folder> -v -o
```

* **ValidateFolder.py**<br><p align="justify"> The `ValidateFolder.py` checks the contents of a study folder against a set of required files for different categories (e.g., Patient, Study, CNA, Fusion, SNV) that are necessary for uploading data to cBioPortal. It logs any missing files and provides a success message if all required files are present.<br>
*Options* <br>`-f` path of the study folder to validate<br>
*Example*:
```
python3 ValidateFolder -f <path_study_folder> 
```
#
### Block Two: Modify Existing Study Folder

 * **Update_script.py**<br><p align="justify">Th function `Update_script.py` covers the update samples process. In particular, after giving an existing study folder and a newer version of this study folder containing novel or updated information, *Update_script.py* concatenates the newer info and update the oldest with the new ones. These modifications are applied to all of the txt files contained inside the study folder<p align="justify">The output will be a new study folder saved in the path selected by the -o option and will be an updated version of the original folder.<br>
 *Options*<br>`-p` path of the original study folder<br>`-n` path to the new study folder<br>`-o` path to save the updated study folder<br>
*Example*: 
```
python3 Update_script -p <path_to_old_study_folder> -n <path_to_new_study_folder> -o <path_to_output_folder>
```
<br>

* **Delete_script.py**<br> <p align="justify">Th covers the delete samples process. In particular, after giving an existing study folder and a list of samples to remove, *Delete_script.py* deletes the info regarding the samples of interest. These modifications are applied to all of the txt files contained inside the study folder.<br>
*Options:*<br>`-p` path of the original study folder<br>`-s` path to the list of samples to remove<br>`-o` path to save the study folder without the removed samples<br>
*Example*:
```
python3 Delete_script -p <path_to_old_study_folder> -n <path_to_new_study_folder> -o <path_to_output_folder>
```
<br>

* **ExtractSamples_script.py**<br><p align="justify">This function covers the extract samples process. In particular, after giving an existing study folder and a list of samples to extract, *ExtractSample_script.py* extracts the info regarding the samples of interest. These modifications are applied to all of the txt files contained inside the study folder.<br><br>*Options:*<br>`-p` path of the original study folder<br>`-s` path to the list of samples to extract<br>`-o` path to save the study folder with the extracted samples<br>
*Example*:
```
python3 ExtractSamples_script -p <path_to_old_study_folder> -n <path_to_new_study_folder> -o <path_to_output_folder>
```

