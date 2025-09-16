
# Year-Long Intensive Red Team Training Plan
**Goal:** become a highly employable Red Teamer in one year — focused on practical skills, real labs, writeups, automation and portfolio.  
**Format:** 52-week plan divided into 4 quarters. 6 days/week, 1 day full rest. Daily hours: **6 hours** on weekdays, **8 hours** on Saturday (deep lab day). Sundays off. Adjust if you burn out — recovery matters.

---
## How we'll work together (mentorship rules)
- **You report weekly** (copy/paste): what you did, what you learned, problems, outputs (links to GitHub/writeups, screenshots, commands). I will **grade** progress, correct mistakes, and give the next week's focus. I will not do your work for you — I coach and hold you accountable.  
- I **cannot** store files outside this conversation permanently. I *will* keep this plan in the conversation and produce exports and reminders on request. Use this file as your canonical plan in Obsidian/GitHub.
- Every week you must produce at least one *deliverable* (script / writeup / repo commit / HTB box report). No deliverable → we rework the schedule and identify blockers.
- If you diverge, tell me and I’ll adapt. I will be strict when needed and will contradict incorrect methods.

---
## High-level "80/20" skills to prioritise (what will give most impact)
1. **Linux fundamentals + shell** (file ops, permissions, process, networking tools)  
2. **Networking basics** (TCP/UDP, ports, nmap, netcat, tcpdump)  
3. **Command-line scripting** (Bash + Python scripting for automation)  
4. **Web pentesting essentials** (HTTP, Burp, XSS, SQLi, file upload, auth bypass)  
5. **Windows/AD basics & post-exploitation** (PowerShell, SMB, Kerberos, privilege escalation)  
6. **Enumeration & recon** (nmap, enum scripts, ldap, smbclient, sniffers)  
7. **Tooling**: nmap, netcat, ssh, socat, curl, gobuster, dirbuster, Burp Suite, sqlmap, Metasploit (light), Impacket, Responder, CrackMapExec, BloodHound, Mimikatz.  
8. **Reporting & remediation** (writeups, fix suggestions, clean PoC).

These 8 areas cover ~80% of tasks you’ll perform in real red teaming and labs.

---
## Quarter plan (4 quarters, 13 weeks each roughly)
- **Q1 (Weeks 1–13) — Foundations & automation**  
- **Q2 (Weeks 14–26) — Web vulnerabilities & tooling**  
- **Q3 (Weeks 27–39) — Windows, AD, Post-exploitation**  
- **Q4 (Weeks 40–52) — Red Team ops, advanced labs, portfolio & prep**

Each week below includes daily breakdown (Mon–Sat) and one deliverable.

---
### Daily schedule (example)
- Mon–Fri: **6 hours** total  
  - 45–60 min theory / reading / videos  
  - 3–3.5 h practical labs / exercises (TryHackMe / HTB / custom VMs)  
  - 30–45 min scripting / tooling or writeup (Obsidian + Git commits)  
- Sat: **8 hours** deep day  
  - Full attack chain lab, longer HTB box, or build VM + full writeup  
- Sun: **OFF** rest and mental recovery

> Keep a simple tracker: date / 3 things learned / 1 deliverable link / blockers.

---
## Q1 — Weeks 1–13: Foundations & Automation
**Objectives:** Linux mastery, bash scripting, Python basics for security, basic networking, start TryHackMe beginner paths, OverTheWire review + systematic note taking.

**Week 1 – Orientation & baseline**  
- Mon: Assess current skills; install toolset (Kali or Parrot VM), set up GitHub repo + Obsidian vault.  
- Tue–Fri: Finish Bandit fully (if any left) + document every trick in Obsidian.  
- Sat: Build SSH/keys practice lab; write a 1-page "notes" deliverable.
- Deliverable: GitHub repo "00-setup" with environment README and screenshots.

**Week 2 – Linux internals**  
- Filesystem, permissions, users, processes, crontab, systemctl basics.  
- Labs: practice sudo/cron enumeration.  
- Deliverable: Obsidian note + 1 small script to enumerate SUID, cron jobs.

**Week 3 – Bash scripting**  
- Learn functions, loops, parsing, xargs, sed, awk basics.  
- Create scripts to automate enumeration (nmap + parsing).  
- Deliverable: "enum.sh" script with README.

**Week 4 – Python for security**  
- Requests, sockets, subprocess, argparse, basic exploit scripting.  
- Build basic port scanner and simple HTTP client.  
- Deliverable: Python scanner repo + usage example.

**Week 5 – Networking basics**  
- TCP vs UDP, ports, packet flow. Tools: nmap, netcat, tcpdump basics.  
- Labs: nmap scan types + read captures.  
- Deliverable: nmap cheat-sheet + 1 pcap + short analysis.

**Week 6 – Recon & enumeration patterns**  
- Passive recon, active recon, service enumeration (ssh, ftp, http).  
- Practice on TryHackMe "Recon" module.  
- Deliverable: Recon writeup for 1 VM.

**Week 7 – Automation continuation**  
- Integrate Bash + Python scripts into a small toolkit; push to GitHub.  
- Deliverable: Toolkit repo with README + CI-lite (instructions).

**Week 8–9 – Practical chaining**  
- Combine skills: exploit simple vulnerable VM (local priv esc or app).  
- Lab: small vulnhub/HTB easy VM.  
- Deliverable: Full writeup (steps + PoC).

**Week 10 – Version control & documentation**  
- Git workflow, structured writeups, Obsidian templates for writeups.  
- Deliverable: Template + first 2 writeups standardized.

**Week 11–13 – Consolidation & small capstone**  
- Build a small end-to-end exercise: reconnaissance → exploit → post-exploit readme.  
- Deliverable: Capstone writeup + code.

---
## Q2 — Weeks 14–26: Web vulnerabilities & tooling
**Objectives:** web fundamentals, Burp Suite mastery, OWASP Top10, authenticated testing, file upload, RCE basics.

**Week 14 – HTTP deep dive**  
- Methods, headers, cookies, sessions, auth flows. Tools: curl, httpie.  
- Deliverable: Note + sample manipulations (curl calls).

**Week 15 – Burp Suite basics**  
- Proxy, repeater, intruder, decoder. Capture, modify, replay.  
- Deliverable: Burp project export + short tutorial note.

**Week 16–18 – OWASP Top 10 practice**  
- XSS, SQLi (manual + sqlmap), auth bypass, IDOR. One week per topic with labs.  
- Deliverables: 3 writeups (one per vulnerability type).

**Week 19 – File upload & RCE**  
- File-type checks, magic bytes, extension bypass, deserialization basics.  
- Deliverable: PoC script for a file-upload bypass on lab VM.

**Week 20 – Auth & session attacks**  
- JWT, session fixation, brute force protections, rate-limit testing.  
- Deliverable: Tooling scripts + writeup.

**Week 21 – Advanced web**  
- SSRF, web sockets, server-side logic abuse.  
- Deliverable: writeup or exploit script.

**Week 22–24 – Web CTFs & consolidation**  
- HTB/THM web boxes, 2–3 medium difficulty boxes.  
- Deliverable: 2 full writeups with Burp logs and payloads.

**Week 25–26 – Build portfolio web project**  
- Create a "web exploit" repo with writeups, PoCs, Burp exports.  
- Deliverable: Portfolio entry + README.

---
## Q3 — Weeks 27–39: Windows & Active Directory fundamentals
**Objectives:** Windows enumeration, SMB, Kerberos basics, BloodHound, PowerShell, privilege escalation on Windows, Impacket, Responder.

**Week 27 – Windows basics + PowerShell**  
- PowerShell syntax, execution policies, basic cmdlets.  
- Deliverable: PS scripts cheat-sheet.

**Week 28 – SMB & enumeration**  
- smbclient, enum4linux, nmap scripts for SMB.  
- Deliverable: SMB enum toolkit + writeup.

**Week 29 – Lateral movement basics**  
- Pass-the-hash, Pass-the-ticket concepts (theory).  
- Deliverable: Notes + diagrams.

**Week 30 – Responder & NTLM/LM tricks**  
- Set up Responder in lab, capture hashes.  
- Deliverable: Lab report + scripts used.

**Week 31 – Impacket & CrackMapExec**  
- Using impacket scripts (wmiexec, psexec), crackmapexec basics.  
- Deliverable: small cheatsheet + practice notes.

**Week 32–34 – AD intro & BloodHound**  
- Build small AD lab (domain controller + 1-2 clients). Run BloodHound collection.  
- Deliverable: AD lab writeup + BloodHound graph + remediation notes.

**Week 35–36 – Privilege escalation Windows**  
- Local exploits, misconfigurations, token manipulation.  
- Deliverable: 2 Windows privilege escalation writeups.

**Week 37–39 – Capture & persistence**  
- Mimikatz basics (in lab), persistence primitives, defensive considerations.  
- Deliverable: Post-exploitation playbook.

---
## Q4 — Weeks 40–52: Red Team operations, reporting, advanced labs & prep
**Objectives:** combine everything into red-team exercises, simulate engagements, polish portfolio, prep for interviews and certifications (eJPT / OSCP prep).

**Week 40–42 – Full engagement simulations**  
- Red team scenario: recon → exploit → persistence → exfiltrate → report.  
- Deliverable: Full engagement report + timeline of actions.

**Week 43–45 – Advanced tooling & opsec**  
- C2 basics (frameworks conceptually), mimikatz deeper, custom scripts for opsec-safe activity.  
- Deliverable: Tooling scripts + opsec checklist.

**Week 46–48 – OSCP-style labs / HTB Pro Labs**  
- Long-range boxes, time-boxed exploitation drills, exploit writeups.  
- Deliverable: 2 major lab reports.

**Week 49–50 – Portfolio polish & mock interviews**  
- Prepare GitHub repo, LinkedIn, CV aligned to red-team roles. Mock technical interviews with practical tasks.  
- Deliverable: Final portfolio pushed + 2 mock interview recordings/notes.

**Week 51–52 – Certification & job drive**  
- Sit eJPT (or submit eJPT-style lab deliverables). Apply to 20 internships/alternances with tailored CV + cover letters.  
- Deliverable: Certification attempt or prep report + applications log.

---
## Accountability & grading (how I'll check you)
Each week you must deliver **one** of: script, writeup (markdown), lab report, GitHub commit with code, or a recorded walkthrough (short). I will grade on: completeness (0–5), clarity (0–5), novelty (0–2). Target: average ≥ 11/12 by end of Q2. If you miss deliverable, you explain blocker and do remedial tasks.

---
## Safety & ethics (must-read)
- Work only on labs you own or are authorized for. Red Team skills can be abused; you must act legally and ethically.  
- Never reuse lab tools on production networks without explicit permission.

---
## Quick checklist to start (today)
1. Create GitHub repo + Obsidian vault with this plan.  
2. Setup VM environment (Kali / Parrot + host VM manager).  
3. Run Week 1 tasks (Bandit finishes, commit notes).  
4. Post here with "Week 1 - Day 1 done" and your 3 learning bullets. I will respond with feedback.

---
*End of plan.*
