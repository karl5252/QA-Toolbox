# Jira + Azure DevOps + Confluence Cleaner 🧹

CLI narzędzie do automatycznego czyszczenia zbędnych projektów z:

- **Azure DevOps**
- **Jira Cloud**
- **Confluence Wiki**

### 🔧 Funkcje

- Tryb **dry-run** (mockowany session + dane)
- Obsługa **statusów HTTP** z własnymi kodami wyjścia
- Obsługa błędów API przez dekorator (`@handle_api_errors`)
- Bezpieczne usuwanie (pomija zasoby współdzielone)
- Pokrycie testami `unittest` + `mock`

---

### 🧪 Przykład użycia

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
