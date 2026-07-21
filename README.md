# kaggle-ptcg-take

Local **data & engine workspace** for the Pokémon TCG AI Battle Challenge (Kaggle).
Agent/dev code lives in a separate repo: **sota1111/ptcg-agent-take**.

提出物の生成・検証・認証・Kaggle への提出は、共通の
[Kaggle 提出ガイド](https://github.com/sota1111/ptcg-agent-core/blob/main/docs/kaggle-submission.md)
を参照してください。

## ⚠️ Nothing under `data/` is committed
The cabt engine, card data (CSV), Card_ID PDFs and raw competition zips are
**competition-use-only (no redistribution)** and also exceed GitHub's 100MB file limit.
They are **gitignored** and must be re-downloaded locally.

## Repopulate `data/`
```bash
python3 -m venv venv && venv/bin/pip install kaggle
export KAGGLE_API_TOKEN=<token from https://www.kaggle.com/settings/api>   # or ~/.kaggle/access_token
venv/bin/kaggle competitions download -c pokemon-tcg-ai-battle            -p data/simulation
venv/bin/kaggle competitions download -c pokemon-tcg-ai-battle-challenge-strategy -p data/strategy
cd data/simulation && unzip -o pokemon-tcg-ai-battle.zip -d extracted
```

## Contents (local only, gitignored)
```
data/simulation/  pokemon-tcg-ai-battle.zip + extracted/ (ptcg_engine C++ src, sample_submission, card CSVs, PDFs)
data/strategy/    pokemon-tcg-ai-battle-challenge-strategy.zip + extracted/
eval/run_match.py local self-play match runner (tracked)
```
