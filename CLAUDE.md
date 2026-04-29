# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

Markdown-based study materials for the Anthropic Academy course ["Building with the Claude API"](https://anthropic.skilljar.com/claude-with-the-anthropic-api). Each `.md` file contains the lesson page content plus English and Japanese video transcripts.

The only executable code lives in `03_Accessing_Claude_with_the_API/exercises/` (Python scripts for Chapter 3).

## Setup

Dependencies: Python 3.8+, `anthropic`, `python-dotenv`.

```bash
pip install anthropic python-dotenv
```

Create a `.env` file at the **project root** (not inside a chapter folder):

```
ANTHROPIC_API_KEY="sk-ant-..."
```

Verify the environment:

```bash
python 03_Accessing_Claude_with_the_API/exercises/00_setup.py
```

## Running Exercises (Chapter 3)

All scripts are self-contained and read `.env` from the project root automatically.

```bash
cd 03_Accessing_Claude_with_the_API/exercises
python 01_first_request.py    # 最初のAPIリクエスト
python 02_multi_turn.py       # マルチターン会話
python 03_system_prompts.py   # システムプロンプト
python 04_temperature.py      # Temperature
python 05_streaming.py        # レスポンスストリーミング
python 06_structured_data.py  # 構造化データ (output_config)
python 07_challenge.py        # 総合チャレンジ（全技術統合）
```

The exercises use `claude-haiku-4-5` to keep costs low.

## Repository Structure

```
NN_Chapter_Name/          # 章ごとのフォルダ（01〜13）
  NN_Lesson_name.md       # 🎬 動画レッスン = ページ本文 + EN/JA トランスクリプト
  NN_Quiz_name.md         # 📝 クイズ/テキスト = ページ本文のみ
03_Accessing_Claude_with_the_API/
  exercises/              # 唯一の実行可能コード（Python）
LEARNING_LOG.md           # 学習進捗・Q&Aの記録（学習者が手動更新）
README.md                 # 章ごとの目次
```

**Chapter map:**

| # | Topic |
|---|-------|
| 01–02 | Introduction & Claude models overview |
| 03 | API basics (messages, streaming, structured output) |
| 04 | Prompt evaluation (eval workflow, grading) |
| 05 | Prompt engineering (clear/direct, XML tags, examples) |
| 06 | Tool use (schemas, multi-turn loops, built-in tools) |
| 07 | RAG & Agentic Search (embeddings, BM25, multi-index) |
| 08 | Claude features (thinking, vision, PDF, caching, Files API) |
| 09 | Model Context Protocol (MCP server/client, resources, prompts) |
| 10 | Anthropic Apps (Claude Code) |
| 11 | Agents & workflows (parallelization, chaining, routing) |
| 12–13 | Final assessment & wrap-up |

## Notes for Teaching Sessions

- Always read the actual `.md` files before explaining a chapter's content — do not rely on prior context alone.
- Terminology follows the materials: use **one-shot / multi-shot** (not "few-shot").
- `LEARNING_LOG.md` records the learner's progress and Q&A history; update it when significant new understanding is reached.
- **Do not invent interpretations or anthropomorphic phrasing not present in the materials.** Phrases like "the app decides/judges/determines..." imply intelligent decision-making that the materials do not describe. State only what the materials actually say. If the source describes mechanical/fixed behavior (e.g. "the app sends ListToolsRequest"), do not paraphrase it as a judgment or decision. Distinguish clearly between (a) facts in the materials, (b) general programming knowledge, and (c) speculation — never blur them.
