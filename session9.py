#!/usr/bin/env python
# coding: utf-8

# In[17]:


from collections import namedtuple
from statistics import mode
from time import perf_counter
from faker import Faker
from datetime import datetime
fake = Faker()

def get_profiles():
    
    profile = namedtuple('profile',fake.profile().keys())
    '''Create Named Tuple by name profile 
        which takes in only the keys from the faker library'''
    
    allprofile = namedtuple('allprofile',['profile'])
    '''Create another named tuple which adds in the profile to it as input'''
    
    p1 = profile(**fake.profile())
    '''This step will generate the profile details from the faker library
   We can use this to keep adding other profiles'''

    allprofile_nt = allprofile(p1)
    '''This step is like setting up count = 0
        then you keep adding the required number of values to it
        example, we have been asked to get 10K profiles
        from the faker lib'''
    
    for _ in range(0,10000):
        p1 = profile(**fake.profile())
        allprofile_nt += allprofile(p1)
        
    return allprofile_nt


def largest_blood(allprofile_nt):
    
    '''This function will tell us the highest blood type in the profiles
    It does so by using mode function to give use the highest occuring blood type in data'''
    
    start = perf_counter()
    mode_blood = mode(list(map(lambda x:x[5],allprofile_nt)))
    end = perf_counter()
    return (f'The largest(highest) type of blood_grp in the profiles is: {mode_blood} and Time Delta is {int(end-start)}ms')

def mean_curr_location(allprofile_nt):
    
    '''This function will calculate the mean of the current location
    for the profiles'''
    
    #params - the profiles we generate earlier are used as input
    
    start = perf_counter()
    x, y = sum(map(lambda t: t[0],map(lambda v : v[4],allprofile_nt)))/len(allprofile_nt),sum(map(lambda t: t[1],map(lambda v : v[4],allprofile_nt)))/len(allprofile_nt)
    end = perf_counter()
    return (f'The average of location is {x,y} and Time Delta is {end-start}')

def oldest_person_age(allprofile_nt):
    
    '''This function will calculate the most oldest person in the profiles
    By searching for minimum of Birthdate from the profiles'''
    
    start = perf_counter()
    oldest_person = min(map(lambda x : x[-1],allprofile_nt))
    end = perf_counter()
    
    return (f'The oldest person among the profiles is: {oldest_person} and Time Delta is {end-start}')

def average_age(allprofile_nt):
    
    '''This function will calculate the average age of people 
    in the profiles'''
    
    today = datetime.today()
    start = perf_counter()
    avg_age = round(sum(map(lambda v : today.year - v[-1].year -((today.month, today.day) < (v[-1].month, v[-1].day)),allprofile_nt))/len(allprofile_nt))
    end = perf_counter()
    
    return (f'The average age in the profiles in {avg_age} and Time Delta is {end-start}')

#Second Task, samething with dictionary
def get_profiles_dict():
    
    '''this function will give us the profiles from the faker library
    but in the form of dictionary'''
    
    allprofile_dict = {}
    
    for _ in range(10000):
        allprofile_dict[_+1] = fake.profile()
    return allprofile_dict
    

def largest_blood_dict(allprofile_dict):
    
    '''This is very similar function to previous largest_blood function
    which gives out the most similar blood type, but here out data is in dictionary'''
    
    start = perf_counter()
    val = mode(list(map(lambda v: v['blood_group'],allprofile_dict.values())))
    end = perf_counter()
    return (f'The largest blood type is {val} and the Time Delta is {end-start}')    

def average_age_dict(allprofile_dict):
    
    '''This function will calculate the average age aof the profile,
    here we use dictionary as input parameter to the function'''
    
    today = datetime.today()
    start = perf_counter()
    avg_age = round(sum(map(lambda v : today.year - v['birthdate'].year -((today.month, today.day) < (v['birthdate'].month, v['birthdate'].day)),allprofile_dict.values()))/len(allprofile_dict))
    end = perf_counter()
    return (f'The average age of profile is {avg_age} and Time delta is {end-start}')

def mean_curr_location_dict(allprofile_dict):
    
    '''This function will calculate the mean of the current location
    for the profiles'''
    
    #params - the profiles we generate earlier are used as input
    
    start = perf_counter()
    x, y = sum(map(lambda t: t[0],map(lambda v : v['current_location'],allprofile_dict.values())))/len(allprofile_dict.values()),sum(map(lambda t: t[1],map(lambda v : v['current_location'],allprofile_dict.values())))/len(allprofile_dict.values())
    end = perf_counter()
    return (f'The average of location is {x,y} and Time Delta is {end-start}')

def oldest_person_dict(allprofile_dict):
    
    '''This function will take in the age of the profiles
    and calculate the oldest among them'''
    
    start = perf_counter()
    val =  min(allprofile_dict.values(),key = lambda v : v['birthdate'])
    end = perf_counter()
    return (f'The oldest among everyone is {val} and Time Delta is {end-start}')


# In[16]:


## Task 3
Company = namedtuple('Company', 'name symbol open high low close')
allcompany = namedtuple('allcompany',['Company'])
random_weight  =  namedtuple('random_weight','weight')

def init_task3()->tuple:
    """
    This function is used to initilize the all company named tuple( where data 
    of all the companies will be stored) and the normalized weights. 
    # Returns:
    It returns the Tuple containing the initailized All Company Named
    tuple and Normalized weights.
    """

    weight = random.uniform(0,1)
    r1 = random_weight(weight)
    
    for _ in range(99):
        weight = random.uniform(0,1)
        r1 += weight,

    sum_value = sum(r1)
    r2 = tuple(map(lambda x: x/sum_value,r1))

    open_ = random.randint(1000,50000) * weight
    close = open_ * random.uniform(0.7,1.15)
    high = open_ * random.uniform(0.85,1.15)
    low = open_ * random.uniform(0.7,1)
    if high < open_:
        high = open_
        if high < close:
            high = close
            if low > high:
                if high>open_:
                    low = open_
    else:
        low = close
        c1 = Company(fake.company(),''.join(random.sample(string.ascii_uppercase, 3)),open_, high, low, close)
        c2 = allcompany(c1)
  # c2.__doc__= """
  # This is a named tuple storing all the Company stock market. Each Company has 
  # name, open, close, high and Low. 
  # """
    return c2, r2

def stock_market(comp_stock:namedtuple ,norm_weights: namedtuple)->namedtuple:
    """
    This function is used to generate the stock market data for 99 Companies
    # Param:
    Comp_stock: Named tuple containing the initialized all Company named tuple
    norm_weights: Tuple containing the normalized weights used to generated the 
    which will be used to calculate the high, open, close and low.
    # Returns:
    It returns a Named tuple containing the stocks value of all 100 companies.
    """
    for _ in range(99):
        weight = norm_weights[_+1]
        open_ = random.randint(1000,50000) * weight
        close = open_ * random.uniform(0.7,1.15)
        high = open_ * random.uniform(0.85,1.15)
        low = open_ * random.uniform(0.7,1)
        if high < open_:
            high = open_
            if high < close:
                high = close
                if low > high:
                    if high>open_:
                        low = open_
                    else:
                        low = close
                        c1 = Company(fake.company(),''.join(random.sample(string.ascii_uppercase, 3)),open_, high, low, close)
                        comp_stock += allcompany(c1)
    return comp_stock


# In[ ]:




