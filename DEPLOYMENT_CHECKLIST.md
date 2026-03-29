# Deployment checklist

## Infrastructure (A1.1)

- [ ] `ENV=prod` (oder gleichwertiges produktionsnahes Verhalten für Staging, siehe [`docs/Deployment.md`](docs/Deployment.md))
- [ ] `DATABASE_URL` gesetzt (Postgres o. Ä.; nicht SQLite auf ephemeral Disk in Prod)
- [ ] `alembic upgrade head` gegen diese Datenbank ausgeführt (vor Live-Traffic)
- [ ] `ALLOWED_ORIGINS` auf echte Frontend-Origins (komma-separiert)
- [ ] `ARCTIS_AUDIT_STORE` gewählt (`jsonl` \| `db` \| `none`); bei `jsonl`: `ARCTIS_AUDIT_JSONL_DIR` beschreibbar und gemountet

## Secrets (A1.2)

Werte nur im **Secret Store** der Umgebung, nicht im Repo ([`docs/Deployment.md`](docs/Deployment.md) Abschnitt Secrets).

- [ ] `ARCTIS_ENCRYPTION_KEY` (Fernet-kompatibel)
- [ ] `CONTROL_PLANE_API_KEY` und `CONTROL_PLANE_URL` für Betrieb/Checks
- [ ] `SENTRY_DSN`
- [ ] `STRIPE_SECRET_KEY` und `STRIPE_WEBHOOK_SECRET` (oder **N/A** mit Begründung, wenn kein Billing; `launch_check` erwartet sie für ein volles Gate — siehe Deployment-Doku)
- [ ] `OPENAI_API_KEY` o. Ä. nur falls ihr globale Provider-Keys setzt (sonst Tenant-Keys in der DB)

## Weitere Punkte

- [ ] PROMETHEUS_ENABLED=true
- [ ] Billing-Webhooks in Stripe-Dashboard zur API-URL konfiguriert (wenn Billing aktiv)
- [ ] Auth0 callback URLs configured
- [ ] Alembic upgrade head applied (siehe A1.1, falls noch nicht abgehakt)
- [ ] Playwright smoke tests green
- [ ] Locust load test stable (<5% errors)
- [ ] DR test OK
- [ ] Statuspage updated
