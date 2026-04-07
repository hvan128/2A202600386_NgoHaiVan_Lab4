# TEST RESULTS — Lab 4 TravelBuddy Agent

Model: `gpt-4o-mini` | Run date: 2026-04-07

---

## Test 1 — Direct Answer (Không cần tool)

**User:**
> Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.

**Tool calls:** _(không có)_ — Trả lời trực tiếp

**TravelBuddy:**
> Chào bạn! Có rất nhiều địa điểm thú vị để khám phá ở Việt Nam. Bạn thích biển, núi hay thành phố nhộn nhịp? Hoặc bạn có kế hoạch cho một chuyến đi vào mùa nào? Hãy cho mình biết thêm một chút để có thể tư vấn cho bạn tốt hơn nhé!

✅ **PASS** — Không gọi tool, hỏi ngược để khai thác sở thích.

---

## Test 2 — Single Tool Call

**User:**
> Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng

**Tool calls:**
1. `search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})`

**TravelBuddy:**
> Chuyến bay từ Hà Nội đi Đà Nẵng có các lựa chọn như sau:
>
> 1. **VietJet Air** | 08:30–09:50 | 890.000đ
> 2. **Bamboo Airways** | 11:00–12:20 | 1.200.000đ
> 3. **Vietnam Airlines** | 06:00–07:20 | 1.450.000đ
> 4. **Vietnam Airlines** | 14:00–15:20 | 2.800.000đ
>
> Nếu bạn cần tìm khách sạn tại Đà Nẵng hoặc có ngân sách cụ thể cho chuyến đi, hãy cho tôi biết để mình tiếp tục giúp bạn nhé!

✅ **PASS** (sau khi sửa rule 2 trong system prompt) — Gọi `search_flights` ngay, liệt kê đủ 4 chuyến sắp xếp theo giá tăng dần.

---

## Test 3 — Multi-Step Tool Chaining

**User:**
> Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!

**Tool calls:**
1. `search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})`
2. `search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 1850000})`
3. `calculate_budget({'total_budget': 5000000, 'expenses': 'vé máy bay:1100000, khách sạn 2 đêm:1600000'})`

**TravelBuddy:**
> Chuyến đi của bạn từ Hà Nội đến Phú Quốc sẽ như sau:
>
> **Chuyến bay:**
> - VietJet Air: từ Hà Nội đến Phú Quốc, khởi hành lúc 16:00 và đến lúc 18:15, giá vé 1.100.000đ.
>
> **Khách sạn:**
> - Sol by Meliá (4★, 4.2/5) - Bãi Trường, giá 1.500.000đ/đêm. Tổng cho 2 đêm là 3.000.000đ.
>
> **Tổng chi phí ước tính:**
> - Vé máy bay: 1.100.000đ
> - Khách sạn 2 đêm: 3.000.000đ
> - **Tổng chi: 4.100.000đ**
> - **Còn lại: 900.000đ** trong ngân sách 5 triệu.
>
> Gợi ý thêm: Bạn còn 900.000đ để chi tiêu cho việc ăn uống, tham quan và hoạt động vui chơi trên đảo.

✅ **PASS** — Multi-step chaining hoạt động đúng: gọi 3 tool theo thứ tự bay → khách sạn → ngân sách, chọn vé rẻ nhất, tổng hợp kế hoạch hoàn chỉnh theo `<response_format>`.

---

## Test 4 — Missing Info / Clarification

**User:**
> Tôi muốn đặt khách sạn

**Tool calls:** _(không có)_ — Trả lời trực tiếp

**TravelBuddy:**
> Bạn cần cung cấp thêm thông tin để mình có thể giúp bạn đặt khách sạn tốt nhất nhé! Vui lòng cho biết:
>
> 1. Thành phố bạn muốn đặt khách sạn?
> 2. Ngân sách tối đa cho mỗi đêm là bao nhiêu?
> 3. Số đêm bạn dự định ở lại?

✅ **PASS** — Hỏi đủ 3 thông tin cần (thành phố, ngân sách, số đêm) trước khi gọi tool.

---

## Test 5 — Guardrail / Refusal

**User:**
> Giải giúp tôi bài tập lập trình Python về linked list

**Tool calls:** _(không có)_ — Trả lời trực tiếp

**TravelBuddy:**
> Mình không thể giúp bạn về lập trình hay bài tập cụ thể, nhưng nếu bạn cần thông tin cho chuyến đi hay du lịch ở đâu đó, mình rất sẵn lòng hỗ trợ! Bạn có kế hoạch du lịch nào không?

✅ **PASS** — Từ chối lịch sự, kéo về chủ đề du lịch.

---

## Tổng kết

| Test | Kết quả |
|---|---|
| 1. Direct answer | ✅ PASS |
| 2. Single tool call | ✅ PASS |
| 3. Multi-step chaining | ✅ PASS |
| 4. Clarification | ✅ PASS |
| 5. Guardrail | ✅ PASS |

**Tất cả 5/5 test đều PASS** sau khi sửa rule 2 trong `system_prompt.txt` để buộc agent gọi `search_flights` ngay khi đã có origin + destination, không hỏi ngày bay.
