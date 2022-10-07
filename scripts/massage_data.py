import argparse 
import pandas as pd

def proc_opts():
  parser = argparse.ArgumentParser('Co ocurrence analyzer')
  parser.add_argument('file', help='Input raw csv')
  parser.add_argument('outfile', help='Prefix for output files')
  return parser.parse_args()

def get_characters(df):
  chars_df = df['transcript'].str.extractall(r'(\w+\:)')
  chars_df = chars_df.droplevel(level=1)
  
  chars_df.reset_index(inplace=True)
  chars_df.rename(columns={0:"character"},inplace=True)
  chars_df['character'] = chars_df['character'].str.strip(":")
  chars_df.sort_values('page',inplace=True)
  chars_df.drop_duplicates(inplace=True)

  print(chars_df)
  return chars_df

if __name__=="__main__":
  args = proc_opts()
  
  twk_df = pd.read_csv(args.file,index_col="page")
  chars_df = get_characters(twk_df)

  chars_df.set_index('page',inplace=True)
  chars_df.to_csv(args.outfile)

