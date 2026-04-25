"""
第3章 演習2 — マルチターン会話
================================
学習目標:
  - Claude がステートレスである理由を体感する
  - 会話履歴を手動で管理する方法を習得する
  - ヘルパー関数でコードを整理する
  - 会話がどのように蓄積されるかを可視化する

実行方法:
  python 02_multi_turn.py
"""

import os
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


# ─────────────────────────────────────────────
# 演習 2-1: ステートレスを体験する（悪い例）
# ─────────────────────────────────────────────

def exercise_2_1():
    section("演習 2-1: ステートレスを体験（悪い例）")
    print("「会話」を意識せずに2回呼び出す → 文脈が失われる\n")

    # 1回目: 名前を伝える
    r1 = client.messages.create(
        model=MODEL,
        max_tokens=128,
        messages=[{"role": "user", "content": "私の名前はアリスです。"}],
    )
    print(f"Claude(1): {r1.content[0].text}")

    # 2回目: 前の会話を渡さないと Claude は忘れている
    r2 = client.messages.create(
        model=MODEL,
        max_tokens=128,
        messages=[{"role": "user", "content": "私の名前を知っていますか？"}],
    )
    print(f"Claude(2): {r2.content[0].text}")
    print("\n⚠ Claude は前の会話を知らないため「名前を教えていない」と答えます。")


# ─────────────────────────────────────────────
# 演習 2-2: 履歴を自前で管理する（良い例）
# ─────────────────────────────────────────────

def chat(messages: list[dict], user_input: str) -> str:
    """
    messages に user_input を追加してAPIを呼び出し、
    assistant の返答を messages に追加して返す。
    """
    messages.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model=MODEL,
        max_tokens=256,
        messages=messages,
    )

    reply = response.content[0].text
    messages.append({"role": "assistant", "content": reply})
    return reply


def exercise_2_2():
    section("演習 2-2: 履歴を渡すと文脈が保持される（良い例）")

    messages: list[dict] = []

    print("Turn 1: 名前を伝える")
    r1 = chat(messages, "私の名前はアリスです。")
    print(f"Claude: {r1}\n")

    print("Turn 2: 名前を聞く（履歴あり）")
    r2 = chat(messages, "私の名前を知っていますか？")
    print(f"Claude: {r2}\n")

    print("Turn 3: 趣味を話す")
    r3 = chat(messages, "私はプログラミングが趣味です。")
    print(f"Claude: {r3}\n")

    print("Turn 4: 自己紹介をまとめてもらう")
    r4 = chat(messages, "私についてわかっていることをまとめてください。")
    print(f"Claude: {r4}")


# ─────────────────────────────────────────────
# 演習 2-3: 会話の蓄積を可視化する
# ─────────────────────────────────────────────

def exercise_2_3():
    section("演習 2-3: 会話履歴の蓄積を可視化する")
    print("APIに毎回送るトークン数が増えていく様子を確認します。\n")

    messages: list[dict] = []
    questions = [
        "量子コンピュータとは何ですか？一文で。",
        "それは従来のコンピュータとどう違いますか？一文で。",
        "実用化されていますか？一文で。",
    ]

    for i, q in enumerate(questions, 1):
        messages.append({"role": "user", "content": q})
        response = client.messages.create(
            model=MODEL,
            max_tokens=128,
            messages=messages,
        )
        reply = response.content[0].text
        messages.append({"role": "assistant", "content": reply})

        print(f"Turn {i}:")
        print(f"  入力トークン: {response.usage.input_tokens:>4}  "
              f"出力トークン: {response.usage.output_tokens:>3}")
        print(f"  Claude: {reply[:80]}{'...' if len(reply) > 80 else ''}")
        print()

    print(f"現在の messages リストの長さ: {len(messages)} ターン")
    print("→ ターンが増えるほど入力トークンが増加し、コストが上がります。")
    print("  長い会話には Compaction / 要約戦略が有効です。")


# ─────────────────────────────────────────────
# 練習問題
# ─────────────────────────────────────────────

def quiz():
    section("🏋️  練習問題")
    print("""
問題: 以下のチャットボットを完成させてください。

  def simple_chatbot():
      messages = []
      print("チャットを開始します（'quit' で終了）")

      while True:
          user_input = input("You: ").strip()
          if user_input.lower() == "quit":
              break
          if not user_input:
              continue

          # ここに chat() を使ったコードを書く
          reply = ___
          print(f"Claude: {reply}")

  simple_chatbot()

ヒント:
  - 上で定義した chat(messages, user_input) 関数を呼び出します
  - messages リストは while ループの外で初期化します
""")

    run = input("練習問題を実行しますか？ (y/N): ").strip().lower()
    if run == "y":
        print("\n--- チャットボット起動 ---")
        history: list[dict] = []
        print("チャットを開始します（'quit' で終了）")
        while True:
            try:
                user_input = input("You: ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            if user_input.lower() == "quit" or not user_input:
                break
            reply = chat(history, user_input)
            print(f"Claude: {reply}")


# ─────────────────────────────────────────────
# メイン
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("第3章 演習2: マルチターン会話")
    print("=" * 50)

    exercise_2_1()
    exercise_2_2()
    exercise_2_3()
    quiz()
