"""
第3章 総合チャレンジ
====================
このファイルは第3章で学んだすべての概念を組み合わせた総合演習です。

カバーする概念:
  - API の基本操作 (演習1)
  - マルチターン会話管理 (演習2)
  - システムプロンプト (演習3)
  - Temperature の使い分け (演習4)
  - ストリーミング (演習5)
  - 構造化データ出力 (演習6)

実行方法:
  python 07_challenge.py
"""

import json
import time
from pathlib import Path
from dotenv import load_dotenv
import anthropic

load_dotenv(dotenv_path=Path(__file__).parent.parent.parent / ".env")

client = anthropic.Anthropic()
MODEL = "claude-haiku-4-5"


def section(title: str):
    print(f"\n{'═' * 55}")
    print(f"  {title}")
    print(f"{'═' * 55}")


def subsection(title: str):
    print(f"\n{'─' * 45}")
    print(f"  {title}")
    print(f"{'─' * 45}")


# ─────────────────────────────────────────────────────
# チャレンジ 1: ニュース記事アナライザー
# ─────────────────────────────────────────────────────
# 使用技術: output_config (演習6) + temperature=0.1 (演習4)

def challenge_1_news_analyzer():
    section("チャレンジ 1: ニュース記事アナライザー")
    print("記事テキストを受け取り、構造化データとして分析結果を返します。\n")

    schema = {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "category": {
                "type": "string",
                "enum": ["politics", "technology", "economy", "sports", "entertainment", "other"],
            },
            "sentiment": {
                "type": "string",
                "enum": ["positive", "neutral", "negative"],
            },
            "key_points": {
                "type": "array",
                "items": {"type": "string"},
                "maxItems": 3,
            },
            "credibility_score": {
                "type": "integer",
                "description": "1-10 の信頼性スコア",
            },
        },
        "required": ["title", "category", "sentiment", "key_points", "credibility_score"],
        "additionalProperties": False,
    }

    articles = [
        """
        東京・渋谷区に新たなスタートアップ支援施設「テックハブ渋谷」がオープンした。
        施設にはコワーキングスペース、メンタリングプログラム、資金調達支援が含まれる。
        初年度は50社のスタートアップ受け入れを目標としている。
        渋谷区長は「若い起業家たちの挑戦を全力でサポートする」とコメントした。
        """,
        """
        国内の物価上昇が続いており、食料品の価格が前年比8%上昇した。
        特にエネルギーコストの増加が家計を直撃しており、政府は緊急の支援策を検討中だ。
        専門家は「来年も厳しい状況が続く可能性が高い」と警告している。
        """,
    ]

    for i, article in enumerate(articles, 1):
        print(f"▶ 記事 {i}:")
        print(f"  {article.strip()[:80]}...\n")

        response = client.messages.create(
            model=MODEL,
            max_tokens=512,
            temperature=0.1,
            output_config={"format": {"type": "json_schema", "schema": schema}},
            messages=[{
                "role": "user",
                "content": f"以下のニュース記事を分析してください:\n\n{article.strip()}",
            }],
        )

        result = json.loads(response.content[0].text)
        print(f"  タイトル      : {result['title']}")
        print(f"  カテゴリ      : {result['category']}")
        print(f"  センチメント  : {result['sentiment']}")
        print(f"  信頼性スコア  : {result['credibility_score']}/10")
        print(f"  キーポイント  :")
        for point in result["key_points"]:
            print(f"    • {point}")
        print()


# ─────────────────────────────────────────────────────
# チャレンジ 2: 多段階コンテンツ生成パイプライン
# ─────────────────────────────────────────────────────
# 使用技術: マルチターン会話 (演習2) + システムプロンプト (演習3)
#           + temperature 使い分け (演習4) + ストリーミング (演習5)

def challenge_2_content_pipeline():
    section("チャレンジ 2: 多段階コンテンツ生成パイプライン")
    print("トピック → アウトライン → 本文 の3段階で記事を生成します。\n")

    topic = "リモートワークが生産性に与える影響"

    # ── ステップ 1: アウトライン生成（低温度＝構造的）──
    subsection("ステップ 1/3: アウトライン生成 (temperature=0.3)")
    print(f"トピック: {topic}\n")

    outline_schema = {
        "type": "object",
        "properties": {
            "sections": {
                "type": "array",
                "items": {"type": "string"},
            },
        },
        "required": ["sections"],
        "additionalProperties": False,
    }

    outline_response = client.messages.create(
        model=MODEL,
        max_tokens=256,
        temperature=0.3,
        output_config={"format": {"type": "json_schema", "schema": outline_schema}},
        messages=[{
            "role": "user",
            "content": f"「{topic}」というテーマのブログ記事のアウトライン（見出し4つ）を作成してください。",
        }],
    )

    outline = json.loads(outline_response.content[0].text)
    sections = outline["sections"]
    print("生成されたアウトライン:")
    for j, s in enumerate(sections, 1):
        print(f"  {j}. {s}")

    # ── ステップ 2: 各セクションの内容を会話で深掘り ──
    subsection("ステップ 2/3: セクション 1 の詳細化（マルチターン）")

    system_writer = (
        "あなたはプロのビジネスライターです。"
        "論理的で読みやすい文章を書き、具体的なデータや例を交えてください。"
        "各返答は3文以内に収めてください。"
    )

    messages: list[dict] = []

    def writer_chat(user_input: str) -> str:
        messages.append({"role": "user", "content": user_input})
        response = client.messages.create(
            model=MODEL,
            max_tokens=200,
            temperature=0.5,
            system=system_writer,
            messages=messages,
        )
        reply = response.content[0].text
        messages.append({"role": "assistant", "content": reply})
        return reply

    first_section = sections[0] if sections else "はじめに"
    print(f"セクション: 「{first_section}」\n")

    r1 = writer_chat(f"「{first_section}」セクションの核心となるメッセージを1文で表現してください。")
    print(f"Turn 1 — 核心メッセージ:\n  {r1}\n")

    r2 = writer_chat("そのメッセージを裏付ける統計や研究例を1つ挙げてください。")
    print(f"Turn 2 — 裏付け:\n  {r2}\n")

    r3 = writer_chat("読者へのアクションアイテムを1つ提案してください。")
    print(f"Turn 3 — アクションアイテム:\n  {r3}\n")

    print(f"  [会話履歴の長さ: {len(messages)} ターン | "
          f"入力トークン推移を確認するには 02_multi_turn.py 参照]")

    # ── ステップ 3: 導入文をストリーミング生成 ──
    subsection("ステップ 3/3: 導入文をストリーミング生成 (temperature=0.7)")

    intro_prompt = (
        f"ブログ記事「{topic}」の導入文を書いてください。"
        "読者の興味を引く書き出しで、80〜100字程度でまとめてください。"
    )

    print("ストリーミング出力:\n")
    print("  ", end="", flush=True)

    t0 = time.time()
    with client.messages.stream(
        model=MODEL,
        max_tokens=200,
        temperature=0.7,
        messages=[{"role": "user", "content": intro_prompt}],
    ) as stream:
        first = True
        for chunk in stream.text_stream:
            if first:
                print(f"[初回トークン: {time.time() - t0:.2f}秒] ", end="", flush=True)
                first = False
            print(chunk, end="", flush=True)

        final = stream.get_final_message()

    print(f"\n\n  [完了] 出力トークン: {final.usage.output_tokens}")


# ─────────────────────────────────────────────────────
# チャレンジ 3: インタラクティブ Q&A ボット（全技術統合）
# ─────────────────────────────────────────────────────
# 使用技術: 全演習の統合 — システムプロンプト + マルチターン
#           + ストリーミング + 構造化メタ情報収集

def challenge_3_qa_bot():
    section("チャレンジ 3: インタラクティブ Q&A ボット（デモモード）")
    print("5ターンの会話をシミュレートします。\n")
    print("システム: Python 学習サポートボット（streaming + 履歴管理）\n")

    system_qa = (
        "あなたは Python プログラミングの学習サポートボットです。"
        "質問には簡潔かつ正確に答えてください。"
        "コード例を示す際は必ず動作を1行コメントで説明してください。"
        "回答は日本語で、3文以内に収めてください。"
    )

    demo_questions = [
        "リストとタプルの違いを教えてください。",
        "それぞれどんな場面で使うのが適切ですか？",
        "辞書型はどう違いますか？",
        "辞書のキーにタプルは使えますか？",
        "これまでの説明を1文にまとめてください。",
    ]

    messages: list[dict] = []

    for i, question in enumerate(demo_questions, 1):
        print(f"[Turn {i}] You: {question}")
        print(f"         Claude: ", end="", flush=True)

        messages.append({"role": "user", "content": question})

        full_reply = []
        with client.messages.stream(
            model=MODEL,
            max_tokens=200,
            system=system_qa,
            messages=messages,
        ) as stream:
            for chunk in stream.text_stream:
                print(chunk, end="", flush=True)
                full_reply.append(chunk)

        print()
        messages.append({"role": "assistant", "content": "".join(full_reply)})
        print()

    print(f"総会話ターン数: {len(messages) // 2}")
    print(f"最終入力トークン数 (最後のリクエスト): "
          "※ stream.get_final_message().usage で確認できます")


# ─────────────────────────────────────────────────────
# 第3章 知識チェック
# ─────────────────────────────────────────────────────

def knowledge_check():
    section("第3章 知識チェック — 重要ポイントの確認")
    print("""
┌─────────────────────────────────────────────────────┐
│  確認項目                              理解度チェック │
├─────────────────────────────────────────────────────┤
│ 1. API の基本                                        │
│    □ messages リストの構造 (role / content)          │
│    □ stop_reason の意味 (end_turn / max_tokens)      │
│    □ content ブロックの安全な取り出し方              │
│                                                     │
│ 2. マルチターン会話                                   │
│    □ Claude はステートレス → 履歴を毎回送る          │
│    □ chat() ヘルパーパターン                         │
│    □ トークン蓄積とコストへの影響                     │
│                                                     │
│ 3. システムプロンプト                                 │
│    □ system パラメータ (None を渡さない)              │
│    □ ペルソナ / 制約 / フォーマット指定               │
│                                                     │
│ 4. Temperature                                      │
│    □ 0.0〜0.3: 確定的 (事実確認・コード生成)          │
│    □ 0.4〜0.7: バランス (要約・説明)                  │
│    □ 0.8〜1.0: 創造的 (創作・ブレスト)               │
│                                                     │
│ 5. ストリーミング                                     │
│    □ client.messages.stream() コンテキストマネージャ │
│    □ stream.text_stream で逐次表示                   │
│    □ stream.get_final_message() で使用量取得         │
│                                                     │
│ 6. 構造化データ                                      │
│    □ 事前入力 + stop_sequences（レガシー手法）        │
│    □ output_config.format (json_schema) が推奨       │
└─────────────────────────────────────────────────────┘
""")

    schema_challenge = {
        "type": "object",
        "properties": {
            "score": {"type": "integer"},
            "strengths": {"type": "array", "items": {"type": "string"}},
            "improvement_areas": {"type": "array", "items": {"type": "string"}},
            "next_steps": {"type": "string"},
        },
        "required": ["score", "strengths", "improvement_areas", "next_steps"],
        "additionalProperties": False,
    }

    print("自己評価レポートを自動生成中...\n")

    response = client.messages.create(
        model=MODEL,
        max_tokens=512,
        temperature=0.3,
        output_config={"format": {"type": "json_schema", "schema": schema_challenge}},
        messages=[{
            "role": "user",
            "content": (
                "Anthropic Claude API の第3章（基本API呼び出し、マルチターン会話、"
                "システムプロンプト、temperature、ストリーミング、構造化データ出力）を"
                "学習した初学者の自己評価レポートを生成してください。"
                "スコアは100点満点、強みと改善点はそれぞれ2つ挙げてください。"
            ),
        }],
    )

    report = json.loads(response.content[0].text)
    print(f"  学習スコア   : {report['score']}/100")
    print(f"  強み         :")
    for s in report["strengths"]:
        print(f"    ✓ {s}")
    print(f"  改善エリア   :")
    for a in report["improvement_areas"]:
        print(f"    △ {a}")
    print(f"  次のステップ : {report['next_steps']}")


# ─────────────────────────────────────────────────────
# メイン
# ─────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  第3章 総合チャレンジ")
    print("  Claude API — 全技術統合演習")
    print("=" * 55)

    challenge_1_news_analyzer()
    challenge_2_content_pipeline()
    challenge_3_qa_bot()
    knowledge_check()

    print("\n" + "=" * 55)
    print("  第3章 完了！お疲れ様でした。")
    print("=" * 55)
    print("""
次のステップ:
  • 第4章: ツール使用 (Tool Use / Function Calling)
  • 第5章: ビジョン (画像入力)
  • 第6章: 高度なプロンプト技術

練習問題を全部実装した方は以下を試してみてください:
  - 本格的なチャットボット UI の構築
  - FastAPI + Claude でバックエンド API 作成
  - LangGraph や CrewAI との組み合わせ
""")
