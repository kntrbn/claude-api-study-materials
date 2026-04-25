"""
第3章 演習 - セットアップ確認
==============================
このファイルを最初に実行して、環境が正しく構築されているか確認します。

実行方法:
  python 00_setup.py
"""

import sys


def check_python_version():
    version = sys.version_info
    ok = version >= (3, 8)
    print(f"  Python {version.major}.{version.minor}: {'✓' if ok else '✗ (3.8+ が必要)'}")
    return ok


def check_anthropic():
    try:
        import anthropic
        print(f"  anthropic SDK: ✓ (version {anthropic.__version__})")
        return True
    except ImportError:
        print("  anthropic SDK: ✗ (未インストール)")
        print("    → pip install anthropic")
        return False


def check_dotenv():
    try:
        import dotenv
        print(f"  python-dotenv: ✓")
        return True
    except ImportError:
        print("  python-dotenv: ✗ (未インストール)")
        print("    → pip install python-dotenv")
        return False


def check_api_key():
    import os
    from pathlib import Path

    # .env ファイルの確認
    env_path = Path(__file__).parent.parent.parent / ".env"
    if env_path.exists():
        print(f"  .env ファイル: ✓ ({env_path})")
    else:
        print(f"  .env ファイル: ! (未作成 — 後述の手順で作成してください)")

    # APIキーの確認（値は表示しない）
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if key:
        masked = key[:8] + "..." + key[-4:] if len(key) > 12 else "***"
        print(f"  ANTHROPIC_API_KEY: ✓ ({masked})")
        return True
    else:
        print("  ANTHROPIC_API_KEY: ✗ (環境変数が見つかりません)")
        print("    → .env ファイルに ANTHROPIC_API_KEY=\"sk-ant-...\" を追加")
        return False


def test_api_connection():
    import anthropic

    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=32,
        messages=[{"role": "user", "content": "Say 'OK' only."}],
    )
    text = response.content[0].text.strip()
    print(f"  API疎通確認: ✓ (応答: {text!r})")
    return True


def main():
    print("=" * 50)
    print("第3章 セットアップ確認")
    print("=" * 50)

    results = []

    print("\n[依存パッケージ]")
    results.append(check_python_version())
    results.append(check_anthropic())
    results.append(check_dotenv())

    if not all(results):
        print("\n✗ パッケージをインストールしてから再実行してください。")
        print("  pip install anthropic python-dotenv")
        return

    print("\n[API キー]")
    # .env があればロード
    try:
        from dotenv import load_dotenv
        load_dotenv(dotenv_path=Path(__file__).parent.parent.parent / ".env")
    except Exception:
        pass
    key_ok = check_api_key()

    if not key_ok:
        print("\n✗ APIキーを設定してから再実行してください。")
        print("  1. https://console.anthropic.com/ でキーを発行")
        print("  2. プロジェクトルートに .env を作成")
        print("  3. ANTHROPIC_API_KEY=\"sk-ant-...\" を記述")
        return

    print("\n[API 疎通確認]")
    try:
        test_api_connection()
    except Exception as e:
        print(f"  API疎通確認: ✗ ({e})")
        print("  → APIキーが正しいか確認してください。")
        return

    print("\n" + "=" * 50)
    print("✓ セットアップ完了！演習を開始できます。")
    print("=" * 50)
    print("\n演習ファイル一覧:")
    print("  01_first_request.py    — 最初のリクエスト")
    print("  02_multi_turn.py       — マルチターン会話")
    print("  03_system_prompts.py   — システムプロンプト")
    print("  04_temperature.py      — Temperature")
    print("  05_streaming.py        — レスポンスストリーミング")
    print("  06_structured_data.py  — 構造化データ")
    print("  07_challenge.py        — 総合チャレンジ")


if __name__ == "__main__":
    from pathlib import Path
    main()
