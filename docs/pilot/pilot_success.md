# A4.5 — Pilot-Success-Kriterien

Damit der Pilot **bewertbar** endet — **vor** Pilotstart mit dem Kunden abstimmen.

---

## Messbare Kriterien

| Metrik | Beispiel | Messung |
|--------|----------|---------|
| **Erfolgsrate Runs** | ≥ 95 % erfolgreiche Executes in Woche 2 | API-Logs / Metriken |
| **Support-Tickets** | ≤ N Tickets pro Woche | Ticketing |
| **Latenz** | p95 unter vereinbartem Schwellenwert | [`Observability.md`](../Observability.md) / Prometheus |
| **Evidence** | Audit kann Nachweise exportieren | Manueller Check |

Platzhalter durch **eure** Ziele ersetzen.

---

## Zeitrahmen

- **Pilot-Dauer:** z. B. 4–8 Wochen  
- **Review-Termine:** z. B. Woche 2 Midpoint, Woche 4 Abschluss  
- **Go/No-Go:** Definition, was „Production Rollout“ bedeutet

---

## Feedback-Mechanismus

- **Quelle:** strukturiertes Interview, Umfrage (NPS optional), oder wöchentlicher Sync  
- **Inhalt:** Was blockiert? Was fehlt in der Doku?  
- **Intern:** Ergebnisse in Produkt-Backlog / Issues spiegeln; **keine** Kundennamen in öffentlichen Issues ohne Zustimmung

---

## Verknüpfung

- Scope-Vorgaben: [`pilot_scope.md`](pilot_scope.md)  
- Commercial Gate: [`../commercial/COMMERCIAL_CHECKLIST.md`](../commercial/COMMERCIAL_CHECKLIST.md)  
- Nach dem Pilot: [`../a5/README.md`](../a5/README.md) (Phase **A5** — Telemetrie, Roadmap 1.1.0, Feedback)
