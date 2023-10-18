# curl -L -O https://github.com/Ensembl/ensembl-vep/archive/release/110.zip
# unzip 110.zip
# cd ensembl-vep-release-110/
# perl INSTALL.pl --NO_TEST


# cd varan_env
# git clone https://github.com/Ensembl/ensembl-vep.git
# cd ensembl-vep
# git pull
# git checkout release/110
# perl INSTALL.pl



conda env create -f environment.yml -p ./varan_env
 source activate ./varan_env
 conda install -y -c bioconda bcftools
 conda install -y -c bioconda htslib
 conda install -y -c bioconda samtools
 #source activate ./varan_env


wget https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/clinvar.vcf.gz -p 
wget https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/clinvar.vcf.gz.tbi -p 


 wget https://ftp.ensembl.org/pub/release-110/variation/indexed_vep_cache/homo_sapiens_vep_110_GRCh37.tar.gz
 mv homo_sapiens_vep_110_GRCh37.tar.gz ftp.ncbi.nlm.nih.gov
 gzip -d ./ftp.ncbi.nlm.nih.gov/homo_sapiens_vep_110_GRCh37.tar.gz


mkdir ./varan_env/vep_db
mkdir ./varan_env/vep_db/GRCh37/
mkdir ./varan_env/vep_db/GRCh37/vep
vep_install -a cf -s homo_sapiens -y GRCh37 -c ./varan_env/vep_db/GRCh37/vep --CONVERT

# python func/setup_log.py
