# A4.4 — Pilot-Checklist

Vor „Pilot live“ und nach erstem produktivem Tag abhaken.

---

## Technisch

- [ ] **Tenant aktiv** — Datensatz und Keys konsistent
- [ ] **API-Key getestet** — `GET /pipelines` oder Minimal-Smoke mit `X-API-Key`
- [ ] **First Request erfolgreich** — mindestens ein Execute oder dokumentierter Test-Run **200** / erfolgreicher Abschluss
- [ ] **Evidence-Bundle erzeugt** — Run-ID vorhanden; `ghost pull-artifacts` / API-Evidence wie im Pilot-Scope vereinbart

## Betrieb

- [ ] **Statuspage erreichbar** — aus Kundensicht (siehe [`sla_and_support.md`](../commercial/sla_and_support.md))
- [ ] **Support-Flow bestätigt** — Test-Ticket oder Probelauf der Inbox; Antwortzeit-Erwartung kommuniziert

---

Nach Abschluss: Ergebnis in [`pilot_success.md`](pilot_success.md) und Retro-Termin.
