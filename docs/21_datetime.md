# Day 21 - Datetime

Python lets us manipulate dates by using the `datetime` module that comes in the standard Python library, so we don't have to install it.  When we work with dates we must understand that what we really modify are datetime objects and not strings.

There are four main objects that we use to handle dates:

- [date](#date)
- [time](#time)
- [datetime](#datetime)
- [timedelta](#timedelta)

Before explaining each of these concepts, it is important that you understand that `datetime` as a module includes a class called the same way (`datetime`).

```python
import datetime

datetime.date
datetime.time
datetime.datetime
datetime.timedelta
```

## date

The `date` class allows us to work only with date (year, month, day). In order to create an instance of the object we use the date class in the following way:

```python
from datetime import date

birthday = date(1993, 12, 29)
print(birthday)

# Output
# 1993-12-29
```

Although we see the given date, what we have assigned is a `datetime.date` type object.

```python
print(type(birthday))
```

### today

The date class has a method that allows us to obtain the current day in this format.

```python
from datetime import date

today = date.today()
print(today)
```

## time

The time class in the same way allows us to create times from given data, however these values are not mandatory and by default the time obtained is 00:00:00.

In case of indicating a specific time, the values must go in the following order in case of not using `keyword arguments`:

```
time(hour, minute, second)
```

## datetime

`datetime` contains the information of both objects mentioned above `date` and `time`, and the values must be added in the same order (year, month, day, hours, minutes, seconds), and like the `time` class, the last 3 values are not mandatory.

```python
from datetime import datetime

my_date = datetime(2020, 8, 5, 15, 29)
print(my_date)

# Output
# 2020-08-05 15:29:00
```

### now

Just like with the `date` class, datetime lets us get the exact date using the `now` method.

```python
from datetime import datetime

now = datetime.now()
print(now)
```

## Attributes

Each of the classes explained above has attributes that we can use to obtain certain information in a specific way.

```python
from datetime import datetime

now = datetime.now()

print(f"Day: {now.day}")
print(f"Month: {now.month}")
print(f"Year: {now.year}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Second: {now.second}")
```

These attributes can be used in the classes mentioned above to which they are related, i.e. we cannot get the year from a `time` type object.

## Methods

Some of the methods we can use are:

- `weekday`: Weekday starting Monday as 0 and ending Sunday as 6.

```python
from datetime import date

now = date(2020, 8, 5)
print(now.weekday())

# Output
# 2 (Miercoles)
```

- `isoweekday`: Day of the week starting on Monday as 1 and ending on Sunday as 7.

```python
from datetime import date

now = date(2020, 8, 5)
print(now.isoweekday())

# Output
# 3 (Miercoles)
```

- `strftime`: Used to represent as a string objects `date`, `time` and `datetime`.

```python
from datetime import datetime

now = datetime.now()
str_date = now.strftime("%b %dth, %Y %H:%M")

print(str_date)
print(type(str_date))

# Output
# Aug 05th, 2020 17:59
# <class 'str'>
```

There are a series of **format codes** that you should use to indicate in which format you want to represent your date.

- `%b`: Month as locale’s abbreviated name. (Aug)
- `%d`: Day of the month as a zero-padded decimal number. (05)
- `%Y`: Year with century as a decimal number. (2020)
- `%H`: Hour (24-hour clock) as a zero-padded decimal number. (17)
- `%M`: Minute as a zero-padded decimal number. (59)

See the [Format Codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) you can use.

## timedelta

We use the timedelta class when we want to get the difference between two dates or times. All the classes of the module `datetime` use some `magical methods` that allow us to make operations and comparisons between dates.

Some of the parameters that we can provide are:

- days
- seconds
- minutes
- hours

```python
from datetime import timedelta

three_days = timedelta(days=3)
print(three_days)

# Output
# 3 days, 0:00:00
```

The timedelta object is representing a duration of 3 days, using this we can add or subtract this time to a given date.

```python
from datetime import timedelta

now = datetime.now()
three_days = timedelta(days=3)

now_plus_three_days = now + three_days

print(now)
print(now_plus_three_days)

# Output
# 2020-08-05 18:40:06.691392
# 2020-08-08 18:40:06.691392
```

In the same way we can do these operations between different datetime objects:

```python
now = date.today()
birthday = date(1993, 12, 29)

delta_difference = now - birthday

print(delta_difference.days)

# Output
# 9716
```

## strptime

This method of the `datetime` class allows us to obtain a date as a string according to a defined format, the format must be represented using the **Format Codes** mentioned above.

In case the date does not correspond with the format, an exception will be launched.

```python
from datetime import datetime

str_date = '2020-12-01 10:30PM'
format = '%Y-%m-%d %H:%M%p'

obj_date = datetime.strptime(str_date, format)
print(obj_date)
print(type(obj_date))

# Output
# 2020-12-01 10:30:00
# <class 'datetime.datetime'>
```

### ValueError

```python
str_date = '2020-12-01'
format = '%Y/%m/%d'

obj_date = datetime.strptime(str_date, format)

# Output
# ValueError: time data '2020-12-01' does not match format '%Y/%m/%d'
```

## Conclusion

This module has some limitations, such as

- Date difference every N years. (timedelta does not accept years or months)
- Obtain a datetime instance of a string without knowing its format.

These and other features that `datetime` may not have you can check out at a library called [dateutil](https://dateutil.readthedocs.io/en/stable/).

> It is important to emphasize that what is mentioned here is not all we can do with the module, but it is an introduction and what I think are some of the main functions that we should know how to use.

[Go to the Challenge](https://github.com/estebansolo/Python30/blob/master/exercises/21_datetime.py)

[Go to the Solution](https://github.com/estebansolo/Python30/blob/master/solutions/21_datetime.py)
