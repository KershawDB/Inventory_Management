# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:42:21 2021

@author: kaise
"""
import matplotlib.pyplot as plt

def naive_model(horizon,order_quantity,initial_stock,demand_rate):
    # Very naive model assuming no lead time, constant demand

    time_data = []
    inventory_data = []
    stock = 0
    for i in range(horizon+1):
        if i == 0:
            stock += initial_stock
            time_data.append(i)
            inventory_data.append(stock)
            if stock < demand_rate:    
                stock += order_quantity
                time_data.append(i)
                inventory_data.append(stock)                   
        else:
            stock -= demand_rate    # demand period is one day, giving units of 'units'
            time_data.append(i)
            inventory_data.append(stock)
            if stock < demand_rate:    
                stock += order_quantity
                time_data.append(i)
                inventory_data.append(stock)
            
    plt.plot(time_data,inventory_data)
    plt.show()
    
naive_model(30, 10, 20, 10)