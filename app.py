import openai
import os
from dotenv import load_dotenv
from prompts import make_prompt
from utils import parse_table

# .env 파일에서 API 키 불러오기
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_synonyms(words):
    prompt = make_prompt(words)

    print("🚀 GPT 요청을 시작합니다...")
    print("입력 단어 목록:", words)
    print("프롬프트:", prompt)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    answer = response.choices[0].message.content
    return parse_table(answer)

if __name__ == "__main__":
    input_words = [
        "happy", "big", "small", "fast", "beautiful",
        "strong", "smart", "hot", "cold", "funny"
    ]

    result = get_synonyms(input_words)

    print("영어 단어 | 유의어1 | 유의어2 | 유의어3 | 한국어 의미")
    print("_" * 60)
    for row in result:
        print(" | ".join(row))