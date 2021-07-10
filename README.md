# session-9-assignment-Shrav25
session-9-assignment-Shrav25 created by GitHub Classroom

####
Name - Shravan C R

####
Email - shravan.ramakrishna@gmail.com


####
Tuples
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.
Functions in Python are first class citizens. This means that they support operations such as being passed as an argument, returned from a function, modified, and assigned to a variable. This is a fundamental concept to understand before we delve into creating Python decorators.

Named Tuples
Named tuples are basically easy-to-create, lightweight object types. Named tuple instances can be referenced using object-like variable dereferencing or the standard tuple syntax. They can be used similarly to struct or other common record types, except that they are immutable.

<h2 align="center"> Assignment Solution </h2>

### Assignments

#### **Assignments 1**

In this Assignment we need to create fake profiles using faker library and store that inside named tuple. Then we need to create a namedtuple containing all the profiles and we need to perform the following operations:

Largest Blood Type

Here I am using lambda function and mapping operation to extract the blood type, Then we are storing it map object to list and pass it as a parameter to mode function defined in statistics library. We measure the time and record the readings.

Mean Current Location

Here I am using lambda function and mapping operation to extract the tuple containing the location, Then we access each tuple and perform an average operation and return the value with the time stamp.

Average Age

Here I am using lambda function and mapping operation to extract the birthdate, We then obtain the age by substracting the birthdate with current date. We then perform the average operation over the age and record the time.

Oldest Person

Here I am using lambda function and mapping operation to extract the birthdate, I then perform a minimum operation with key as the extracted birthdate and record the time.
#### **Assignments 2**

It is pretty much the same as done in Assignment 1 except it is done via dictionary in dictionary.

#### **Assignments 3**

Here in this Assignment we need to create a stock market scenario by generating 100 company data. Name is created using faker library. Symbol is generating using random sample from ascii characters. Weights are randomly generated in range 0 to 1 and stored in namedtuple. Then the weights are being normalized and are stored in tuple. open value is generated from randint from range 1000 to 50000 multiplied. High, Low and close is generated from multiplying the open value with randomly generated value from range 0.85 to 1.15, 0.7 to 1 and 0.7 to 1.15 respectively.We then compare the high, open, close and low value for border conditions. Then these randomly generated values are stored in named tuples.
