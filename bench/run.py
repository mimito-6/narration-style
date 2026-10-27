import json, subprocess, sys, os, concurrent.futures as cf
here = os.path.dirname(os.path.abspath(__file__))
import shutil
CLAUDE = shutil.which("claude")
skill = open(os.path.join(here, "..", "skill", "narration-style", "SKILL.md"), encoding="utf-8").read()
qs = json.load(open(os.path.join(here, "questions.json"), encoding="utf-8"))
MODEL = "haiku"
cwd = os.environ.get("NB_CWD", "C:/Users/mimito/AppData/Local/Temp/nb")
CONCISE = "回答請簡潔，不要寒暄、客套、道歉、重述問題或結尾追問，只給必要資訊。"
conds = {
 "base":    (None, "{q}"),
 "concise": (CONCISE, "{q}"),
 "skill":   (skill, "{q}"),
}
ROUNDS = 2
def run(item):
    qid, cname, q = item
    sp, tpl = conds[cname]
    cmd = [CLAUDE,"-p",tpl.format(q=q),"--model",MODEL,"--output-format","json","--tools","","--disable-slash-commands","--setting-sources","","--strict-mcp-config"]
    if sp: cmd += ["--append-system-prompt", sp]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", cwd=cwd)
    try: d = json.loads(r.stdout)
    except Exception: return dict(id=qid, cond=cname, error=r.stdout[:300]+r.stderr[:300])
    u = d["usage"]
    return dict(id=qid, cond=cname, input=u["input_tokens"]+u["cache_creation_input_tokens"]+u["cache_read_input_tokens"],
                output=u["output_tokens"], result=d["result"], cost=d["total_cost_usd"])
jobs = [(x["id"]+"#"+str(r), c, x["q"]) for r in range(ROUNDS) for x in qs for c in conds]
with cf.ThreadPoolExecutor(4) as ex: out = list(ex.map(run, jobs))
json.dump(out, open(os.path.join(here, "results.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(sum(1 for o in out if "error" in o), "errors of", len(out))
