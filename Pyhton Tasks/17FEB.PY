'''task  : 
1️⃣ Create a Series from [10, 20, 30, 40].

2️⃣ Create a Series with values [5, 6, 7] and index ["a","b","c"].

3️⃣ Create a Series from dictionary:

{"Math": 85, "Sci": 90, "Eng": 88}


4️⃣ Create a Series with scalar value 100 repeated for 5 indices.

5️⃣ Print first 3 values of a Series.

6️⃣ Print last 2 values.

7️⃣ Get the datatype of a Series.

8️⃣ Find number of elements in Series.

9️⃣ Select value using label "b".

🔟 Select value using position 2.

1️⃣1️⃣ Slice first 4 elements.

1️⃣2️⃣ Filter values greater than 50.

1️⃣3️⃣ Replace value 20 with 200.

1️⃣4️⃣ Rename index "a" to "alpha".

1️⃣5️⃣ Sort a Series by values.'''




import pandas as pd

# 1️⃣ Create a Series from [10, 20, 30, 40].
s1 = pd.Series([10, 20, 30, 40])
print("Series 1:", s1)

# 2️⃣ Create a Series with values [5, 6, 7] and index ["a","b","c"].
s2 = pd.Series([5, 6, 7], index=["a", "b", "c"])
print("\nSeries 2:", s2)

# 3️⃣ Create a Series from dictionary: {"Math": 85, "Sci": 90, "Eng": 88}
s3 = pd.Series({"Math": 85, "Sci": 90, "Eng": 88})
print("\nSeries 3:", s3)

# 4️⃣ Create a Series with scalar value 100 repeated for 5 indices.
s4 = pd.Series(100, index=range(5))
print("\nSeries 4:", s4)

# 5️⃣ Print first 3 values of a Series.
print("\nFirst 3 values of Series 1:", s1.head(3))

# 6️⃣ Print last 2 values.
print("\nLast 2 values of Series 1:", s1.tail(2))

# 7️⃣ Get the datatype of a Series.
print("\nDatatype of Series 1:", s1.dtype)

# 8️⃣ Find number of elements in Series.
print("\nNumber of elements in Series 1:", s1.size)


# 9️⃣ Select value using label "b".
print("\nValue at label 'b' in Series 2:", s2["b"])


# 🔟 Select value using position 2
print("\nValue at position 2 in Series 1:", s1.iloc[2])


# 1️⃣1️⃣ Slice first 4 elements.
print("\nFirst 4 elements of Series 1:", s1.iloc[:4])

                
