# Release-Prozess (Arctis)

## Tag `v0.1.0` und G4

- **Tag-Schema:** `v` + Version aus `pyproject.toml`, z. B. **`v0.1.0`**.
- **`v0.1.0` erst setzen**, wenn der **Staging-E2E-Lauf (G4)** mindestens einmal **erfolgreich** durchgelaufen ist — siehe [`ghost_staging_e2e.md`](ghost_staging_e2e.md). Vorher keinen Release-Tag für diese Version auf `main`/`master` pushen, wenn ihr G4 als Gate nutzt.

## Versionierung

- **Schema:** [Semantic Versioning](https://semver.org/) — `MAJOR.MINOR.PATCH`.
- **Quelle der Wahrheit:** `[project] version` in [`pyproject.toml`](../pyproject.toml).
- **Vorab-Builds:** optional `0.2.0-dev1` / `.devN` nach Team-Konvention — im CHANGELOG im Abschnitt **[Unreleased]** sammeln, bis ein Release-Tag gesetzt wird.

## Git-Tag

- Empfehlung: Tag-Name **`v` + Version**, z. B. `v0.1.0` (entspricht der Version in `pyproject.toml`).
- Tag auf dem Commit, der exakt die veröffentlichte `pyproject.toml`-Version enthält.

## Ablauf (kurz)

1. Einträge aus **[Unreleased]** in [`CHANGELOG.md`](../CHANGELOG.md) unter eine neue Versionsüberschrift verschieben (Datum + Version).
2. `pyproject.toml`-Version anheben (falls noch nicht geschehen).
3. PR reviewen und mergen.
4. Nach erfolgreichem **G4** (falls als Gate vereinbart): Tag setzen — `git tag -a vX.Y.Z -m "Release X.Y.Z"` und pushen.
5. Release-Notes (GitHub/GitLab): Breaking Changes, API vs. Ghost-CLI, Sicherheitshinweise; optional Links zu [`arctis_ghost_demo_60.md`](arctis_ghost_demo_60.md) / Demo-Matrix.

## GitHub Actions (automatisch)

Nach **`git push origin vX.Y.Z`** (nach merge auf `main`/`master`):

| Workflow | Datei | Ergebnis |
|----------|--------|----------|
| **Release** | [`.github/workflows/release.yml`](../.github/workflows/release.yml) | GitHub **Release** mit **Wheel**, **sdist** (`.tar.gz`) und **`SHA256SUMS`** |
| **Docker** | [`.github/workflows/docker-publish.yml`](../.github/workflows/docker-publish.yml) | Image **`ghcr.io/<org>/<repo>:<version>`** und **`latest`** bei Tag-Push (kein `latest` bei Pre-Release-Tags mit `-` im Namen, z. B. `v1.0.0-rc.1`). **Manuell:** Actions → *Docker publish* → **Run workflow** (nutzt die Version aus `pyproject.toml`, kein `latest`). |

**Voraussetzung (Tag-Push):** Der Tag **`vX.Y.Z`** muss exakt zu **`[project].version`** in [`pyproject.toml`](../pyproject.toml) passen. Sonst schlagen **Release** und **Docker** (bei Tag-Trigger) mit einem Fehler ab.

**GHCR:** Erstes Push: unter **Packages** im Repo/Org ggf. Sichtbarkeit **public** setzen, damit `docker pull` ohne Login funktioniert.

## Migration zur Organisation arctis (GitHub)

**Reihenfolge (manuell in github.com; reversibel nur begrenzt — alte Org nicht automatisch löschen):**

| Schritt | Aktion |
|---------|--------|
| 1 | **Organisation erstellen:** Name `arctis`, Plan **Free**, du als **Owner** (oder Einladung annehmen). |
| 2 | **Repo prüfen:** Alle Branches/Tags/Releases vor Transfer dokumentieren; [Workflows](https://docs.github.com/en/actions/using-workflows/about-workflows) sind im Repo bereits YAML-valide. |
| 3 | **Secrets:** [Repository-Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository) werden beim **Transfer** ggf. **nicht** übernommen — nach dem Umzug unter **Settings → Secrets and variables → Actions** prüfen und fehlende Werte neu setzen. |
| 4 | **Transfer:** Repository **Settings → General → Danger zone → Transfer ownership** → Zielorganisation **`arctis`**, Repo-Name **`arctis`**. Nach Transfer: kanonische URL **`https://github.com/arctis/arctis`**. |
| 5 | **Lokal:** `git remote set-url origin https://github.com/arctis/arctis.git` und `git fetch origin`. |
| 6 | **GHCR:** Workflows pushen nach **`ghcr.io/arctis/arctis`** (aus `GITHUB_REPOSITORY`); kein Workflow-Patch nötig. **`workflow_dispatch`** bleibt aktiv. |
| 7 | **Packages:** **Packages** (rechts im Repo oder unter Org) → Container → **Package settings** → **Change visibility** → **Public** (für anonymes Pull). |
| 8 | **Test:** `docker pull ghcr.io/arctis/arctis:0.1.2` (nach erfolgreichem Release-Tag `v0.1.2`). |
| 9 | **Alte Organisation:** Nicht automatisch löschen; später manuell entscheiden (Redirects können bestehen bleiben). |

**Workflow-Berechtigungen:** Als Owner unter **Settings → Actions → General → Workflow permissions** ggf. **Read and write** aktivieren, damit Releases und Packages geschrieben werden.

## Ghost-CLI

- Neue Flags oder `ghost.yaml`-Felder: im CHANGELOG unter **Added**/**Changed** erwähnen; Verweis auf [`ghost_cli_reference.md`](ghost_cli_reference.md).
