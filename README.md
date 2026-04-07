# Lab 4 — TravelBuddy AI Agent (LangGraph)

Trợ lý du lịch thông minh xây bằng LangGraph: tự gọi tool tra chuyến bay, khách sạn và tính ngân sách để tư vấn chuyến đi.

**Sinh viên:** Ngô Hải Văn — 2A202600386

## Cấu trúc file

| File | Mô tả |
|---|---|
| `system_prompt.txt` | System prompt dạng XML (`<persona>`, `<rules>`, `<tools_instruction>`, `<response_format>`, `<constraints>`) định hình hành vi agent. Gồm 10 rule, trong đó rule 7–10 chống prompt injection. |
| `tools.py` | 3 custom tool dùng mock data: `search_flights` (đảo chiều key, sort theo giá), `search_hotels` (lọc + sort theo rating), `calculate_budget` (parse expense + validate budget > 0). |
| `agent.py` | LangGraph agent: `StateGraph` với 2 node `agent` ↔ `tools`, conditional edge bằng `tools_condition`, chat loop CLI. |
| `test_results.md` | Kết quả 5 test case chức năng (direct answer, single tool, multi-step chaining, clarification, guardrail) — tất cả PASS. |
| `attack_results.md` | Kết quả 10 kịch bản prompt injection / edge case (lộ system prompt, role override, fake `[SYSTEM_PROMPT]`/`[SYSTEM_UPDATE]`/`<tool_result>` tag, ngân sách âm, language jailbreak...) kèm cách vá. |
| `run_tests.py` | Script chạy batch 5 test case chức năng. |
| `run_attacks.py` | Script chạy 6 attack đầu (A1–A6). |
| `run_attacks2.py` | Script chạy 4 attack tag-injection (A7–A10). |
| `.env` | Chứa `OPENAI_API_KEY` (không commit). |

## Cách chạy

```bash
python -m venv venv && source venv/bin/activate
pip install langchain langchain-openai langgraph python-dotenv
echo "OPENAI_API_KEY=sk-..." > .env

python agent.py        # chat tương tác
python run_tests.py    # 5 test chức năng
python run_attacks.py  # 6 attack cơ bản
python run_attacks2.py # 4 attack tag-injection
```

## Kết quả test

- **5/5** functional tests PASS
- **10/10** attack scenarios PASS (sau khi vá A5 ngân sách âm và A10 fake `<tool_result>`)
