---
title: "Your Agent's Skills Are Code. Audit Them."
description: "Introducing SkillTriage, a static security auditor for AI agent skills and Claude Code plugins, mapped to the OWASP Agentic Skills Top 10."
date: 2026-10-26
author: "Bo Kaung"
tags:
  - ai-agents
  - security
  - owasp
  - claude-code
  - static-analysis
cover: /assets/images/skilltriage-cover.png
image: /assets/images/skilltriage-cover.png
---

If you use Claude Skills or Claude Code plugins, you are running code and
instructions you probably have not reviewed. I know I was: dozens installed, and
no good answer to a simple question — *what can this thing do to my machine?*

I was working through the OWASP Top 10 lists when I found the
[OWASP Agentic Skills Top 10](https://github.com/OWASP/www-project-agentic-skills-top-10).
It names exactly what I had been ignoring:

1. Malicious Skills
2. Supply Chain Compromise
3. Over-Privileged Skills
4. Insecure Metadata
5. Untrusted External Instructions
6. Weak Isolation
7. Update Drift
8. Poor Scanning
9. No Governance
10. Cross-Platform Reuse

I had never validated my own skills and plugins. Through 2026, organizations
including [Cyber Security News](https://cybersecuritynews.com/), the
[Cloud Security Alliance](https://cloudsecurityalliance.org/), and the
[Non-Human Identity Management Group](https://nhimg.org/) have documented the
same pattern: agent capabilities are spreading faster than the review around
them. A skill runs with the agent's privileges. A plugin can register a hook that
runs automatically. A remote MCP server sees what the agent sends it.

So I built the tool I wanted: a static auditor that inspects a skill or plugin
before installation, shows evidence, and never executes anything. I called it
**SkillTriage** — triage, not a verdict.

![A SkillTriage terminal scan of a deliberately risky example skill: a critical download-and-execute finding, an instruction-manipulation chain, and an approval bypass.](/assets/images/skilltriage-terminal.png)

*A failing scan: download-and-execute, an instruction-manipulation chain, and an approval bypass.*

## What it is

SkillTriage is a Python 3.11+ CLI with **zero third-party runtime
dependencies**. It reads a skill directory, a Claude Code plugin root, or a
`.zip`/`.tar.gz`, runs **107 rules** mapped to AST01–AST10, and emits text, JSON,
Markdown, SARIF, or a self-contained offline HTML report. It never executes
target code, fetches a URL, or calls a model — the property that makes it safe to
point at something you do not trust.

A plugin is treated as **one artifact**: manifest, commands, agents, bundled
skills, hooks, MCP servers, and marketplace entry are inspected together. The
riskiest part is often not a `SKILL.md`; it is the hook that runs on every tool
call, or the MCP server the manifest starts.

## What it looks like

The HTML report is one file: no CDN, fonts, external images, or network
requests; a restrictive CSP; owner-only permissions by default, because reports
can contain excerpts from the artifact.

![The SkillTriage HTML report: summary tiles, the target, and per-finding evidence, rationale, remediation, and CWE references.](/assets/images/skilltriage-report.png)

*The HTML report is one offline file: summary, evidence, rationale, remediation, and CWE references.*

The terminal output is the same data with fewer pixels: what failed, why, where
the evidence is, and how to fix it.

## What it catches

- **Execution and manipulation.** Download-and-execute, reverse shells,
  destructive commands, persistence, credential access, exfiltration, identity
  writes, prompt overrides, concealment, and approval bypasses.
- **Supply chain.** Unpinned or URL/VCS dependencies, install scripts,
  executable configuration, missing provenance, unpinned MCP launches, and
  cleartext MCP transport.
- **Over-privileged components.** Shell, filesystem, network, and tool scope;
  wildcard grants; plugin commands and agents asking for more than the task. A
  scoped `Bash(ls *)` is not broad; an unscoped `Bash(*)` is.
- **Metadata and hooks.** Unsafe YAML, duplicate keys, invisible characters,
  escaping or missing component paths; `PreToolUse`/`PermissionRequest` hooks
  that return an allow decision, escape the plugin root, or reference a missing
  script.
- **MCP and secrets.** `npx pkg@latest`, `uvx --from git+…`, images without a
  digest, non-loopback `http://`, literal header/env credentials (values are
  never stored), PEM and URL secrets, base64 payloads, invisible Unicode.
- **Context, not suppression.** Docs and examples lower noise, but outside a
  documentation path a critical finding cannot be talked down by a comment or a
  word such as “test”. Declared intent can downgrade technique rules only with an
  explicit policy allowance and a matching inventory hash.

## How it works

![The SkillTriage pipeline: target, safe load and normalize, 107 AST01–AST10 rules, context and correlation, then gate and report. It never executes target content or fetches a URL.](/assets/images/skilltriage-pipeline.png)

*Five stages, no execution and no network. The report formats are rendered only at the end.*

1. **Load safely.** Walk without following symlinks, open with `O_NOFOLLOW`,
   bound every read, and defend archive extraction against zip-slip, bombs,
   traversal, links, devices, and decompression.
2. **Parse safely.** A restricted YAML subset, `json` and `tomllib`, with
   explicit nesting bounds and no object construction.
3. **Normalize.** Skills and plugin artifacts become one model.
4. **Run 107 rules.** Score context and correlate credential + network, or
   manipulation + execution, into higher-severity chains. Correlations use code,
   `SKILL.md`, or structured plugin config — never command or agent prose.
5. **Gate and report.** Apply policy, suppressions, baseline, and declared
   intent; render text, JSON, Markdown, SARIF, or HTML.

The rule count is a map of coverage, not a quality score:

![Horizontal bar chart of 107 SkillTriage rules by OWASP control: AST01 Malicious Skills 24, AST02 Supply Chain Compromise 8, AST03 Over-Privileged Skills 14, AST04 Insecure Metadata 21, AST05 Untrusted External Instructions 4, AST06 Weak Isolation 8, AST07 Update Drift 7, AST08 Poor Scanning 10, AST09 No Governance 7, AST10 Cross-Platform Reuse 4.](/assets/images/skilltriage-rules-light.png)

*Rule distribution by OWASP control at the time of writing. Counts show coverage, not quality.*

## What I found on my machine

I ran it over my own installed corpus: **67 targets** — 43 Claude Code plugins
and 24 standalone skills — with **zero scan errors and zero rule errors**. Only
one target gated: an offensive-security skill I wrote myself. That is the case
the intent policy exists for.

The rest produced a handful of genuine findings — four unpinned MCP launches and
some low-severity duplicate component names — but no plugin gated under the
default policy. That is a useful result, not proof that those plugins are safe.
It means the configured checks did not find enough evidence to block.

## The part I care about most: not making things worse

A tool that reads hostile input has to survive hostile input. The loader refuses
a symlinked target root, never follows a symlink inside a target, bounds per-file
reads, and treats archive decompression and entry counts as attack surfaces.
Parsers cannot construct objects. Every report field is escaped for control,
bidi, and invisible characters before it reaches a terminal or HTML.

Two decisions came out of an independent review:

- **Inline suppressions are opt-in.** A `skilltriage:disable` comment lives
  inside the artifact, so honoring it by default would let a package silence its
  own findings. Baselines are the reviewed-acceptance mechanism; inline
  suppressions require `--trust-inline-suppressions`.
- **A target cannot weaken its own gate.** Project config is not auto-loaded from
  the current directory; it must be passed with `--config`. A declared intent is
  honored only when policy allows it and the inventory record's content hash
  matches the current artifact. Findings are downgraded, never removed.

The reviewer found three critical issues and a set of high and medium ones. The
critical issues were: a skill could suppress every finding against itself with a
comment, a planted project config could disable the gate, and a one-word context
trick could push a critical payload below the threshold. All three are fixed with
regression tests; the high and medium findings are fixed or documented as
limits. The full review, including what was not tested, is in
[`docs/security/review-v0.1.md`](https://github.com/cicada-369/SkillTriage/blob/main/docs/security/review-v0.1.md).

## What it does not do

- **No dynamic testing.** It does not execute hooks, start MCP servers, or
  observe runtime file and network activity. That is the sandboxed v0.2
  milestone, with its own threat model.
- **Hooks and MCP are inspected, not run.** Approval-injection detection follows
  the hook command and the script it directly references; an indirectly invoked
  script is a gap.
- **No signature verification.** Signature presence is recorded, not verified.
  Dependencies are inspected, not resolved, so transitive CVEs are out of scope.
  URLs are classified, not fetched.
- **Marketplace scope.** A marketplace manifest is evaluated only at an audited
  plugin root; standalone Connectors are not audited.
- **False positives happen** around security documentation, red-team tooling,
  and detector code. Context scoring, baselines, and intent are the controls. A
  clean report means the configured checks did not trigger; it does not prove
  safety.
- **Platform coverage.** The suite runs on Linux today; Windows and macOS file
  modes and archive semantics have not been exercised.

## Try it

SkillTriage is Apache-2.0 and lives at
[github.com/cicada-369/SkillTriage](https://github.com/cicada-369/SkillTriage).
It is not on PyPI in v0.1; install from source or use the single-file zipapp.

```bash
git clone https://github.com/cicada-369/SkillTriage.git
cd SkillTriage
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .

# Scan the default install locations
skilltriage scan

# One plugin, with a shareable offline report
skilltriage scan ~/.claude/plugins/cache/<market>/<plugin>/<version> \
  -o report.html --open

# A downloaded package, as SARIF for CI
skilltriage audit ./downloaded-skill --format sarif -o skilltriage.sarif
```

The default gate fails on HIGH or CRITICAL findings with HIGH confidence.
`--profile advisory` never fails; `--profile strict` gates at MEDIUM. For CI,
SARIF works with GitHub code scanning, and `--fail-on none` makes a scan
report-only.

If you maintain an offensive-security skill, declare its intent and inventory it
before allowing the downgrade:

```bash
# metadata.skilltriage.intent: offensive-security in SKILL.md
skilltriage scan --inventory --update-inventory
skilltriage scan --inventory --allow-intent offensive-security
```

The declaration alone changes nothing: the policy must allow the value and the
inventory hash must match the bytes you reviewed. The technique findings stay in
every report, with the downgrade visible.

More detail:
[plugin coverage](https://github.com/cicada-369/SkillTriage/blob/main/docs/PLUGINS.md),
[declared intent](https://github.com/cicada-369/SkillTriage/blob/main/docs/INTENT.md),
and the [rule catalog](https://github.com/cicada-369/SkillTriage/blob/main/docs/RULES.md).

## What’s next

The next layer is the one the tool refuses to fake: **sandboxed dynamic
testing**. Start the MCP server, run the hook, capture tool calls, and see what
the artifact actually does — behind explicit consent, network-none defaults, and
syscall/process observation. Static analysis tells you what to review; a sandbox
tells you what happened. After that: signature and content-hash verification,
SBOM/CVE resolution, and more plugin ecosystems.

If you try SkillTriage, the most useful thing you can send me is **what it gets
wrong**. False positives make a scanner easy to ignore; false negatives are
worse. Open an issue, or use the private security advisory flow for
vulnerabilities.

Your agent's skills are code. Audit them before you trust them.

---

**Bo Kaung** · Builder/Breaker/Defender · [LinkedIn](https://www.linkedin.com/in/bokaung) · [Hashnode](https://bokaung.hashnode.dev/)

*Further reading: the
[OWASP Agentic Skills Top 10](https://github.com/OWASP/www-project-agentic-skills-top-10)
and its [published site](https://owasp.github.io/www-project-agentic-skills-top-10/);
[SkillTriage](https://github.com/cicada-369/SkillTriage); the
[SARIF specification](https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html)
and [GitHub code scanning](https://docs.github.com/en/code-security/code-scanning).*
