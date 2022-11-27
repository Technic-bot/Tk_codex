import argparse 
import pandas as pd

def proc_opts():
  parser = argparse.ArgumentParser('Twokinds CSV massager')
  parser.add_argument('file', help='Input raw csv')
  parser.add_argument('outchars', help='Prefix for output files')
  parser.add_argument('outdial', help='Prefix for output files')
  return parser.parse_args()

def get_characters(df):
  chars_df = df['transcript'].str.extractall(r'(\w+\:)')
  chars_df = chars_df.droplevel(level=1)
  
  chars_df.reset_index(inplace=True)
  chars_df.rename(columns={0:"character"},inplace=True)
  chars_df['character'] = chars_df['character'].str.strip(":")
  chars_df.sort_values('page',inplace=True)
  chars_df.drop_duplicates(inplace=True)

  return chars_df

def get_dialogue(df):
  df['dialogue'] = df['transcript'].str.split('\n')
  dial = df.explode('dialogue')
  dial['speaker'] = dial['dialogue'].str.extract(r'(\w+\:)')
  dial['dialogue'] = dial['dialogue'].str.replace(r'(\w+\:)','',regex=True)
  dial['speaker'] = dial['speaker'].str.strip(':')
  return dial[['dialogue','speaker']]

if __name__=="__main__":
  args = proc_opts()
  
  twk_df = pd.read_csv(args.file,index_col="page")

  chars_df = get_characters(twk_df)
  chars_df.set_index('page',inplace=True)
  chars_df.to_csv(args.outchars)

  dial_df = get_dialogue(twk_df)
  dial_df.to_csv(args.outdial)

