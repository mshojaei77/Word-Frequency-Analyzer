import requests
from bs4 import BeautifulSoup
from collections import Counter
import csv
import matplotlib.pyplot as plt
import calendar
import heapq
import spacy
import tkinter as tk
from tkinter import messagebox

# Global Attributes
nlp = spacy.load('en_core_web_sm')  
parsed_data = dict()  

# Core Functionality
def main():
    window = tk.Tk()
    window.title("Word Frequency Analyzer")
    window.geometry('350x200')
    
    frame = tk.Frame(window)
    frame.pack(pady=20)
    
    tk.Label(frame, text="Month Number: ").grid(row=0, column=0)
    month_entry = tk.Entry(frame)
    month_entry.grid(row=0, column=1)
    
    tk.Label(frame, text="Year: ").grid(row=1, column=0)
    year_entry = tk.Entry(frame)
    year_entry.grid(row=1, column=1)
    
    analyze_button = tk.Button(window, text="Analyze", command=lambda: analyze(month_entry.get(), year_entry.get()))
    analyze_button.pack(pady=10)
    
    window.mainloop()

def analyze(month_str, year_str):
    try:
        month_number = int(month_str)
        month = month_number_to_name(month_number)
        year = int(year_str)
        
        if month is not None:
            month_number_str = str(month_number).zfill(2)
            url = f'https://edition.cnn.com/article/sitemap-{year}-{month_number_str}.html'
            print(f'\nURL: {url}')
            most_repeated_words = get_most_repeated_words(url)
            print(f'Most Repeated Words: {most_repeated_words}')
            write_to_csv(most_repeated_words, f'{month}_{url.split("//")[1].replace("/", "_")}.csv')
            print_chart(most_repeated_words[:20], month, year)
        else:
            messagebox.showerror("Invalid Input", "Invalid month number. Please enter a number between 1 and 12.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Invalid month or year. Please enter valid numerical values.")

def get_text(url):
    if url in parsed_data:
        return parsed_data[url]

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    parsed_data[url] = soup.get_text()
    return parsed_data[url]

def get_word_count(url):
    non_important_words = set([
        "the", "to", "in", "on", "at", "and", "or", "but", "is", "are", "was", "un",
        "were", "am", "a", "an", "of", "for", "with", "as", "by", "about", "map",
        "like", "through", "over", "before", "between", "2023", "cnn", "site",
        "after", "since", "during", "without", "under", "news2022", "news2023",
        "within", "along", "following", "across", "from", "how", "title", "articles",
        "behind", "beyond", "plus", "except", "based", "new", "news", "s",
        "but", "up", "down", "it", "its", "it's", "this", "that", "those", "these",
        "he", "she", "they", "we", "i", "me", "him", "her", "us", "them",
        "my", "mine", "your", "yours", "his", "hers", "its", "ours", "theirs",
        "also", "although", "because", "before", "besides", "consequently",
        "despite", "however", "if", "instead", "nevertheless", "since",
        "so", "then", "therefore", "though", "unless", "until", "when",
        "where", "while", "no", "oh", "post", "wikipedia", "portal", "may", "page",
        "current", "events", "05", "main", "search", "create", "news2023", "says",
        "league", "open", "first", "inter", "press", "ips", "headlines", "can",
        "guterres", "wednesday", "ukraine", "russia", 'eastunited', 'kingdomus',
    ])
    text = get_text(url)
    doc = nlp(text)
    words = [
        t.text.lower() for t in doc if not t.is_stop and not t.is_digit and not t.is_punct and not t.is_space and
        not t.like_url and not t.like_email and not t.ent_type_ in
        ['DATE', 'TIME', 'PERCENT', 'MONEY', 'QUANTITY', 'ORDINAL', 'CARDINAL'] and
        t.text.lower() not in non_important_words
    ]
    return Counter(words)

def get_most_repeated_words(url):
    word_count = get_word_count(url)
    most_repeated_words = heapq.nlargest(20, word_count.items(), key=lambda i: i[1])
    return most_repeated_words

def write_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['word', 'count'])
        writer.writerows(data)

def print_chart(counts, month, year):
    words, counts = zip(*counts)
    plt.figure(figsize=(12, 5))
    plt.barh(words, counts)
    plt.title(f'Top 20 most frequently used words in {month} {year}')
    plt.xlabel('Frequency')
    plt.ylabel('Word')
    plt.show()

def month_number_to_name(month_number):
    if 1 <= month_number <= 12:
        return calendar.month_name[month_number]
    return None

if __name__ == "__main__":
    main()