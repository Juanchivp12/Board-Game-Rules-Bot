# Board Game Rules Bot

Ask a board game rules question and get an answer straight from the rulebook, with a link to the section it came from.

Board game rulebooks are a pain to search mid-game. Root's is 50 pages of cross-referencing rules and finding one specific thing takes forever. So I'm building a bot you can just ask "can the Vagabond move into a clearing with no path?" and it pulls the answer from the actual rulebook instead of me flipping through it.

It uses RAG (retrieval-augmented generation). Basically, instead of letting an LLM answer from memory and risk making rules up, it looks up the relevant parts of the rulebook first and answers from those. Every answer shows which section it came from so you can check it.

I'm building this to learn how RAG actually works end to end, partly as prep for an AI engineering internship.

## What it does

- Ask questions in plain English
- Answers cite the rulebook section they came from
- Says "not in the rules" instead of guessing when it doesn't know
- Works with multiple games, you pick which one and it only searches that rulebook
- Simple chat UI

## How it works

Rulebooks get split into chunks, embedded, and stored in a vector database tagged by game. When you ask something, it grabs the closest-matching chunks for that game and hands them to the LLM to write a cited answer.

## Stack

- Python for the ingestion and retrieval
- An LLM API for the answers
- Chroma for the vector store
- FastAPI for the API
- Postgres for query history and metadata
- AWS to deploy it

## Status

Work in progress, building it in phases:

- [ ] Load a rulebook, chunk it, basic Q&A
- [ ] Embeddings + vector store
- [ ] Citations + "I don't know" guardrail
- [ ] Multiple games
- [ ] API, Postgres, UI, deploy

Started with Root since I know the game well enough to tell when an answer is wrong.

## Setup

Coming once there's something to run.
