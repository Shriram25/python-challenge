import os
import csv

fname = input("Enter a file name:")
csvpath = os.path.join("Resources",fname)
num_words =0
num_lines =0
num_periods = 0
num_letters = 0
with open(csvpath,'r') as f:
    for line in f:
        line = line.strip()
        
        if not line:
            continue
       
        words = line.split()
        num_words += len(words)
        for item in words:
            num_letters = num_letters+len(item)

        num_lines = num_lines+1
        periods = line.split(".")
        num_periods += len(periods)

print(words)
print(periods)
print(f"Approximate Word Count: {num_words}")
print(f"Approximate Sentence Count: {num_periods-1}")
print(f"Average Number of Letters: {round(num_letters/num_words,2)}")
print(f"Average Sentence Length: {num_words/(num_periods-1)}")




