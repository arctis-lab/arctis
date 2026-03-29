# A4.1 — Tenant-Setup

Checkliste für **Betrieb** vor dem ersten produktiven Pilot-Lauf. Technische Details: [`Authentication.md`](../Authentication.md), [`Deployment.md`](../Deployment.md).

---

## 1. Tenant anlegen

- In der **Kontroll-Datenbank** einen **Tenant**-Datensatz anlegen (siehe Modelle unter `arctis/db/` — konkrete Schritte: Admin-Tool, Seed-Skript oder SQL nach internem Runbook).  
- **Tenant-ID** notieren und dem Kunden nur über **sichere Kanäle** mitteilen, falls benötigt.

---

## 2. API-Key generieren

- Neuen **API-Key** für diesen Tenant erzeugen, **hashed** in `api_keys` speichern, **Klartext-Key einmalig** an autorisierte Kontakte übergeben (nicht per unsicherer Chat).  
- **Scopes** setzen (`tenant_user`, ggf. `tenant_admin` für Metriken/Evidence-Routen) — siehe [`security_production.md`](../security_production.md).

---

## 3. Limits setzen (Bezug A3.1)

- **Rate-Limits** und Budgetfelder gemäß Vertrag bzw. [`pricing_and_limits.md`](../commercial/pricing_and_limits.md) in den entsprechenden DB-Strukturen pflegen (`tenant_rate_limits`, `api_key_rate_limits`, Budget-Kontext).  
- Abweichungen dokumentieren (intern).

---

## 4. Audit-Store-Pfad prüfen

- `ARCTIS_AUDIT_STORE` (`jsonl` \| `db` \| `none`) und bei **`jsonl`** das Verzeichnis `ARCTIS_AUDIT_JSONL_DIR`: beschreibbar, gemountet, Backup eingeplant — siehe [`Deployment.md`](../Deployment.md), [`DR.md`](../DR.md).
