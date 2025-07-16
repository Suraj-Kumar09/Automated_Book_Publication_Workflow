# 📚 Automated Book Publication Workflow

An end-to-end AI-powered pipeline to scrape online book chapters, rewrite ("spin") them using LLMs, perform iterative human + AI review cycles, and manage agentic coordination with semantic search, versioning, and voice control.

---

## 🚀 Features

### ✅ Core Capabilities
- 🔍 **Scraping & Screenshots** from URLs (Wikisource) using Playwright
- ✍️ **AI Writing & Review** using LLMs for spinning and refining chapters
- 🧑‍💻 **Human-in-the-loop Interface** for Writer → Reviewer → Editor flow
- 🤖 **Agentic API** with semantic search, voice commands, and versioning
- 🧠 **RL Reward System** for writer/reviewer model feedback and ranking

---

## 🏗 Folder Structure

automated_book_publication/
│
├── backend/
│   ├── scraping/
│   │   ├── playwright_scraper.py      ← Scrape text + take screenshots
│   │   └── rl_reward_system.py        ← Reward model based on scraping quality (e.g., completeness, accuracy)
│   │
│   ├── ai_writer/
│   │   ├── chapter_spinner.py         ← LLM call for rewriting ("spinning")
│   │   ├── reviewer_agent.py          ← AI-based content reviewer/refiner
│   │   └── rl_writer_reward.py        ← Reward model for writer (clarity, novelty, structure)
│   │
│   ├── human_loop/
│   │   ├── writer_interface.py        ← Interface endpoint for human writers
│   │   ├── reviewer_interface.py      ← Interface for human reviewers
│   │   └── editor_interface.py        ← Final editor view + approval logic
│   │
│   ├── agentic_api/
│   │   ├── api_router.py              ← FastAPI endpoints for agent communication
│   │   ├── versioning_manager.py      ← ChromaDB version control
│   │   ├── semantic_search.py         ← Search similar content/snippets
│   │   └── voice_commands.py          ← Voice-to-intent interface (Whisper/STT + command parser)
│   │
│   ├── database/
│   │   ├── chromadb_setup.py          ← Setup and manage ChromaDB collections
│   │   └── metadata_store.py          ← Track versions, feedback, RL scores
│   │
│   └── main.py                        ← FastAPI app runner
│
├── frontend/
│   ├── pages/
│   │   ├── upload_url_page.jsx        ← User inputs the Wikisource URL
│   │   ├── writer_dashboard.jsx       ← Human writer edits/spins content
│   │   ├── review_interface.jsx       ← Human reviewer gives feedback
│   │   └── editor_finalize.jsx        ← Final approval interface
│   │
│   └── components/
│       ├── voice_command_bar.jsx      ← Issue voice commands to agent
│       └── version_viewer.jsx         ← View and compare different content versions
│
├── data/
│   ├── screenshots/                   ← Screenshots of original web pages
│   └── versions/                      ← Spun + reviewed versions (JSON)
│
├── rl_models/
│   ├── reward_model.py                ← Custom reward function for writer/reviewer
│   ├── trainer.py                     ← RL training using human/AI feedback
│   └── inference_ranker.py            ← Rank different generations based on reward
│
├── utils/
│   ├── logging.py
│   └── config.py                      ← API keys, model paths, flags
│
└── requirements.txt

## 🔮 Future Scope
RL-based optimization with human feedback loops

Chapter-to-chapter narrative consistency via memory agents

Full PDF/EPUB export

Git-style version comparison

Multilingual support for global publishing

