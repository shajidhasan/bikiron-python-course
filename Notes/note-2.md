---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('../assets/background.png')
color: #46466c
---

<style>
  /* :root {
    --color-highlight: 
  } */
  section {
    font-family: 'Baloo Da 2', serif !important;
  }
  h1 {
    font-family: 'Trebuchet MS'
  }
</style>

![bg left:50% 90%](../assets/logo.png)

# Notes - 2

- Variables
- Numbers and arithmetic
- String and string manipulation
- The Python interpreter

---

# Comments

মাঝে মাঝে নিজেদের জন্য বা অন্যকে বোঝানোর জন্য প্রোগ্রামে মন্তব্য লিখে রাখার প্রয়োজন পড়ে। এসব মন্তব্য লিখতে হয় এভাবে - 
```python

# This is a comment, this won't disturb the program
print("Hello, world!")
# The line above will print "Hello, world!" to the console

```

পাইথন ইন্টারপ্রেটার কমেন্টগুলোকে উপেক্ষা করে যাবে। কিন্তু আমরা প্রয়োজনীয় জিনিসপাতি নিজেদের সুবিধার্তে লিখে রাখতে পারি। 

---

# Variables

কোনো ভ্যালু জমা রাখার জন্য ভ্যারিয়েবল তৈরি করা হয়। ভ্যারিয়েবল ডিফাইন করতে হয় এভাবে:
```python
name = "Shajid Hasan"
age = 20
```
এখানে `name` ও `age` হলো ভ্যারিয়েবলের নাম। আর `"Shajid Hasan"` ও `20` হলো ভ্যারিয়েবলের ভ্যালুগুলো।

---

# Variables

তুমি চাইলে প্রিন্ট করে দেখতে পারো, ভ্যারিয়েবলগুলো ঠিকঠাক কাজ করছে কিনা।

```python
name = "Shajid Hasan"
age = 20
print("My name is", name)
print("I am", age, "years old")
```

প্রোগ্রামটি রান করলে দেখতে পাবে -
```
My name is Shajid Hasan
I am 20 years old
```

---

# Numbers

- পাইথন প্রোগ্রামিংয়ে আমরা দুই ধরণের সংখ্যা নিয়ে সাধারণত কাজ করবো।
    1. **পূর্ণ সংখ্যা** বা integer (**int** type)। যেমন: `10`, `304`, `5993` ইত্যাদি।
    2. **ভগ্নাংশ সংখ্যা** বা floating point (**float** type)। যেমন: `3.1416`, `56.5`, `20.18` ইত্যাদি।


---

# Arithmetics
 
ধরো আমি এভাবে দুটো সংখ্যা ভ্যারিয়েবল ডিফাইন করেছি।

```python
a = 10
b = 3
```

এদের নিয়ে গাণিতিক হিসাবের জন্য ৭ টি এরিথম্যাটিক অপারেটর রয়েছে।

1. **যোগ অপারেটর**
    ```python
    c = a + b
    # c is 13
    ```

---

2. **বিয়োগ অপারেটর**
    ```python
    c = a - b
    # c is 7
    ```

3. **গুণ অপারেটর**
    ```python
    c = a * b
    # c is 30
    ```

4. **ভাগ অপারেটর**
    ```python
    c = a / b
    # c is 3.333333 (float)
    ```
---

5. **ফ্লোর ভাগ অপারেটর**
    ```python
    c = a // b
    # c is 3 (int)
    ```
    লক্ষ্য করো, ফ্লোর ভাগ করলে দশমিকের পরের অংশটুকু বাদ যায়। অর্থাৎ আমরা একটি **int** বা **পূর্ণ সংখ্যা** পাবো। কিন্তু সাধারণ ভাগ অপারেটর দিয়ে **float** বা **ভগ্নাংশ সংখ্যা** পাওয়া যায়। 

6. **ভাগশেষ অপারেটর**
    ```python
    c = a // b
    # c is 1, কারণ 10 কে 3 দিয়ে ভাগ দিলে ভাগশেষ 1
    ```
---
7. **সূচক অপারেটর**
    ```python
    c = a ** b
    # c is 1000, কারণ 10^3 = 1000
    ```

এই অপারেটরগুলো দিয়ে বিভিন্ন গাণিতিক হিসাব সহজেই করে ফেলা যায়।

---

# Strings

- স্ট্রিং হলো অক্ষরের সমাবেশ। যেমন: `"Bikiron"`, `"fire"`, `"ironman"`, `"রহিম"` ইত্যাদি।
- সহজ কথায়, টেক্সটই হলো স্ট্রিং।
- স্ট্রিংয়ের দুপাশে অবশ্যই কোটেশন থাকবে। সিঙ্গেল কোট (`'string'`) অথবা ডাবল কোট (`"string"`) উভয়েই হতে পারে।
- স্ট্রিংকে নানানভাবে ম্যানিপুলেট করা যায়।

---

# Working with strings

ধরো আমি এভাবে একটি স্ট্রিং ভ্যারিয়েবল ডিফাইন করেছি:
```python
town = "mymensingh"
```
এখন এই স্ট্রিঙের উপর বিভিন্ন কাজ চালানো যায়। যেমন:

1. স্ট্রিংটি কত অক্ষরের বের করতে চাইলে `len` ফাংশনটি ব্যবহার করতে পারি।
    ```python
    print("The length is:", len(town))
    # Will print - The length is 10
    ```

---

2. **n তম** অক্ষর বের করতে চাইলে:
    ```python
    print("The first letter is", town[0])
    # মনে রাখবে, পাইথনে প্রথমটা মানে হলো শূন্যতম
    
    print("The second letter is", town[1])
    
    print("The last letter is", town[-1])
    # শেষের দিক থেকে -1, -2 করে যাবে 
    ```
    অর্থাৎ n তম অক্ষরের জন্য এভাবে লিখতে হবে `town[n-1]`। 1 বিয়োগ হয়েছে কারণ শূন্য থেকে ইন্ডেক্স শুরু হয়।

---

3. **a থেকে b তম** অক্ষরগুলো(সাবস্ট্রিং) বের করতে চাইলে:
    ```python
    print(town[3:7])
    # Will print - ensi
    ```
    অর্থাৎ তুমি যদি `town` স্ট্রিং ভ্যারিয়েবলটির **a তম** থেকে **b তম** পর্যন্ত অক্ষরগুলো বের করতে চাও তবে সিন্ট্যাক্স হবে `town[a-1:b]`।

---

4. স্ট্রিং নিয়ে কাজ করতে হলে আমাদের ছোটো হাতের অক্ষর ও বড় হাতের অক্ষরের মাঝে কনভার্শন জানা থাকা চাই। যেমন:

```python
town = "mymensingh"

new_string = town.upper()
# new_string এর ভ্যালু হবে "MYMENSINGH", অর্থাৎ সবগুলো অক্ষর বড় হাতের হয়ে যাবে।
# তেমনি, lower() ব্যবহার করে ছোটো হাতের বানানো যাবে।

new_string = town.capitalize()
# new_string এর ভ্যালু হবে "Mymensingh", শুধু প্রথম অক্ষর বড় হাতের হবে।

```

আরো কিছু খুব ইউজফুল মেথডস আছে! ওগুলো সম্পর্কে আমরা পরে জানবো।

---

# The Python interpreter

- পাইথন কিন্তু ইন্টারপ্রেটেড ল্যাঙ্গুয়েজ (কমপাইলড না)।
- একটা পাইথন প্রোগ্রাম লাইন বাই লাইন এক্সিকিউট হয়।
- পাইথন ইন্টারপ্রেটারে এক লাইন এক লাইন করে কোড রান করা যায়।
- কোড টেস্টিংয়ের জন্য ইন্টারপ্রেটার খুব কার্যকরী।

---

# Use the Python interpreter

টার্ট মেনুতে `python` লিখে সার্চ করলেই ইন্টারপ্রেটারটি পাবে। অথবা, VSCode এর টার্মিনালে `python` লিখে এন্টার করলেও ইন্টারপ্রেটারটি চালু হবে।
এখানে যা কমান্ড লিখবে, তার পরের লাইনে সেটা এক্সিকিউট হবে। যেমন:
```
>>> print("Hello, world!")
Hello world!
>>> name = "Ayesha"
>>> print("Hello", name)
Hello Ayesha
```

---

<!-- _class: lead -->

# See you in the next class!
আজ ক্লাসে যা যা শিখেছি তার নোট সংগ্রহ করতে ভুলো না!
