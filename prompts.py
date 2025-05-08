def make_prompt(words):
    word_list = ", ".join(words)
    prompt = f"""다음 영어 단어 각각에 대해 유의어 3개와 한국어 의미를 표 형식으로 보여줘.
단어 리스트: {word_list}

결과는 다음과 같이 보여줘:
영어 단어 | 유의어1 | 유의어2 | 유의어3 | 한국어 의미
"""
    return prompt