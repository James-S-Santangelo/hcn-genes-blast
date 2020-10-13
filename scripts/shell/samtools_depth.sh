# Script to calculate depth at each position within regions


export BAM_INPATH=../../../GWSD_Genome-Wide-Delection-Demography/gwsd/data/raw/bam/bwa_mapping/RGmod
export BAM_LIST=../../resources/samtools_depth_bams.list
export OUTPATH=../../analysis/samptools_depth
export LOG_PATH=./log_files/samtools_depth
export BED_FILE=../../resources/hcn_coding_sequences_withFlanks.bed

find ${BAM_INPATH} -name "*.bam" > ${BAM_LIST}


function samtools_depth {

    local BAMFILE=${1}
    local SAMPLE=$(basename ${1%_merged*})
    local OUTFILE=${OUTPATH}/${SAMPLE}_hcnLoci.depth
    local LOGFILE=${LOG_PATH}/${SAMPLE}_samtools_depth.log

    #echo "BAMFILE: ${BAMFILE}"
    #echo "SAMPLE: ${SAMPLE}"
    #echo "OUTFILE: ${OUTFILE}"
    #echo "LOGFILE: ${LO_FILE}"
    #echo ""

    echo "Computing depth across regions for ${BAMFILE}" > ${LOGFILE}
    samtools depth -a -b ${BED_FILE} -o ${OUTFILE} ${BAMFILE} 2>> ${LOGFILE}

    echo "" >> ${LOGFILE}
    echo "Done computing depth" >> ${LOGFILE}
}


export -f samtools_depth
mkdir -p ${OUTPATH} ${LOG_PATH}

cat ${BAM_LIST} | parallel -j 40 --progress --verbose samtools_depth {}


