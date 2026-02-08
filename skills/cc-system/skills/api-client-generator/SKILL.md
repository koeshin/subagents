---
name: api-client-generator
description: Generates Python or TypeScript API clients from a base URL or JSON schema. Use when the user needs to interact with an external API and needs a wrapper class.
tools: write_to_file, read_file
---

# API Client Generator

Generates type-safe API clients for external services.

## Usage

1. **Provide Context**: The user should provide the Base URL and endpoints (or a JSON schema).
2. **Select Language**: Python (`requests`) or TypeScript (`fetch`/`axios`).
3. **Generate**: The skill uses the assets to scaffold the client.

## Components

### Python Client
Located at `assets/python_client.py`.
Features:
- `requests` session management.
- Type hints.
- Exception handling.
- Environment variable configuration for keys.

### TypeScript Client
(Planned) Located at `assets/ts_client.ts`.

## Example

**User**: "Create a Python client for https://api.example.com"
**Agent Action**:
1. Read `assets/python_client.py`
2. Customize `BASE_URL` and add methods for known endpoints.
3. Write to `api_client.py`
