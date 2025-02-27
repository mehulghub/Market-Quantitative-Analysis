#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np
from scipy.stats import norm 
import datetime as dt


# In[32]:


get_ipython().system(' pip install yfinance')


# In[33]:


import yfinance as yf


# In[34]:


#Calculating Historical Volatility for last one year on daily returns
def vol_cal(df):
    TRADING_DAYS= 252
    returns= np.log(df["Close"]/df["Close"].shift(1))    
    returns.fillna(0, inplace=True)
    vol= returns.std()*np.sqrt(TRADING_DAYS) #annualizing the standard deviation by multiplying with square root of 252
    return vol


# In[35]:


# 1.Cost of Carry Model


# In[36]:


def cost_to_carry(St, r, d, T):
    
    #Ft: Futures price
    #St: Spot price
    #r: Risk-free rate
    #d: Storage cost
    #T: Time to maturity (0.5 years for six months)
     
    Ft= St*np.exp((r+d)*T)    
    
    return Ft


# In[37]:


# 2.Black Scholes Model


# In[38]:


def black_scholes(St, X, r, T, vol):
    
    # c= call option price
    # St= spot price 
    # X= strike price
    # rt= risk-free rate
    # T= Time to Maturity
    # v= volatility
    
    #calculating d1 and d2
    d1= (np.log(St/X) + (r+ 0.5*vol**2)*T)/(vol*T**0.5)
    d2= d1- vol*(T**0.5)
    
    #Calculating the Call Option Price using Black Scholes Model
    c= St*norm.cdf(d1) - X*np.exp(-r*T)*norm.cdf(d2)
    
    return c


# In[39]:


#3. Monte Carlo Simulation


# In[40]:


def monte_carlo_sim(St, T, vol):
    
    num_simulations= 10000 #Number of Simulations
    days= 252 #Considering 252 Trading days
    t= T/days
    
    #Simulating Path Prices
    np.random.seed(42) #Reproducibility of Random numbers
    prices_path= np.zeros((days, num_simulations))
    prices_path[0]= St
    for i in range(1, days):
        z= np.random.standard_normal(num_simulations)
        prices_path[i]= prices_path[i-1]*np.exp((r- 0.5*vol**2)*t + vol* np.sqrt(t)*z)
        
    # Calculating the average simulated price at maturity
    average_simulated_price = np.mean(prices_path[-1])
    
    return average_simulated_price


# In[41]:


if __name__== "__main__":
    
    St= 425.10 # Bloomberg website states coffee commodity spot price= 425.10 USd/lb 
    r= 0.0419 # US Department of Treasury website states Daily Treasury Bill rate for 6 months= 4.19 on 10/02/2025(dd/mm/yyyy)
    d= 0.01 # assumption
    T= 0.5 # 6 months
    X= 426.10 #A little higher than Strike Price
    
    #Downloading Coffee dataset and calculating volatility
    df= yf.download("KC=F", dt.datetime(2024, 2, 10), dt.datetime(2025, 2, 10))
    vol= vol_cal(df)
    vol= vol.iloc[0] #Because vol is an array of length one but we need that value
    
    #1. Cost of Carry Model
    Ft=cost_to_carry(St, r, d, T)
    print(f"The fair price of Futures Contract of Coffee in {T*12} months is {Ft: .3f} Cents per Pound")
    
    # 2.Black Scholes Model
    c= black_scholes(St, X, r, T, vol)
    print(f"The Call Option Price using Black Scholes is USd {c:.3f} per Pound.") 
    
    #3. Monte Carlo Simulation
    average_simulated_price= monte_carlo_sim(St, T, vol)
    print(f"The average simulated price of the coffee futures contract at 6 months maturity is USd {average_simulated_price:.3f} per Pound.")


# In[ ]:





# In[ ]:





# In[ ]:




