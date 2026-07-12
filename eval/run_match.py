"""Minimal local self-play match runner for the PTCG AI Battle eval environment.
Proves the cabt engine can run a full agent-vs-agent match locally on Linux.
Usage: python run_match.py <sample_submission_dir> [deck0.csv] [deck1.csv]
"""
import sys, os, random, importlib.util

SAMPLE = sys.argv[1]
sys.path.insert(0, SAMPLE)                     # make `cg` importable
os.chdir(SAMPLE)                               # so deck.csv & libcg.so resolve

from cg import game                            # battle_start/select/finish
from cg.api import to_observation_class

def load_deck(path):
    with open(path) as f:
        return [int(x) for x in f.read().split("\n")[:60]]

def random_agent(obs_dict):
    obs = to_observation_class(obs_dict)
    if obs.select is None:            # deck-selection phase
        return None                   # handled by runner
    n = len(obs.select.option)
    k = obs.select.maxCount
    lo = obs.select.minCount
    k = max(lo, min(k, n))
    return random.sample(range(n), k) if n else []

def run(deck0, deck1, max_steps=100000):
    obs, start = game.battle_start(deck0, deck1)
    if obs is None:
        raise RuntimeError(f"BattleStart failed: errorPlayer={start.errorPlayer} errorType={start.errorType}")
    steps = 0
    while steps < max_steps:
        cur = obs.get("current")
        if cur and cur.get("result", -1) != -1:
            return cur["result"], steps
        sel = random_agent(obs)
        obs = game.battle_select(sel)
        steps += 1
    return -1, steps  # unfinished

if __name__ == "__main__":
    random.seed(42)
    d0 = load_deck(sys.argv[2]) if len(sys.argv) > 2 else load_deck("deck.csv")
    d1 = load_deck(sys.argv[3]) if len(sys.argv) > 3 else d0
    result, steps = run(d0, d1)
    game.battle_finish()
    print(f"MATCH DONE: winner=player{result}  decisions={steps}")
