---
name: gaokao-writing
description: >-
  Write Gaokao (Chinese National College Entrance Exam) full-mark essays through a rigorous seven-stage workflow: (1) topic comprehension 审题, (2) resource gathering 查找资料, (3) outline drafting 写提纲, (4) outline review 核对修改提纲, (5) full-text writing 写全文, (6) special-grade examiner scoring with modification feedback 高考语文特级阅卷老师评分提修改意见, and (7) iterative revision until score reaches 55+ on a 60-point scale. Use this skill whenever the user asks to "写高考作文", "gaokao essay", "满分作文", "高分作文", "高考语文作文", "高考写作", "高考真题作文", "语文特级教师评分", "高考阅卷", or needs help producing a Chinese college entrance exam essay that satisfies the strict grading criteria. The skill is grounded in 10 years of Gaokao essay prompts and full-mark sample essays (2016-2025) and the "审-立-构-材-语" five-dimension writing model.
---

# Gaokao Writing Skill

A complete, repeatable workflow for producing 55+ (out of 60) full-mark Gaokao essays.
Built on 10 years of real essay prompts and grading criteria, this skill uses a
**seven-stage loop** with an embedded "special-grade examiner" reviewer that scores
each draft and emits specific, actionable modification feedback.

Use this skill whenever the user wants to write, evaluate, or improve a Gaokao essay
and explicitly demands a high-scoring (55-60) deliverable.

## When to use

| Trigger phrase | Use this skill? |
|---|---|
| "帮我写高考作文 / 帮我写一篇高考满分作文" | Yes |
| "高考作文题目 + 写 / 高考真题作文" | Yes |
| "我想写一篇55+的高考作文" | Yes |
| "高考语文作文 / 高考写作 / 高考作文提分" | Yes |
| "需要语文特级教师打分 / 模拟阅卷" | Yes |
| "我想练习高考作文" | Yes |
| "想看往年高考作文题目和满分作文" | Yes (analysis mode) |
| "我想写一篇议论文 / 散文" (not Gaokao-specific) | No (use general writing) |
| "英文作文 / English essay" | No |

## Default output

- A complete Chinese Gaokao essay (800-1000 字) on a 2025-style or past-year prompt.
- Final score: **55-60/60** (一类卷).
- Three to five iterations of revision with explicit "before / after" diffs.
- One examiner scoring report per iteration using the official 60-point rubric.

---

## The seven-stage workflow

```
Stage 1                Stage 2              Stage 3          Stage 4
审题  →  查找资料  →  写提纲  →  核对修改提纲
                                                 ↓
Stage 7 (loop until score ≥ 55)  ←  Stage 6  ←  Stage 5
按意见修改                          评分提意见    写全文
```

The skill does not skip stages. It does not combine stages. It does not declare success
before the loop in Stage 7 returns a score ≥ 55.

### Stage 1 — 审题 (Topic Comprehension)

Produce a structured 审题 brief that includes:

1. **材料原题** (verbatim prompt)
2. **题型判断** (材料作文 / 命题作文 / 任务驱动型)
3. **核心概念** (1-3 key words)
4. **关系分析** (一元 / 二元 / 多元)
5. **任务指令** (文体 / 字数 / 身份 / 情境)
6. **立意方向** (3-5 candidate central claims)
7. **最佳立意** (top 1 with justification)

Output as a markdown table or numbered list, in Chinese.

Required minimum:
- 5 candidate central claims
- 1 best central claim with reasoning
- 1-2 sentence 立意 polarity ("正向 / 反向 / 辩证")
- 1-2 candidate 标题 (title) drafts

### Stage 2 — 查找资料 (Resource Gathering)

Gather concrete materials before writing. Output a structured 资料包 with:

1. **古例** (≥ 2 historical Chinese figures/events with detail)
2. **今例** (≥ 2 contemporary Chinese figures/events with detail)
3. **外例** (≥ 1 international figure/event with detail, optional but score-boosting)
4. **古诗文名句** (≥ 3 directly quotable lines, with source + meaning + usage)
5. **时政热点** (≥ 1 current event with date and impact)
6. **哲理概念** (≥ 1 philosophical concept useful for depth, e.g., 辩证统一 / 知行合一)
7. **三组可选素材组合** (3 different素材 packages from which the writer picks one)

Use web search, webfetch, or the bundled `references/topical-banks.md` for these.
Do not invent fake sources. If a piece of data is uncertain, label it "未确认" and
prefer a well-known fact.

### Stage 3 — 写提纲 (Outline Draft)

Produce a complete outline with:

- **标题** (working title, 8-15 字, novel and high-impact)
- **开头段** (≥ 100 字 draft)
- **主体段** (3-5 段落 outline, each with 中心句 + 1-2 素材 + 分析角度)
- **辩证段 / 拓展段** (optional, but score-boosting)
- **结尾段** (≥ 100 字 draft)
- **字数估算** (target 800-1000 字 total)

Output the outline in a tree structure so the writer can fill in body text in Stage 5.

### Stage 4 — 核对修改提纲 (Outline Review and Revision)

Apply the "五查" check before any prose is written:

| Check | Question | If NO, fix before proceeding |
|---|---|---|
| 1. 扣题 | Does every section directly serve the central claim? | Cut sections that drift |
| 2. 平衡 | Are the素材 均衡 (古今中外)? | Add missing 维度 |
| 3. 层次 | Is the 论证 层层递进, not flat? | Add 辩证段 or 拓展段 |
| 4. 详略 | Is the 详略 比例 合理 (主体详, 过渡略)? | Trim or expand |
| 5. 收束 | Does the 结尾 actually 升华, not just restate? | Rewrite 结尾 |

Output: a revised outline with a "修改理由" column for each change.

### Stage 5 — 写全文 (Full-Text Writing)

Write the full essay. Hard constraints:

- 800-1000 字 (count chars, not words)
- 段落数: 5-7 段
- 开头 ≤ 150 字, 结尾 ≤ 150 字
- 主体段 200-350 字 each
- 至少 1 处古诗文名句自然化用
- 至少 1 处当代人物或时政
- 至少 1 处辩证或反向思维
- 避免套话、避免翻译腔、避免网络流行语

Write in a literary but precise register. Avoid parallelism for its own sake.
Favor short, declarative sentences for arguments; favor longer, lyrical sentences
for emotional/reflective passages.

### Stage 6 — 高考语文特级阅卷老师评分提修改意见 (Examiner Scoring and Feedback)

This is the heart of the skill. Simulate a 高考语文特级阅卷老师 (special-grade
Gaokao Chinese examiner) and produce:

1. **评分** (score out of 60, with 一类/二类/三类/四类/五类 classification)
2. **分项得分**:
   - 审题 (10/10 max)
   - 立意 (15/15 max)
   - 内容 (15/15 max)
   - 结构 (10/10 max)
   - 语言 (10/10 max)
3. **具体修改意见** (≥ 5 distinct, actionable items, e.g., "第二段例子堆砌过多，
   建议保留1-2个并加分析") with priority 高/中/低
4. **加分建议** (≥ 2 specific suggestions to push score higher)
5. **减分风险** (≥ 2 risks to flag, e.g., "立意与某位考生高度雷同，疑似套作")

If the score is ≥ 55, the loop terminates and the essay is ready for delivery.
If the score is < 55, proceed to Stage 7.

### Stage 7 — 按意见修改 + 再次评分 (Iterative Revision)

For each unresolved 减分项 + 高/中优先级修改意见:

1. Edit the essay (do not rewrite; refine specific sections).
2. Note the change in a "修改记录" (revision log) with before/after snippets.
3. Re-score using Stage 6 rubric.
4. Loop until score ≥ 55 OR after 5 iterations (whichever first).

Hard cap: maximum 5 iterations. If after 5 iterations the score is still
< 55, surface the瓶颈 explicitly to the user with:
- The 2-3 highest-priority issues that survived all revisions
- A recommended next-step plan (e.g., "建议扩大素材积累" or "建议先做1周专门审题训练")

---

## Output package (deliver to user)

When the workflow completes, package the following:

1. **final essay** (`essay.md` — the 800-1000 字 final version)
2. **审题 brief** (`stage1-topical-analysis.md`)
3. **资料包** (`stage2-materials.md`)
4. **最终提纲** (`stage4-final-outline.md` with revision log)
5. **每次评分的评分报告** (`stage6-scorer-report-iter-N.md` for each iteration)
6. **修改记录** (`stage7-revision-log.md` showing before/after for each fix)
7. **最终成绩单** (`final-score.md` with score, breakdown, and one-paragraph 评语)

The final 评语 should be written in the voice of a 语文特级教师 and include
both strengths and growth areas for the writer.

---

## Scoring rubric (the 60-point system)

Use this rubric consistently in Stage 6.

| 维度 | 满分 | 一类(54-60) | 二类(48-53) | 三类(42-47) | 四类(36-41) | 五类(<36) |
|------|------|------------|------------|------------|------------|-----------|
| 审题 | 10 | 完全扣题 | 基本扣题 | 部分偏离 | 明显跑题 | 完全跑题 |
| 立意 | 15 | 深刻有思辨 | 较深刻 | 平实 | 肤浅 | 错误 |
| 内容 | 15 | 充实有层次 | 较充实 | 较单薄 | 空洞 | 套作 |
| 结构 | 10 | 严谨完整 | 较完整 | 基本完整 | 不完整 | 混乱 |
| 语言 | 10 | 流畅有文采 | 通顺 | 基本通顺 | 病句多 | 难以卒读 |

### 基础等级分 (initial 一类/二类/三类)

- 一类 (54-60): 审题立意 + 内容 + 结构 + 语言 ≥ 45, 整体优秀
- 二类上 (50-53): 审题立意 ≥ 18, 内容 ≥ 10, 结构 ≥ 7, 语言 ≥ 6
- 二类下 (48-49): 审题立意 ≥ 16, 整体合格
- 三类 (42-47): 审题立意 ≥ 12
- 四类及以下: 跑题、字数不足、套作、字迹过差

### 综合分调整 (modifier)

- 加分项: 文采 +1~2, 创新立意 +1~2, 思想深度 +1
- 减分项: 错别字 -1, 病句 -1, 套作 -3, 字数不足 -5~-10

---

## Related files

| File | Open when |
|---|---|
| [references/writing-model.md](references/writing-model.md) | You need the 审-立-构-材-语 5-dimension model in detail |
| [references/prompt-bank.md](references/prompt-bank.md) | You need real Gaokao prompts from 2016-2025 to practice on |
| [references/sample-essays.md](references/sample-essays.md) | You need full-mark sample essays to learn patterns from |
| [references/scorer-rubric.md](references/scorer-rubric.md) | You need the detailed examiner scoring rubric |
| [assets/title-bank.md](assets/title-bank.md) | You need a bank of high-impact 标题 to use or adapt |
| [assets/quote-bank.md](assets/quote-bank.md) | You need a bank of 古诗文名句 with usage examples |
| [evals/eval-prompts.md](evals/eval-prompts.md) | You need test prompts to evaluate the skill |

---

## Quality bar

A finished essay from this skill must:

- Score **≥ 55/60** on the official rubric
- Have an 开头 that **catches attention in 5 seconds**
- Have an 结尾 that **leaves a lasting impression**
- Use ≥ 1 古诗文名句 **naturally, not as a sticker**
- Use ≥ 2 concrete 中国人物 or 事件 with **specificity, not vagueness**
- Demonstrate **at least one layer of 辩证 thinking** beyond the surface
- Be **free of 网络流行语, 翻译腔, and 假大空 rhetoric**

If any of these fail, return to the relevant stage. Do not deliver.

## Common failure modes to avoid

1. **套作** — Pre-written essays that ignore the specific prompt. The skill must
   always start from the actual 材料 and re-derive 立意, 素材, 标题.
2. **跑题** — Essays that look pretty but miss the core 立意. Stage 1 must be
   done rigorously, and Stage 4 must explicitly verify 扣题.
3. **同质化** — All essays sounding the same because the writer used the same
   outline and same素材. Stage 2 must require 3 distinct 素材 packages and the
   writer must pick based on the specific prompt.
4. **空喊口号** — "作为新时代青年，我们要……" with no substantive content.
   Forbid this sentence pattern; demand concrete examples and analysis.
5. **文化堆砌** — Listing 10 名人名言 without weaving them into an argument.
   Require at most 3-4 direct quotes, each with 1-2 sentences of analysis.
6. **结尾平淡** — "让我们共同努力" 等套话. Forbid this; require the 结尾 to
   achieve 升华 with a memorable image, paradox, or call to action.

## Source notes

This skill is derived from public, official sources:

- 教育部考试中心 (National Education Examinations Authority) 2016-2025 命题思路报告
- 各省教育考试院 阅卷标准 (Beijing, Shanghai, Jiangsu, Zhejiang, etc.)
- 主流媒体公开的高分/满分作文与阅卷组点评 (高考网, 学科网, 21世纪教育网, 求学网, 北京高考在线, 文易搜, etc.)
- 语文特级教师公开发表的阅卷经验与写作教学论文

All bundled materials are based on public-domain or fair-use excerpts. The skill
makes no claim on individual copyrighted essays and uses them only for educational
pattern analysis, not for verbatim reproduction.
