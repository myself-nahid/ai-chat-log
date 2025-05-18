import os
import string
import argparse
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer

def process_file(file_path):
    """Parse a single chat log file and return messages"""
    messages = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('User: ') or line.startswith('AI: '):
                speaker, content = line.split(': ', 1)
                messages.append({'speaker': speaker, 'content': content})
    return messages

def preprocess_text(text):
    """Clean text for TF-IDF analysis"""
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    return text

def get_summary(messages, top_keywords):
    """Generate summary for a conversation"""
    total_messages = len(messages)
    user_count = sum(1 for msg in messages if msg['speaker'] == 'User')
    
    # Extract user's main topics
    user_words = []
    for msg in messages:
        if msg['speaker'] == 'User':
            content = preprocess_text(msg['content'])
            user_words.extend(content.split())
    user_keywords = [word for word, _ in Counter(user_words).most_common(2)]
    
    # Build summary
    summary = [
        f"- The conversation had {total_messages} exchanges.",
        f"- The user asked mainly about {user_keywords[0]} and {user_keywords[1]}." if len(user_keywords) >= 2 
        else f"- The user asked mainly about {user_keywords[0]}." if user_keywords 
        else "- No clear user topics detected.",
        f"- Most significant keywords: {', '.join(top_keywords)}."
    ]
    return '\n'.join(summary)

def main():
    parser = argparse.ArgumentParser(description='AI Chat Log Summarizer')
    parser.add_argument('--input', type=str, required=True,
                       help='Path to chat log file or directory')
    args = parser.parse_args()

    # Process input (file or directory)
    all_docs = []
    file_paths = []
    
    if os.path.isfile(args.input):
        file_paths = [args.input]
    elif os.path.isdir(args.input):
        file_paths = [os.path.join(args.input, f) for f in os.listdir(args.input) 
                     if f.endswith('.txt')]
    
    # Read and preprocess all files
    for path in file_paths:
        messages = process_file(path)
        combined_text = ' '.join([preprocess_text(msg['content']) for msg in messages])
        all_docs.append(combined_text)

    # TF-IDF Analysis
    tfidf = TfidfVectorizer(stop_words='english', max_features=1000)
    tfidf_matrix = tfidf.fit_transform(all_docs)
    feature_names = tfidf.get_feature_names_out()

    # Generate summaries
    for i, path in enumerate(file_paths):
        messages = process_file(path)
        scores = tfidf_matrix[i].toarray().flatten()
        top_indices = scores.argsort()[-5:][::-1]
        top_keywords = [feature_names[idx] for idx in top_indices if scores[idx] > 0]
        
        print(f"\nSummary for {os.path.basename(path)}:")
        print(get_summary(messages, top_keywords[:5]))

if __name__ == "__main__":
    main()