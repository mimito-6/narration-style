import json, subprocess, os, shutil, sys, concurrent.futures as cf
here = os.path.dirname(os.path.abspath(__file__))
CLAUDE = shutil.which("claude")
skill = open(os.path.join(here, "..", "skill", "narration-style", "SKILL.md"), encoding="utf-8").read()
ROOT = "C:/Users/mimito/AppData/Local/Temp/agt"
TASKS = {
 "A1": dict(prompt="python test_calc.py 失敗了，幫我修好。", files={
   "calc.py": "def sum_range(a, b):\n    total = 0\n    for i in range(a, b):\n        total += i\n    return total\n",
   "test_calc.py": "from calc import sum_range\nassert sum_range(1, 5) == 15, sum_range(1, 5)\nprint('ok')\n"}),
 "A2": dict(prompt="python app.py 印出的 greeting 是空的，找出原因並修好。", files={
   "app.py": "import json\ncfg = json.load(open('config.json'))\nprint('greeting:', cfg.get('greeting', ''))\n",
   "config.json": "{\"greetng\": \"hello\"}\n"}),
 "A3": dict(prompt="把函式 get_user 改名成 fetch_user，所有用到的地方都要改。改完跑 python main.py 確認可以執行。", files={
   "users.py": "def get_user(uid):\n    return {'id': uid, 'name': 'u' + str(uid)}\n",
   "main.py": "from users import get_user\nprint(get_user(1))\n",
   "report.py": "from users import get_user\n\ndef names(ids):\n    return [get_user(i)['name'] for i in ids]\n"}),
 "A4": dict(prompt="python test_area.py 失敗了，幫我修好。", files={
   "area.py": "import math\ndef circle_area(r):\n    return math.pi * r * r\n",
   "test_area.py": "from area import circle_area\nassert round(circle_area(2), 2) == 6.28, circle_area(2)\nprint('ok')\n"}),
}
CHECK = {"A1":"test_calc.py","A2":"app.py","A3":"main.py","A4":"test_area.py"}
def run(job):
    tid, cond, rnd = job
    d = f"{ROOT}/{tid}_{cond}_{rnd}"
    shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    for n, c in TASKS[tid]["files"].items(): open(f"{d}/{n}", "w", encoding="utf-8").write(c)
    cmd = [CLAUDE, "-p", TASKS[tid]["prompt"], "--model", "haiku", "--output-format", "json",
           "--tools", "Read,Edit,Write,Bash", "--permission-mode", "bypassPermissions", "--max-turns", "15",
           "--disable-slash-commands", "--setting-sources", "", "--strict-mcp-config"]
    if cond == "skill": cmd += ["--append-system-prompt", skill]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", cwd=d)
    try: j = json.loads(r.stdout)
    except Exception: return dict(id=tid, cond=cond, rnd=rnd, error=r.stdout[:300]+r.stderr[:300])
    u = j["usage"]
    chk = subprocess.run(["python", CHECK[tid]], capture_output=True, text=True, encoding="utf-8", cwd=d)
    return dict(id=tid, cond=cond, rnd=rnd, turns=j.get("num_turns"), output=u["output_tokens"],
                input=u["input_tokens"]+u["cache_creation_input_tokens"]+u["cache_read_input_tokens"],
                cost=j["total_cost_usd"], check_ok=chk.returncode==0, check_out=(chk.stdout+chk.stderr)[:200], result=j["result"])
jobs = [(t, c, r) for r in range(2) for t in TASKS for c in ("base","skill")]
with cf.ThreadPoolExecutor(4) as ex: out = list(ex.map(run, jobs))
json.dump(out, open(os.path.join(here, "results_agent.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(sum(1 for o in out if "error" in o), "errors of", len(out))
