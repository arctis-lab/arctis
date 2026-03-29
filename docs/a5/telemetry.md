# A5.1 — Telemetrie & Nutzung auswerten

**Ziel:** Aus **Sentry**, **Prometheus/Metriken** und ggf. **produktinternen Reports** lernen — ohne PII zu verletzen.

---

## Quellen

| Quelle | Typische Fragen |
|--------|-----------------|
| **Sentry** | Neue Hotspots, Regressionen nach Deploys |
| **Prometheus / Logs** | Latenz, 5xx, 429 — siehe [`Observability.md`](../Observability.md) |
| **API-/Tenant-Metriken** | Nutzung pro Tenant (intern, scope-beachtend) |

---

## Rhythmus

- **Wöchentlich** in der Pilotphase; **monatlich** im Regelbetrieb — oder nach Incident.  
- **Ergebnis:** kurzes internes Memo (Was haben wir geändert? Was ist Backlog?)

---

## Datenschutz

- Keine Roh-**Kundendaten** in öffentlichen Tickets; Aggregation und Anonymisierung bevorzugen.
