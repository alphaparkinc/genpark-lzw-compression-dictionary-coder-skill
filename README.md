# genpark-lzw-compression-dictionary-coder-skill

[![GitHub Stars](https://img.shields.io/github/stars/alphaparkinc/genpark-lzw-compression-dictionary-coder-skill?style=social)](https://github.com/alphaparkinc/genpark-lzw-compression-dictionary-coder-skill)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Zero External Dependencies](https://img.shields.io/badge/dependencies-0%20(pure%20standard%20library)-brightgreen.svg)](client.py)
[![MCP Ready](https://img.shields.io/badge/MCP-Ready-purple.svg)](mcp_server.py)

> **Lempel-Ziv-Welch (LZW) dynamic dictionary lossless encoder and decoder**

Part of the **GenPark Autonomous Agent Matrix**, developed for production AI agents operating across local and distributed enterprise networks.

---

## 🏗️ Architecture

```mermaid
flowchart TD
    A[Raw Data Stream / Text] --> B[genpark-lzw-compression-dictionary-coder-skill]
    B --> C[Pure Python Standard Library Compression Engine]
    C --> D[Optimal Compact Bitstream / Token Sequence]
    B --> E[MCP Protocol Endpoint stdio]
    E --> F[Cursor / Claude Desktop / Windsurf Integration]
```

## 🚀 Quickstart

### Native Python Execution
```bash
python example_usage.py
```

### Standard Library Verification
```python
from client import *
```

### MCP Server (Claude Desktop / Cursor)
```json
{
  "mcpServers": {
    "genpark-lzw-compression-dictionary-coder-skill": {
      "command": "python",
      "args": ["-m", "genpark_lzw_compression_dictionary_coder_skill.mcp_server"]
    }
  }
}
```

## 📄 License
MIT License.
