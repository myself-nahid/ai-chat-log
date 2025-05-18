import string
from collections import Counter

def main():
    file_path = 'chat.txt'
    stop_words = {
        'the', 'is', 'and', 'a', 'an', 'in', 'it', 'to', 'of', 'for', 'you', 'your',
        'i', 'me', 'my', 'we', 'our', 'he', 'she', 'they', 'them', 'this', 'that',
        'these', 'those', 'be', 'are', 'was', 'were', 'have', 'has', 'had', 'do',
        'does', 'did', 'can', 'could', 'will', 'would', 'should', 'what', 'where',
        'when', 'how', 'why', 'if', 'then', 'there', 'here', 'so', 'not', 'with',
        'as', 'at', 'on', 'up', 'down', 'out', 'about', 'into', 'over', 'under',
        'again', 'further', 'once', 'more', 'most', 'very', 'just', 'now', 'than',
        'no', 'yes', 'am', 'pm'
    }

    # Read and parse the chat log
    messages = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('User: ') or line.startswith('AI: '):
                speaker, content = line.split(': ', 1)
                messages.append({'speaker': speaker, 'content': content})

    # Calculate message statistics
    total_messages = len(messages)
    user_count = sum(1 for msg in messages if msg['speaker'] == 'User')
    ai_count = total_messages - user_count

    # Extract keywords from all messages
    all_words = []
    for msg in messages:
        content = msg['content'].translate(str.maketrans('', '', string.punctuation)).lower()
        for word in content.split():
            if word not in stop_words:
                all_words.append(word)
    top_keywords = [word for word, _ in Counter(all_words).most_common(5)]

    # Extract keywords from user messages for nature line
    user_words = []
    for msg in messages:
        if msg['speaker'] == 'User':
            content = msg['content'].translate(str.maketrans('', '', string.punctuation)).lower()
            user_words.extend(word for word in content.split() if word not in stop_words)
    user_keyword_counts = Counter(user_words)
    top_user_keywords = [word for word, _ in user_keyword_counts.most_common(2)]

    # Generate nature line
    if len(top_user_keywords) >= 2:
        nature_line = f"- The user asked mainly about {top_user_keywords[0]} and {top_user_keywords[1]}."
    elif len(top_user_keywords) == 1:
        nature_line = f"- The user asked mainly about {top_user_keywords[0]}."
    else:
        nature_line = "- The conversation did not contain specific topics from the user."

    # Generate and print the summary
    print("Summary:")
    print(f"- The conversation had {total_messages} exchanges.")
    print(nature_line)
    print(f"- Most common keywords: {', '.join(top_keywords)}.")

if __name__ == "__main__":
    main()