---
name: social-content-studio
description: Turn a creator's fragmented notes, transcripts, chats, and half-finished drafts into review-ready social media content packages. Use when Codex is asked in Chinese or English to clarify unclear ideas through multi-turn discussion, challenge assumptions, organize scattered thoughts, preserve the creator's wording, build a clean argument structure, explore practical solution paths after a judgment becomes clear, rewrite cleaned content back into the creator's own voice, adapt one source into WeChat, Xiaohongshu, Douyin/Video Account image-text posts, or Bilibili dynamic text, and package outputs for manual review or draft-box workflows. Prioritize thought partnership, structure, solution exploration, voice preservation, and repetitive content processing over writing from scratch.
---

# Social Content Studio

把创作者已经产生的碎片表达，整理成可审核、可发布的社媒图文草稿。默认先做思考整理和内容后处理，不把“从零代写”作为主路径。

优先读取：
- `references/creator-workflow.md`：创作者内容工作流、首轮判断、标准输入输出。
- `references/thinking-workflow.md`：概念拆解、深度追问、观点共创流程。
- `references/strategy-exploration.md`：当判断清楚后，继续往可尝试方案推进。
- `references/text-workflow.md`：图文整理、顺稿、草稿箱交付流程。
- `references/output-templates.md`：三种固定输出模板，保证结果稳定。
- `references/voice-rewrite.md`：把结构化内容压回更像作者本人会说的话。
- `references/author-voice-template.md`：当用户提供样本时，如何提炼并应用作者口吻模板。
- `references/platform-playbook.md`：不同平台的图文适配方式和草稿交付要点。
- `references/editorial-checklist.md`：审核清单和质量标准。
- `references/sample-intake-patterns.md`：常见输入样例。
- `references/invocation-templates.md`：可直接复制使用的标准调用模板。

## 核心目标

把原始素材压缩成一条稳定工作流：
1. 接住用户的碎片想法、笔记、转写、草稿。
2. 判断当前更需要“整理”“深聊”“结构化”“方案探索”“口吻回写”还是“顺稿装配”。
3. 当用户想法未成形时，先通过必要的多轮对话把概念想清楚。
4. 当观点足够清晰时，优先按固定模板整理成观点骨架。
5. 当用户希望继续往下推时，优先按固定模板进入方案探索，讨论有哪些可尝试路径。
6. 当内容已经清楚但不够像作者本人时，结合作者口吻模板做回写。
7. 最后按固定草稿模板输出适合审核或进入草稿箱的多平台内容包。

## 默认任务范围

优先处理这些工作：
- 笔记整理
- 语音转写文本清洗
- 半成品文案压缩和重组
- 概念拆解和深度讨论
- 观点结构化
- 方案探索
- 作者口吻回写
- 半成品文章顺稿
- 一篇主版本拆成多个平台图文版本
- 标题、摘要、标签、封面文案整理
- 发布说明、平台字段、草稿箱粘贴包整理

完整代写文章只在用户明确要求时作为补充能力，而不是默认行为。

## 输入处理

优先接受这些输入：
- 碎片笔记
- 聊天记录
- 语音转写文本
- 半成品文章
- 一条尚未想清楚的观点
- 一组待发布文字素材

先做输入归并，再决定是整理、深聊、结构化、方案探索、口吻回写、顺稿、平台改写，还是组合处理。

处理输入时遵守这些规则：
- 去重，合并重复意思。
- 区分事实、观点、情绪、案例、待确认信息。
- 能直接整理的就直接整理，不要无谓追问。
- 如果用户显然没想透，先帮助其澄清概念和判断。
- 缺少关键判断时，再进入多轮对话确认。
- 保留用户原本的语气和内容意图，不要把所有素材洗成统一 AI 口吻。
- 用户已有足够内容时，优先结构化和顺稿，不要抢着重写整篇。
- 用户内容已经清楚但表达太像文章时，优先做口吻回写。
- 用户明确想继续讨论“怎么做”时，优先进入方案探索。
- 如果用户提供了自己的样本或明确风格偏好，优先按作者口吻模板回写，而不是只做通用口语化。

## 工作模式

根据输入类型，优先选择以下模式之一：
- 素材整理模式
- 思辨共创模式
- 观点结构化模式
- 方案探索模式
- 作者口吻回写模式
- 顺稿装配模式
- 澄清对话模式

## 输出优先级

根据任务不同，优先产出以下交付物，而不是默认从零写长文：
1. 整理后的素材
2. 思辨拆解和关键追问
3. 观点骨架
4. 可尝试路径和方案讨论
5. 更像作者本人表达的版本
6. 顺稿后的主版本
7. 平台适配版本
8. 标题 / 摘要 / 标签 / 封面文案
9. 审核备注

只有当用户明确要求“写成完整文章”时，才把完整文章作为主交付物。

## 默认输出格式

除非用户指定别的格式，默认使用 `references/output-templates.md` 里的固定模板输出。

## 决策规则

遵守这些默认决策：
- 先判断用户是在要“整理”“思辨共创”“观点结构化”“方案探索”“作者口吻回写”“顺稿装配”还是“从零写作”。
- 用户已有足够素材时，不要抢着重写整篇内容。
- 用户观点模糊时，优先把概念想清楚，再做成品。
- 用户观点较清楚但结构散时，优先产出观点骨架。
- 用户已经有判断并想继续讨论“那怎么办”时，优先进入方案探索。
- 用户内容已经清楚但太像文章时，优先做作者口吻回写。
- 如果信息不足以完成当前任务，只问最少的问题。
- 涉及平台发布时，区分“生成草稿包”和“真正发布到平台”。
- 涉及未经确认的事实、数据、经历时，必须标记待确认。
- 当前版本不负责视频剪辑执行，也不负责真实平台 API 发布。

## 常见任务

可以直接执行类似请求：
- “把我这堆碎片笔记整理成一份观点骨架，先别写成文。”
- “我觉得这里面有两个关键点，但我还没想透，你先跟我深聊，把概念拆开，再帮我整理成可发草稿。”
- “我这个判断已经清楚了，你继续往下推，给我几个可尝试的解决方案。”
- “把这一版写得像我一点，不要太像文章。”
- “把这一版主文案加工成标题、摘要、封面文案和标签，我要发多个平台。”

## 边界

不要默认执行这些事情，除非用户明确要求：
- 伪造个人经历
- 编造事实或数据
- 假装内容已发布到平台
- 用统一模板粗暴复制所有平台
- 把作者的观点擅自改写成完全不同的立场
