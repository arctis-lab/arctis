# Beispiele — Customer-Execute (Ghost)

## `customer_execute_body.json`

Minimaler **Execute-Body** für `POST /customer/workflows/{workflow_id}/execute` — dieselbe Struktur wie die von **`ghost init-demo`** erzeugte Datei `input.json` (siehe [`arctis_ghost/init_demo.py`](../../arctis_ghost/init_demo.py)).

**Verwendung mit der CLI:**

```bash
ghost run customer_execute_body.json
# oder die Datei nach body.json kopieren / umbenennen:
ghost run body.json
```

Voraussetzungen: `ghost.yaml` mit gültiger `workflow_id`, erreichbare API, `ARCTIS_API_KEY` — siehe [`ghost_cli_reference.md`](../ghost_cli_reference.md).

**Kern-Story (Run → Artefakte → Prüfung):** [`ghost_quickstart.md`](../ghost_quickstart.md#customer-execute-von-null-bis-verify).
