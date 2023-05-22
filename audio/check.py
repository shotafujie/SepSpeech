import os, sys
import argparse
import array
import math
import numpy as np
import random
import wave
import pandas as pd

def main(args):
    #音声ファイル名が含まれている？csvファイルを読み込む
    df_speech = pd.read_csv(args.speech_csv)
    
    for index, row in df_speech.iterrows():
        #source列を音声ファルのパスとする
        speech_path=row['source']
        #ファイルを開く
        speech = wave.open(speech_path, 'r')
        buffer = speech.readframes(speech.getnframes())
        #振幅を定義
        amplitude = (np.frombuffer(buffer, dtype="int16")).astype(np.float64)
        print(amplitude.shape)
        #1000個の要素を0に初期化して配列amplitudeに追加
        amplitude=np.append(amplitude, np.zeros(1000,))
        print(amplitude.shape)
        exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #str型の'--speech-csv'をオプショナル引数として定義
    parser.add_argument('--speech-csv', type=str, required=True)
    args=parser.parse_args()

    main(args)
