# Arctis Ghost — Demo 60 (60-Sekunden-Kundenstory)

**Zweck:** Ein durchgängiger Ablauf, den du **live** oder **aufgezeichnet** zeigen kannst: von der Datei bis zum **Evidence-Bundle** und **Skill-Reports** — ohne Engine-Import, nur HTTP + Ordner.

## Arctis in 60 Sekunden (für Leser ohne Repo-Kontext)

| Frage | Kurzantwort |
|--------|-------------|
| **Was ist Arctis?** | Plattform für **Pipeline A** (IR, Engine, Control Plane) mit **FastAPI**; **Ghost** ist die CLI dazu — **HTTP-only**, keine zweite Policy im Client. |
| **Wer nutzt was?** | **Entwickler/Platform** integrieren die API; **Kunden/Field** starten mit **Ghost** im Ordner (`ghost.yaml`, Payload, `outgoing/…`). |
| **Wie startet der erste Run?** | Dieselbe **6‑Schritt-Sequenz** wie im README: [**Try Arctis in 30 seconds**](../README.md#try-arctis-in-30-seconds) — hier unten als **Storyboard (~60 s Erzählzeit)** ausformuliert; technisch identisch zu [`demo_60.md`](demo_60.md). |

**Einordnung:** Dieses Skript ist die **60-Sekunden-Baseline**; für **rollenbasierte** Landingpage-Module (C-Level, Security, Tech, …) siehe [arctis_ghost_demo_matrix.md](arctis_ghost_demo_matrix.md) — dort Story-Arc und welche Artefakte du pro Modul betonen solltest.

**Begleitdokumente:** Technischer Gesamtplan in [arctis_ghost_project_plan.md](arctis_ghost_project_plan.md); **Terminal‑Schrittfolge** (kommando‑genau, inkl. `init-demo` → `doctor` → … → `verify`) in [demo_60.md](demo_60.md) und Beispielauszug [assets/ghost_demo_flow_sample.txt](assets/ghost_demo_flow_sample.txt).

---

## 1. Was die Demo beweisen soll (eine Zeile)

> „Ich lege eine Geschäftsdatei in einen Ordner — Sekunden später habe ich **Ergebnis**, **Nachweis** und **erklärbare** KI-Entscheidungen — ohne neues UI-Projekt und ohne zweite Governance-Wahrheit.“

---

## 2. Voraussetzungen (vor dem Termin)

| Punkt | Minimum | Empfehlung |
|-------|---------|------------|
| API | Erreichbare Arctis-Basis-URL, gültiger API-Key, Scope `tenant_user` | Zusätzlich **Mock-Header** (`X-Arctis-Mock: true`) für deterministische Demos (serverseitig; Ghost-CLI sendet ihn **nicht** automatisch) |
| Ghost | Paket aus dem **Repo-Root**: `pip install -e .` → Kommando `ghost` / `python -m arctis_ghost` | `ghost doctor` zeigt **grün** |
| Demo-Ordner | Einmal `ghost init-demo` (legt `ghost.yaml`, `input.json`, `README.md` an) | Festes Verzeichnis auf dem Desktop des Presenters |
| Workflow | Im Tenant existiert ein Demo-`workflow_id` (UUID) | Optional: eigenes Rezept (`ghost run --recipe … --input …`) statt nur `input.json` |

**Skill-Envelope:** Wenn der Execute-Body ein **`skills`**-Array enthält, liefert **`GET /runs/{run_id}`** typischerweise **`execution_summary.skill_reports`** — sichtbar in **`ghost evidence`** und exportierbar mit **`ghost pull-artifacts`** (lokal: `outgoing/<run_id>/skill_reports/*.json`). Fehlen Daten (z. B. Skill liefert bewusst leere Payload), ist das **kein** Demo-Fehler.

---

## 3. Storyboard (ca. 60 Sekunden)

### 0:00–0:08 — Hook

- **Sagen:** „Die meisten Governance-Tools wollen ein neues Portal. Arctis Ghost braucht nur einen **Ordner** und eure bestehende API.“
- **Zeigen:** Explorer-Fenster: Demo-Ordner mit `ghost.yaml`, `input.json`; **`outgoing/`** vor `pull-artifacts` leer oder nach dem Lauf mit **`outgoing/<run_id>/`** (kanonisch laut [README](../README.md) / [ghost_quickstart.md](ghost_quickstart.md)) — nicht mit dem Repo-`input/` für Test-Tasks verwechseln.

### 0:08–0:18 — First-Run in einem Satz

- **Sagen:** „Erstinstallation: ein Befehl legt Config, Beispiel-Execute-JSON und eine **Kurzanleitung** an — minimale PLG-Schranke, kein Workshop.“
- **Zeigen:** `README.md` nach `ghost init-demo` (Schritte: `workflow_id` und API-Key setzen → `ghost doctor` → `ghost run` …; technische Folge: [demo_60.md](demo_60.md)).

### 0:18–0:35 — Der magische Moment

- **Tun:** Vor dem Run: **`ghost doctor`** (API erreichbar). Beispieldatei im Demo-Ordner: `input.json` aus **init-demo** **oder** eigene JSON-Datei / `ghost run --recipe … --input …` — **Hot-Folder-Watcher** ist **Roadmap**, nicht Teil der aktuellen CLI.
- **Sagen:** „Ghost baut den **API-Body** (optional aus **Rezept**), setzt **Idempotency-Key** — und Ihr seht Ergebnis + Nachweis über **Watch**, **Explain**/**Evidence** und **Artefakte auf Platte**.“
- **Zeigen:** Terminal: `ghost run input.json` **oder** `ghost run --recipe recipes/demo.yaml --input data.json`, dann `ghost watch <run_id>`.
- **Optional:** `ghost explain RUN_ID` — **Kurzfassung** aus dem Run-Objekt (kein vollständiges Evidence-JSON).

### 0:35–0:50 — Beweis & Differenzierung

- **Zeigen:** Customer Output bzw. Run-Objekt: `ghost evidence RUN_ID` oder `ghost fetch RUN_ID`.
- **Zeigen:** Lokales Bundle: `ghost pull-artifacts RUN_ID` → unter `outgoing_root` (Standard `outgoing/`) liegt **`outgoing/<run_id>/envelope.json`** plus **`skill_reports/*.json`** (wenn die API Reports liefert). Anschließend **`ghost verify RUN_ID`** — Abgleich lokales Envelope ↔ API (siehe [ghost_cli_reference.md](ghost_cli_reference.md) P12).
- **Zeigen:** Mindestens einen **Skill Report** in der Evidence-Ausgabe **oder** unter `skill_reports/` nach **pull-artifacts**.
- **Sagen:** „Das ist nicht nur Output — das ist **prüfbar**. Jeder Schritt hing an **Policy, Budget und Tenant** — nicht an einem Skript auf meinem Laptop.“

### 0:50–1:00 — Close & nächster Schritt

- **Sagen:** „Nächster Schritt bei euch: Profile in `ghost.yaml`, Rezepte pro Team, **`ghost run --dry-run`** für Tests — Roadmap: Hot-Folder-Ideen (`incoming/…` in älteren Plänen) sind **nicht** die aktuelle CLI; Kanonik: [ghost_quickstart.md](ghost_quickstart.md).“
- **Optional:** Link auf **Customer-Execute**-Doku / API — `ghost verify` setzt voraus, dass **`pull-artifacts`** zuvor gelaufen ist (lokales `envelope.json`).

**Zeitpuffer:** Wenn das Netz zickt, Mock einschalten und nur den **lokalen** outgoing-Tree zeigen — die Story bleibt gleich.

---

## 4. Checkliste: sichtbare Artefakte (Zielbild vs. aktueller CLI-Stand)

**Aktuell (Repo):** Nach `ghost pull-artifacts RUN_ID` typisch:

- [ ] `outgoing/<run_id>/envelope.json` (u. a. `run_id`, `skill_report_keys`, Zeitstempel)
- [ ] `outgoing/<run_id>/skill_reports/<skill_id>.json` — wenn `execution_summary.skill_reports` gesetzt ist
- [ ] Optional: `routing.json`, `cost.json` im gleichen Run-Ordner
- [ ] Nach Pull: `ghost verify RUN_ID` → **`envelope verify: OK`** (Voraussetzung: `pull-artifacts` hat `envelope.json` geschrieben)

**Zielbild (Roadmap / spätere Writer-Erweiterung):** u. a. `summary.txt`, `result.json`, `outgoing/errors/`, feste `incoming/`-Konvention — siehe [arctis_ghost_project_plan.md](arctis_ghost_project_plan.md) §6.5.

- [ ] Terminal: kein unerklärter Crash; HTTP-Fehler von `ghost` sind farbig gemeldet

---

## 5. Einwände — kurze Antworten

| Einwand | Antwort |
|---------|---------|
| „Ist das sicher?“ | Alles Laufende geht über **eure** API mit **Scopes** und **Evidence** — Ghost ist ein dünner Client, keine zweite Policy. |
| „Was ist mit PII?“ | **Sandbox/Mock** für Tests; sensible Erweiterungen (lokale Redaktion) als **Ghost-Plugin** oder separates Gateway — siehe Projektplan Horizont H3. |
| „Wir haben schon RPA.“ | Ghost ersetzt RPA nicht — er **standardisiert** den Weg zu **einer** Governance-API und macht Outputs **auditierbar**. |

---

## 6. Nach der Demo (Follow-up)

- Terminal-Schritte (kommando-genau): [demo_60.md](demo_60.md).
- Skill-/Evidence-Referenz: [demo_matrix.md](demo_matrix.md); Landingpage-Module: [arctis_ghost_demo_matrix.md](arctis_ghost_demo_matrix.md).
- Technischer Deep-Dive: [arctis_ghost_project_plan.md](arctis_ghost_project_plan.md) §3 (Skills), §6 (Ghost-Paket), §15 (Erlebnis-Schicht).
- Rollout im Team: [arctis_rollout_anleitung_jetzt_bis_produkt.md](arctis_rollout_anleitung_jetzt_bis_produkt.md) §13.

---

*Revision: Storyboard für Live- und Video-Demos; an API-First und „kein Engine-Import“ gebunden.*
