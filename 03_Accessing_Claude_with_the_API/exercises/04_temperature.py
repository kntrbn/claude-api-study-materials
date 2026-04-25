"""
第3章 演習4 — Temperature
============================
学習目標:
  - temperature パラメータの役割を理解する
  - 低温度（確定的）と高温度（創造的）の違いを体感する
  - タスクタイプと推奨温度の関係を学ぶ

実行方法:
  python 04_temperature.py
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


def ask(prompt: str, temperature: float, max_tokens: int = 128, system: str | None = None) -> str:
    params: dict = {
        "model": MODEL,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": [{"role": "user", "content": prompt}],
    }
    if system:
        params["system"] = system
    response = client.messages.create(**params)
    return response.content[0].text


# ─────────────────────────────────────────────
# 演習 4-1: 同じ質問を異なる温度で3回ずつ聞く
# ─────────────────────────────────────────────

def exercise_4_1():
    section("演習 4-1: 温度の違いを体感する")
    print("同じ質問を temperature=0.0 と temperature=1.0 で3回ずつ聞きます。\n")

    prompt = "創造的な会社名を1つ考えてください。名前だけ答えてください。"

    for temp in [0.0, 1.0]:
        label = "低温度（確定的）" if temp == 0.0 else "高温度（創造的）"
        print(f"▶ temperature={temp} — {label}")
        results = [ask(prompt, temperature=temp) for _ in range(3)]
        for i, r in enumerate(results, 1):
            print(f"  [{i}] {r.strip()}")
        unique = len(set(r.strip().lower() for r in results))
        print(f"  → ユニーク数: {unique}/3\n")

    print("観察: 低温度では同じ（または似た）答えが繰り返されやすく、")
    print("      高温度では毎回異なる答えが出やすくなります。")


# ─────────────────────────────────────────────
# 演習 4-2: タスクに合った温度の選択
# ─────────────────────────────────────────────

def exercise_4_2():
    section("演習 4-2: タスクと温度の対応")

    tasks = [
        {
            "name": "事実確認（低温度推奨）",
            "prompt": "日本の人口はおよそ何人ですか？数字だけ答えてください。",
            "temp": 0.1,
            "reason": "事実には正確さが必要。創造性は不要。",
        },
        {
            "name": "コード生成（低温度推奨）",
            "prompt": "Python でリストの要素を逆順にする1行コードを書いてください。",
            "temp": 0.2,
            "reason": "正解が決まっているタスクは低温度が安定。",
        },
        {
            "name": "俳句作成（高温度推奨）",
            "prompt": "春をテーマにした俳句を1つ作ってください。",
            "temp": 0.9,
            "reason": "創作には多様性・独創性が欲しい。",
        },
        {
            "name": "ブレインストーミング（高温度推奨）",
            "prompt": "スマートフォンアプリのアイデアを1つ提案してください。アイデア名と一言説明のみ。",
            "temp": 0.8,
            "reason": "多様なアイデアを出したい場合は高温度。",
        },
    ]

    for task in tasks:
        reply = ask(task["prompt"], temperature=task["temp"])
        print(f"▶ {task['name']} (temp={task['temp']})")
        print(f"  質問: {task['prompt']}")
        print(f"  返答: {reply.strip()[:100]}")
        print(f"  理由: {task['reason']}\n")


# ─────────────────────────────────────────────
# 演習 4-3: temperature の推奨範囲早見表
# ─────────────────────────────────────────────

def exercise_4_3():
    section("演習 4-3: 推奨温度の早見表")
    print("""
  ┌────────────────┬─────────────┬────────────────────────────────┐
  │ temperature    │ 特性        │ 向いているタスク                │
  ├────────────────┼─────────────┼────────────────────────────────┤
  │ 0.0 〜 0.3     │ 確定的・正確│ 事実確認・コード生成・データ抽出│
  │ 0.4 〜 0.7     │ バランス    │ 要約・教育コンテンツ・問題解決  │
  │ 0.8 〜 1.0     │ 創造的・多様│ 創作・ブレインストーミング・詩  │
  └────────────────┴─────────────┴────────────────────────────────┘

  重要: temperature は確率分布を変えるだけで「保証」はしません。
        低温度でも時々違う答えが出ることがあります。
""")


# ─────────────────────────────────────────────
# 練習問題
# ─────────────────────────────────────────────

def quiz():
    section("🏋️  練習問題")
    print("""
問題: 以下の2つのタスクに適切な temperature を設定し、
      出力の違いを確認してください。

  タスクA（適切な温度は？）:
    prompt = "10 + 25 * 3 の答えを数字だけで教えてください。"
    → temperature = ___  # あなたの答えを入れる

  タスクB（適切な温度は？）:
    prompt = "秋の夜長をテーマにした短い詩を作ってください。"
    → temperature = ___  # あなたの答えを入れる

  それぞれ3回実行して出力のバリエーションを観察しましょう。
  タスクAは毎回同じになりますか？タスクBはどうでしょう？

  ヒント: 上の早見表を参考にしてください。
""")


# ─────────────────────────────────────────────
# メイン
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("第3章 演習4: Temperature")
    print("=" * 50)

    exercise_4_1()
    exercise_4_2()
    exercise_4_3()
    quiz()
