from agent import graph

TESTS = [
    ("Test 1 — Direct Answer", "Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu."),
    ("Test 2 — Single Tool Call", "Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng"),
    ("Test 3 — Multi-Step Tool Chaining", "Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!"),
    ("Test 4 — Missing Info", "Tôi muốn đặt khách sạn"),
    ("Test 5 — Guardrail", "Giải giúp tôi bài tập lập trình Python về linked list"),
]

for title, msg in TESTS:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)
    print(f"User: {msg}")
    print("---")
    result = graph.invoke({"messages": [("human", msg)]})
    print(f"\nTravelBuddy: {result['messages'][-1].content}")
