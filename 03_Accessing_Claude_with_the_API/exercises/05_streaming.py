"""
第3章 演習5 — レスポンスストリーミング
========================================
学習目標:
  - ストリーミングと非ストリーミングの体験差を理解する
  - client.messages.stream() の使い方を習得する
  - stream.text_stream と stream.get_final_message() の使い分けを学ぶ
  - ストリームイベントの種類を把握する

実行方法:
  python 05_streaming.py
"""

import time
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
# 演習 5-1: 非ストリーミング vs ストリーミング体験
# ─────────────────────────────────────────────

def exercise_5_1():
    section("演習 5-1: 非ストリーミング vs ストリーミングの体験差")

    prompt = "日本の四季それぞれの魅力を、各季節2〜3文で説明してください。"

    # ─ 非ストリーミング ─
    print("▶ 非ストリーミング（全文が届くまで待機）")
    print("  [待機中", end="", flush=True)
    t0 = time.time()
    response = client.messages.create(
        model=MODEL,
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}],
    )
    elapsed = time.time() - t0
    print(f"] {elapsed:.1f}秒後に一括受信")
    text = response.content[0].text
    print(f"  (先頭80文字): {text[:80]}...\n")

    # ─ ストリーミング ─
    print("▶ ストリーミング（トークンが届き次第表示）")
    t0 = time.time()
    with client.messages.stream(
        model=MODEL,
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        first_token = True
        for text_chunk in stream.text_stream:
            if first_token:
                print(f"  [最初のトークンまで: {time.time() - t0:.2f}秒]")
                print("  ", end="", flush=True)
                first_token = False
            print(text_chunk, end="", flush=True)

        final = stream.get_final_message()
        print(f"\n\n  [完了] 総トークン: "
              f"入力={final.usage.input_tokens}, "
              f"出力={final.usage.output_tokens}")


# ─────────────────────────────────────────────
# 演習 5-2: stream.text_stream だけを使う（最も簡単）
# ─────────────────────────────────────────────

def exercise_5_2():
    section("演習 5-2: text_stream を使ったシンプルなストリーミング")

    print("チャットUIのような体験を再現します。\n")
    print("Claude: ", end="", flush=True)

    with client.messages.stream(
        model=MODEL,
        max_tokens=256,
        messages=[{"role": "user", "content": "プログラミングを始める人へのアドバイスを3つ教えてください。"}],
    ) as stream:
        for chunk in stream.text_stream:
            print(chunk, end="", flush=True)

    print()  # 改行


# ─────────────────────────────────────────────
# 演習 5-3: イベントの種類を観察する
# ─────────────────────────────────────────────

def exercise_5_3():
    section("演習 5-3: ストリームイベントの種類を観察する")
    print("stream=True で低レベル API を使い、イベントを確認します。\n")

    event_counts: dict[str, int] = {}
    total_text = []

    for event in client.messages.create(
        model=MODEL,
        max_tokens=64,
        messages=[{"role": "user", "content": "1+1は？数字だけ答えて。"}],
        stream=True,
    ):
        etype = event.type
        event_counts[etype] = event_counts.get(etype, 0) + 1

        if etype == "content_block_delta" and hasattr(event.delta, "text"):
            total_text.append(event.delta.text)

    print("受信イベント一覧:")
    for etype, count in event_counts.items():
        print(f"  {etype:<35} × {count}")

    print(f"\n組み立てたテキスト: {''.join(total_text)!r}")
    print("""
イベントの流れ:
  message_start        → メッセージ開始
  content_block_start  → コンテンツブロック開始
  content_block_delta  → テキストの断片（ここにテキストが入る）
  content_block_stop   → コンテンツブロック終了
  message_delta        → stop_reason や usage が入る
  message_stop         → メッセージ終了
""")


# ─────────────────────────────────────────────
# 演習 5-4: get_final_message() で完全なレスポンスを取得
# ─────────────────────────────────────────────

def exercise_5_4():
    section("演習 5-4: ストリーミング後に完全なメッセージを取得")
    print("ストリーミングしながら、最後に usage や stop_reason も取得できます。\n")

    with client.messages.stream(
        model=MODEL,
        max_tokens=128,
        messages=[{"role": "user", "content": "Pythonの主な特徴を2つ挙げてください。"}],
    ) as stream:
        print("リアルタイム出力: ", end="", flush=True)
        for chunk in stream.text_stream:
            print(chunk, end="", flush=True)

        print("\n")
        msg = stream.get_final_message()

    print("get_final_message() で取得した情報:")
    print(f"  stop_reason  : {msg.stop_reason}")
    print(f"  input_tokens : {msg.usage.input_tokens}")
    print(f"  output_tokens: {msg.usage.output_tokens}")
    print(f"  model        : {msg.model}")


# ─────────────────────────────────────────────
# 練習問題
# ─────────────────────────────────────────────

def quiz():
    section("🏋️  練習問題")
    print("""
問題: 以下のストリーミングチャットボットを完成させてください。

  def streaming_chatbot():
      messages = []
      print("ストリーミングチャット開始 ('quit' で終了)")

      while True:
          user_input = input("You: ").strip()
          if user_input.lower() == "quit":
              break

          messages.append({"role": "user", "content": user_input})

          print("Claude: ", end="", flush=True)

          # ここにストリーミングコードを書く
          with client.messages.stream(
              model=MODEL,
              max_tokens=___,      # (1) 適切な値を設定
              messages=___,        # (2) messages を渡す
          ) as stream:
              full_text = []
              for chunk in ___:   # (3) text_stream を反復
                  print(chunk, end="", flush=True)
                  full_text.append(chunk)

          print()
          # (4) assistant の返答を messages に追加する
          messages.append(___)

  streaming_chatbot()

ヒント:
  (1) max_tokens=512 程度で十分です
  (2) 会話履歴をそのまま渡します
  (3) stream.text_stream を反復します
  (4) {"role": "assistant", "content": "".join(full_text)}
""")


# ─────────────────────────────────────────────
# メイン
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("第3章 演習5: レスポンスストリーミング")
    print("=" * 50)

    exercise_5_1()
    exercise_5_2()
    exercise_5_3()
    exercise_5_4()
    quiz()
