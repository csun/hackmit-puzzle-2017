import pandas as pd
import hashlib, binascii, sys, collections, pprint

md5 = hashlib.md5
df = pd.read_pickle('merged.pkl')
df.dropna(inplace=True)
alpha = list('abcdefghijklmnopqrstuvwxyz1234567890')

def find_names():
    watch_letter = input('Second character:\t')
    # make duplicate character list
    duplicates_alpha = [char*2 for char in alpha]

    # generate md5 column in dataframe
    df['md5'] = [md5(x.encode('utf-8')).hexdigest() for x in df['name']]

    #find the ones that all start with 0
    startszero = []
    for code in df['ccode'].tolist():
        if len(list(str(code)))>1:
            if list(str(code))[1] == watch_letter:
                startszero.append(code)

    interest_names = [df.query('@x in ccode')['name'].tolist()[0] for x in startszero]
    return interest_names
#    pprint.pprint(interest_names)
    #dupes, dupes_names, dupes_inf = [], [], []

    # go search for duplicates and make dupes_inf, a tupled array of [name, ccode, [common characters w/ count]]
    #for duplicate in duplicates_alpha:
    #    dupes += [x for x in df['ccode'].tolist() if duplicate in str(x)]
    #    dupes_names += df.query('ccode == @dupes[-1]')['name'].tolist()
    #    inf = [dupes_names[-1], dupes[-1], 
    #           collections.Counter(dupes_names[-1]).most_common(2)]
    #    if inf not in dupes_inf:
    #        dupes_inf.append(inf)

    # makes binary of all the hashes
    #dupes_inf_bin = int("".join(format(x, 'b') for x in bytearray(dupes_inf[1][0].encode('utf-8'))),2)
    #print(len(bin(dupes_inf_bin)))
    #dupes_inf_bin64 = int(dupes_inf_bin,2) >> 32
    #dupes_inf_bin64 = bin(dupes_inf_bin64)
    #n=8
    #groups = [dupes_inf_bin64[i:i+n] for i in range(2, len(dupes_inf_bin64), n)]
    #n=4
    #pprint.pprint([groups[0][i:i+n] for i in range(2, len(groups[0]), n)])
    #groups = [x for x in ]
    #pprint.pprint([x[0] for x in dupes_inf])