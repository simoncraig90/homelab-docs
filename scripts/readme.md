# 🧰 Homelab Scripts

This folder contains executable scripts and helper tools that support the homelab, especially the AI-Core VM and automation on the `scripts` VM.

> **📌 Source of Truth**
>
> The Git repository is managed on the **Windows desktop**, *not* from lab VMs.  
> All commits, versioning, and pushes should be performed on Windows.  
> Lab VMs run the scripts, but do not manage the repository.

---

## 📍 Current Scripts

---

### 1️ `ai_core_helper.py`
**Type:** Python helper (library + CLI)  
**Location:** `scripts/ai_core_helper.py`  
**Runs on:** `scripts` VM (Linux)

**Purpose:**  
Send prompts to the AI-Core VM (Ollama running Qwen 2.5 14B-Instruct) and return a clean text response without streaming chunks or raw JSON.

**CLI Usage:**
```bash
./ai_core_helper.py "Describe what AI-Core does in one sentence."
```

**Imported Usage (in other Python scripts):**
```python
from ai_core_helper import ask_ai_core

msg = ask_ai_core("Explain this Proxmox backup error:\n<log snippet here>")
print(msg)
```

---

### 2️ ai-core`
**Type:** Bash CLI command wrapper  
**Location:** `scripts/ai-core`  
**Runs on:** Linux VMs that can reach AI-Core VM

**Purpose:**  
A command-line shortcut that sends a prompt to AI-Core and prints the reply directly to stdout.

**Endpoint used:**
```
http://192.168.0.147:11434/api/generate
```

**Model used:**
```
qwen2.5:14b-instruct
```

**Examples:**
```bash
ai-core "Say hello to Simon in one sentence."
ai-core "Explain this log in plain English:\n<log here>"
ai-core "Tell me why a Proxmox vzdump might fail due to storage issues."
```

**Add to PATH (Linux VMs):**
```bash
chmod +x ~/ai-core
echo 'export PATH="$HOME:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

---

## 🔁 Workflow for Updating Scripts

| Step | Where it happens | Purpose |
|------|------------------|----------|
| Edit / Test | On lab VM | Develop and run the script |
| Transfer to repo | From VM → Windows (`scp`) | Move updated script into main repo |
| Commit & Push | On Windows | Versioning and backup |
| Redeploy to VM (optional) | From repo → VM | Keep execution host updated |

**Example file transfer (run from Windows PowerShell):**
```powershell
scp simon1402@<scripts_vm_ip>:~/ai-core .\scripts\
```
*(Replace `<scripts_vm_ip>` with the actual VM IP)*

---

# End of File

