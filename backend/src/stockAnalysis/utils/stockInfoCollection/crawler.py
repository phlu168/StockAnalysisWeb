from datetime import datetime
from iexfinance import *
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from pymongo import MongoClient
portNum = 27017
DBName = "stockHistoryPrice"


class stockInfo:
    def __init__(self, name="default", id=0):
        self.name = name.lower()
        self.id = id
        
        
    def connectMongo(self):
        #db = MongoClient(port=portNum)[DBName]  
        try:
            db = MongoClient(port=portNum)[DBName]
            print("successful connect to db: ",db)
        except:
            print("cur port", portNum,"cur Database", DBName)
        try:
            collection = db[self.name]
            #print("company name is ", collection)
            return collection
        except:
            print(self.name)
            print("no company data")
        

    def lastest(self):
        collection = self.connectMongo()
        #print(collection)
        #print(collection.find().sort("date",-1).limit(1))
        cur = collection.find().sort("date",-1).limit(1)
        print(datetime.now().strftime("%Y/%m/%d"))
        self.curDate = datetime.now().strftime("%Y/%m/%d")
        for doc in cur:
            self.lastestDate = doc["date"]
            print(self.lastestDate)
    

    def update(self):

        collection = self.connectMongo()
        self.lastest()
        print("company name is ", collection)
        self.getFromIEX(self.lastestDate, self.curDate)
        #print("update:", self.data)
        self.data = self.data[1:]
        print(self.data)
        updateData = self.data.to_dict(orient='records')
        try:
            collection.insert_many(updateData)
        except:
            print("lastest date!")


        
        
    # put lastest data into mysql

    #def date( year, month, day):
        

    def date(self, year, month, day):
        return datetime(year, month, day)

    def getInfo(self):
        pass
        # get data to mySQL
        

    def getFromIEX(self, start, end):
        self.start = start
        self.end = end
        self.data = get_historical_data(self.name.upper(), self.start, self.end,  output_format='pandas')
        self.data.insert(0, "date", pd.to_datetime(self.data.index))
        #self.data["date"] = pd.to_datetime(self.data.index)
        #self.data.set_index('date', inplace = True)
        print(self.data.head())
        #visualize(self.data)
    
    def preprocess(self):
        self.data = self.data.reset_index()
    
    def addLabel(self):
        self.preprocess()
        rowNums = len(self.data.index)
        rangeToday = pd.RangeIndex(start=0, stop=rowNums-1, step=1)
        rangeNext = pd.RangeIndex(start=1, stop=rowNums, step=1)
        self.data["nextDay"] = 0
        self.data.loc[rangeToday,["nextDay"]] = self.data.loc[rangeNext,["close"]].values

        
        

def visualize(data, type = "line"):
    # add date from index
    #data["date"] = pd.to_datetime(data.index)
    
    fig, ax = plt.subplots(figsize=(15,7))
    # replace date
    #data.set_index('date', inplace = True)
    data.close.plot(ax=ax)

    ax.grid(True)
    # set x axis every month
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y %b'))
    


    
    
