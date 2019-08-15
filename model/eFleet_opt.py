# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:40:04 2019

@author: XDong
"""

import pandas as pd
import numpy as np
import datetime
import math

from func_timeout import func_timeout,FunctionTimedOut
from scipy import optimize
from datetime import datetime,timedelta
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt



############################## Objective Function ######################################################

#Summer
def func_summer(z):
    z=[int(x) for x in z]    
    m=np.zeros([numOfEVs,duration])
    for i in range(numOfEVs):
        m[i][z[i]:z[i]+chargingTime-1]=1
        m[i][z[i]+chargingTime-1]=pctLast1hr
    c=np.sum(m,axis=0)*conPerEV
    
    s=sorted(z)

    charging_time_range=[x if x<24 else x-24 for x in list(range(18,18+duration)) ]

    data_1yr_t=data_1yr[data_1yr.Summer_Winter_flag=='Summer']
    data_1yr_t['new demand']=data_1yr_t['billing demand']
    data_1yr_t['new kWh.2']=data_1yr_t['kWh.2']

    for i in range(duration):
        #update new demand for each hour
        data_1yr_t['new demand'] = np.where((
                    (data_1yr_t['Measure_hour']==charging_time_range[i])
                    & (data_1yr_t['Measure_weekday'] !=6)
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-01-01') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-05-28') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-09-03') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-11-22') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-12-25') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2019-01-01') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2019-05-27')), 
            data_1yr_t['new demand']+c[i],  data_1yr_t['new demand'])
        #update consumption
        data_1yr_t['new kWh.2'] = np.where((
                    (data_1yr_t['Measure_hour']==charging_time_range[i])
                    & (data_1yr_t['Measure_weekday'] !=6)
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-01-01') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-05-28') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-09-03') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-11-22') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-12-25') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2019-01-01') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2019-05-27')), 
            data_1yr_t['new kWh.2']+c[i]/4,  data_1yr_t['new kWh.2'])

    data_1yr_t['extra kWh']=data_1yr_t['new kWh.2']-data_1yr_t['kWh.2']
    extra_total=sum(data_1yr_t['extra kWh'])

    #(1155075-1151250)/15/5

    #peak demand
    data_1yr_t_peak=data_1yr_t.loc[data_1yr_t['peak_flag']==1]
    data_1yr_t_peak_demand=data_1yr_t_peak.loc[data_1yr_t_peak.groupby('Measure_month')['new demand'].idxmax()]
    
    
    total_peak_demand_t=sum(data_1yr_t_peak_demand['new demand'])

    #base demand
    data_1yr_t_base=data_1yr_t.loc[data_1yr_t.groupby('Measure_month')['new demand'].idxmax()]
    total_base_demand_t=sum(data_1yr_t_base['new demand'])

    extra_on_peak_t=round(sum(data_1yr_t_peak['new kWh.2'])-total_on_peak_summer)
    extra_off_peak_t=extra_total-extra_on_peak_t

    extra_base_demand_t=total_base_demand_t-total_base_demand_summer
    extra_peak_demand_t=total_peak_demand_t-total_peak_demand_summer
    total_extra_t=extra_base_demand_t*base_demand_rate+extra_peak_demand_t*peak_demand_rate+extra_on_peak_t*on_peak_rate+extra_off_peak_t*off_peak_rate
    global fzmin_summer
    global zmin_summer
    if total_extra_t<fzmin_summer:
        fzmin_summer=total_extra_t
        zmin_summer=s
        #print(f"z:{sorted(z)},f(z):{total_extra_t},\n\t base_d:{total_base_demand_t},peak_d:{total_peak_demand_t},\n\t total_on_peak:{extra_on_peak_t+total_on_peak_summer}")
    return total_extra_t
    

#Winter
def func_winter(z):
    z=[int(x) for x in z]
    m=np.zeros([numOfEVs,duration])
    for i in range(numOfEVs):
        m[i][z[i]:z[i]+chargingTime-1]=1
        m[i][z[i]+chargingTime-1]=pctLast1hr
    c=np.sum(m,axis=0)*conPerEV
    s=sorted(z)

    charging_time_range=[x if x<24 else x-24 for x in list(range(18,18+duration)) ]

    data_1yr_t=data_1yr[data_1yr.Summer_Winter_flag=='Winter']
    data_1yr_t['new demand']=data_1yr_t['billing demand']
    data_1yr_t['new kWh.2']=data_1yr_t['kWh.2']

    for i in range(duration):
        #update new demand for each hour
        data_1yr_t['new demand'] = np.where((
                    (data_1yr_t['Measure_hour']==charging_time_range[i])
                    & (data_1yr_t['Measure_weekday'] !=6)
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-01-01') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-05-28') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-09-03') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-11-22') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-12-25') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2019-01-01') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2019-05-27')), 
            data_1yr_t['new demand']+c[i],  data_1yr_t['new demand'])
        #update consumption
        data_1yr_t['new kWh.2'] = np.where((
                    (data_1yr_t['Measure_hour']==charging_time_range[i])
                    & (data_1yr_t['Measure_weekday'] !=6)
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-01-01') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-05-28') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-09-03') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-11-22') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2018-12-25') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2019-01-01') 
                    & (data_1yr_t['Measure_date']+timedelta(days=1) !='2019-05-27')), 
            data_1yr_t['new kWh.2']+c[i]/4,  data_1yr_t['new kWh.2'])

    data_1yr_t['extra kWh']=data_1yr_t['new kWh.2']-data_1yr_t['kWh.2']
    extra_total=sum(data_1yr_t['extra kWh'])

    #(1155075-1151250)/15/5

    #peak demand
    data_1yr_t_peak=data_1yr_t.loc[data_1yr_t['peak_flag']==1]
    data_1yr_t_peak_demand=data_1yr_t_peak.loc[data_1yr_t_peak.groupby('Measure_month')['new demand'].idxmax()]

    total_peak_demand_t=sum(data_1yr_t_peak_demand['new demand'])

    #base demand
    data_1yr_t_base=data_1yr_t.loc[data_1yr_t.groupby('Measure_month')['new demand'].idxmax()]

    total_base_demand_t=sum(data_1yr_t_base['new demand'])

    extra_on_peak_t=round(sum(data_1yr_t_peak['new kWh.2'])-total_on_peak_winter)
    extra_off_peak_t=extra_total-extra_on_peak_t
    
    extra_base_demand_t=total_base_demand_t-total_base_demand_winter
    extra_peak_demand_t=total_peak_demand_t-total_peak_demand_winter
    total_extra_t=extra_base_demand_t*base_demand_rate+extra_peak_demand_t*peak_demand_rate+extra_on_peak_t*on_peak_rate+extra_off_peak_t*off_peak_rate
    global fzmin_winter
    global zmin_winter
    if total_extra_t<fzmin_winter:
        fzmin_winter=total_extra_t
        zmin_winter=s
        #print(f"z:{sorted(z)},\tf(z):{total_extra_t},\n\t base_d:{total_base_demand_t},peak_d:{total_peak_demand_t},\n\t total_on_peak:{extra_on_peak_t+total_on_peak_winter}")
    return total_extra_t



############################## Wrapper Function ######################################################

def opt_summer_wrapper(timeout=30):
    global fzmin_summer
    global zmin_summer
    fzmin_summer=9999999999
    zmin_summer=[]
    
    lw=[0]*numOfEVs
    up=[9]*numOfEVs
    x0=np.random.randint(low=0, high=9, size=numOfEVs)
        
    try:
        func_timeout(timeout,optimize.dual_annealing,
                           kwargs={'func':func_summer,'bounds':list(zip(lw,up)),'seed':123,'x0':x0})
        #optimize.dual_annealing(func, bounds=list(zip(lw, up)), seed=123,x0=x0,maxiter=10000)
    except FunctionTimedOut:
       print(f"\nAfter {timeout} seconds of search,\nThe min cost is ${fzmin_summer} when z= {zmin_summer}")
    except Exception as e:
        print(f"other exception!{e}")
    
    return fzmin_summer,zmin_summer
        

def opt_winter_wrapper(timeout=30):
    global fzmin_winter
    global zmin_winter
    fzmin_winter=9999999999
    zmin_winter=[]
    
    lw=[0]*numOfEVs
    up=[9]*numOfEVs
    x0=np.random.randint(low=0, high=9, size=numOfEVs)
        
    try:
        func_timeout(timeout,optimize.dual_annealing,
                           kwargs={'func':func_winter,'bounds':list(zip(lw,up)),'seed':123,'x0':x0})
        #optimize.dual_annealing(func, bounds=list(zip(lw, up)), seed=123,x0=x0,maxiter=10000)
    except FunctionTimedOut:
        print(f"\nAfter {timeout} seconds of search,\nThe min cost is ${fzmin_winter} when z= {zmin_winter}")
    except Exception as e:
        print(f"other exception!{e}")
    
    return fzmin_winter,zmin_winter
        

#combine summer and winter wrapper

def opt_main_wrapper(filepath='C:/Users/XDong/OneDrive - Duke Energy/Documents/Projects/EV charging-florida/UPS Orlando 15 minute interval data.xlsx',
                     On_peak_rate=0.11148,
                     Off_peak_rate=0.04846,
                     Base_demand_rate=6.15,
                     Peak_demand_rate=4.49,
                     NumOfEVs=10, #number of blocks (each block contains 5 evs)
                     Duration=14, #hrs (6pm to 8am)
                     ChargingTime=5, #hrs for charging a ev
                     ConPerEV=150, #powerrate per block
                     RemainPct=0.25,
                     timeout=20#3*3600 #seconds
                     ):
    global on_peak_rate
    global off_peak_rate
    global base_demand_rate
    global peak_demand_rate
    
    on_peak_rate=On_peak_rate
    off_peak_rate=Off_peak_rate
    base_demand_rate=Base_demand_rate
    peak_demand_rate=Peak_demand_rate
    
    global numOfEVs
    global duration
    global chargingTime
    global conPerEV
    global pctLast1hr
    
    numOfEVs=NumOfEVs
    duration=Duration
    chargingTime=math.ceil(ChargingTime*(1-RemainPct))
    conPerEV=ConPerEV
    pctLast1hr=ChargingTime*(1-RemainPct)-int(ChargingTime*(1-RemainPct))
    
    #data prepartation
    data=pd.read_excel(filepath,'Total',skiprows=2)
    
    data['Measure_date']=data['DATE'].apply(lambda x:datetime.strptime(str(x).zfill(6),'%m%d%y'))
    data['Measure_month']=data['Measure_date'].dt.month
    data['Measure_hour']=data['TIME'].apply(lambda x: math.floor(x/100)-1 if x%100==0 else math.floor(x/100))
    data['Measure_minute']=data['TIME'].apply(lambda x: 60 if x%100==0 else x%100)
    data['Measure_weekday']=data['Measure_date'].apply(lambda x:x.weekday()+1)
    data['Summer_Winter_flag']=data['Measure_date'].apply(lambda x: 'Summer' if (x.month>=4) & (x.month<=10) else 'Winter')
    
    #set peak_flag default value to 0
    data['peak_flag']=0
    
    #flag peak time for summer
    data.loc[(data['Summer_Winter_flag']=='Summer') & (data['Measure_hour']>=12) & (data['Measure_hour']<=20)
             & (data['Measure_weekday']>=1) & (data['Measure_weekday']<=5)
             ,'peak_flag']=1
    
    #flag peak time for winter
    data.loc[(data['Summer_Winter_flag']=='Winter') & 
             (((data['Measure_hour']>=6) & (data['Measure_hour']<=9)) | ((data['Measure_hour']>=18) & (data['Measure_hour']<=21)))
             & (data['Measure_weekday']>=1) & (data['Measure_weekday']<=5)
             ,'peak_flag']=1
    
    #flag off-peak time for holidays
    # Holidays: New Year's day, Memorial Day, Independence Day, Labor Day, Thanksgiving Day and Christmas.
    
    data.loc[(data['Measure_date'] == '2018-01-01') |
             (data['Measure_date'] == '2018-05-28') |
             (data['Measure_date'] == '2018-07-04') |
             (data['Measure_date'] == '2018-09-03') |
             (data['Measure_date'] == '2018-11-22') |
             (data['Measure_date'] == '2018-12-25') |
             (data['Measure_date'] == '2019-01-01')      
             ,'peak_flag']=0
    
    global data_1yr
    data_1yr=data[(data['Measure_date']>='2018-04-01') & (data['Measure_date']<='2019-03-31')]
    
    #find peak demand per month
    peak_demand_1=data_1yr.loc[data_1yr['peak_flag']==1]
    
    peak_demand=peak_demand_1.loc[peak_demand_1.groupby('Measure_month')['billing demand'].idxmax()]
    total_peak_demand=sum(peak_demand['billing demand'])
    
    global total_peak_demand_summer
    total_peak_demand_summer=sum(peak_demand[peak_demand.Summer_Winter_flag=='Summer']['billing demand'])
    global total_peak_demand_winter
    total_peak_demand_winter=sum(peak_demand[peak_demand.Summer_Winter_flag=='Winter']['billing demand'])
    
    #find base demand per month
    base_demand=data_1yr.loc[data_1yr.groupby('Measure_month')['billing demand'].idxmax()]
    total_base_demand=sum(base_demand['billing demand'])
    
    #Winter
    global total_base_demand_winter
    total_base_demand_winter=sum(base_demand[base_demand.Summer_Winter_flag=='Winter']['billing demand'])
    
    #Summer
    global total_base_demand_summer
    total_base_demand_summer=sum(base_demand[base_demand.Summer_Winter_flag=='Summer']['billing demand'])
    
    #total on peak
    total_on_peak=sum(peak_demand_1['kWh.2']) 
    global total_on_peak_summer
    total_on_peak_summer=sum(peak_demand_1[peak_demand_1.Summer_Winter_flag=='Summer']['kWh.2']) 
    global total_on_peak_winter
    total_on_peak_winter=sum(peak_demand_1[peak_demand_1.Summer_Winter_flag=='Winter']['kWh.2']) 
    
    #total off peak
    total_off_peak=sum(data_1yr['kWh.2'])-total_on_peak
    
    #calculate total price
    total_price=total_on_peak*on_peak_rate+total_off_peak*off_peak_rate+total_base_demand*base_demand_rate+total_peak_demand*peak_demand_rate
    
    cost_summer,schedule_summer=opt_summer_wrapper(timeout=timeout)

    cost_winter,schedule_winter=opt_winter_wrapper(timeout=timeout)
    
    
    
    dollar_mile=((cost_summer+cost_winter)*1.165)/(NumOfEVs*ConPerEV*ChargingTime*(1-RemainPct)*308)
    
    summer_schedule=[str(x+6)+'PM' if x+6<12 else str(x-6)+'AM'  for x in schedule_summer]
    winter_schedule=[str(x+6)+'PM' if x+6<12 else str(x-6)+'AM'  for x in schedule_winter]
    
    return total_price,cost_summer,summer_schedule,cost_winter,winter_schedule,dollar_mile

