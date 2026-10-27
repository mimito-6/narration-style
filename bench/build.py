import json,collections,os
here=os.path.dirname(os.path.abspath(__file__)); root=os.path.dirname(here)
R=json.load(open(os.path.join(here,"results.json"),encoding="utf-8"))
qs=json.load(open(os.path.join(here,"questions.json"),encoding="utf-8"))
qd={q["id"]:q for q in qs}
d=collections.defaultdict(lambda:collections.defaultdict(list))
for r in R: d[r["id"].split("#")[0]][r["cond"]].append(r)
avg=lambda v,k:sum(x[k] for x in v)/len(v)
C=("base","concise","skill")
tab=[]
for q in qs:
    c=d[q["id"]]; tab.append((q["id"],q["cat"],[avg(c[k],"output") for k in C],avg(c["base"],"input"),avg(c["skill"],"input")))
n=len(tab)
tot=[sum(t[2][i] for t in tab) for i in range(3)]
in_extra=sum(t[4]-t[3] for t in tab)/n
cost=[sum(r["cost"] for r in R if r["cond"]==k) for k in C]
cat=collections.OrderedDict()
for t in tab:
    v=cat.setdefault(t[1],[0,0,0])
    for i in range(3): v[i]+=t[2][i]
pct=lambda a,b:round(100*(1-a/b))
summ=dict(n=n,tot=tot,in_extra=in_extra,cost=cost,cat={k:v for k,v in cat.items()})
json.dump(summ,open(os.path.join(here,"summary.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
md="| 題號 | 類別 | 不用 skill | 只說「請簡潔」 | 旁白體 skill | skill 省 |\n|---|---|--:|--:|--:|--:|\n"
for t in tab: md+=f"| {t[0]} | {t[1]} | {t[2][0]:.0f} | {t[2][1]:.0f} | {t[2][2]:.0f} | {pct(t[2][2],t[2][0])}% |\n"
md+=f"| **合計** | | **{tot[0]:.0f}** | **{tot[1]:.0f}** | **{tot[2]:.0f}** | **{pct(tot[2],tot[0])}%** |\n"
cmd="| 類別 | 不用 skill | 只說「請簡潔」 | 旁白體 skill | skill 省 | 簡潔指令省 |\n|---|--:|--:|--:|--:|--:|\n"
for k,v in cat.items(): cmd+=f"| {k} | {v[0]:.0f} | {v[1]:.0f} | {v[2]:.0f} | {pct(v[2],v[0])}% | {pct(v[1],v[0])}% |\n"
open(os.path.join(here,"table_per_question.md"),"w",encoding="utf-8").write(md)
open(os.path.join(here,"table_per_category.md"),"w",encoding="utf-8").write(cmd)
# html
bars=""
for k,v in cat.items():
    for i,(lab,col) in enumerate((("不用 skill","#b9b4a8"),("請簡潔","#8fb3a0"),("旁白體","#d9822b"))):
        bars+=f'<div class="row"><span class="l">{k if i==0 else ""}</span><div class="b" style="width:{v[i]/max(x[0] for x in cat.values())*60:.1f}%;background:{col}"></div><span class="v">{v[i]/ (len([t for t in tab if t[1]==k])):.0f}</span></div>'
html=f"""<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>旁白體 narration-style</title>
<style>body{{font-family:system-ui,"Noto Sans TC",sans-serif;max-width:760px;margin:2rem auto;padding:0 1rem;color:#2b2a27;background:#faf8f3}}h1{{margin-bottom:.2em}}.big{{font-size:3rem;font-weight:700;color:#d9822b}}.card{{background:#fff;border:1px solid #e6e1d4;border-radius:12px;padding:1rem 1.2rem;margin:1rem 0}}pre{{background:#f1ede2;padding:.8rem;border-radius:8px;white-space:pre-wrap}}.row{{display:flex;align-items:center;gap:.5rem;margin:3px 0}}.l{{width:5.5em;font-size:.85rem}}.b{{height:14px;border-radius:3px}}.v{{font-size:.8rem;color:#777}}table{{border-collapse:collapse;width:100%;font-size:.85rem}}td,th{{border-bottom:1px solid #e6e1d4;padding:4px 6px;text-align:right}}td:first-child,th:first-child,td:nth-child(2),th:nth-child(2){{text-align:left}}.leg span{{display:inline-block;margin-right:1em;font-size:.85rem}}</style>
<h1>旁白體 narration-style</h1><p>用「動作」取代客套與報備，只留必要資訊與下一步。</p>
<div class="card"><div class="big">輸出 −{pct(tot[2],tot[0])}%</div>平均每題輸出 {tot[0]/n:.0f} → {tot[2]/n:.0f} tokens（Haiku 5.5，{n} 題 × 2 輪）。<br>代價：skill 每次多載入約 {in_extra:.0f} input tokens；單次呼叫總費用省 {pct(cost[2],cost[0])}%（已含 skill 的 input）。純指令「請簡潔」輸出省 {pct(tot[1],tot[0])}%，但沒有旁白風格。</div>
<div class="card"><b>長這樣</b><pre>你：還是登不進去欸
（抓起外套衝回座位，重新打開電腦）
原因是密碼驗證沒處理空白字元，已補上，現在沒問題了。

你：今天好累喔
（默默把一杯熱茶推到你桌上）</pre></div>
<div class="card"><b>各類別平均輸出 tokens</b><div class="leg"><span style="color:#b9b4a8">■ 不用 skill</span><span style="color:#8fb3a0">■ 請簡潔</span><span style="color:#d9822b">■ 旁白體</span></div>{bars}</div>
<div class="card"><b>各題原始數據（輸出 tokens，2 輪平均）</b><table><tr><th>題</th><th>類別</th><th>無</th><th>簡潔</th><th>旁白</th></tr>{''.join(f'<tr><td>{t[0]}</td><td>{t[1]}</td><td>{t[2][0]:.0f}</td><td>{t[2][1]:.0f}</td><td>{t[2][2]:.0f}</td></tr>' for t in tab)}</table></div>
<p style="font-size:.8rem;color:#777">資料來自 <code>bench/results.json</code>，由 <code>claude -p --output-format json</code> 實測。完整說明見 REPORT.md。</p></html>"""
os.makedirs(os.path.join(root,"docs"),exist_ok=True)
open(os.path.join(root,"docs","index.html"),"w",encoding="utf-8").write(html)
print(summ["n"],tot,in_extra,cost,[pct(tot[i],tot[0]) for i in (1,2)])
