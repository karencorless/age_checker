# Age Checker Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def user_old_enough(DOB):
    # Takes date of birth and checks if user is older than 16 

    Parameters:
        DOB: a date in the format `YYYY-MM-DD`
    
    Returns:
        Boolean True/False if user is old enough

    Side effects:
        Date is beyond present date, throw error
        Impossible DOB (far too old) 
        Formatting issues (ie day vs month, DD-MM-YYYY vs YYYY-MM-DD)
        If user is exactly 16

```

```python
def denied_entry(DOB, user_old_enough):

    Parameters:
        DOB: a date in the format `YYYY-MM-DD`
        user_old_enough: verifies user age is over 16

    Returns:
        If user is younger than 16, "access is denied", [current age], [required age]

    Side effects:
        No obvious side effects 


```
```python
def access_granted(DOB, user_old_enough):

    Parameters:
        DOB: a date in the format `YYYY-MM-DD`
        user_old_enough: verifies user age is over 16

    Returns:
        If user is 16 OR older, "access has been granted"

    Side effects:
        No obvious side effects


```


```python
# EXAMPLE

def extract_uppercase(mixed_words):
    """Extracts uppercase words from a string

    Parameters: (list all parameters and their types)
        mixed_words: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a list of strings, each one a word (e.g. ["WORLD"])

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
Given a DOB where user is 16 years old
It returns an access granted message
"""
user_old_enough(2009-01-01) => ["access has been granted"]

"""
Given a DOB where user turns 16 years old that DAY
It returns an access granted message
"""
user_old_enough(2009-04-08) => ["access has been granted"]

"""
Given a DOB where user is under 16
It returns an access denied message, current age, minimum age
"""
user_old_enough(2009-04-08) => ["access is denied "], you are [current age], you need to be [required age]

"""
Given a DOB in the wrong format
It throws an error
"""
user_old_enough(08-04-2009) => throws an error 

"""
Given a DOB older than 200 
It throws an error
"""
user_old_enough(08-04-1009) => throws an error 

"""
Given a DOB 
It throws an error
"""
user_old_enough(08-04-2009) => throws an error 

```



```python
# EXAMPLE

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
extract_uppercase("hello WORLD") => ["WORLD"]

"""
Given two uppercase words
It returns a list with both words
"""
extract_uppercase("HELLO WORLD") => ["HELLO", "WORLD"]

"""
Given two lowercase words
It returns an empty list
"""
extract_uppercase("hello world") => []

"""
Given a lower and a mixed case word
It returns an empty list
"""
extract_uppercase("hello WoRLD") => []

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
extract_uppercase("hello WORLD!") => ["WORLD"]

"""
Given an empty string
It returns an empty list
"""
extract_uppercase("") => []

"""
Given a None value
It throws an error
"""
extract_uppercase(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
