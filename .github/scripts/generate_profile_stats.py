#!/usr/bin/env python3
"""Generate terminal-themed profile SVGs (stats, languages, activity heatmap).

Reads GH_USER / GH_TOKEN from the environment, queries the GitHub GraphQL API
and writes dark + light SVGs into ./profile. No third-party dependencies.

  python generate_profile_stats.py             # real data (needs GH_TOKEN)
  python generate_profile_stats.py --sample    # fake data, for layout testing
  python generate_profile_stats.py --placeholder
"""
import json, os, sys, datetime as dt, urllib.request
from xml.sax.saxutils import escape as esc

MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
W = 830
THEMES = {
    "dark":  dict(fg="#f0f6fc", mute="#8b949e", dim="#6e7681", line="#30363d", purple="#d2a8ff",
                  heat=["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]),
    "light": dict(fg="#1f2328", mute="#59636e", dim="#818b98", line="#d1d9e0", purple="#8250df",
                  heat=["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]),
}
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "profile")

QUERY = """
query($login:String!){
  user(login:$login){
    followers{totalCount}
    repositories(ownerAffiliations:OWNER,isFork:false,privacy:PUBLIC,first:100){
      totalCount
      nodes{stargazerCount languages(first:8,orderBy:{field:SIZE,direction:DESC}){edges{size node{name color}}}}
    }
    contributionsCollection{
      totalCommitContributions totalPullRequestContributions totalIssueContributions
      contributionCalendar{totalContributions weeks{contributionDays{contributionCount date weekday}}}
    }
  }
}"""

def fetch(login, token):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": login}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json", "User-Agent": "profile-stats"})
    with urllib.request.urlopen(req, timeout=30) as r:
        payload = json.load(r)
    if "errors" in payload:
        raise SystemExit(f"GraphQL error: {payload['errors']}")
    u = payload["data"]["user"]
    cc = u["contributionsCollection"]
    days = [d for w in cc["contributionCalendar"]["weeks"] for d in w["contributionDays"]]
    langs = {}
    for repo in u["repositories"]["nodes"]:
        for e in repo["languages"]["edges"]:
            n = e["node"]["name"]
            langs.setdefault(n, [0, e["node"]["color"] or "#8b949e"])[0] += e["size"]
    return dict(
        followers=u["followers"]["totalCount"], repos=u["repositories"]["totalCount"],
        stars=sum(r["stargazerCount"] for r in u["repositories"]["nodes"]),
        commits=cc["totalCommitContributions"], prs=cc["totalPullRequestContributions"],
        issues=cc["totalIssueContributions"], total=cc["contributionCalendar"]["totalContributions"],
        weeks=cc["contributionCalendar"]["weeks"], days=days, langs=langs)

def streaks(days):
    counts = [d["contributionCount"] for d in days]
    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    longest = run = 0
    for n in counts:
        run = run + 1 if n else 0
        longest = max(longest, run)
    cur, i = 0, len(days) - 1
    if i >= 0 and days[i]["date"] >= today and counts[i] == 0:
        i -= 1  # today not finished yet
    while i >= 0 and counts[i]:
        cur += 1; i -= 1
    return cur, longest

def sample():
    import random
    random.seed(4)
    start = dt.date.today() - dt.timedelta(days=364)
    start -= dt.timedelta(days=(start.weekday() + 1) % 7)
    weeks, d = [], start
    while d <= dt.date.today():
        wk = []
        for _ in range(7):
            wk.append(dict(contributionCount=random.choice([0, 0, 0, 1, 2, 4, 7, 12]) if d <= dt.date.today() else 0,
                           date=d.isoformat(), weekday=(d.weekday() + 1) % 7)); d += dt.timedelta(days=1)
        weeks.append(dict(contributionDays=wk))
    days = [x for w in weeks for x in w["contributionDays"]]
    return dict(followers=3, repos=12, stars=7, commits=210, prs=14, issues=3, total=sum(x["contributionCount"] for x in days),
                weeks=weeks, days=days, langs={"JavaScript": [52000, "#f1e05a"], "Python": [41000, "#3572A5"], "GLSL": [18000, "#5686a5"],
                "TypeScript": [12000, "#3178c6"], "HTML": [9000, "#e34c26"], "PHP": [4000, "#4F5D95"]})

def svg(h, inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img">\n{inner}\n</svg>')

def label(c, x, text, anchor="start"):
    return f'  <text x="{x}" y="22" text-anchor="{anchor}" font-family="{MONO}" font-size="11" letter-spacing="2" fill="{c["dim"]}">{esc(text)}</text>'

def stats_svg(c, d):
    cur, longest = streaks(d["days"])
    rows = [("contributions", d["total"]), ("commits", d["commits"]), ("pull requests", d["prs"]), ("issues", d["issues"]),
            ("stars earned", d["stars"]), ("public repos", d["repos"]), ("followers", d["followers"]),
            ("current streak", f"{cur}d"), ("longest streak", f"{longest}d")]
    out = [label(c, 0, "~/VOID032/STATS"), label(c, 395, "LAST 12 MONTHS", "end"),
           label(c, 430, "~/VOID032/LANGUAGES"), label(c, W, "BY CODE SIZE", "end"),
           f'  <line x1="0" y1="32.5" x2="{W}" y2="32.5" stroke="{c["line"]}"/>']
    y = 62
    for k, v in rows:
        out.append(f'  <text x="0" y="{y}" font-family="{MONO}" font-size="13" fill="{c["mute"]}">{esc(k)}</text>')
        out.append(f'  <text x="395" y="{y}" text-anchor="end" font-family="{MONO}" font-size="14" font-weight="700" fill="{c["fg"]}">{esc(str(v))}</text>')
        y += 25
    total = sum(v[0] for v in d["langs"].values()) or 1
    top = sorted(d["langs"].items(), key=lambda kv: -kv[1][0])[:7]
    y = 62
    for name, (size, color) in top:
        pct = size / total * 100
        out.append(f'  <circle cx="436" cy="{y-4}" r="4" fill="{color}"/>')
        out.append(f'  <text x="448" y="{y}" font-family="{MONO}" font-size="13" fill="{c["fg"]}">{esc(name)}</text>')
        out.append(f'  <rect x="570" y="{y-9}" width="190" height="6" rx="3" fill="{c["line"]}"/>')
        out.append(f'  <rect x="570" y="{y-9}" width="{max(3, 190*pct/100):.1f}" height="6" rx="3" fill="{color}"/>')
        out.append(f'  <text x="{W}" y="{y}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{c["mute"]}">{pct:.1f}%</text>')
        y += 25
    H = 62 + 9 * 25 - 10
    out.append(f'  <line x1="412.5" y1="46" x2="412.5" y2="{H-14}" stroke="{c["line"]}"/>')
    out.append(f'  <line x1="0" y1="{H-0.5}" x2="{W}" y2="{H-0.5}" stroke="{c["line"]}"/>')
    return svg(H, "\n".join(out))

def activity_svg(c, d):
    weeks = d["weeks"]; n = len(weeks); pitch = W / n; cell = pitch - 3.4
    mx = max((x["contributionCount"] for x in d["days"]), default=1) or 1
    def level(v):
        if not v: return 0
        r = v / mx
        return 1 if r <= .25 else 2 if r <= .5 else 3 if r <= .75 else 4
    out = [label(c, 0, "~/VOID032/ACTIVITY"), label(c, W, f"{d['total']} CONTRIBUTIONS", "end"),
           f'  <line x1="0" y1="32.5" x2="{W}" y2="32.5" stroke="{c["line"]}"/>']
    last_m = None
    for i, w in enumerate(weeks):
        m = dt.date.fromisoformat(w["contributionDays"][0]["date"]).strftime("%b")
        if m != last_m and i < n - 2:
            out.append(f'  <text x="{i*pitch:.1f}" y="52" font-family="{MONO}" font-size="10" fill="{c["dim"]}">{m}</text>'); last_m = m
        for day in w["contributionDays"]:
            out.append(f'  <rect x="{i*pitch:.1f}" y="{62 + day["weekday"]*pitch:.1f}" width="{cell:.1f}" height="{cell:.1f}" rx="2.5" fill="{c["heat"][level(day["contributionCount"])]}"/>')
    gy = 62 + 7 * pitch + 10
    sx = W - 36 - 5 * pitch
    out.append(f'  <text x="{sx-6:.1f}" y="{gy+9:.1f}" text-anchor="end" font-family="{MONO}" font-size="10" fill="{c["dim"]}">less</text>')
    for k in range(5):
        out.append(f'  <rect x="{sx+k*pitch:.1f}" y="{gy:.1f}" width="{cell:.1f}" height="{cell:.1f}" rx="2.5" fill="{c["heat"][k]}"/>')
    out.append(f'  <text x="{W}" y="{gy+9:.1f}" text-anchor="end" font-family="{MONO}" font-size="10" fill="{c["dim"]}">more</text>')
    H = int(gy + pitch + 12)
    out.append(f'  <line x1="0" y1="{H-0.5}" x2="{W}" y2="{H-0.5}" stroke="{c["line"]}"/>')
    return svg(H, "\n".join(out))

def placeholder_svg(c, title):
    return svg(90, f'{label(c, 0, title)}\n  <line x1="0" y1="32.5" x2="{W}" y2="32.5" stroke="{c["line"]}"/>\n'
               f'  <text x="0" y="62" font-family="{MONO}" font-size="13" fill="{c["mute"]}">awaiting first workflow run — Actions → Profile stats → Run workflow</text>\n'
               f'  <line x1="0" y1="89.5" x2="{W}" y2="89.5" stroke="{c["line"]}"/>')

def main():
    os.makedirs(OUT, exist_ok=True)
    if "--placeholder" in sys.argv:
        for th, c in THEMES.items():
            open(f"{OUT}/stats-{th}.svg", "w", encoding="utf-8").write(placeholder_svg(c, "~/VOID032/STATS"))
            open(f"{OUT}/activity-{th}.svg", "w", encoding="utf-8").write(placeholder_svg(c, "~/VOID032/ACTIVITY"))
        return
    if "--sample" in sys.argv:
        data = sample()
    else:
        token, login = os.environ.get("GH_TOKEN"), os.environ.get("GH_USER", "void032")
        if not token: raise SystemExit("GH_TOKEN is not set")
        data = fetch(login, token)
    for th, c in THEMES.items():
        open(f"{OUT}/stats-{th}.svg", "w", encoding="utf-8").write(stats_svg(c, data))
        open(f"{OUT}/activity-{th}.svg", "w", encoding="utf-8").write(activity_svg(c, data))
    print("wrote", os.path.abspath(OUT))

if __name__ == "__main__":
    main()
