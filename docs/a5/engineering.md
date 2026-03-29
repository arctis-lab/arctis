# A5.2 — Bugs & Engineering

**Ziel:** Stabile Releases trotz laufender Pilots.

---

## Bugfix-Flow

1. **Eingang:** Support-Ticket, Sentry, interne Tests — priorisieren (P1–P3 analog [`sla_and_support.md`](../commercial/sla_and_support.md)).  
2. **Fix:** Branch/PR, Review, Tests (`pytest` / relevante Suites).  
3. **Kommunikation:** Kund:innen nur bei **wirksamen** Änderungen oder Sicherheitshinweisen — siehe [`release_notes.md`](../commercial/release_notes.md).

---

## Technische Schulden

- In Issues labeln (`tech-debt`); quartalsweise Kapazität einplanen — nicht alles in einen Release packen.
