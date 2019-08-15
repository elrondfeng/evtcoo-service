# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 07:46:31 2019

@author: XDong
"""
import sys
sys.path.append("C:/Users/XDong/OneDrive - Duke Energy/Documents/Projects/EV charging-florida/production")

import warnings
warnings.filterwarnings("ignore")

import eFleet_opt as eFo

#test main wrapper
total_cost_base,cost_summer,schedule_summer,cost_winter,schedule_winter,dollar_mile=eFo.opt_main_wrapper(filepath='C:/Users/XDong/OneDrive - Duke Energy/Documents/Projects/EV charging-florida/UPS Orlando 15 minute interval data.xlsx',
                                                                                                         On_peak_rate=0.11148,
                                                                                                         Off_peak_rate=0.04846,
                                                                                                         Base_demand_rate=6.15,
                                                                                                         Peak_demand_rate=4.49,
                                                                                                         NumOfEVs=10, #number of blocks (each block contains 5 evs)
                                                                                                         Duration=14, #hrs (6pm to 8am)
                                                                                                         ChargingTime=5, #hrs for charging a ev
                                                                                                         ConPerEV=75, #powerrate per block
                                                                                                         RemainPct=0.25, #remaining percentage of battery life before charging
                                                                                                         timeout=30# timeout(seconds) for optimization for summer/winter(seconds)
                                                                                                         )

print(f'''Total base cost: {total_cost_base}
Extra cost summer:{cost_summer}
schedule summer(start time): {schedule_summer}
Extra cost winter:{cost_winter}
schedule winter(start time): {schedule_winter}
dollar per mile:{dollar_mile}''')