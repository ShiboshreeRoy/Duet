# বাইনারি ফাইল পড়ুন
with open("README_binary.txt", "r", encoding="utf-8") as file:
    binary_data = file.read()

# বাইনারি ডাটা স্প্লিট করে ASCII টেক্সটে রূপান্তর
text = ''.join([chr(int(b, 2)) for b in binary_data.split()])

# মূল টেক্সট প্রিন্ট করুন বা নতুন ফাইলে সংরক্ষণ করুন
with open("README_restored.md", "w", encoding="utf-8") as restored_file:
    restored_file.write(text)

print("ফাইল পুনরুদ্ধার সম্পন্ন! 🎉")
