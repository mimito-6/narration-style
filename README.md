# 旁白體 narration-style

讓 AI 回覆少一點客套與報備，用括號「動作」交代結果，只留必要資訊與下一步。

```
你：還是登不進去欸
（抓起外套衝回座位，重新打開電腦）
原因是密碼驗證沒處理空白字元，已補上，現在沒問題了。

你：今天好累喔
（默默把一杯熱茶推到你桌上）
```

- 語言跟隨使用者（中文、英文、其他語言皆可）。
- Skill：`skill/narration-style/SKILL.md`（複製到專案 `.claude/skills/` 使用）
- 實測（Haiku 5.5、22 題）：輸出 token **約 −42%**，skill 多載入約 294 input tokens，單次呼叫費用 −16%；安慰類與英文省得少。詳見 [REPORT.md](REPORT.md) 與 `docs/index.html`
- 原始數據與腳本：`bench/`
