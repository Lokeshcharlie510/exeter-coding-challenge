import csv, sys, time
import os
import psutil

def initialize_french_dictionary():
    with open('C:\Users\Home\Desktop') as csv_file:
reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            french_dict[row[0]] = [row[1],0]

def translate(input_file):
    print('Reading files.....')
    fp1 = open('C:\Users\Home\Desktop', 'w')
    check_list = french_dict.keys()
    with open(input_file, 'r') as input_text:
        while True:
            line = input_text.readline()
            if not line:
                break
            buffer = ''
            for word in line.split():
                filtered = filter(str.isalpha,word)
                query = "".join(filtered)
                if query in check_list:
                    querySuccess = french_dict[query][0]
                    french_dict[query][1] += 1
                    word = word.replace(query, querySuccess)
                buffer += word + ''
            buffer = buffer.strip()
            fp1.write(buffer + '\n')
    fp1.close()
    print(f'File {input_file} is translated from english to french')
    return True

def generateFrequencyCsv():
    print('Generating frequency file.....')
    with open('C:\Users\Home\Desktop', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['English', 'French', 'Frequency'])
        for words in french_dict:
            writer.writerow([words, french_dict[words][0], french_dict[words][1]])
    print('Done.')
    return True

def generatePerformance(process_time, memory_info):
    print('Generating performance.txt.....')
    with open('C:\Users\Home\Desktop', 'w') as file:
        file.write(f"Time to process : {process_time} seconds\n") 
        file.write(f"Memory used : {memory_info} MB")
    print('Done.')

if __name__ == '__main__':
    startTime = time.time()
    frenchDict = {}
ipFile = 'C:\Users\Home\Desktop'

    if len(sys.argv) == 2:
ipFile = sys.argv[1]

    initialize_french_dictionary()
    translate(ipFile)
    generateFrequency_csv()
completeTime = time.time()
    memUsed = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
totalTime = completeTime - startTime

    generatePerformance(totalTime, memoryUsed)
