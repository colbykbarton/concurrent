from concurrent import futures
import threading
import time
import urllib.request

flags = ['aa', 'ac', 'ae', 'af', 'ag', 'aj', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'as', 'at', 'au', 'av', 'ax',
         'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'bg', 'bh', 'bk', 'bl', 'bm', 'bn', 'bo', 'bp', 'bq', 'br', 'bt', 'bu',
         'bv', 'bx', 'by',
         'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'cg', 'ch', 'ci', 'cj', 'ck', 'cm', 'cn', 'co', 'cr', 'cs', 'ct', 'cu',
         'cv', 'cy',
         'da', 'dj', 'do', 'dr', 'dx',
         'ec', 'ee', 'eg', 'ei', 'ek', 'en', 'er', 'es', 'et', 'ez',
         'fi', 'fj', 'fk', 'fm', 'fo', 'fp', 'fr', 'fs',
         'ga', 'gb', 'gg', 'gh', 'gi', 'gj', 'gk', 'gl', 'gm', 'gq', 'gr', 'gt', 'gv', 'gy',
         'ha', 'hk', 'hm', 'ho', 'hr', 'hu',
         'ic', 'id', 'im', 'in', 'io', 'ip', 'ir', 'is', 'it', 'iv', 'iz',
         'ja', 'je', 'jm', 'jn', 'jo',
         'ke', 'kg', 'kn', 'kr', 'ks', 'kt', 'ku', 'kv', 'kz',
         'la', 'le', 'lg', 'lh', 'li', 'lo', 'ls', 'lt', 'lu', 'ly',
         'ma', 'mc', 'md', 'mg', 'mx',
         'nc', 'ne', 'nf', 'ng', 'nh', 'ni', 'nl', 'no', 'np', 'nr', 'ns', 'nu', 'nz',
         'od',
         'pa', 'pc', 'pe', 'pk', 'pl', 'pm', 'po', 'pp', 'pu',
         'qa',
         'ri', 'rm', 'rn', 'ro', 'rp', 'rq', 'rs', 'rw',
         'sa', 'sb', 'sc', 'se', 'sf', 'sg', 'sh', 'si', 'sk', 'sl', 'sm', 'sn', 'so', 'sp', 'st', 'su', 'sv', 'sw',
         'sx', 'sy', 'sz',
         'tb', 'td', 'th', 'ti', 'tk', 'tl', 'tn', 'to', 'tp', 'ts', 'tt', 'tu', 'tv', 'tw', 'tx', 'tz',
         'ug', 'uk', 'um', 'up', 'us', 'uv', 'uy', 'uz',
         'vc', 've', 'vi', 'vm', 'vq', 'vt',
         'wa', 'wf', 'wq', 'ws', 'wz',
         'ym',
         'za', 'zi']
outFile = open(r"fthread.txt", "w")
start_time = time.time()
cpu_start = time.process_time()
filesize = 0

def getsize(count, blocksize, totalSize):
    global filesize
    filesize += totalSize

def downloadFun(x):
    y = urllib.request.urlretrieve(
        "https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/" + x + "-lgflag.gif",
        "flags/" + x + ".gif", reporthook=getsize)
    print(y[1][3])
    return y[1][3]


fun = futures.ThreadPoolExecutor()
result = fun.map(downloadFun, flags)
myResults = list(result)
print("Total bytes downloaded: " + str(filesize))
outFile.write("Total bytes Downloaded: " + str(filesize) + "\n")
end_time = time.time()
print("Time elapsed is: ", str(end_time - start_time))
outFile.write("Time elapsed is: " + str(end_time - start_time) + "\n")
cpu_end = time.process_time()
print("CPU Time in Seconds: ", str(cpu_end - cpu_start))
outFile.write("CPU Time in Seconds: " + str(cpu_end - cpu_start))