"""
第3章 演習6 — 構造化データ
============================
学習目標:
  - アシスタント事前入力（prefill）の仕組みを理解する
  - stop_sequences で生成を制御する方法を習得する
  - 純粋な JSON / コード / CSV を Claude から取得する
  - output_config.format によるモダンな構造化出力を知る

実行方法:
  python 06_structured_data.py
"""

import json
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
# 演習 6-1: 事前入力なしの問題を確認する
# ─────────────────────────────────────────────

def exercise_6_1():
    section("演習 6-1: 事前入力なしだと余分なテキストが混入する")
    print("JSONを返すよう頼んでも、説明文や ```json``` が付いてくる場合があります。\n")

    response = client.messages.create(
        model=MODEL,
        max_tokens=256,
        messages=[{
            "role": "user",
            "content": "ユーザー情報をJSON形式で返してください。名前:田中、年齢:30、職業:エンジニア",
        }],
    )
    raw = response.content[0].text
    print("生の出力:")
    print(raw)
    print()

    # JSON として解析できるか試す
    try:
        # ```json ... ``` を除去してみる
        cleaned = raw.strip()
        if cleaned.startswith("```"):
            lines = cleaned.split("\n")
            cleaned = "\n".join(lines[1:-1])
        parsed = json.loads(cleaned)
        print(f"解析成功（手動クリーニングが必要でした）: {parsed}")
    except json.JSONDecodeError as e:
        print(f"解析失敗: {e}")
    print()
    print("→ 事前入力 + stop_sequences を使うとクリーンに取得できます。")


# ─────────────────────────────────────────────
# 演習 6-2: 事前入力 + stop_sequences でクリーンな JSON
# ─────────────────────────────────────────────

def get_clean_json(prompt: str) -> dict:
    """
    アシスタント事前入力と stop_sequences を組み合わせて
    純粋な JSON を取得する。
    """
    messages = [
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": "{"},  # ← 事前入力: JSON の開始を固定
    ]

    response = client.messages.create(
        model=MODEL,
        max_tokens=512,
        messages=messages,
        stop_sequences=["}"],  # ← 閉じ括弧で停止
    )

    # 事前入力の "{" と stop直前までのテキストを結合
    raw = "{" + response.content[0].text + "}"
    return json.loads(raw)


def exercise_6_2():
    section("演習 6-2: 事前入力 + stop_sequences でクリーンな JSON を取得")

    prompts = [
        "ユーザー情報をJSON形式のみで返してください。名前:田中太郎、年齢:28、職業:デザイナー",
        "商品情報をJSONのみで返してください。商品名:ノートPC、価格:89800、在庫:15",
    ]

    for prompt in prompts:
        print(f"プロンプト: {prompt[:50]}...")
        try:
            data = get_clean_json(prompt)
            print(f"  取得成功: {data}")
        except json.JSONDecodeError as e:
            print(f"  解析エラー: {e}")
        print()


# ─────────────────────────────────────────────
# 演習 6-3: コードブロックの取得
# ─────────────────────────────────────────────

def get_python_code(task: str) -> str:
    """
    ```python ... ``` ブロックを確実に取得する。
    事前入力で ```python を固定し、``` で停止する。
    """
    messages = [
        {"role": "user", "content": task},
        {"role": "assistant", "content": "```python\n"},  # ← コードブロック開始を固定
    ]

    response = client.messages.create(
        model=MODEL,
        max_tokens=512,
        messages=messages,
        stop_sequences=["```"],  # ← コードブロック終了で停止
    )

    return response.content[0].text.strip()


def exercise_6_3():
    section("演習 6-3: Pythonコードを確実に取得する")

    tasks = [
        "フィボナッチ数列の最初の10項を返す関数を書いてください。",
        "リストの重複要素を除去して返す関数を書いてください。",
    ]

    for task in tasks:
        print(f"タスク: {task}")
        code = get_python_code(task)
        print("取得したコード:")
        for line in code.split("\n"):
            print(f"  {line}")
        print()

        # 実際に実行してみる
        try:
            exec_globals: dict = {}
            exec(code, exec_globals)
            print("  ✓ コードは構文エラーなく実行できました")
        except SyntaxError as e:
            print(f"  ✗ 構文エラー: {e}")
        except Exception:
            print("  ✓ コードは構文エラーなし（実行時エラーは無視）")
        print()


# ─────────────────────────────────────────────
# 演習 6-4: CSVデータの取得
# ─────────────────────────────────────────────

def get_csv(prompt: str) -> str:
    messages = [
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": ""},
    ]

    response = client.messages.create(
        model=MODEL,
        max_tokens=512,
        messages=[{"role": "user", "content": prompt + "\nCSVのヘッダーと行のみを返してください。説明文は不要です。"}],
    )
    return response.content[0].text.strip()


def exercise_6_4():
    section("演習 6-4: CSV データを取得する")

    prompt = (
        "日本の主要都市トップ5の人口データをCSVで作成してください。"
        "列: 都市名, 都道府県, 人口（万人）"
    )
    print(f"プロンプト: {prompt}\n")
    csv_data = get_csv(prompt)
    print("取得したCSV:")
    for line in csv_data.split("\n")[:8]:  # 最大8行
        print(f"  {line}")


# ─────────────────────────────────────────────
# 演習 6-5: モダンな構造化出力（output_config）
# ─────────────────────────────────────────────

def exercise_6_5():
    section("演習 6-5: output_config.format によるモダンな構造化出力")
    print("Haiku 4.5 以降で利用可能な公式の構造化出力 API を使います。\n")

    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"},
            "skills": {
                "type": "array",
                "items": {"type": "string"},
            },
        },
        "required": ["name", "age", "skills"],
        "additionalProperties": False,
    }

    response = client.messages.create(
        model=MODEL,
        max_tokens=256,
        output_config={"format": {"type": "json_schema", "schema": schema}},
        messages=[{
            "role": "user",
            "content": "架空のソフトウェアエンジニアの情報を生成してください。",
        }],
    )

    raw = response.content[0].text
    print("生の出力:")
    print(f"  {raw}\n")

    data = json.loads(raw)
    print("解析結果:")
    print(f"  名前  : {data['name']}")
    print(f"  年齢  : {data['age']}")
    print(f"  スキル: {', '.join(data['skills'])}")
    print()
    print("→ output_config を使うとスキーマに準拠した JSON が保証されます。")
    print("  事前入力 + stop_sequences より確実で推奨される方法です。")


# ─────────────────────────────────────────────
# 練習問題
# ─────────────────────────────────────────────

def quiz():
    section("🏋️  練習問題")
    print("""
問題: 以下の関数を完成させてください。
      商品レビューを受け取り、構造化データとして返す関数です。

  def analyze_review(review_text: str) -> dict:
      \"\"\"
      レビューテキストを分析して以下のデータを返す:
        - sentiment: "positive" | "neutral" | "negative"
        - score: 1〜5の評価（整数）
        - keywords: キーワードのリスト（最大3つ）
        - summary: 一言要約
      \"\"\"
      schema = {
          "type": "object",
          "properties": {
              "sentiment": {"type": "string", "enum": ["positive", "neutral", "negative"]},
              "score": {"type": "integer"},
              "keywords": {"type": "array", "items": {"type": "string"}},
              "summary": {"type": "string"},
          },
          "required": ["sentiment", "score", "keywords", "summary"],
          "additionalProperties": False,
      }

      response = client.messages.create(
          model=MODEL,
          max_tokens=___,                    # (1) 適切な値
          output_config=___,                 # (2) schema を使った output_config
          messages=[{
              "role": "user",
              "content": f"以下のレビューを分析してください:\\n{review_text}",
          }],
      )

      return json.loads(response.content[0].text)


  # テスト
  result = analyze_review(
      "このヘッドフォンは音質が素晴らしくて大満足！"
      "ただし装着感が少し硬かったです。全体的には買ってよかったです。"
  )
  print(result)

ヒント:
  (1) max_tokens=256 程度で十分
  (2) {"format": {"type": "json_schema", "schema": schema}}
""")


# ─────────────────────────────────────────────
# メイン
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("第3章 演習6: 構造化データ")
    print("=" * 50)

    exercise_6_1()
    exercise_6_2()
    exercise_6_3()
    exercise_6_4()
    exercise_6_5()
    quiz()
