"""Auntie Trinity's Workbench: deterministic lost-acknowledgement lesson.

Standard library only. Synthetic ledger; no network or customer data.
"""
from __future__ import annotations
import json
from dataclasses import dataclass, field

@dataclass
class Ledger:
    entries: list[dict] = field(default_factory=list)
    seen: dict[str, str] = field(default_factory=dict)

    def commit(self, key: str, amount: int, *, guarded: bool) -> str:
        if guarded and key in self.seen:
            return self.seen[key]
        receipt = f"TX-{len(self.entries) + 1:03d}"
        self.entries.append({"receipt": receipt, "key": key, "amount": amount})
        if guarded:
            self.seen[key] = receipt
        return receipt

def run(guarded: bool) -> dict:
    ledger = Ledger()
    first = ledger.commit("refund-001", 25, guarded=guarded)
    # Simulated missing acknowledgement: caller never receives 'first'.
    retry = ledger.commit("refund-001", 25, guarded=guarded)
    count = len(ledger.entries)
    return {"guarded": guarded, "first_receipt": first,
            "retry_receipt": retry, "commits": count,
            "exactly_once": count == 1, "entries": ledger.entries}

if __name__ == "__main__":
    results = {"reference": run(True), "deliberately_broken": run(False)}
    print(json.dumps(results, indent=2))
    assert results["reference"]["exactly_once"], "Guarded case must not duplicate"
    assert not results["deliberately_broken"]["exactly_once"], "Mutation must be caught"
    print("PASS: safe retry demonstrated; deliberate duplicate detected.")
