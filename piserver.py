# Python Web Server Library
from flask import Flask, render_template
from point import Point

# Neurosky EEG Brainwave Library
import bluetooth
from mindwavemobile.MindwaveDataPoints import EEGPowersDataPoint
from mindwavemobile.MindwaveDataPointReader import MindwaveDataPointReader

import os
import psutil
import threading
import queue
import time
import random
import json

# EEG Raw Powers
deltaQ = queue.Queue()
thetaQ = queue.Queue()
lowalphaQ = queue.Queue()
highalphaQ = queue.Queue()
lowbetaQ = queue.Queue()
highbetaQ = queue.Queue()
lowgammaQ = queue.Queue()
midgammaQ = queue.Queue()

# EEG Interpreted Data
meditation = queue.Queue()
attention = queue.Queue()
signal = queue.Queue()

def simulate_eeg(delay):
    pos = 0
    while True:
        time.sleep(delay)
        
        deltaQ.put(Point(pos,random.randint(500,1000)))
        thetaQ.put(Point(pos,random.randint(500,1000)))
        lowalphaQ.put(Point(pos,random.randint(500,1000)))
        highalphaQ.put(Point(pos,random.randint(500,1000)))
        lowbetaQ.put(Point(pos,random.randint(500,1000)))
        highbetaQ.put(Point(pos,random.randint(500,1000)))
        lowgammaQ.put(Point(pos,random.randint(500,1000)))
        midgammaQ.put(Point(pos,random.randint(500,1000)))

        meditation.put(random.randint(10,100)) # simulate meditation
        attention.put(random.randint(10,100)) # simulate attention
        signal.put(random.randint(10,100)) # simulate signal strength
        
        pos += 1

def capture_eeg():
    if __name__ == '__main__':
        mindwaveDataPointReader = MindwaveDataPointReader()
        mindwaveDataPointReader.start()
        if (mindwaveDataPointReader.isConnected()):    
            pos = 0
            while(True):
                dataPoint = mindwaveDataPointReader.readNextDataPoint()
                if (dataPoint.__class__ is EEGPowersDataPoint):
                    # print(dataPoint)
                    deltaQ.put(Point(pos,getattr(dataPoint,'delta')))
                    thetaQ.put(Point(pos,getattr(dataPoint,'theta')))
                    lowalphaQ.put(Point(pos,getattr(dataPoint,'lowAlpha')))
                    highalphaQ.put(Point(pos,getattr(dataPoint,'highAlpha')))
                    lowbetaQ.put(Point(pos,getattr(dataPoint,'lowBeta')))
                    highbetaQ.put(Point(pos,getattr(dataPoint,'highBeta')))
                    lowgammaQ.put(Point(pos,getattr(dataPoint,'lowGamma')))
                    midgammaQ.put(Point(pos,getattr(dataPoint,'midGamma')))
                    pos += 1
        else:
            print("EEG Equipment not Found")

def get_eeg_data(queuedData, maxSize):

    if queuedData.empty():
        sample = "No data yet"
    else:
        sample = [] 
        run = True
        while (queuedData.empty() == False and run == True):
            piece = queuedData.get()
            sample.append(piece.getDict())
            if (len(sample) >= maxSize):
                run = False
    return sample
    
def queue_average(queuedData, sampleSize):
    sum = 0
    size = 1
    while (size <= sampleSize and queuedData.empty() == False):
        sum += queuedData.get()
        size += 1
    queuedData.queue.clear()
    return round(sum/size,2)

def thread_worker():
    simulate_eeg(0.005)
    #capture_eeg()    

# Turn-on the worker thread.
threading.Thread(target=thread_worker, daemon=True).start()

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    PROPAGATE_EXCEPTIONS=True

)

# Web Application Pages

@app.route("/")
def render_homepage():
    return "<p>Hello, World!</p>"
      
@app.route('/testonly')
def render_testpage():
    return render_template('testonly.html')
    
@app.route('/dashboard')
def render_dashboard():
    return render_template('dashboard.html')
    
# EEG Raw Data Endpoints    
    
@app.route('/eeg/raw_delta', methods=['GET'])
def get_raw_delta():
    return get_eeg_data(deltaQ, 50)
    
@app.route('/eeg/raw_theta', methods=['GET'])
def get_raw_theta():
    return get_eeg_data(thetaQ, 50)
    
@app.route('/eeg/raw_lowalpha', methods=['GET'])
def get_raw_lowalpha():
    return get_eeg_data(lowalphaQ, 50)
    
@app.route('/eeg/raw_highalpha', methods=['GET'])
def get_raw_highalpha():
    return get_eeg_data(highalphaQ, 50)
    
@app.route('/eeg/raw_lowbeta', methods=['GET'])
def get_raw_lowbeta():
    return get_eeg_data(lowbetaQ, 50)
        
@app.route('/eeg/raw_highbeta', methods=['GET'])
def get_raw_highbeta():
    return get_eeg_data(highbetaQ, 50)

@app.route('/eeg/raw_lowgamma', methods=['GET'])
def get_raw_lowgamma():
    return get_eeg_data(lowgammaQ, 50)

@app.route('/eeg/raw_midgamma', methods=['GET'])
def get_raw_midgamma():
    return get_eeg_data(midgammaQ, 50)
    
# EEG Interpretations
    
@app.route('/eeg/meditation')
def get_meditation():
    return str(queue_average(meditation,10))

@app.route('/eeg/attention')
def get_attention():
    return str(queue_average(attention,10))

@app.route('/eeg/signal')
def get_signal():
    return str(queue_average(signal,10))

# SOC Information Endpoints    
    
@app.route('/soc/cpu_usage')
def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(3)
    return str(cpu_usage)
    
@app.route('/soc/cpu_load')
def get_cpu_load():
    # Getting loadover15 minutes
    load1, load5, load15 = psutil.getloadavg()
    cpu_load = round((load15/os.cpu_count()) * 100,1)
    return str(cpu_load)
    
@app.route('/soc/ram_usage')
def get_ram_usage():
    ram_usage = psutil.virtual_memory()[2]
    return str(ram_usage)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
