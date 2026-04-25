"""
第3章 演習3 — システムプロンプト
==================================
学習目標:
  - system パラメータの使い方を習得する
  - システムプロンプトで Claude の振る舞いを制御する
  - 同じ質問に対してシステムプロンプトで回答スタイルが変わることを体験する
  - system=None を渡せない理由を理解する

実行方法:
  python 03_system_prompts.py
"""

from pathlib import Path
from dotenv import load_dotenv
import anthropic

load_dotenv(dotenv_path=Path(__file__).parent.parent.parent / ".env")

client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"


def section(title: str):
    print(f"\n{'─' * 50}")
    print(f"  {title}")
    print(f"{'─' * 50}")


def chat_with_system(user_input: str, system: str | None = None, max_tokens: int = 256) -> str:
    """
    system が指定されている場合のみ params に追加する。
    None を渡すと API エラーになるため、条件分岐が必要。
    """
    params: dict = {
        "model": MODEL,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": user_input}],
    }
    if system:
        params["system"] = system

    response = client.messages.create(**params)
    return response.content[0].text


# ─────────────────────────────────────────────
# 演習 3-1: システムプロンプトなし vs あり
# ─────────────────────────────────────────────

def exercise_3_1():
    section("演習 3-1: システムプロンプトなし vs あり")

    question = "機械学習とは何ですか？"

    print(f"質問: {question!r}\n")

    print("[A] システムプロンプトなし:")
    reply_a = chat_with_system(question)
    print(f"  {reply_a[:200]}{'...' if len(reply_a) > 200 else ''}\n")

    system_expert = (
        "あなたは初心者向けに分かりやすく技術を説明する教育者です。"
        "専門用語を使う場合は必ず簡単な言葉で補足してください。"
        "回答は3文以内に収めてください。"
    )
    print("[B] 教育者ペルソナ:")
    reply_b = chat_with_system(question, system=system_expert)
    print(f"  {reply_b}\n")

    system_researcher = (
        "You are a research scientist. Answer in English using precise technical terms."
        " Keep responses to 2 sentences."
    )
    print("[C] 研究者ペルソナ（英語）:")
    reply_c = chat_with_system(question, system=system_researcher)
    print(f"  {reply_c}")


# ─────────────────────────────────────────────
# 演習 3-2: タスク外の行動を制限する
# ─────────────────────────────────────────────

def exercise_3_2():
    section("演習 3-2: タスク外の行動を制限する")
    print("カスタマーサポートボットが範囲外の質問をされたときの動作を確認\n")

    system_support = (
        "あなたは「ポケットWiFi Pro」のカスタマーサポートです。"
        "製品に関する質問のみ回答してください。"
        "関係のない質問には「申し訳ありませんが、弊社製品に関するご質問のみ"
        "お受けしております」と答えてください。"
    )

    queries = [
        "接続が切れやすいのですが、対処法はありますか？",
        "明日の天気を教えてください。",
    ]

    for q in queries:
        reply = chat_with_system(q, system=system_support)
        print(f"ユーザー: {q}")
        print(f"Bot    : {reply}\n")


# ─────────────────────────────────────────────
# 演習 3-3: 数学チューターを作る
# ─────────────────────────────────────────────

def exercise_3_3():
    section("演習 3-3: 数学チューターを作る")
    print("直接答えず、ステップごとにガイドするチューターを実装\n")

    system_tutor = (
        "あなたは忍耐強い数学チューターです。"
        "生徒の質問に直接答えてはいけません。"
        "代わりに、ヒントと問いかけでステップバイステップに解法へ導いてください。"
        "1回の返答は2〜3文に収めてください。"
    )

    messages: list[dict] = []

    def tutor_chat(user_input: str) -> str:
        messages.append({"role": "user", "content": user_input})
        response = client.messages.create(
            model=MODEL,
            max_tokens=256,
            system=system_tutor,
            messages=messages,
        )
        reply = response.content[0].text
        messages.append({"role": "assistant", "content": reply})
        return reply

    print("生徒: 2x + 3 = 11 の解き方がわかりません。")
    r1 = tutor_chat("2x + 3 = 11 の解き方がわかりません。")
    print(f"先生: {r1}\n")

    print("生徒: 3 を移動すればいいですか？")
    r2 = tutor_chat("3 を移動すればいいですか？")
    print(f"先生: {r2}\n")

    print("生徒: 両辺から 3 を引くと 2x = 8 になりました！")
    r3 = tutor_chat("両辺から 3 を引くと 2x = 8 になりました！")
    print(f"先生: {r3}")


# ─────────────────────────────────────────────
# 練習問題
# ─────────────────────────────────────────────

def quiz():
    section("🏋️  練習問題")
    print("""
問題: 以下の条件を満たすシステムプロンプトを書いてください。

  条件:
    1. Claude が「料理レシピアドバイザー」として振る舞う
    2. 必ずレシピを提案する際に材料リストから始める
    3. 調理時間を常に明示する
    4. 料理と無関係な質問には答えない

  テスト質問:
    - "カルボナーラの作り方を教えてください"
    - "最近のニュースを教えてください"（→ 答えてはいけない）

  雛形:
    system_recipe = (
        "あなたは..."  # ここを完成させる
    )

    print(chat_with_system("カルボナーラの作り方を教えてください", system=system_recipe))
    print(chat_with_system("最近のニュースを教えてください", system=system_recipe))
""")


# ─────────────────────────────────────────────
# メイン
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("第3章 演習3: システムプロンプト")
    print("=" * 50)

    exercise_3_1()
    exercise_3_2()
    exercise_3_3()
    quiz()
