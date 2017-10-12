import pandas as pd
import glob

if __name__=="__main__":
    data = pd.DataFrame()
    outfile = '../indiegogo_raw_data.tsv'

    for f in glob.glob('*.csv'):
        print("Processing {}...".format(f))
        # Load in_forever_funding as str to replace a null value causing type
        # error (the remaining values are boolean)
        data = pd.concat([data,pd.read_csv(f,
                                           dtype={'in_forever_funding': str})])
        data.in_forever_funding.replace(['null'], ['True'], inplace=True)

    print('Saving concatenated file as {}'.format(outfile))
    data.to_csv(outfile, index=False, sep="\t")