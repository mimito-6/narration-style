import json,collections,sys
f=sys.argv[1] if len(sys.argv)>1 else "results.json"
R=json.load(open(f,encoding="utf-8"))
qs={q["id"]:q for q in json.load(open("questions.json",encoding="utf-8"))}
d=collections.defaultdict(dict)
for r in R:
    qid,_=r["id"].split("#"); d[qid].setdefault(r["cond"],[]).append(r)
avg=lambda v,k:sum(x[k] for x in v)/len(v)
rows=[]
for qid,c in d.items():
    rows.append((qid,qs[qid]["cat"],{k:avg(v,"output") for k,v in c.items()},{k:avg(v,"input") for k,v in c.items()}))
tot=collections.defaultdict(float);cat=collections.defaultdict(lambda:collections.defaultdict(float));itot=collections.defaultdict(float)
for qid,ct,o,i in rows:
    for k in o: tot[k]+=o[k]; cat[ct][k]+=o[k]; itot[k]+=i[k]
print(json.dumps({"out":tot,"in":itot},ensure_ascii=False))
for k,v in cat.items(): print(k,{a:round(b) for a,b in v.items()},"skill vs base %.0f%%"%(100*(1-v["skill"]/v["base"])))
json.dump([[r[0],r[1],r[2],r[3]] for r in rows],open("summary_"+f,"w",encoding="utf-8"),ensure_ascii=False)
