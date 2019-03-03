import pandas as pd
import random
import datetime

def generateDate(original_date):
    x = original_date.split(" ")
    alternative_date = ["11/12/2018", "11/13/2018"]
    return random.choice(alternative_date) + " " + x[1] + x[2]

def convertTimeTo24(t):
    if t[-2:] == "PM":
        if t[:2] == "12":
            return "12" + ':' + t.split(':')[1][:2]
        else:
            return str(int(t.split(':')[0]) + 12) + ':' + t.split(':')[1][:2]
    else:
        return t[:-2]

def convertEpochTime(t):
    x = t.split(' ')
    month = x[0].split('/')[0]
    date = x[0].split('/')[1]
    year = x[0].split('/')[2]
    rtime = convertTimeTo24(x[1])
    return datetime.datetime(int(year),int(month),int(date),int(rtime.split(':')[0]),int(rtime.split(':')[1])).strftime('%s')

def findFirstHole(time, holedict):
    minpothole = 0
    potflag = 1000000000
    for key, value in holedict.iteritems():
        # print (time - value[0]) / 3600.0
        if ((time - value[0]) / 3600.0 + value[2]) * value[1] < potflag:
            minpothole = key
            potflag = ((time - value[0]) / 3600.0 + value[2]) * value[1]
    return minpothole


        # data['Created'] = data.apply(lambda x: generateDate(x.Created), axis=1)


def DynamicScheduling ():
    data = pd.read_csv('regulatedData.csv')
    data['Created'] = data.apply(lambda x: convertEpochTime(x.Created), axis=1)

    ctrList = []
    waitingList = {}  # {ctr: [time, count, units]}

    for index, row in data.iterrows():
        if row['Ctr'] in ctrList:
            waitingList[str(row['Ctr'])][1] += 1
            if int(row['Created']) < waitingList[str(row['Ctr'])][0]:
                waitingList[str(row['Ctr'])][0] = int(row['Created'])
        else:
            ctrList.append(row['Ctr'])
            waitingList[str(row['Ctr'])] = [int(row['Created']), 1, row['Units']]

    Time = 1542137980
    waitingListCopy = waitingList
    firsthole = str(findFirstHole(Time, waitingListCopy))
    holeSchedule = []
    while len(waitingListCopy) != 0:
        holeSchedule.append({firsthole: waitingList[firsthole]})
        del waitingListCopy[firsthole]
        firsthole = str(findFirstHole(Time, waitingListCopy))

    return holeSchedule