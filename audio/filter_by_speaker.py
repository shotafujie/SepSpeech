import argparse
import array
import math
import numpy as np
import random
import wave
import pandas as pd

'''
 話者名（話者情報）をもとに振り分ける
'''
def main(args):

    speakers=[]
    #読み込み用でファイルをfとして開く
    with open(args.speakers, 'r') as f:
        lines = f.readlines()
        for line in lines:
           #両端の空白文字を除去して，追加
           speakers.append(line.strip())

    df = pd.read_csv(args.csv)
    for index, row in df.iterrows():
        speaker = row['speaker']
        #argsがTrueならば，読み込んだCSVのindex番目の行を削除する.
        if args.remove is True:
            if speaker in speakers:
                df.drop(index=index, inplace=True)
                continue
        else:
            if speaker not in speakers:
                df.drop(index=index, inplace=True)
                continue
    df.to_csv(args.output_csv, index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', type=str, required=True)
    parser.add_argument('--output-csv', type=str, required=True)
    parser.add_argument('--remove', action='store_true')
    parser.add_argument('--speakers', type=str, required=True)
    args=parser.parse_args()

    main(args)
