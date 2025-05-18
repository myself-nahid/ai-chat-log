# AI Chat Log Summarizer 🗣️🤖

A Python tool to parse and summarize chat logs between a user and an AI.  
**Features**: Message statistics, keyword extraction (basic + TF-IDF), and multi-file batch processing.

---

## 📋 Project Overview

This script processes `.txt` chat logs (formatted as `User:` and `AI:` exchanges) and generates a summary including:
- Total message count.
- User vs. AI message distribution.
- Top keywords using **frequency analysis** or **TF-IDF** (advanced).
- A brief description of the conversation's focus.

### 🚀 **Bonus Features**  
1. **TF-IDF Keyword Extraction**  
   Uses `scikit-learn` to identify significant keywords based on term frequency and uniqueness across conversations.  
2. **Multi-File Processing**  
   Summarize all `.txt` files in a folder with a single command.

---

## 🛠️ Dependencies

Install required packages:  
```bash
pip install scikit-learn
```

## 🚀 How to Run
Basic Usage (Single File)
```
python chat_summarizer.py --input chat1.txt
```
Batch Processing (Folder)
```
python chat_summarizer.py --input discussions/
```

## 📂 Repository Structure
```
project/
├── chat_summarizer.py    # Main script (with bonus features)
├── chat1.txt             # Sample chat log
├── chat2.txt             # Sample chat log
└── discussions/          # Folder with multiple logs
    ├── discussion1.txt
    └── discussion2.txt
```

## 📸 Sample Outputs
Single File Summary
Command:
```
python chat_summarizer.py --input chat1.txt
```
Output:
```
Summary for chat1.txt:
- The conversation had 6 exchanges.
- The user asked mainly about for and what.
- Most significant keywords: analysis, python, data, used, automation.
```

Batch Processing
Command:
```
python chat_summarizer.py --input discussions/
```
Output:
```
Summary for discussion1.txt:
- The conversation had 6 exchanges.
- The user asked mainly about how and do.
- Most significant keywords: python, frontend, web, apps, backend.

Summary for discussion2.txt:
- The conversation had 6 exchanges.
- The user asked mainly about what and tools.
- Most significant keywords: data, large, matplotlib, math, manipulation.
```