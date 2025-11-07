# Interactive Text Summarizer using Hugging Face Transformers

!pip install transformers sentencepiece --quiet


from transformers import pipeline


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


print("Welcome to the AI Text Summarizer!")
print("Enter or paste your text below (press Enter twice to summarize):")


lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

text = " ".join(lines)

if len(text) < 50:
    print("\n⚠️ Please enter a longer text (at least 50 characters).")
else:
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    print("\n🔹 Summary:\n", summary[0]['summary_text'])
