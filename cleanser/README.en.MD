# Jira + Azure DevOps + Confluence Cleaner 🧹

CLI tool for automatically cleaning up stale projects from:

- **Azure DevOps**
- **Jira Cloud**
- **Confluence Wiki**

## 🔧 Features

- **Dry-run mode** with mocked sessions and fake data
- Custom **exit codes** mapped from HTTP status
- API error handling via a **decorator** (`@handle_api_errors`)
- Safe deletion logic (skips protected/shared resources)
- Fully tested with `unittest` + `mock`

---

## 🔮 Usage Example

```bash
# Azure DevOps
python -m cleanser ado -t YOUR_TOKEN -o YOUR_ORG -d

# Jira Cloud
python -m cleanser jira -t YOUR_TOKEN -d

# Wiki (Confluence)
python -m cleanser wiki -u YOUR_EMAIL -t YOUR_API_TOKEN -d
```

## Exit Codes

| Code | Meaning                                         |
|------|-------------------------------------------------|
| 0    | "Success"                                       |
| 1    | "Unexpected error occurred"                     |
| 2    | "Invalid arguments or missing parameters"       |
| 10   | "Authorization failed (401/403)"                |
| 20   | "API not found or endpoint misconfigured (404)" |
| 29   | "Timeout or no response from API"               |
| 30   | "Rate limit reached (HTTP 429)"                 |
| 40   | "Protected resource (e.g. shared group)"        |
| 99   | "Dry-run completed successfully"                |

---

## 🌐 [Kliknij tutaj po polsku](README.pl.md)

