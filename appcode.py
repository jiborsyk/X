import csv
import json
import os.path
import urllib.request
import urllib.parse






def GetData(url):
    response = urllib.request.urlopen(url)
    content = json.loads(response.read().decode())
    data = []
    for i in content['data']:
        m = []
        m.append(i[10])
        m.append(i[11])
        m.append(i[13])
        m.append(i[15])
        m.append(i[18])
        m.append(i[8])
        data.append(m)
    return data



def WriteDataToCSVFile(filename, data):
    with open(filename, 'w') as file:
        csvWriter = csv.writer(file)
        for row in data:
            csvWriter.writerow(row)

def ReadDataFromCSVFile(filename):
    data = []
    with open(filename, newline='') as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            data.append(row)
    return data

WriteDataToCSVFile('NYAnimalEndangerment.csv',GetData('https://data.ny.gov/api/views/tk82-7km5/rows.json?accessType=DOWNLOAD'))


#Input: N/A , output: dictionary of dictionaries, {animal:{g3:23,g4:25...}...}

def sortByAnimal():
    rawData = ReadDataFromCSVFile("NYAnimalEndangerment.csv")
    output = {}
    for row in rawData:
        if row[0] in output:
            if 'GH' in row[4] or 'G1' in row[4]:
                output[row[0]]['Near Extinction']  += 1
            elif 'G2' in row[4]:
                output[row[0]]['Critically Endangered']  += 1
            elif 'G3' in row[4]:
                output[row[0]]['Vulnerable'] += 1
            else:
                output[row[0]]['Stable'] +=1

        if row[0] not in output:
            status = {}
            status['Near Extinction']  = 0
            status['Critically Endangered']  = 0
            status['Vulnerable']  = 0
            status['Stable'] = 0
            if 'GH' in row[4] or 'G1' in row[4]:
                status['Near Extinction']  = 1
            elif 'G2' in row[4]:
                status['Critically Endangered']  = 1
            elif 'G3' in row[4]:
                status['Vulnerable'] = 1
            else:
                status['Stable'] = 1

            output[row[0]] = status

    return output

def specieslocation():
    massdata = ReadDataFromCSVFile("NYAnimalEndangerment.csv")
    coordata = ReadDataFromCSVFile('coordinates.csv')
    output = {}
    for row in massdata:
        if row[5] in output:
            if 'GH' in row[4] or 'G1' in row[4]:
                output[row[5]]['Near Extinction']  += 1
            elif 'G2' in row[4]:
                output[row[5]]['Critically Endangered']  += 1
            elif 'G3' in row[4]:
                output[row[5]]['Vulnerable'] += 1

        if row[5] not in output:
            status = {}
            status['Near Extinction']  = 0
            status['Critically Endangered']  = 0
            status['Vulnerable']  = 0
            if 'GH' in row[4] or 'G1' in row[4]:
                status['Near Extinction']  = 1
            elif 'G2' in row[4]:
                status['Critically Endangered']  = 1
            elif 'G3' in row[4]:
                status['Vulnerable'] = 1

            output[row[5]] = status

    for county in coordata:
        output[county[0]]['lon'] = str(float(county[2])*-1)
        output[county[0]]['lat'] = county[1]

    return output

def addsearch(search):
    with open('search.txt','w') as file:
        file.write('success!')
    # massdata = ReadDataFromCSVFile("NYAnimalEndangerment.csv")
    # output = []
    # for row in massdata:
    #     if search == row[5]:
    #         output.append('success!')
    # with open('search.txt','w') as file:
    #     for line in output:
    #         file.write('successs!')


def get_search():
    fullsearch = []
    with open('search.txt') as file:
        for line in file:
            fullsearch.append(line)
    return fullsearch
