# Observability (A1.4)

Überblick über **Sentry**, **Prometheus** (Text-Export in der API), **Grafana** (außerhalb des Repos) und **Alerts** — abgestimmt auf [`DEPLOYMENT_CHECKLIST.md`](../DEPLOYMENT_CHECKLIST.md).

---

## 1. Sentry (Fehler & Traces)

| Thema | Details |
|--------|---------|
| Variable | `SENTRY_DSN` — wie ein Secret behandeln ([`Deployment.md`](Deployment.md) A1.2). |
| Aktivierung | Gesetzt in [`arctis/app.py`](../arctis/app.py): `sentry_sdk.init` mit `FastApiIntegration`, `environment=ENV`. |
| Datenschutz | `before_send` entfernt Cookies und redigiert `x-api-key`, `authorization`, `cookie` in Request-Headern. |
| Alerts | In der **Sentry-UI** (Issue-Alerts, Performance) konfigurieren — nicht im Repo versionieren. |

---

## 2. Prometheus (Metrik-Export)

| Thema | Details |
|--------|---------|
| Endpunkt | **`GET /metrics/prometheus`** — `text/plain` im OpenMetrics-Format ([`metrics.py`](../arctis/api/routes/metrics.py)). |
| **Authentifizierung** | **`X-API-Key`** mit Scope **`tenant_admin`** oder **`system_admin`** (`@RequireScopes`). Es gibt **keinen** öffentlichen unauthentifizierten `/metrics`-Scrape in der Standard-App. |
| Inhalt | u. a. Request-Latenz und Fehlerklassen aus [`RequestMetricsMiddleware`](../arctis/api/middleware.py) und weitere Counters/Histogramme unter [`arctis/observability/metrics.py`](../arctis/observability/metrics.py). |

### Scraping betreiben

- **Empfehlung:** Dedizierter API-Key mit `tenant_admin` oder `system_admin`, nur für Monitoring; Wert im Secret Store; Prometheus **scrape_config** mit Header `X-API-Key: <key>` (oder Sidecar/Reverse-Proxy, der den Header setzt).
- **Grafana:** Wird **nicht** mit Arctis ausgeliefert — verbindet ihr mit eurer Prometheus-Instanz und baut Dashboards (Latenz, 4xx/5xx, Ratenlimits) selbst.

> Hinweis: Die Umgebungsvariable **`PROMETHEUS_ENABLED`** erscheint in älteren Notizen, ist aber **kein** Schalter in `arctis.config` — Steuerung erfolgt über den Endpunkt und API-Key wie oben.

---

## 3. Zusätzliche JSON-Metriken (nicht Prometheus-Text)

Unter Präfix `/metrics` (gleiche Auth wie üblich):

- `GET /metrics/review_sla`, `GET /metrics/reviewer_load` — Review-SLA-/Lastkennzahlen (JSON), siehe [`metrics.py`](../arctis/api/routes/metrics.py).

---

## 4. Alerts (Betrieb)

| Quelle | Idee |
|--------|------|
| **Sentry** | Neue Issues, Regressionen, Spike in Fehlerquote. |
| **Prometheus/Alertmanager** | z. B. hohe 5xx-Rate, erhöhte Latenz auf normalisierten Routen, 429-Spitzen — siehe auch [security_production.md](security_production.md) (Rate-Limits). |
| **Logs** | Strukturierte App-Logs (`INFO` in Prod); keine Roh-API-Keys loggen. |

Konkrete Schwellenwerte hängen von SLA und Traffic ab und gehören in euer Runbook, nicht als feste Werte ins Repo.

---

## 5. Weiterlesen

- [security_production.md](security_production.md) — CORS, Rate-Limits, Budget-Hinweise  
- [Deployment.md](Deployment.md) — Secrets, Infrastruktur  
- [DR.md](DR.md) — Verfügbarkeit, Backups  
