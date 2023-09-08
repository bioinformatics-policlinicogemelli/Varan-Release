#! /bin/bash
#PBS -o /home/04914107/lung/vep.stdout
#PBS -e /home/04914107/lung/vep.stderr
#PBS -l select=1:ncpus=16:mem=50g
#PBS -M alessia.preziosi@guest.policlinicogemelli.it
#PBS -m ae
#PBS -N vep
#PBS -q workq

module load anaconda/3

conda init bash
source ~/.bashrc
conda activate /data/hpc-data/shared/pipelines/varan/varan_env


for vcf in $(find /home/04914107/lung -maxdepth 1 -type f -name '*.vcf'); do
    vep -i $vcf -o $vcf.vep \
    --tab \
    --no_stats \
    --species homo_sapiens \
    --assembly GRCh37 \
    --offline \ 
    --cache_version 88 \
    --dir /data/hpc-data/shared/pipelines/varan/vep_db/GRCh37/vep \
    --canonical \
    --xref_refseq \
    --hgvs \
    --hgvsg \
    --symbol \
    --variant_class \
    --check_existing \
    --allele_number \
    --minimal \
    --pick_order canonical \
    --fork 4 \
    --custom /data/hpc-data/shared/pipelines/varan/ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/clinvar.vcf.gz,ClinVar,vcf,exact,0,CLNSIG
done
