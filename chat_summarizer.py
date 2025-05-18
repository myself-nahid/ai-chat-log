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

    

if __name__ == "__main__":
    main()