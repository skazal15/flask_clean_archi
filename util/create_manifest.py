import pandas as pd
from util.create_folder import create_folder
import os


def create_manifest(Batch):
    cwd = os.getcwd()
    path_raw_data = os.path.join(cwd,"data/",Batch)
    path_processed_data = os.path.join(cwd,"data/", Batch)
    manifest_file = os.path.join(path_processed_data, Batch+"_manifest.tsv")

    files = pd.Series(os.listdir(path_raw_data))
    fastq_files = files[files.str.endswith('.fastq.gz')]
    df = pd.DataFrame({'filename': fastq_files})
    df['sample-id'] = df['filename'].str.extract(r'(.*)(_L001_R.*_001.fastq.gz)')[0]
    df.drop_duplicates(subset=['sample-id'], keep='first', inplace=True)
    df['forward-absolute-filepath'] = df['sample-id'].apply(lambda x: os.path.join(path_raw_data, f"{x}_L001_R1_001.fastq.gz"))
    df['reverse-absolute-filepath'] = df['sample-id'].apply(lambda x: os.path.join(path_raw_data, f"{x}_L001_R2_001.fastq.gz"))
    df[['sample-id', 'forward-absolute-filepath', 'reverse-absolute-filepath']].to_csv(manifest_file, sep='\t', index=False)

def create_sample(folder,Group):
    for group in Group:
        cwd = os.getcwd()
        path_raw_data = os.path.join(cwd,"data/",folder)
        path_processed_data = os.path.join(cwd,"sample/", folder)
        sample_file = os.path.join(path_processed_data, folder+"_sample_names_"+group+".tsv")

        if os.path.isdir(path_processed_data):
                print("folder ready")
        else:
            create_folder(path_processed_data)

        files = pd.Series(os.listdir(path_raw_data))
        fastq_files = files[files.str.endswith('.fastq.gz')]
        df = pd.DataFrame({'filename': fastq_files})
        df['sample-id'] = df['filename'].str.extract(r'(.*)(_L001_R.*_001.fastq.gz)')[0]
        df.drop_duplicates(subset=['sample-id'], keep='first', inplace=True)
        df['group']=group
        df[['sample-id','group']].to_csv(sample_file, sep='\t', index=False)



