import argparse 
import pandas as pd

def proc_opts():
  parser = argparse.ArgumentParser('Twokinds CSV massager')
  parser.add_argument('file', help='Input raw csv')
  parser.add_argument('outfile', help='Prefix for output files')

  return parser.parse_args()

if __name__=="__main__":
  args=proc_opts()
  twk_df = pd.read_csv(args.file,index_col="page")

  max_page = twk_df.index.max()
  print(f"Max page is: {max_page}")

  unq_chars = twk_df['speaker'].unique()
  print(twk_df['speaker'].isna() )
  print(twk_df.loc[1186])
  print(unq_chars)

