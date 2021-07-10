import os,inspect,re,random
import pytest
from datetime import datetime
from decimal import Decimal
from html import escape
from collections import namedtuple
import session9 as s9

README_CONTENT_CHECK_FOR = [
    'Blood',
    'Location',
    'Age',
    'Person',
    'random',
    'lambda',
    'fake',
    'profile',
    'namedtuple',
    'tuple'
]
input_1 = None
input_2 = None
def test_function_name_had_cap_letter():
    """
    caps letter check in functions
    """
    functions = inspect.getmembers(nt, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
    
def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 300, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 18, 'You are not writing proper heading'

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_get_profiles():
    global input1
    input1 = s9.get_profiles()
    assert 10000 == len(input1),"you need to create 10000 entries"

def test_get_profiles_dict():
    global input2
    input2 = s9.get_profiles_dict()
    assert 10000 == len(input2),"you need to create 10000 entries"

def test_oldest_person_time_check():
    assert session9.oldest_person_age(input1)[0] <= nt.oldest_person_dict(input2)[0], "Check why dictionary is Fast"

def test_average_age_time_check():
    assert s9.average_age(input1)[0] <= nt.average_age_dict(input2)[0], "Check why dictionary is Fast"

def test_average_coords_time_check():
    assert session9.mean_curr_location(input1)[0] <= nt.mean_curr_location_dict(input2)[0], "Check why dictionary is Fast"

def test_bloodgroup_test():
    assert s9.largest_blood(input1)[0] <= nt.largest_blood_dict(input2)[0], "Check why dictionary is Fast"

def test_init_task3():
    global input3
    x,y = s9.init_task3()
    input3 = s9.stock_market(x,y)
    assert 100 == len(input3),"you need to create 100 entries"