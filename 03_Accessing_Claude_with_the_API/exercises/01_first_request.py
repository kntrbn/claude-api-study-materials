"""
第3章 演習1 — 最初のAPIリクエスト
====================================
学習目標:
  - anthropic クライアントの初期化
  - messages.create() の基本パラメータを理解する
  - レスポンスオブジェクトの構造を把握する
  - stop_reason の意味を理解する

実行方法:
  python 01_first_request.py
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import anthropic

load_dotenv(dotenv_path=Path(__file__).parent.parent.parent / ".env")


# ─────────────────────────────────────────────
# ユーティリティ
# ─────────────────────────────────────────────

def section(title: str):
    print(f"\n{'─' * 50}")
    print(f"  {title}")
    print(f"{'─' * 50}")


client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"  # 演習用に軽量モデルを使用


# ─────────────────────────────────────────────
# 演習 1-1: 最小リクエスト
# ─────────────────────────────────────────────

def exercise_1_1():
    section("演習 1-1: 最小リクエスト")

    response = client.messages.create(
        model=MODEL,
        max_tokens=256,
        messages=[
            {"role": "user", "content": "日本の首都はどこですか？一言で答えてください。"}
        ],
    )

    print("▶ レスポンス全体:")
    print(f"  id          : {response.id}")
    print(f"  model       : {response.model}")
    print(f"  stop_reason : {response.stop_reason}")
    print(f"  usage       : input={response.usage.input_tokens}, output={response.usage.output_tokens}")
    print(f"\n▶ テキスト抽出:")
    print(f"  {response.content[0].text}")


# ─────────────────────────────────────────────
# 演習 1-2: max_tokens の動作確認
# ─────────────────────────────────────────────

def exercise_1_2():
    section("演習 1-2: max_tokens の動作確認")
    print("max_tokens=10 で長い回答を要求 → stop_reason が変わることを確認")

    response = client.messages.create(
        model=MODEL,
        max_tokens=10,  # 意図的に短く設定
        messages=[
            {"role": "user", "content": "日本の歴史について詳しく教えてください。"}
        ],
    )

    print(f"  stop_reason : {response.reason if hasattr(response, 'reason') else response.stop_reason}")
    print(f"  出力トークン: {response.usage.output_tokens}")
    print(f"  テキスト    : {response.content[0].text!r}")
    print()
    if response.stop_reason == "max_tokens":
        print("  ✓ max_tokens に達したため途中で停止しました")
        print("    → 実際のアプリでは max_tokens を十分大きく設定するか")
        print("      ストリーミング(演習5)を使いましょう")
    else:
        print(f"  stop_reason = {response.stop_reason!r}")


# ─────────────────────────────────────────────
# 演習 1-3: 複数の content block を持つ場合
# ─────────────────────────────────────────────

def exercise_1_3():
    section("演習 1-3: content ブロックの反復処理")
    print("通常は content[0] だけですが、ツール使用時などは複数になります。")
    print("安全な取り出し方を練習します。\n")

    response = client.messages.create(
        model=MODEL,
        max_tokens=128,
        messages=[{"role": "user", "content": "「こんにちは」と言ってください。"}],
    )

    # ✗ 危険な取り出し方（type チェックなし）
    # text = response.content[0].text  # ThinkingBlock 等では AttributeError

    # ✓ 安全な取り出し方
    texts = [block.text for block in response.content if block.type == "text"]
    print(f"  テキストブロック数 : {len(texts)}")
    for i, t in enumerate(texts):
        print(f"  [{i}] {t}")


# ─────────────────────────────────────────────
# 練習問題
# ─────────────────────────────────────────────

def quiz():
    section("🏋️  練習問題")
    print("""
問題: 以下のコードを完成させてください。

  response = client.messages.create(
      model=MODEL,
      max_tokens=___,          # (1) 512 トークンを上限に設定
      messages=[
          {"role": "___", "content": "Python の lambda とは何ですか？"}
          #             ^ (2) 正しい role を入れる
      ],
  )

  # (3) テキストを安全に取り出す
  text = ___

  print(text)

ヒント:
  (1) max_tokens は整数で上限を指定します（目標値ではありません）
  (2) ユーザー発言のロールは "user" です
  (3) response.content[0].text または内包表記で type=="text" をフィルタ
""")

    print("実際に試してみましょう ↓")
    # ここに自分のコードを書いてください
    # response = client.messages.create(...)
    # text = ...
    # print(text)


# ─────────────────────────────────────────────
# メイン
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("第3章 演習1: 最初のAPIリクエスト")
    print("=" * 50)

    exercise_1_1()
    exercise_1_2()
    exercise_1_3()
    quiz()
