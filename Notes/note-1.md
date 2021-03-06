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

# Notes - 1
- Introduction
- Installing Python and VSCode
- IDE, GUI vs console programs
- "Hello, world!" program

---

<!-- _class: lead -->

# Disclaimer
এই নোট ফাইলে দেওয়া অনেক তথ্য ভবিষ্যতে পরিবর্তীত হয়ে যেতে পারে। কাজেই তুমি এটি কখন দেখছো, সেটার উপর ভিত্তি করে সবকিছুর মিল নাও পেতে পারো।

---

# Installing **Python** 🐍

পাইথনের প্রোগ্রাম রান করার জন্য আগে পাইথন রানটাইম কম্পিউটারে ইনস্টল করে নিতে হবে।

1. https://python.org - এই লিংকে যাও।
2. **Downloads** এ ক্লিক করো।
3. হলুদ রঙের **Download Python 3.10.x** বাটনে ক্লিক করো।
4. ডাউনলোড হওয়া ফাইলটি রান করো।


---

# Installing **Python** 🐍

5. পাইথন ইনস্টলার রান করার পর **Add Python 3.10 to PATH** চেকবক্সে ক্লিক(চেক) করে নিবে।
6. তারপর **Install Now** এ ক্লিক করবে।

টাডা! 🎇
কিছুক্ষণের মাঝেই পাইথন ইনস্টল হয়ে যাবে।

---

# What's an **IDE** 🤔

- IDE এর ফুল ফর্ম হলো - **Integrated Development Environment**।
- ডেভেলপমেন্টের সময় প্রয়োজনীয় জিনিসপাতি যেমন ডিবাগিং, প্যাকেজিং, ভুল ধরিয়ে দেওয়া, অটোকম্প্লিট ইত্যাদি সুবিধা দেয়।
- পাইথনের জন্য পপুলার একটি IDE হলো **PyCharm**, কিন্তু আমরা ভবিষ্যতে কিছু সুবিধা পাওয়ার জন্য **VSCode** ব্যবহার করবো।


---

# Setting up **VSCode** for Python

1. https://code.visualstudio.com/ যাও।
2. **Download for Windows** বাটনে ক্লিক করো।
3. ইনস্টলার ডাউনলোড হলে ওটা রান করো, আর ইনস্টল করো।
4. VSCode এর এক্সটেনশন প্যানেল থেকে **PyLance** এক্সটেনশনটি ইনস্টল করো।
5. এছাড়াও তোমার পছন্দমতন থিমস 🎨 ইনস্টল করে নিতে পারো।

---

# Console vs graphical programs

1. ভবিষ্যতে আমরা **GUI** (Graphical User Interface) সম্বলিত প্রোগ্রাম বানাবো, কিন্তু প্রথম দিকে আমাদের প্রোগ্রামগুলো কেবল কনসোলে রান হবে।
2. কনসোলে রান হবে মানে আমাদের প্রোগ্রামে বাটন, ছবি ইত্যাদি থাকবে না। কিন্তু টেক্সট থাকবে, আর আমরা ইউজারের ইনপুট নিতে পারবো।
3. কনসোলে কোনো টেক্সট লিখাকে আমরা print করা বলবো। 

---

# Writing your first program

1. একটি ফাঁকা ফোল্ডার 📂 তৈরি করো যেখানে তোমার প্রোগ্রাম গুলো রাখবে।
2. **VSCode** দিয়ে ফোল্ডারটি ওপেন করো।
3. বামে **Explorer** প্যানেলে ফোল্ডারটির নাম দেখতে পাবে। ওটার উপর মাউস পয়েন্টার নিলে নতুন ফাইল তৈরির বাটন দেখতে পাবে।
4. নতুন ফাইল তৈরির বাটনে ক্লিক করো আর ফাইলটির একটা নাম দাও। যেমন: `hello.py`। নামের শেষে `.py` দিতে ভুলো না।
5. এখন এডিটরে তোমার প্রোগ্রাম লিখতে পারবে। প্রথম প্রোগ্রাম হিসেবে আমরা শুধুমাত্র কনসোলে **Hello, world!** কথাটা প্রিন্ট করবো।

---

# Say hello to the world!

`hello.py` ফাইলটিতে নিম্নের কোড লিখো:

```python
print("Hello, world!")

```

- এখানে `print` হলো একটি ফাংশন। ফাংশন কল করার সময় ওপেনিং আর ক্লোজিং ব্র্যাকেট থাকে।
- প্রিন্ট ফাংশনের ব্র্যাকেটগুলোর মাঝে যা দেওয়া হবে তা কনসোলে প্রিন্ট হবে।

---

# Say hello to the world!

- কোনো টেক্সটকে অবশ্যই কোটেশন("") দিয়ে আবদ্ধ করতে হবে। যেমন: `print(Hello,world!)` লিখলে প্রোগ্রামটি কিন্তু কাজ করবে না। `print("Hello, world!")` লিখতে হবে।
- কোটেশন দিয়ে আবদ্ধ টেক্সটকে বলা হয় **স্ট্রিং(string)**। এ বিষয়ে পরে আরো জানবো।

---

# Running your first program

- **VSCode** এ `CTRL + J` বাটন প্রেস করলে টার্মিনাল দেখতে পাবে। 
- টার্মিনালে `python hello.py` লিখলে `hello.py` প্রোগ্রামটি রান হবে। তোমার ফাইলের নাম অন্য কিছু হলে তাই লিখতে হবে। যেমন: `python filename.py`।
- সবকিছু ঠিকঠাক করলে নিচে `Hello, world!` কথাটি দেখতে পাবে।
 
---

<!-- _class: lead -->

If all went well...
# 🎉 **Congratulations!** 🎉
তুমি প্রথমবারের মতন একটি পাইথন প্রোগ্রাম রান করলে!
এবার অন্য কিছু প্রিন্ট করার চেষ্টা করো।

---

<!-- _class: lead -->

# **What you know now**
That's it! If you had any trouble, kindly refer to the video or ask in the group. 🎊
