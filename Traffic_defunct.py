import requests
import schedule
import time

# API result manipulation
def mod_traffic(raw_data):
    simple_raw = raw_data.replace('>','<')
    mod_raw = simple_raw.split('<')
    return mod_raw

# Current speed
def current_speed(raw_data):
    mod_raw = mod_traffic(raw_data)
    speedLoc = mod_raw.index('currentSpeed')
    return float(mod_raw[speedLoc+1])

# Free flow speed
def free_speed(raw_data):
    mod_raw = mod_traffic(raw_data)
    speedLoc = mod_raw.index('freeFlowSpeed')
    return float(mod_raw[speedLoc+1])

# Current travel time
def current_travel_time(raw_data):
    mod_raw = mod_traffic(raw_data)
    timeLoc = mod_raw.index('currentTravelTime')
    return float(mod_raw[timeLoc+1])

# Free flow travel time
def free_travel_time(raw_data):
    mod_raw = mod_traffic(raw_data)
    timeLoc = mod_raw.index('freeFlowTravelTime')
    return float(mod_raw[timeLoc+1])

# Stadium Ave (Coordinate pin between Cary and Armstrong)
def stdm1():
    stdm1_traffic_response = requests.get("https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/xml?key=oitAkMc7xSmlfKN0csJC0lzE2T7GbR7M&point=40.431349,-86.916151")
    stdm1_traffic_contents = str(stdm1_traffic_response.content)
    return stdm1_traffic_contents

def get_stdm1_CS():
    stdm1_traffic_contents = stdm1()
    stdm1_current_speed = current_speed(stdm1_traffic_contents)
    return stdm1_current_speed
    stdm1_free_speed = free_speed(stdm1_traffic_contents)
    stdm1_currentTT = current_travel_time(stdm1_traffic_contents)
    stdm1_freeTT = free_travel_time(stdm1_traffic_contents)
    stdm1_ratio = stdm1_current_speed / stdm1_free_speed

def get_stdm1_FS():
    stdm1_traffic_contents = stdm1()
    stdm1_free_speed = free_speed(stdm1_traffic_contents)
    return stdm1_free_speed

# Stadium 2 (Coordinate pin at Owen covering Martin Jischke)
def stdm2():
    stdm2_traffic_response = requests.get("https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/xml?key=oitAkMc7xSmlfKN0csJC0lzE2T7GbR7M&point=40.431461,-86.921018")
    stdm2_traffic_contents = str(stdm2_traffic_response.content)
    return stdm2_traffic_contents

def get_stdm2_CS():
    stdm2_traffic_contents = stdm2()
    stdm2_current_speed = current_speed(stdm2_traffic_contents)
    return stdm2_current_speed

def get_stdm2_FS():
    stdm2_traffic_contents = stdm2()
    stdm2_free_speed = free_speed(stdm2_traffic_contents)
    return stdm2_free_speed

def nw():
    nw_traffic_response = requests.get("https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/xml?key=oitAkMc7xSmlfKN0csJC0lzE2T7GbR7M&point=40.428597,-86.910962")
    nw_traffic_contents = str(nw_traffic_response.content)
    return nw_traffic_contents

def get_nw_CS():
    nw_traffic_contents = nw();
    nw_current_speed = current_speed(nw_traffic_contents)
    return nw_current_speed

def get_nw_FS():
    nw_traffic_contents = nw();
    nw_free_speed = free_speed(nw_traffic_contents)
    return nw_free_speed

def state1():
    state1_traffic_response = requests.get("https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/xml?key=oitAkMc7xSmlfKN0csJC0lzE2T7GbR7M&point=40.424017,-86.911131")
    state1_traffic_contents = str(state1_traffic_response.content)
    return state1_traffic_contents

def get_state1_CS():
    state1_traffic_contents = state1();
    state1_current_speed = current_speed(state1_traffic_contents)
    return state1_current_speed

def get_state1_FS():
    state2_traffic_contents = state();
    state2_free_speed = free_speed(state2_traffic_contents)
    return state2_free_speed

def state2():
    state2_TR = requests.get("https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/xml?key=oitAkMc7xSmlfKN0csJC0lzE2T7GbR7M&point=40.424217,-86.918719")
    state2_TC = str(state2_TR)
    return state2_TC

def get_state2_CS():
    TC = state2()
    CS = current_speed(TC)
    return CS

def get_state2_FS():
    TC = state2()
    FS = free_speed(TC)
    return FS

def state3():
    state3_TR = requests.get("https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/xml?key=oitAkMc7xSmlfKN0csJC0lzE2T7GbR7M&point=40.424264,-86.921786")
    state3_TC = str(state3_TR)
    return state3_TC

def get_state3_CS():
    TC = state3()
    CS = current_speed(TC)
    return CS

def get_state3_FS():
    TC = state3()
    FS = free_speed(TC)
    return FS

def stdm1_ratio():
    CS = get_stdm1_CS
    FS = get_stdm1_FS
    ratio = CS / FS
    return ratio

def stdm2_ratio():
    CS = get_stdm2_CS
    FS = get_stdm2_FS
    ratio = CS / FS
    return ratio

def nw_ratio():
    CS = get_nw_CS
    FS = get_nw_FS
    ratio = CS / FS
    return ratio

def state1_ratio():
    CS = get_state1_CS
    FS = get_state1_FS
    ratio = CS / FS
    return ratio

def state2_ratio():
    CS = get_state2_CS
    FS = get_state2_FS
    ratio = CS / FS
    return ratio

def state3_ratio():
    CS = get_state3_CS
    FS = get_state3_FS
    ratio = CS / FS
    return ratio

#stdm2_currentTT = current_travel_time(stdm2_traffic_contents)
stdm2_freeTT = free_travel_time(stdm2_traffic_contents)
stdm2_ratio = stdm2_current_speed / stdm2_free_speed

# Northwestern Ave (Coordinate pin at ECE Bldg)
nw_currentTT = current_travel_time(nw_traffic_contents)
nw_freeTT = free_travel_time(nw_traffic_contents)
nw_ratio = nw_current_speed / nw_free_speed

# State St 1(Coordinate pin at Krannert/Grant St)
state1_current_speed = current_speed(state1_traffic_contents)
state1_free_speed = free_speed(state1_traffic_contents)
state1_currentTT = current_travel_time(state1_traffic_contents)
state1_freeTT = free_travel_time(state1_traffic_contents)
state1_ratio = state1_current_speed / state1_free_speed

#State St 2(Coordinate pin at Lilly covering Russell and University)
state2_traffic_response = requests.get("https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/xml?key=oitAkMc7xSmlfKN0csJC0lzE2T7GbR7M&point=40.424217,-86.918719")
state2_traffic_contents = str(state2_traffic_response.content)
state2_current_speed = current_speed(state2_traffic_contents)
state2_free_speed = free_speed(state2_traffic_contents)
state2_currentTT = current_travel_time(state2_traffic_contents)
state2_freeTT = free_travel_time(state2_traffic_contents)
state2_ratio = state2_current_speed / state2_free_speed

#State St 3(Coordinate pin at FST covering Martin Jischke)
state3_traffic_response = requests.get("https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/xml?key=oitAkMc7xSmlfKN0csJC0lzE2T7GbR7M&point=40.424264,-86.921786")
state3_traffic_contents = str(state3_traffic_response.content)
state3_current_speed = current_speed(state3_traffic_contents)
state3_free_speed = free_speed(state3_traffic_contents)
state3_currentTT = current_travel_time(state3_traffic_contents)
state3_freeTT = free_travel_time(state3_traffic_contents)
state3_ratio = state3_current_speed / state3_free_speed

# Demo Day Simulation - Traffic on Stadium
#stdm1_ratio = 0.5
#stdm2_ratio - 0.8
#stdm3_ratio = 0.6

# Demo Day Simulation - Traffic on State
#state1_ratio = 0.5
#state2_ratio = 0.8
#state3_ratio = 0.7

# Detour Function. Returns true if all state ratios are greater than stdm ratios
def detour_call(stdm1_ratio, stdm2_ratio, nw_ratio, state1_ratio, state2_ratio, state3_ratio):
    status = False
    if state1_ratio > nw_ratio and state2_ratio > stdm1_ratio and state3_ratio > stdm2_ratio:
        status = True

    return status

def run_traffic(stdm1_ratio, stdm2_ratio, nw_ratio, state1_ratio, state2_ratio, state3_ratio):
    if detour_call(stdm1_ratio, stdm2_ratio, nw_ratio, state1_ratio, state2_ratio, state3_ratio):
        print("State is faster")
    else:
        print("Stdm is faster")

schedule.every(5).minutes.do(run_traffic,stdm1_ratio, stdm2_ratio, nw_ratio, state1_ratio, state2_ratio, state3_ratio)

while True:
    schedule.run_pending()
    time.sleep(1)
    