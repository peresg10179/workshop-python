conda install pandas
python3 -m pip install --upgrade pandas
In [1]: df = pd.DataFrame({"A": [1, 2], "B": [True, False]})

In [2]: df.all(axis=None)
Out[2]: False

>>> # NumPy 1.15, pandas 0.23.1
>>> np.any(pd.DataFrame({"A": [False], "B": [False]}))
A    False
B    False
dtype: bool

# 0.22.0... Silently coerce the datetime.date
>>> Series(pd.date_range('2017', periods=2)) == datetime.date(2017, 1, 1)
0     True
1    False
dtype: bool

# 0.23.0... Do not coerce the datetime.date
>>> Series(pd.date_range('2017', periods=2)) == datetime.date(2017, 1, 1)
0    False
1    False
dtype: bool

# 0.23.1... Coerce the datetime.date with a warning
>>> Series(pd.date_range('2017', periods=2)) == datetime.date(2017, 1, 1)
/bin/python:1: FutureWarning: Comparing Series of datetimes with 'datetime.date'.  Currently, the
'datetime.date' is coerced to a datetime. In the future pandas will
not coerce, and the values not compare equal to the 'datetime.date'.
To retain the current behavior, convert the 'datetime.date' to a
datetime with 'pd.Timestamp'.
  #!/bin/python3
0     True
1    False
dtype: bool





# 0.22.0... Silently coerce the datetime.date
>>> Series(pd.date_range('2017', periods=2)) == datetime.date(2017, 1, 1)
0     True
1    False
dtype: bool

# 0.23.0... Do not coerce the datetime.date
>>> Series(pd.date_range('2017', periods=2)) == datetime.date(2017, 1, 1)
0    False
1    False
dtype: bool

# 0.23.1... Coerce the datetime.date with a warning
>>> Series(pd.date_range('2017', periods=2)) == datetime.date(2017, 1, 1)
/bin/python:1: FutureWarning: Comparing Series of datetimes with 'datetime.date'.  Currently, the
'datetime.date' is coerced to a datetime. In the future pandas will
not coerce, and the values not compare equal to the 'datetime.date'.
To retain the current behavior, convert the 'datetime.date' to a
datetime with 'pd.Timestamp'.
  #!/bin/python3
0     True
1    False
dtype: bool

In [1]: df = pd.DataFrame({'foo': [1, 2, 3, 4],
   ...:                    'bar': ['a', 'b', 'c', 'd'],
   ...:                    'baz': pd.date_range('2018-01-01', freq='d', periods=4),
   ...:                    'qux': pd.Categorical(['a', 'b', 'c', 'c'])
   ...:                    }, index=pd.Index(range(4), name='idx'))
   ...: 

In [2]: df
Out[2]: 
     foo bar        baz qux
idx                        
0      1   a 2018-01-01   a
1      2   b 2018-01-02   b
2      3   c 2018-01-03   c
3      4   d 2018-01-04   c

In [3]: df.dtypes
Out[3]: 
foo             int64
bar            object
baz    datetime64[ns]
qux          category
dtype: object

In [4]: df.to_json('test.json', orient='table')

In [5]: new_df = pd.read_json('test.json', orient='table')

In [6]: new_df
Out[6]: 
     foo bar        baz qux
idx                        
0      1   a 2018-01-01   a
1      2   b 2018-01-02   b
2      3   c 2018-01-03   c
3      4   d 2018-01-04   c

In [7]: new_df.dtypes
Out[7]: 
foo             int64
bar            object
baz    datetime64[ns]
qux          category
dtype: object



In [8]: df.index.name = 'index'

In [9]: df.to_json('test.json', orient='table')

In [10]: new_df = pd.read_json('test.json', orient='table')

In [11]: new_df
Out[11]: 
   foo bar        baz qux
0    1   a 2018-01-01   a
1    2   b 2018-01-02   b
2    3   c 2018-01-03   c
3    4   d 2018-01-04   c

In [12]: new_df.dtypes
Out[12]: 
foo             int64
bar            object
baz    datetime64[ns]
qux          category
dtype: object

n [13]: df = pd.DataFrame({'A': [1, 2, 3]})

In [14]: df
Out[14]: 
   A
0  1
1  2
2  3

In [15]: df.assign(B=df.A, C=lambda x:x['A']+ x['B'])
Out[15]: 
   A  B  C
0  1  1  2
1  2  2  4
2  3  3  6

n [2]: df = pd.DataFrame({"A": [1, 2, 3]})

In [3]: df.assign(A=lambda df: df.A + 1, C=lambda df: df.A * -1)
Out[3]:
   A  C
0  2 -1
1  3 -2
2  4 -3
Perilaku Baru:

In [16]: df.assign(A=df.A+1, C= lambda df: df.A* -1)
Out[16]: 
   A  C
0  2 -2
1  3 -3
2  4 -4

In [17]: left_index = pd.Index(['K0', 'K0', 'K1', 'K2'], name='key1')

In [18]: left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
   ....:                      'B': ['B0', 'B1', 'B2', 'B3'],
   ....:                      'key2': ['K0', 'K1', 'K0', 'K1']},
   ....:                     index=left_index)
   ....: 

In [19]: right_index = pd.Index(['K0', 'K1', 'K2', 'K2'], name='key1')

In [20]: right = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
   ....:                       'D': ['D0', 'D1', 'D2', 'D3'],
   ....:                       'key2': ['K0', 'K0', 'K0', 'K1']},
   ....:                      index=right_index)
   ....: 

In [21]: left.merge(right, on=['key1', 'key2'])
Out[21]: 
       A   B key2   C   D
key1                     
K0    A0  B0   K0  C0  D0
K1    A2  B2   K0  C1  D1
K2    A3  B3   K1  C3  D3

# Build MultiIndex
In [22]: idx = pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('a', 2),
   ....:                                  ('b', 2), ('b', 1), ('b', 1)])
   ....: 

In [23]: idx.names = ['first', 'second']

# Build DataFrame
In [24]: df_multi = pd.DataFrame({'A': np.arange(6, 0, -1)},
   ....:                         index=idx)
   ....: 

In [25]: df_multi
Out[25]: 
              A
first second   
a     1       6
      2       5
      2       4
b     2       3
      1       2
      1       1

# Sort by 'second' (index) and 'A' (column)
In [26]: df_multi.sort_values(by=['second', 'A'])
Out[26]: 
              A
first second   
b     1       1
      1       2
a     1       6
b     2       3
a     2       4
      2       5
	  
	  In [1]: from cyberpandas import IPArray

In [2]: values = IPArray([
   ...:     0,
   ...:     3232235777,
   ...:     42540766452641154071740215577757643572
   ...: ])
   ...:
   ...:
   
   In [3]: ser = pd.Series(values)

In [4]: ser
Out[4]:
0                         0.0.0.0
1                     192.168.1.1
2    2001:db8:85a3::8a2e:370:7334
dtype: ip

In [5]: ser.isna()
Out[5]:
0     True
1    False
2    False
dtype: bool
In [27]: cat1 = pd.Categorical(["a", "a", "b", "b"],
   ....:                       categories=["a", "b", "z"], ordered=True)
   ....: 

In [28]: cat2 = pd.Categorical(["c", "d", "c", "d"],
   ....:                       categories=["c", "d", "y"], ordered=True)
   ....: 

In [29]: df = pd.DataFrame({"A": cat1, "B": cat2, "values": [1, 2, 3, 4]})

In [30]: df['C'] = ['foo', 'bar'] * 2

In [31]: df
Out[31]: 
   A  B  values    C
0  a  c       1  foo
1  a  d       2  bar
2  b  c       3  foo
3  b  d       4  bar

In [32]: df.groupby(['A', 'B', 'C'], observed=False).count()
Out[32]: 
         values
A B C          
a c bar     NaN
    foo     1.0
  d bar     1.0
    foo     NaN
  y bar     NaN
    foo     NaN
b c bar     NaN
...         ...
  y foo     NaN
z c bar     NaN
    foo     NaN
  d bar     NaN
    foo     NaN
  y bar     NaN
    foo     NaN

[18 rows x 1 columns]

In [33]: df.groupby(['A', 'B', 'C'], observed=True).count()
Out[33]: 
         values
A B C          
a c foo       1
  d bar       1
b c foo       1
  d bar       1
  In [34]: cat1 = pd.Categorical(["a", "a", "b", "b"],
   ....:                       categories=["a", "b", "z"], ordered=True)
   ....: 

In [35]: cat2 = pd.Categorical(["c", "d", "c", "d"],
   ....:                       categories=["c", "d", "y"], ordered=True)
   ....: 

In [36]: df = DataFrame({"A": cat1, "B": cat2, "values": [1, 2, 3, 4]})

In [37]: df
Out[37]: 
   A  B  values
0  a  c       1
1  a  d       2
2  b  c       3
3  b  d       4

In [38]: pd.pivot_table(df, values='values', index=['A', 'B'],
   ....:                dropna=True)
   ....: 
Out[38]: 
     values
A B        
a c       1
  d       2
b c       3
  d       4

In [39]: pd.pivot_table(df, values='values', index=['A', 'B'],
   ....:                dropna=False)
   ....: 
Out[39]: 
     values
A B        
a c     1.0
  d     2.0
  y     NaN
b c     3.0
  d     4.0
  y     NaN
z c     NaN
  d     NaN
  y     NaN
  
  In [40]: s = pd.Series(np.arange(5), np.arange(5) + 1)

In [41]: s
Out[41]: 
1    0
2    1
3    2
4    3
5    4
dtype: int64

In [58]: ts = Timestamp('2014-08-01 09:00', tz='US/Eastern')

In [59]: ts
Out[59]: Timestamp('2014-08-01 09:00:00-0400', tz='US/Eastern')

In [60]: ts.tz_localize(None)
Out[60]: Timestamp('2014-08-01 09:00:00')

In [61]: didx = DatetimeIndex(start='2014-08-01 09:00', freq='H', periods=10, tz='US/Eastern')

In [62]: didx
Out[62]: 
DatetimeIndex(['2014-08-01 09:00:00-04:00', '2014-08-01 10:00:00-04:00',
               '2014-08-01 11:00:00-04:00', '2014-08-01 12:00:00-04:00',
               '2014-08-01 13:00:00-04:00', '2014-08-01 14:00:00-04:00',
               '2014-08-01 15:00:00-04:00', '2014-08-01 16:00:00-04:00',
               '2014-08-01 17:00:00-04:00', '2014-08-01 18:00:00-04:00'],
              dtype='datetime64[ns, US/Eastern]', freq='H')

In [63]: didx.tz_localize(None)
Out[63]: 
DatetimeIndex(['2014-08-01 09:00:00', '2014-08-01 10:00:00',
               '2014-08-01 11:00:00', '2014-08-01 12:00:00',
               '2014-08-01 13:00:00', '2014-08-01 14:00:00',
               '2014-08-01 15:00:00', '2014-08-01 16:00:00',
               '2014-08-01 17:00:00', '2014-08-01 18:00:00'],
              dtype='datetime64[ns]', freq='H')
			  
			  