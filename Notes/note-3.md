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

# Notes - 3

- Output formatting
- Taking input
- Conditions

---

# Output formatting

পাইথনে আউটপুট ফর্ম্যাটিংয়ের বেশ কয়েকটা উপায় আছে। আমরা শিখবো তিনটি উপায়।

1. **String modulo operator**
    ```python
    name = "Shajid"
    friend = "Prangon"
    money = 12

    print("%s's friend %s has %d taka." % (name, friend, money))
    # Shajid's friend Prangon has 10 taka.
    ```

---

লক্ষ্য করো,

- যেখানে স্ট্রিং বসবে সেখানে `%s` হয়েছে।
- যেখানে সংখ্যা(integer) বসবে সেখানে `%d` হয়েছে।
- তারপর সবশেষে স্ট্রিংয়ের পর `%` ও ফার্স্ট ব্র্যাকেটে সিরিয়াল করে ভ্যারিয়েবলের নাম গুলো দেওয়া হয়েছে। সঠিক সিরিয়ালে থাকা কিন্তু জরুরি।

এভাবে দশমিক ভগ্নাংশ সংখ্যার জন্য আছে `%f`। দশমিক চিহ্নের পর কত ঘর পর্যন্ত প্রিন্ট করবে সেটার জন্য `%.2f` বা `%.4f` এরকম করে লিখতে পারো। প্রথমটি দশমিক চিহ্নের পর দুই ঘর, ও পরেরটি চার ঘর পর্যন্ত প্রিন্ট করবে। এভাবে 2 বা 4 এর জায়গায় ইচ্ছামত সংখ্যা ব্যবহার করা যাবে।

---

2. **`str.format()` মেথড**
    ```python
    name = "Shajid"
    friend = "Prangon"
    money = 12

    print("{}'s friend {} has {} taka.".format(name, friend, money))
    # Shajid's friend Prangon has 10 taka.
    ```

    লক্ষ্য করো, যেখানে যেখানে ভ্যারিয়েবলের মান বসবে সেখানে সেখানে `{}` বসেছে। পরে ডট দিয়ে `format` মেথডে সিরিয়ালি ভ্যারিবলগুলোর নাম লিখতে হবে। যদি ভগ্নাংশ সংখ্যার দশমিক চিহ্নের পর 2 টি ডিজিট প্রিন্ট করতে চাও, তবে সেই সংখ্যাটির ক্ষেত্রে `{:.2f}` দেওয়া লাগবে। 2 এর জায়গায় যেকোনো সংখ্যা দিতে পারো।

---

3. **f-Strings**
    ```python
    name = "Shajid"
    friend = "Prangon"
    money = 12

    print(f"{name}'s friend {friend} has {money} taka.")
    # Shajid's friend Prangon has 10 taka.
    ```

    এখানে দেখো স্ট্রিংয়ের কোটেশনের আগে একটা **f** বসেছে। **f** বসিয়ে সেকেন্ড ব্র্যাকেটের ভেতর ভ্যারিয়েবলের নাম স্ট্রিংয়ের মধ্যেই লিখে দেওয়া যায়!

---

# Taking input

প্রিন্ট করার জন্য যেমন `print()` ফাংশনটি আছে, তেমনি ইনপুট নেওয়ার জন্য `input()` ফাংশনটি আছে।

যেমন:
```python
name = input("Enter your name: ")
print(f"Hello, {name}! Kemon achho?")
```
এই প্রোগ্রামটি রান করে দেখো। প্রথমে প্রোগ্রামটি নাম জানতে চাইবে, পরে তুমি নাম ইনপুট করলে তোমার নাম উল্লেখ করে হেলো জানিয়ে কেমন আছো জিজ্ঞেস করবে।

---

অর্থাৎ, `input()` ফাংশনটি দিয়ে কোনো একটি ভ্যালু ইউজারের কাছ থেকে সংগ্রহ করে একটা ভ্যারিয়েবলে রেখে দেওয়া যায়। যা লিখে ইউজারের কাছ থেকে তথ্য চাওয়া হবে, তা ইনপুট ফাংশনের ব্র্যাকেটের ভেতর দেওয়া হয়। যেমন: `input("Tell me your age: ")`।

কিন্তু মনে রাখবে, ইনপুট ফাংশনটি সবসময় স্ট্রিং আকারে ভ্যারিয়েবলটি রাখবে। তুমি যদি ইউজারের কাছ থেকে কোনো সংখ্যা নিয়ে তার সাথে যোগ বিয়োগ বা গাণিতিক কোনো অপারেশন করতে চাও, তবে সেই ইনপুটটি আগে `int` বা `float` টাইপে কনভার্ট করে নিতে হবে।

চলো একটি গুণ করার প্রোগ্রাম বানাই এবার!

---

# A multiplication program

```python
a = input("Enter number a: ")
b = input("Enter number b: ")

a = int(a)
b = int(b)
# এখানে a ও b কে int এ কনভার্ট করা হয়েছে।

result = a * b

print(f"The result is: {result}")
```

তোমার বুঝতে সমস্যা হলে লেকচারটি আবার দেখে নিতে পারো।

---

# Conditions

কোনো শর্তের উপর সিদ্ধান্ত নিতে হলে পাইথনে আমাদের কন্ডিশনসের উপর দখল থাকা চাই। নিচের প্রোগ্রামটি লক্ষ্য করো:

```python
fruit = "mango"

if fruit == "mango":
    print("This is my favorite fruit.")
else:
    print("This is not my favorite.")
```

এখানে দেখো `fruit` ভ্যারিয়েবলটির মান বসিয়েছি `"mango"`। পরে নিচে তা চেক করেছি।

---

যদি `fruit` এর ভ্যালু `"mango"` হয়, তবে প্রিন্ট হবে `"This is my favorite fruit."`, আর তা না হলে প্রিন্ট হবে `"This is not my favorite."`
প্রোগ্রামটি রান করে দেখো। পরে ফ্রুটের মান বদলে আবার রান করে দেখো কি হয়!

মনে রাখবে

- `if` এর পর কন্ডিশন বসে। উপরের প্রোগ্রামের কন্ডিশন হলো `name == "mango"`, এখানে ডাবল সমান চিহ্ন হলো একটি কন্ডিশনাল অপারেটর। এটার মানে দুটো ভ্যালু একই কিনা। এরকম আরো কয়েকটা কন্ডিশনাল অপারেটর আছে।
- কন্ডিশনের পর একটা কোলন বসাতে হয় `:`। তারপর নিচে ইনটেন্ডেশান দিয়ে কন্ডিশন ট্রু হলে কি হবে সেটি বলতে হয়। ইনটেন্ডেশান হলো ফাঁকা জায়গা।  

---

- আরো কন্ডিশন বসাতে চাইলে `elif` ইউজ করতে হবে। `if` এর মতোই `elif` এর কন্ডিশন ও কন্ডিশন ট্রু হলে কি ঘটবে তা বসাতে হবে। 
- কোনো কন্ডিশন ট্রু না হলে কি করতে হবে তা বসবে `else` ব্লকে।

পরের পৃষ্ঠায় একটি সংখ্যা জোড় না বিজোড় তা যাচাইয়ের জন্য একটি প্রোগ্রাম লিখে দেওয়া হলো!

---

# Check if a number is odd or even
 
```python
num = input("Enter a number: ")
num = int(num) # Converting it to an integer

if num % 2 == 0:
    print(f"The number {num} is an EVEN number!")
else:
    print(f"The number {num} is an ODD number!")
```

Modulo operator `%` দিয়ে যে ভাগশেষ বের করে, মনে আছে? এখানে `num % 2` এর মান হলো `num` কে `2` দিয়ে ভাগ করলে ভাগশেষ কত হবে সেটা। উপরে কন্ডিশনে বলা হয়েছে, ভাগশেষটি যদি `0` হয়, তবে যেন জোড় প্রিন্ট হয়, অন্যথায় বিজোড়।

---
<!-- _class: lead -->
# **That's it for now!**
যদি নোটের কিছু বুঝতে সমস্যা হয়, তবে এই ক্লাসের ভিডিওটি দেখবে।
