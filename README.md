# 🤖 Autonomous AI Code Review System

> An AI-powered code review platform that automatically analyzes GitHub Pull Requests using static analysis tools and Large Language Models (LLMs) to generate intelligent, actionable review feedback.

---

## 📖 Overview

The **Autonomous AI Code Review System** is designed to automate the software code review process by combining traditional static analysis with modern Large Language Models.

Instead of only detecting security issues, the system understands Pull Requests, analyzes code changes, aggregates findings from multiple scanners, and produces human-readable code review reports.

The project follows **Clean Architecture** principles, making it modular, scalable, and easy to extend with additional scanners or AI models.

---

## ✨ Features

### ✅ Implemented

- GitHub Pull Request integration
- Pull Request metadata retrieval
- Changed file retrieval
- Repository cloning
- Automatic branch checkout
- Semgrep security scanning
- Bandit security scanning
- Finding aggregation
- Domain-driven architecture
- Clean Architecture
- Unit testing with Pytest

### 🚧 In Progress

- LLM-powered code review generation
- Prompt engineering
- AI review summarization
- Markdown review reports

### 📅 Planned

- GitHub Review API integration
- Inline review comments
- FastAPI REST API
- Docker deployment
- CI/CD integration
- Multi-agent review workflow

---

# 🏗 Architecture

```text
                 GitHub Pull Request
                         │
                         ▼
                GitHub API Service
                         │
                         ▼
                  Fetch PR Details
                         │
                         ▼
                Fetch Changed Files
                         │
                         ▼
                  Git Clone Service
                         │
                         ▼
                  Checkout PR Branch
                         │
                         ▼
                 Static Analysis Layer
              ┌─────────────────────────┐
              │        Semgrep          │
              │        Bandit           │
              └─────────────────────────┘
                         │
                         ▼
                 Aggregate Findings
                         │
                         ▼
                  Review Pipeline
                         │
                         ▼
            LLM Review Generation (WIP)
                         │
                         ▼
             GitHub Review Comments
```

---

# 📂 Project Structure

```text
backend/
│
├── app/
│   ├── api/
│   ├── application/
│   ├── core/
│   ├── domain/
│   └── infrastructure/
│
scripts/
tests/
```

---

# ⚙ Tech Stack

### Backend

- Python 3.10+
- FastAPI

### Source Control

- GitPython
- GitHub REST API

### Static Analysis

- Semgrep
- Bandit

### AI

- OpenAI-compatible API
- Qwen3-VL (GCP Deployment)

### Testing

- Pytest

---

# 🔄 Review Pipeline

```text
Pull Request

      │

      ▼

Fetch PR Metadata

      │

      ▼

Fetch Changed Files

      │

      ▼

Clone Repository

      │

      ▼

Checkout Branch

      │

      ▼

Run Semgrep

      │

      ▼

Run Bandit

      │

      ▼

Aggregate Findings

      │

      ▼

Generate AI Review (Coming Soon)

      │

      ▼

Publish GitHub Review (Coming Soon)
```

---

# ✅ Current Progress

| Component | Status |
|-----------|--------|
| Domain Layer | ✅ |
| Application Layer | ✅ |
| Infrastructure Layer | ✅ |
| GitHub API | ✅ |
| Git Clone | ✅ |
| Pull Request Retrieval | ✅ |
| Changed File Retrieval | ✅ |
| Semgrep Integration | ✅ |
| Bandit Integration | ✅ |
| Review Pipeline | ✅ |
| LLM Integration | 🚧 |
| AI Review Report | 🚧 |
| GitHub Review Comments | ⏳ |
| REST API | ⏳ |

---

# 🚀 Getting Started

Clone the repository

```bash
git clone https://github.com/Noman-ashraf1/auto-pr.git
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run tests

```bash
pytest
```

---

# 🧪 Development Scripts

Example scripts used during development:

```text
scripts/
├── test_github.py
├── test_github_files.py
├── test_git_clone.py
├── test_semgrep.py
├── test_bandit.py
├── test_review_pipeline.py
└── test_llm.py
```

---

# 🎯 Roadmap

- [x] Project initialization
- [x] Domain model
- [x] GitHub integration
- [x] Repository cloning
- [x] Semgrep integration
- [x] Bandit integration
- [x] Review pipeline
- [ ] LLM integration
- [ ] AI-powered review generation
- [ ] GitHub Review API
- [ ] FastAPI endpoints
- [ ] Docker deployment
- [ ] CI/CD pipeline
- [ ] Multi-agent review workflow

---

# 🤝 Contributing

Contributions, ideas, and suggestions are welcome. Feel free to open an issue or submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.


















