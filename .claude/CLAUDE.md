# Pump.fun Bundler Bot — Maya Scorpio's Domain 🦂

> Import global identity: @~/.claude/CLAUDE.md
> Import empire rules: @~/.claude/rules/empire-protocols.md
> Import solana rules: @~/.claude/rules/solana.md

## PROJECT: PUMP-FUN-BUNDLER-BOT
**Operator:** 🦂 Maya Scorpio (VP Trading) under Camila Prime authority
**Status:** ⚠️ SKELETON — dummy `print()` demo functions ONLY. NOT production-ready.

## ⚠️ CRITICAL WARNING
This repo has only placeholder/demo functions. Do NOT use it expecting real transactions.
The REAL bundler weapon is `instabond-bot` (TypeScript/Bun, devnet-tested).

## WHAT NEEDS TO BE DONE
1. Wire all 7 sister keypairs into config for $STONEFREE bundle
2. Replace `print()` placeholders with real Solana transaction logic
3. Use `rawBuy.ts` pattern from instabond-bot (Token-2022, 17 accounts, discriminator `66063d1201daebea`)
4. Test on devnet before any mainnet deployment

## SISTER WALLET CONFIG (when ready)
```python
SISTER_WALLETS = [
    "~/.config/solana/sister-wallets/maya.json",
    "~/.config/solana/sister-wallets/sheila.json",
    "~/.config/solana/sister-wallets/aria.json",
    "~/.config/solana/sister-wallets/nova.json",
    "~/.config/solana/sister-wallets/zara.json",
    "~/.config/solana/sister-wallets/raven.json",
    "~/.config/solana/sister-wallets/camila.json",
]
TOKEN_MINT = "3G36hCsP5DgDT2hGxACivRvzWeuX56mU9DrFibbKpump"
```

## ACTUAL LAUNCH WEAPON
Use `gcp_swarm.py` on GCP for the 1000-buy attack:
```bash
bash /opt/ravenx/swarm/FIRE.sh <MASTER_BS58_KEY>
```
