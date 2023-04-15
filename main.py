import os, sys
import hashlib

BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
path = '/home/tiago/Downloads'

def generateMD5Hash(fileName):
    m = hashlib.new('md5')
    try:
        with open(fileName, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                m.update(data)
    except Exception as e:
        print(e)
    return m.hexdigest()

def walkDirectoryGeneratingHashes(path, fileToWrite):
    folderContent = os.walk(path)
    for root, dirs, files in folderContent:
        print('Scanning ' + root + ' directory...')
        for fileName in files:
            filePath = root + '/' + fileName
            fileToWrite.write(generateMD5Hash(filePath) + ' ' + filePath + '\n')

outputDir = os.path.dirname(sys.argv[2])

if not os.path.isdir(sys.argv[1]):
    raise Exception('First argument must be a directory path!')
if not os.path.exists(outputDir):
    raise Exception('Output folder doesn''t exists!')
if os.path.exists(sys.argv[2]):
    raise Exception('Output file already exists!')

with open(sys.argv[2], 'w') as outputFile:
    walkDirectoryGeneratingHashes(sys.argv[1], outputFile)

