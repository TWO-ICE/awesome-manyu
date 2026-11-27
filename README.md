<div align="center">
  <img src="assets/banner.png" alt="Awesome 漫剧 · 开源 AI 漫剧工具集合" width="100%" />
</div>

# 🎬 Awesome 漫剧 · 开源 AI 漫剧 / AI 短剧工具集合

> ## 📌 置顶推荐 · 洛书 AI Canvas（低价 AI 影视 / 漫剧创作工作台）
>
> **在线使用**：<https://canvas.luoshu.wavesbig.cn>
>
> 基于开源项目 [*ddcat-ai/open-ai-canvas*（影策）](https://github.com/ddcat-ai/open-ai-canvas) 二次开发，接入自有低价渠道 —— 无限画布 + 剧本分镜 + 多模态生成 + Agent 工作流，主打一个**便宜可用**。
>
> | 能力 | 规格 | 价格 |
> |---|---|---|
> | 视频生成 | 480p | **¥0.06 / 秒** |
> | 视频生成 | 768p | **¥0.12 / 秒** |
> | 视频超分 | 1K | **¥0.08 / 秒** |
> | 视频超分 | 2K | **¥0.16 / 秒** |
> | 图片生成 | gpt-image-2.6 | **¥0.10 / 张** |
>
> 🙏 **致谢原项目**：本项目站在 [ddcat-ai/open-ai-canvas](https://github.com/ddcat-ai/open-ai-canvas)（MIT 协议，2064⭐，官网 <https://yingce.tv>）的肩膀上，感谢原作者开源。此处致谢原项目与自家部署版本，两者请勿混淆。

> 中文世界最全的开源漫剧工具地图：**按生产流水线分类 · License 红绿灯 · 数据每周自动刷新**

<!-- manyu:meta -->
📊 收录 **271** 个项目 ｜ 数据更新于 **2026-11-27** ｜ 由 GitHub Actions 每周自动刷新
<!-- /manyu:meta -->

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](./LICENSE)
[![Auto Refresh](https://img.shields.io/badge/data%20refresh-weekly-blue)](.github/workflows/refresh.yml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)

---

## 🧭 三步上手

| 你的需求 | 直接看 |
|---|---|
| 一句话 / 一个想法出片 | [火宝短剧](#一all-in-one-一站式平台) · [VideoClaw](#一all-in-one-一站式平台) |
| 手里有小说想改编漫剧 | [Toonflow](#一all-in-one-一站式平台) · [ArcReel](#一all-in-one-一站式平台) · [LumenX](#一all-in-one-一站式平台) · [网文改编专题](#四网文改编专题-征集中) |
| 想本地跑、数据不出本机 | [LocalMiniDrama](#一all-in-one-一站式平台) · [ComfyUI](#31-生图与角色一致性) 自建 |
| 只想补某一个环节 | 按 [生产流水线](#三生产流水线单环节工具) 找：生图 / 生视频 / 配音 / 翻译 / 合成 |

## 🚦 License 图例

| 标记 | 含义 |
|---|---|
| ✅ | 宽松协议（MIT / Apache-2.0 等），可自由商用 |
| 📚 | Copyleft（GPL / AGPL 等），可商用但有传染性，商用前读条款 |
| ⚠️ | 自定义协议或含 NC（禁商用）条款，**商用前必须读原仓库 LICENSE 原文** |
| ❌ | 无有效开源协议 / 明确仅限研究用途 |
| 🏢 | 超过 12 个月未更新，疑似停止维护 |

---

## 一、All-in-ONE 一站式平台

剧本到成片全流程覆盖，开箱即用。

<!-- manyu:table:allinone -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [OpenMontage](https://github.com/OpenMontageInc/OpenMontage) | 83734 | 全球最大开源 AI 视频生产系统：12 条生产流水线、100+ 工具、Agent 驱动，一句话创意到成片 | 📚 AGPL-3.0 |
| [Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | 22994 | 无限画布 AI 视频创作平台：剧本创作、智能分镜、角色场景资产管理、生图生视频 | ✅ MIT |
| [huobao-drama](https://github.com/chatfire-AI/huobao-drama) | 18038 | 一句话生成完整短剧：剧本→分镜→视频→配音→FFmpeg 合成全自动 | ⚠️ CC BY-NC-SA |
| [waoowaoo](https://github.com/waooAI/waoowaoo) | 14991 | 工业级全流程 AI 影视生产平台，短片到真人级影视 | ⚠️ Elastic-2.0 |
| [dramaclaw](https://github.com/dramaclaw/dramaclaw) | 7226 | 通用 AIGC 视频引擎：剧本到成片一条流水线 | ⚠️ Elastic-2.0 |
| [Jellyfish](https://github.com/Forget-C/Jellyfish) | 7356 | 端到端生产工作台：章节脚本→分镜与关联资产 | ✅ Apache-2.0 |
| [ArcReel](https://github.com/ArcReel/ArcReel) | 6799 | 小说/剧本→角色场景道具资产→分镜→视频→剪映草稿 | 📚 AGPL-3.0 |
| [printfilm](https://github.com/yi1108/printfilm) | 7151 | 模板驱动 AI 短视频/漫剧平台（FastAPI），含计费与管理后台、开放 API | ✅ MIT |
| [moyin-creator](https://github.com/MemeCalculate/moyin-creator) | 4881 | AI 影视生产级工具，支持 Seedance 2.0，剧本到成片批量化 | 📚 AGPL-3.0 |
| [LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | 2563 | 纯 JavaScript 本地运行，数据零上传，支持 AI 真人剧+漫剧 | ✅ MIT |
| [AIComicBuilder](https://github.com/LingyiChen-AI/AIComicBuilder) | 1987 | AI 动态漫画生成器：脚本→分格→成片 | ✅ Apache-2.0 |
| [VideoClaw](https://github.com/HITsz-TMG/VideoClaw) | 1926 | AI 全自动化视频生成员工：一个想法→完整短剧/漫剧 | ✅ MIT |
| [lumenx](https://github.com/alibaba/lumenx) | 1513 | 阿里开源：小说文本→剧本分析→角色定制→分镜→动态漫剧视频 | ✅ MIT |
| [aid-studio](https://github.com/shijue-aid/aid-studio) | 1831 | 自托管 AI 短剧/动态漫画工作室，Docker/systemd 部署，多模型多供应商 | ✅ MIT |
| [OpenMontage](https://github.com/charliewwdev/OpenMontage) | 71 | 自托管AI短剧工坊：剧本→角色场景道具→分镜→视频→配音剪辑 | 📚 AGPL-3.0 |
| [ViMax](https://github.com/HKUDS/ViMax) | 13042 | Agentic 视频生成：导演 Agent 驱动，从想法到成片自动化 | ✅ MIT |
| [BigBanana-AI-Director](https://github.com/shuyu-labs/BigBanana-AI-Director) | 2483 | 工业级一站式 AI 短剧导演：定妆→搭景→分镜→成片全程可控 | ⚠️ 自定义（读原文） |
| [ai_story](https://github.com/xhongc/ai_story) | 2133 | AI 视频/动漫/漫剧自动化生成工具，故事输入成片输出 | ⚠️ 自定义（读原文） |
| [ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | 1824 | 融光：基于 Agent 的全流程 AI 短剧/漫剧/视频创作平台 | ✅ MIT |
| [LingGuo-Drama](https://github.com/LingGuoAI/LingGuo-Drama) | 1692 | 灵果短剧 AI：一句话生成完整短剧/漫剧 | ⚠️ 自定义（读原文） |
| [infinite-creation](https://github.com/SwotAtmk/infinite-creation) | 426 | 提交小说/剧本，本地 ComfyUI 全流程出片 | ⚠️ 自定义（读原文） |
| [VideoAgent](https://github.com/HKUDS/VideoAgent) | 2160 | [EMNLP2026] "VideoAgent: All-in-One Agentic Framework for Vide… | ✅ MIT |
| [ai-shortVideo-pipeline](https://github.com/myccarl/ai-shortVideo-pipeline) | 865 | End-to-end AI short-video production pipeline. FastAPI orchest… | ✅ MIT |
| [TapCanvas](https://github.com/anymouschina/TapCanvas) | 733 | 面向 AI 影视、漫剧与多模态内容生产的 Agent 原生无限画布, 主推一键成片 agent，编排可控 | ✅ MIT |
| [Open-AI-Micro-Drama-Generator](https://github.com/Anil-matcha/Open-AI-Micro-Drama-Generator) | 593 | AI short drama & micro-drama video generator — turns any idea … | ⚠️ 自定义（读原文） |
| [AI-drama-pound](https://github.com/POUND0423/AI-drama-pound) | 573 | AI drama pound | ✅ MIT |
| [ViralForge](https://github.com/fendouai/ViralForge) | 559 | Agent-native viral video studio: deconstruct scripts, replicat… | ✅ Apache-2.0 |
| [aipdd-drama-agent](https://github.com/liujh0729-jpg/aipdd-drama-agent) | 524 | aipdd开源的集成画布与agent，实现短剧制作 | ⚠️ 自定义（读原文） |
| [motion-previs-studio](https://github.com/wassermanproductions/motion-previs-studio) | 386 | Open-source desktop app for AI-film motion, depth, pose, and c… | ✅ Apache-2.0 |
| [open-apex-drama](https://github.com/Sxuan-Coder/open-apex-drama) | 329 | 第三方红果短剧客户端，免登录、免广告、免费使用，支持真人剧、AI漫剧、AI短剧等多种短剧。支持Windows和安卓双端播放 | 📚 AGPL-3.0 |
| [Drama3-Studio](https://github.com/nkxx188/Drama3-Studio) | 289 | The simplest, most user-friendly Drama3 creation tool, deeply … | ✅ MIT |
| [OpenReels](https://github.com/tsensei/OpenReels) | 250 | Open-source AI pipeline that turns any topic into a publish-re… | ✅ MIT |
| [hongguo-android-cast](https://github.com/skydeadpeng/hongguo-android-cast) | 196 | 红果短剧（Hongguo Drama）+ 黄果漫剧（Huangguo）多端客户端：Android 手机 / Android … | 📚 GPL-3.0 |
| [juben](https://github.com/VanGong1999/juben) | 194 | multi-agent platform for short-drama planning, writing & evalu… | ✅ MIT |
| [MiniMaxH3-Studio](https://github.com/rookiestar28/MiniMaxH3-Studio) | 166 | Direct MiniMax H3 like a pro: Idea in, finished video out. A c… | ✅ Apache-2.0 |
<!-- /manyu:table:allinone -->

## 二、🤖 编剧与 Agent Skills（漫剧圈新物种）

给 Claude Code / Codex 等 Agent 用的技能包，不装平台、直接在终端里排生产。

### 2.1 📝 编剧 / 网文改编

<!-- manyu:table:writing -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | 8092 | 基于 Claude Code 的长篇网文辅助创作系统：一致性与长程记忆 | 📚 GPL-3.0 |
| [human-writing](https://github.com/KKKKhazix/human-writing) | 4776 | 让 AI 写的中文读起来像一个具体的人，通用创作与改稿 Skill | ✅ MIT |
| [sepia](https://github.com/Nanako0129/sepia) | 3964 | 去 AI 味写作 Skill，任意 Agent 可装 | ✅ MIT |
| [screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills) | 2195 | 专业影视编剧 Agent 技能集 | ✅ MIT |
| [short-drama](https://github.com/0xsline/short-drama) | 1687 | 专业短剧剧本创作：选题立项→分集撰写→质量自检→合规审核→海外 | ✅ MIT |
| [shanyin-screenwriting-master](https://github.com/Shanyin-ai/shanyin-screenwriting-master) | 1546 | 山音超级编剧：全格式影视编剧技能，1-3 分钟到长剧全覆盖 | ✅ MIT |
| [Chinese-WebNovel-Skill](https://github.com/Tomsawyerhu/Chinese-WebNovel-Skill) | 1072 | 中文网文小说写作 skill | ⚠️ 自定义（读原文） |
| [narrative-to-screen-reader](https://github.com/zhlmi/narrative-to-screen-reader) | 141 | 叙事转译：把手上的故事翻译成影视开发语言 | ⚠️ 自定义（读原文） |
| [novel-to-manju](https://github.com/senmanx/novel-to-manju) | 86 | 小说转漫剧短视频全流程提示词 Skill：爆款改文→剧本→人物场景资产 | ⚠️ 自定义（读原文） |
| [novel-to-ai-short-drama-skill](https://github.com/muxia0396/novel-to-ai-short-drama-skill) | 35 | 小说改编 AI 短剧：分镜、运镜、表演调度与时长 | ✅ MIT |
| [inkos](https://github.com/Narcooo/inkos) | 11469 | Story Creation AI Agent for novel, scripts, translation, inter… | 📚 AGPL-3.0 |
| [oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode) | 8969 | 网文写作 Agent 技能包：扫榜、拆文、大纲细纲、长短篇连载、伏笔追踪、去AI味与封面生成，适配 Claude Code … | ✅ MIT |
| [AI_NovelGenerator](https://github.com/YILING0013/AI_NovelGenerator) | 6554 | 使用ai生成多章节的长篇小说，自动衔接上下文、伏笔 | 📚 AGPL-3.0 |
| [AI-Novel-Writing-Assistant](https://github.com/ExplosiveCoderflome/AI-Novel-Writing-Assistant) | 3570 | 面向长篇小说创作的 AI Native 开源系统，用 Agent、世界观、写法引擎、RAG 和整本生产工作流，帮助新手从一句… | 📚 AGPL-3.0 |
| [ComfyUI_VNCCS](https://github.com/AHEKOT/ComfyUI_VNCCS) | 1809 | Visual Novel Character Creation Suite is a comprehensive tool … | ✅ MIT |
| [reveric](https://github.com/looplj/reveric) | 1031 | Agent Native 一站式 AI 小说，短剧桌面创作工作台 | 📚 AGPL-3.0 |
| [oh-story-dsh](https://github.com/zenstory-ai/oh-story-dsh) | 839 | DeepSeek Harness 故事创作插件：集成网文写作、短剧漫剧、小说改游戏与视频解说四个可视化工作台 ｜ DeepS… | ✅ MIT |
| [SonicVale](https://github.com/xcLee001/SonicVale) | 658 | 一个开源的多角色、多情绪 AI 配音生成平台，支持小说、剧本、视频等内容的自动配音与导出。 | 📚 AGPL-3.0 |
| [rea-toon](https://github.com/JuneYaooo/rea-toon) | 338 | AI 拆解学习短剧：为什么火、剧本怎么写、每一镜怎么拍 | Break down any short drama with … | ⚠️ 自定义（读原文） |
| [AI_novel](https://github.com/tyxben/AI_novel) | 270 | AI 小说推文自动化 - 小说一键转短视频（有声书+AI配图），适用于抖音/小红书 | ✅ MIT |
| [huobao-drama-ai](https://github.com/dav-niu474/huobao-drama-ai) | 113 | 🎬 AI短剧创作平台 — 从剧本到成片，一站式AI短剧制作工作台。支持70+大模型(GLM5.1/DeepSeek V4/Q… | ✅ MIT |
<!-- /manyu:table:writing -->

### 2.2 🧰 全流程技能包

<!-- manyu:table:skills -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [shuohao-skills](https://github.com/eternityspring/shuohao-skills) | 7213 | AI 短剧制作 skill 集合：拆角色、排大纲、出场景道具设定、写剧本、切分镜 | ✅ Apache-2.0 |
| [drama-skills](https://github.com/zenstory-ai/drama-skills) | 5108 | 短剧/漫剧 skill 合集：剧本、角色资产、分镜、图/视频提示词、审查，适配 Claude Code 与 Codex | ✅ MIT |
| [story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | 2549 | 中文故事文案→手绘白板动画视频 | ✅ MIT |
| [ai-shotlive](https://github.com/sorker/ai-shotlive) | 355 | 小说→剧本→分镜→提示词→关键帧→视频→AI 剪辑一站式 | ⚠️ 自定义（读原文） |
| [manju-laoli-skill](https://github.com/lixiaoxiao9888-create/manju-laoli-skill) | 3290 | 漫剧老李 AIGC 创作全流程多技能套装 | ✅ MIT |
| [XiaoLuo-AI-Drama-Skill](https://github.com/zhurui0523/XiaoLuo-AI-Drama-Skill) | 534 | 小罗 AI 漫剧创作技能包 | ⚠️ 自定义（读原文） |
| [short-drama-factory](https://github.com/lixiaoxiao9888-create/short-drama-factory) | 698 | Short-Drama Factory：抖音/红果爆款短剧工厂 | ✅ MIT |
| [screen-creative-skills](https://github.com/VanGong1999/screen-creative-skills) | 527 | 影视创作技能集合：编剧到导演全链路 | ✅ MIT |
| [OnlyShot](https://github.com/A-cat-with-carrots/OnlyShot) | 431 | 神仙鱼 AI 短剧工业流水线 Claude Skill | ✅ MIT |
| [Micro-Drama-Skills](https://github.com/zhaihao118/Micro-Drama-Skills) | 345 | AI 驱动的短剧全流程自动化制作系统（Claude Skills） | ⚠️ 自定义（读原文） |
| [DirectorSKILL](https://github.com/wuwangzhang1216/DirectorSKILL) | 428 | Claude Code AI 电影制作技能 | ✅ MIT |
| [workrally](https://github.com/Tencent/workrally) | 210 | 腾讯：面向 AI Agent 的 AIGC 漫剧视频创作全流程工具集 | ⚠️ 自定义（读原文） |
| [film-studio-skills](https://github.com/machina-exm/film-studio-skills) | 186 | 7 个可安装的电影制片厂 Agent 技能 | ⚠️ 自定义（读原文） |
| [ComfyUI-Agent-Kit](https://github.com/SlavaSexton/ComfyUI-Agent-Kit) | 125 | 给 AI coding agent 用的一个 ComfyUI 全能技能 | ✅ Apache-2.0 |
| [ai-film-skills](https://github.com/62656456/ai-film-skills) | 156 | Open Film Skills：21 个独立模块化电影技能 | ✅ Apache-2.0 |
| [ai-short-drama-skill](https://github.com/xixihhhh/ai-short-drama-skill) | 119 | Dramake：面向 Codex / Claude Code / WorkBuddy 的短剧技能 | ✅ MIT |
| [ai-short-drama](https://github.com/Hao0321/ai-short-drama) | 85 | AI 短剧故事架构与剧本创作 skill | ✅ MIT |
| [open-source-video-gen-skill](https://github.com/mini-yifan/open-source-video-gen-skill) | 43 | Vibe Video：一句话想法→成片，开源 MiniMax H3 方案 | ⚠️ 自定义（读原文） |
| [spark-video](https://github.com/JohnKeating1997/spark-video) | 35 | AI 视频生产 skill：premise→成片 | ⚠️ 自定义（读原文） |
| [humanizer](https://github.com/blader/humanizer) | 74121 | Agent skill that removes signs of AI-generated writing from text | ✅ MIT |
| [Recordly](https://github.com/webadderallorg/Recordly) | 37556 | Create polished demo videos without editing skills. Mac/Window… | 📚 AGPL-3.0 |
| [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 22955 | AI video skill for Claude Code & Codex — cinematic, editable p… | ✅ Apache-2.0 |
| [capcut-mate](https://github.com/Hommy-master/capcut-mate) | 2214 | 开源剪映小助手｜剪映API | 扣子插件 | Open-source CapCut automation toolkit t… | ✅ Apache-2.0 |
| [violin](https://github.com/shang-zhu/violin) | 1089 | Open-source Video Translation Skill | ✅ MIT |
| [Nomi](https://github.com/aqm857886159/Nomi) | 670 | Open-source AI video workbench. Bring any model or your local … | 📚 AGPL-3.0 |
| [DaVinci-AutoEdit-Agent](https://github.com/liuluhaixiu/DaVinci-AutoEdit-Agent) | 532 | AI自动剪辑的“第一次接触”，一款基于davinci mcp的全自动自媒体视频剪辑skill | ✅ MIT |
| [h3lite](https://github.com/Rimagination/h3lite) | 528 | A hardware-aware Codex skill for local MiniMax H3 video genera… | ✅ MIT |
| [marketplace](https://github.com/aiskillstore/marketplace) | 501 | Security-audited skills for Claude, Codex & Claude Code. One-c… | ⚠️ 自定义（读原文） |
| [ai-anime-series](https://github.com/10291124jcjc-dotcom/ai-anime-series) | 433 | AI 动画单元剧：固定原创角色，一句话出一集。角色设定图 + 宫格故事板 + 即梦 Seedance 一次生成。Claude… | ⚠️ 自定义（读原文） |
| [Orkas-VideoStudio](https://github.com/Orkas-AI/Orkas-VideoStudio) | 382 | Open-source alternative to Claude Motion and CapCut: your codi… | ✅ MIT |
| [pai-code](https://github.com/Utopai-Research/pai-code) | 362 | Local AI filmmaking studio — skills, canvas, timeline — driven… | ⚠️ 自定义（读原文） |
| [video-skills-toolkit](https://github.com/bozhouDev/video-skills-toolkit) | 169 | Video skills toolkit for Remotion talking-head, sketch story, … | ✅ MIT |
<!-- /manyu:table:skills -->

### 2.3 🎬 导演 / 分镜 / 镜头设计

<!-- manyu:table:directing -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [Seedance2-Storyboard-Generator](https://github.com/liangdabiao/Seedance2-Storyboard-Generator) | 2970 | Seedance 分镜生成：故事→直接能拿去出图出视频的制作文档 | ⚠️ 自定义（读原文） |
| [seedance-2-5-video-director](https://github.com/liyue-aigc/seedance-2-5-video-director) | 825 | Seedance 2.5 视频导演 Skill：提示词、脚本、诊断、人物锁定 | ✅ MIT |
| [shanyin-director-master](https://github.com/Shanyin-ai/shanyin-director-master) | 654 | 山音超级导演：导演定调→节奏规划→剧本微调→分镜拆解 | ✅ MIT |
| [visual-skills](https://github.com/smixs/visual-skills) | 773 | AI 电影导演技能集：电影语言与视觉叙事 | ✅ CC-BY-4.0 |
| [h3-storyboard-skill](https://github.com/phileiny/h3-storyboard-skill) | 201 | MiniMax H3 分镜/运镜 Claude Code skill | ✅ MIT |
| [short-drama-production](https://github.com/suihe1/short-drama-production) | 207 | 短剧生产总控 skill：专业导演分镜 + MiniMax H3 | ✅ Apache-2.0 |
| [Seedance-ShotDesign-Skills](https://github.com/woodfantasy/Seedance-ShotDesign-Skills) | 139 | Seedance 2.5 镜头设计技能 | ⚠️ MIT-0 |
| [seedance-2-5-fight-director](https://github.com/liyue-aigc/seedance-2-5-fight-director) | 141 | Seedance 2.5 高燃动作戏导演 skill（Codex） | ⚠️ 自定义（读原文） |
| [fight-video-create-skill](https://github.com/qualsenWeb/fight-video-create-skill) | 118 | AI 打斗视频创作/设计技能 | ⚠️ 自定义（读原文） |
| [fight-prompt-director](https://github.com/irenerachel/fight-prompt-director) | 90 | AI 动作导演：打斗场面提示词编排 | ✅ MIT |
| [seedance-skill](https://github.com/alchaincyf/seedance-skill) | 71 | 白模驱动的 AI 视频工作台（Seedance） | ✅ MIT |
| [acheng-director-skill](https://github.com/AharaOoO/acheng-director-skill) | 79 | 阿城导演：电影级导演综合引擎 | ✅ Apache-2.0 |
| [muse-video-skill](https://github.com/LuoJiangYong/muse-video-skill) | 216 | 视频创作虚拟剧组引擎：创意→剧本/分镜/美术/提示词 | ✅ MIT |
| [storyboard-director](https://github.com/kevinchin12/storyboard-director) | 37 | 提示词可控的分镜 skill（Codex） | ✅ MIT |
| [story-video-director](https://github.com/zlbigger/story-video-director) | 35 | 任意故事→图片素材、分镜、中文视听提示词与 API 清单 | ✅ MIT |
| [stickman-video-director](https://github.com/kaomei/stickman-video-director) | 8609 | AI Agent Skill (Claude Code, Codex & more): Turn any script in… | ✅ MIT |
| [ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) | 2924 | Multi-segment MiniMax H3 Director for official ComfyUI MiniMax… | ✅ Apache-2.0 |
| [open-ai-canvas](https://github.com/ddcat-ai/open-ai-canvas) | 2064 | 【影策】面向 AI 影视创作的开源无限画布工作台，集成多模态生成、分镜编排、素材管理与 Agent 工作流。 | ✅ MIT |
| [infinite-canvas](https://github.com/tigerowo/infinite-canvas) | 1805 | 开源 AI 创作工作台，集成无限画布、Agent、导演台、全景图、AI 生图、图片编辑、视频生成、画布编排等，兼容 Open… | 📚 AGPL-3.0 |
| [ai-moive-studio](https://github.com/869413421/ai-moive-studio) | 1672 | 自然语言驱动的无限画布工作流 Agent，让 AI 视频创作第一次真正变成可编辑的工作流。 AICON 面向创作者，提供从剧… | ✅ Apache-2.0 |
| [aimangastudio](https://github.com/morsoli/aimangastudio) | 1509 | 一个利用 AI 制作漫画的工具，支持脚本创作、分镜设计和角色风格控制。访问地址：https://aimangastudio.… | ⚠️ 自定义（读原文） |
| [StoryGen-Atelier](https://github.com/0xsline/StoryGen-Atelier) | 1029 | AI-assisted storyboard and video generation tool. Uses Gemini … | ✅ Apache-2.0 |
| [Maestro](https://github.com/Blizaine/Maestro) | 1021 | An all-in-one, 100% local AI video, image, and music studio. D… | ⚠️ 自定义（读原文） |
| [novanova-studio](https://github.com/Swayingleaves/novanova-studio) | 1020 | [NovaNova Studio] 一个 Agent 驱动的集 AI图片生成、AI视频生成、无限画布、自定义模型 API 、… | ✅ MIT |
| [storyai-3d-director-desk](https://github.com/jiguang132/storyai-3d-director-desk) | 908 | A browser-based 3D director desk demo built with React, Vite, … | ✅ MIT |
| [director](https://github.com/s1dashu/director) | 889 | Direct complete videos with multi-mode workflows for research,… | ✅ MIT |
| [ComfyUI-MiniMaxH3-TimelineDirector](https://github.com/Songssx/ComfyUI-MiniMaxH3-TimelineDirector) | 798 | Editable reference-media timeline director for ComfyUI MiniMax… | 📚 GPL-3.0 |
| [wind-comic](https://github.com/ChrisChen667788/wind-comic) | 728 | Multi-agent AI pipeline that turns one line of text into a fin… | ✅ MIT |
| [CineGen-ShortDrama](https://github.com/UllrAI/CineGen-ShortDrama) | 584 | AI Director - AI Manga, Anime, Animation, storyboard, Generati… | ⚠️ 自定义（读原文） |
| [chaojifeng-video-design](https://github.com/mileson/chaojifeng-video-design) | 564 | 超级峰的视频设计方法论｜面向 AI Agent 的视频主线、分镜、声画节奏、制作与交付验收 Skill | ✅ MIT |
| [director-desk](https://github.com/mangfufu/director-desk) | 556 | AI 短剧白模预演与摄影机调度工具 | ✅ MIT |
| [video-ai-talking](https://github.com/yizhi-chengzi/video-ai-talking) | 522 | 想做真人口播，又不必自己对着镜头念。上传一段真人出镜视频，写好字幕，本机配音并对口型，合成竖屏 MP4。密钥只留在浏览器里。 | ✅ MIT |
| [dramaxis](https://github.com/Agions/dramaxis) | 468 | 🎬 Dramaxis (剧枢) — 电影级多智能体影视叙事与智能解说平台 (Tauri 2 + Rust + React 1… | ✅ MIT |
| [OpenDirector](https://github.com/ThinkFlowLab/OpenDirector) | 465 | Build an easy-to-use workflow for the next generation of video… | ✅ Apache-2.0 |
| [AI-Canvas-tauri](https://github.com/Tenney95/AI-Canvas-tauri) | 414 | AI画布、AI短剧创作工具：免费、轻量的无限画布，支持短剧剧本、角色管理、分镜、图像/视频生成和短剧剪辑，集成 ComfyU… | ⚠️ 自定义（读原文） |
| [open-storyboard-canvas](https://github.com/ganbo-gab/open-storyboard-canvas) | 407 | Local-first AI storyboard infinite canvas for storyboarding: 3… | ⚠️ 自定义（读原文） |
| [agent-storyboard](https://github.com/Yuuhann1999/agent-storyboard) | 404 | 本地优先的 Agent 视频分镜工作台：让 Codex、Claude Code 通过 MCP 写分镜、生成图片/视频素材和配… | ✅ MIT |
| [novelvids](https://github.com/Anning01/novelvids) | 395 | 从故事创作、角色资产管理、分镜设计，到 AI 图片与视频生成，打造完整的开源 AI 漫剧与短剧创作工作台。支持创作助手、无限… | ✅ MIT |
| [smy-seedance-storyboard](https://github.com/liangdabiao/smy-seedance-storyboard) | 275 | 你给一个故事，它还你一套能直接拿去出图、出视频的上美影短剧制作文档。** "上美影"= 上海美术电影制片厂，就是《大闹天宫》… | ⚠️ 自定义（读原文） |
| [Anim-Director](https://github.com/HITsz-TMG/Anim-Director) | 267 | Controllable Animation Video Generation with Large Models-base… | ⚠️ 自定义（读原文） |
| [seedance-storyboard-generator-realman](https://github.com/liangdabiao/seedance-storyboard-generator-realman) | 267 | 真人实拍质感AI短剧分镜生成器 - Seedance Realman Storyboard Skill 一个帮你把故事/剧本… | ⚠️ 自定义（读原文） |
| [Kinema](https://github.com/chillzhuang/Kinema) | 248 | 由 Codex、Claude Code 等工具驱动 AI漫剧、AI电影、AI解说的 AI大模型 影像智能体。控制章节与分镜的… | 📚 AGPL-3.0 |
| [ZJT](https://github.com/jeffstric/ZJT) | 243 | Open-source, AI-agent-driven platform that turns a marketing b… | ⚠️ 自定义（读原文） |
| [ai-costume-gallery-zh](https://github.com/Deeyu/ai-costume-gallery-zh) | 241 | AI 参考图库中文版｜服装（写实 1,407 套／动画 1,320 套）、脸型 1,499 张、姿势线稿与深度图各 1,43… | ⚠️ 自定义（读原文） |
| [3d-director-desk](https://github.com/xiaozangao/3d-director-desk) | 221 | 浏览器端 3D 运镜与分镜导演台，支持人物、道具、轨迹点和动作时间轴 | ✅ MIT |
| [oh-my-minimaxh3-director](https://github.com/TFboy1/oh-my-minimaxh3-director) | 180 | MiniMax H3 驱动的全自动 AI 视频导演流水线——自动分镜、工作流分配、参数确认、批量生成、剪映一键拼合。 | ✅ MIT |
| [video-shotcraft-dsh](https://github.com/kingselyjoe/video-shotcraft-dsh) | 176 | 面向 DeepSeek Harness 的电影感产品视频 Agent Skill，包含 152 张镜头配方卡、Remotio… | ✅ Apache-2.0 |
| [MuseDock](https://github.com/renmengwen/MuseDock) | 172 | MuseDock 是一个本地优先的 AI 短视频创作与编辑工作台。它将素材整理、脚本与分镜、配音字幕、画面生成、视频渲染和后… | ✅ Apache-2.0 |
| [MiniMax-H3-Director-Cut-Studio](https://github.com/karuvanan/MiniMax-H3-Director-Cut-Studio) | 160 | Premiere-inspired PySide6 director studio for MiniMax H3 Ref2V… | ⚠️ 自定义（读原文） |
| [Vibefilming](https://github.com/wangzai-double-milk/Vibefilming) | 151 | Open-source AI director agent that turns one plain sentence in… | ✅ MIT |
| [openframe](https://github.com/murongg/openframe) | 141 | 开源免费的 AI 漫剧创作工作台：从剧本到角色/场景、分镜、视频生成与导出（FCPXML/EDL），支持 Web 与桌面端。 | 📚 AGPL-3.0 |
| [reference-video-director](https://github.com/sgyno09-source/reference-video-director) | 138 | reference video director | ⚠️ 自定义（读原文） |
| [insightcut-jianying-image-video](https://github.com/SkyNotSilent/insightcut-jianying-image-video) | 124 | InsightCut — AI 图片视频与可编辑剪映草稿工作台：文稿转分镜、图片、配音和字幕，支持 Jianying dra… | ✅ MIT |
| [forest-laoli-h3](https://github.com/lixiaoxiao9888-create/forest-laoli-h3) | 111 | 漫剧老李 · MiniMax H3（海螺 3.0）短剧全流程 Skill v2.1.1 · forest-laoli-h3 … | ✅ MIT |
<!-- /manyu:table:directing -->

### 2.4 💬 提示词库

<!-- manyu:table:prompts -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [seedance2-skill](https://github.com/dexhunter/seedance2-skill) | 4587 | Seedance 2 最佳提示词生成 skill | ✅ MIT |
| [awesome-seedance](https://github.com/LearnPrompt/awesome-seedance) | 2661 | Evidence-led Seedance 提示词库，带实测画面对照 | ✅ MIT |
| [higgsfield-ai-prompt-skill](https://github.com/OSideMedia/higgsfield-ai-prompt-skill) | 962 | Higgsfield 电影感提示词 Claude skill | ✅ MIT 🏛️已归档 |
| [zy-cinematic-realism](https://github.com/popopo-99/zy-cinematic-realism) | 735 | 场景想法→克制电影写实感提示词 | ⚠️ 自定义（读原文） |
| [ai-shortfilm-prompts](https://github.com/jnMetaCode/ai-shortfilm-prompts) | 570 | 任意想法→AI 短片提示词 Claude Code Skill | ✅ MIT |
| [lanshu-awesome-ai-video-kit](https://github.com/cclank/lanshu-awesome-ai-video-kit) | 469 | 411 个提示词 · 15 模型 · 7 个 Claude skill，企业项目实战沉淀 | ✅ MIT |
| [minimax-h3-prompt-skill-T8](https://github.com/T8mars/minimax-h3-prompt-skill-T8) | 357 | MiniMax H3 Creative DNA 提示词案例 | ✅ MIT |
| [awesome-seedance-2.5-prompts-skills](https://github.com/AtlasCloudAI/awesome-seedance-2.5-prompts-skills) | 276 | 100+ 精选 Seedance 2.5 提示词，附真实出片 | ⚠️ 自定义（读原文） |
| [open-higgsfield](https://github.com/wide-trace/open-higgsfield) | 7005 | A studio for image and video generation — one prompt bar, each… | ⚠️ 自定义（读原文） |
| [hand-drawn-styles](https://github.com/threerocks/hand-drawn-styles) | 2752 | Claude Code skill：把内容套进内置手绘画风配方,产出可直接复制的生图提示词。内置儿童涂色/极简线条/蜡笔童涂… | ✅ MIT |
| [awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) | 2260 | 🎬 2000+ curated Seedance 2.0 video generation prompts — cinema… | ⚠️ 自定义（读原文） |
| [AI-automatically-generates-novels](https://github.com/wfcz10086/AI-automatically-generates-novels) | 974 | 一个基于ai +提示词 的aigc创作生产力工具， 已经有数百家工作室和个人作者通过该工具实现了快速、批量生成小说、剧本、镜头。 | ✅ Apache-2.0 |
| [make-prompt-seedance2](https://github.com/liangdabiao/make-prompt-seedance2) | 780 | 一句话：试错成本越来越高，提示词的重要性从来没有像今天这样大。seedance2结构化提示语和通用SKILL，整合了 See… | ⚠️ 自定义（读原文） |
| [prompt-lens](https://github.com/raojiacui/prompt-lens) | 712 | 反推出AI视频的提示词，并配有音频分析功能，可提取视频中的台词文案，并且一句话就可剪辑出你要的视频 | ✅ MIT |
| [ComfyUI-MiniMaxH3-Director](https://github.com/seesee75-commits/ComfyUI-MiniMaxH3-Director) | 367 | A timeline editor for MiniMax H3 inside ComfyUI - storyboard p… | 📚 GPL-3.0 |
| [seedance-tvc-director](https://github.com/nutllwhy/seedance-tvc-director) | 361 | A Seedance 2.5 TVC director Skill for 15s, 30s and custom comm… | ✅ MIT |
| [ComfyUI-MiniMax-H3-Guide](https://github.com/ethanfel/ComfyUI-MiniMax-H3-Guide) | 358 | Guided MiniMax H3 prompt preparation node for ComfyUI | 📚 GPL-3.0 |
| [seedance-prompt](https://github.com/zhouwei713/seedance-prompt) | 346 | Hermes skill for realistic AI video prompts for Seedance and t… | ✅ MIT |
| [ComfyUI-MiniMaxH3-Prompt-Writer](https://github.com/duckyshell/ComfyUI-MiniMaxH3-Prompt-Writer) | 324 | Multimodal MiniMax H3 prompt writer for ComfyUI with local and… | ✅ MIT |
| [minimax-h3-prompt-composer](https://github.com/BMB12d3/minimax-h3-prompt-composer) | 315 | Free offline prompt composer for MiniMax H3 video generation i… | ⚠️ 自定义（读原文） |
| [ComfyUI-MiniMax-H3-Promptor](https://github.com/1038lab/ComfyUI-MiniMax-H3-Promptor) | 274 | A powerful, ComfyUI Custom node automation suite for generatin… | 📚 GPL-3.0 |
| [story-shot-agent](https://github.com/neopen/story-shot-agent) | 248 | 剧本分镜智能体（PenShot）：电影/动漫/短剧/小说→分镜片段→视频提示词。基于 LLM 通过 LangGraph+Ll… | ✅ Apache-2.0 |
| [xiakeman-ai-short-drama](https://github.com/XiakeMan777/xiakeman-ai-short-drama) | 242 | AI漫剧 / AI仿真人短剧/Seedance2.0专用创作工具：剧本创作、剧本分析、小说改编、AI 分镜、图片资产和 Se… | ⚠️ 自定义（读原文） |
| [awesome-MiniMax-H3-cases](https://github.com/SkyNotSilent/awesome-MiniMax-H3-cases) | 223 | 2801 playable MiniMax H3 / Hailuo H3 cases, 731 complete publi… | ✅ MIT |
| [KupkaProd-Cinema-Pipeline](https://github.com/Matticusnicholas/KupkaProd-Cinema-Pipeline) | 206 | Autonomous AI movie studio — turn a text prompt into a fully p… | ⚠️ 自定义（读原文） |
| [qisi-video-remix](https://github.com/wyuzhi/qisi-video-remix) | 198 | 视频创意改编 Agent Skill：参考视频 → 剧本 → 分镜 → 分段生成提示词。By qisi | ✅ MIT |
| [ai-visual-director](https://github.com/jijiutong/ai-visual-director) | 186 | AI Visual Director Skill: Generate storyboards, characters, sc… | ✅ MIT |
| [cut-director](https://github.com/Fangx-AI/cut-director) | 184 | CutDirector: a ChatCut skill for talking-head editing, with re… | ⚠️ 自定义（读原文） |
| [lengyi-seedance2.5-prompt](https://github.com/woyin2024/lengyi-seedance2.5-prompt) | 148 | 专为Seedance 2.5量身打造的提示词skill，可以把任何想法/主题/小说片段，变成一支高级的30秒电影。A pro… | ✅ MIT |
| [ai-video-workflow](https://github.com/toki-plus/ai-video-workflow) | 114 | 全自动AI原生视频生成工作流，集成文生图(LibLib)/图生视频(即梦)/文生音乐(即梦)和AI提示词生成(豆包)，一键创… | ✅ MIT |
<!-- /manyu:table:prompts -->

## 三、生产流水线单环节工具

### 3.1 🖼️ 生图与角色一致性

<!-- manyu:table:img -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 148832 | 节点式生成工作流引擎，漫剧出图/出视频的事实标准底座 | 📚 GPL-3.0 |
| [PhotoMaker](https://github.com/TencentARC/PhotoMaker) | 10081 | 照片级人物一致性定制（腾讯 ARC） | ⚠️ 自定义（读原文） 🏢 |
| [Qwen-Image](https://github.com/QwenLM/Qwen-Image) | 8501 | 阿里文生图，中文文字渲染强，海报/字幕图好用 | ✅ Apache-2.0 |
| [IP-Adapter](https://github.com/tencent-ailab/IP-Adapter) | 6720 | 图像提示词适配器，角色参考控制的事实标准 | ✅ Apache-2.0 🏢 |
| [StoryDiffusion](https://github.com/HVision-NKU/StoryDiffusion) | 6504 | 一致性角色 + 漫画序列生成，连续分格不换脸 | ✅ Apache-2.0 🏢 |
| [Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | 36501 | Uncensored AI Image & Video Generator — Free AI image & video … | ✅ MIT |
| [InvokeAI](https://github.com/invoke-ai/InvokeAI) | 29168 | Invoke is a leading creative engine that uses image and video … | ✅ Apache-2.0 |
| [LivePortrait](https://github.com/KlingAIResearch/LivePortrait) | 19597 | Bring portraits to life! | ⚠️ 自定义（读原文） |
| [DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) | 13444 | Enjoy the magic of Diffusion models! | ✅ Apache-2.0 |
| [InfiniteTalk](https://github.com/MeiGen-AI/InfiniteTalk) | 8487 | ​​Unlimited-length talking video generation​​ that supports im… | ✅ Apache-2.0 |
| [remove-ai-watermarks](https://github.com/wiltodelta/remove-ai-watermarks) | 6550 | Remove visible and invisible AI watermarks from images and vid… | ✅ Apache-2.0 |
| [Awesome-Video-Diffusion](https://github.com/showlab/Awesome-Video-Diffusion) | 5854 | A curated list of recent diffusion models for video generation… | ⚠️ 自定义（读原文） |
| [AgnesAI-Models](https://github.com/AgnesAI-Labs/AgnesAI-Models) | 5320 | Official Agnes AI gateway and model catalog for OpenAI-compati… | ⚠️ 自定义（读原文） |
| [editor](https://github.com/diffusionstudio/editor) | 3575 | The VS Code of video editing, built for agents | 📚 MPL-2.0 |
| [LightX2V](https://github.com/ModelTC/LightX2V) | 3031 | Lightweight Image Video Action Generation Inference Framework | ✅ Apache-2.0 |
| [VideoX-Fun](https://github.com/aigc-apps/VideoX-Fun) | 2347 | 📹 A more flexible framework that can generate videos at any re… | ✅ Apache-2.0 |
| [MeiGen-AI-Design-MCP](https://github.com/jau123/MeiGen-AI-Design-MCP) | 1813 | Discover inspiration and create images and videos with the lat… | ✅ MIT |
| [comfyui-mcp](https://github.com/artokun/comfyui-mcp) | 960 | Local-first, agent-native control plane for ComfyUI — MCP serv… | ✅ MIT |
| [awesome-generative-ai-apps](https://github.com/Anil-matcha/awesome-generative-ai-apps) | 829 | 50+ open-source generative AI apps you can clone, deploy, and … | ✅ MIT |
| [ComfyUI-WanAnimatePlus](https://github.com/wuwukaka/ComfyUI-WanAnimatePlus) | 427 | Seamless video connection and multi-reference image support fo… | ✅ Apache-2.0 |
| [ComfyUI-MiniMax-H3-Studio](https://github.com/thaakeno/ComfyUI-MiniMax-H3-Studio) | 147 | Reference-aware MiniMax H3 still-image production studio for C… | ✅ MIT |
<!-- /manyu:table:img -->

### 3.2 🎥 开源视频生成模型速查

<!-- manyu:table:video -->
| 模型 | ⭐ | 最低显存 | License | 点评 |
|---|---|---|---|---|
| [Wan2.2](https://github.com/Wan-Video/Wan2.2) | 18968 | 24GB（量化） | ✅ Apache-2.0 | 开源质量标杆，中文提示词原生支持，T2V+I2V |
| [CogVideo](https://github.com/zai-org/CogVideo) | 13234 | 16-24GB | ✅ Apache-2.0 🏢 | 智谱出品，可控性好，适合微调 |
| [HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo) | 12836 | 24GB（量化） | ⚠️ 自定义（读原文） | 腾讯，画质上限高，电影感强 |
| [LTX-Video](https://github.com/Lightricks/LTX-Video) | 11508 | 12-16GB | ✅ Apache-2.0 | 秒级出片，支持同步生成音频 |
| [SkyReels-V2](https://github.com/SkyworkAI/SkyReels-V2) | 7849 | 14GB+ | ⚠️ 自定义（读原文） | 昆仑万维，电影感镜头运动，支持无限时长 |
| [HunyuanVideo-1.5](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5) | 4619 | 14GB（卸载） | ⚠️ 自定义（读原文） | 轻量版，消费级显卡可跑 |
| [Index-anisora](https://github.com/bilibili/Index-anisora) | 2547 | — | ✅ Apache-2.0 | B 站二次元动漫风格视频模型，漫剧对口 |
| [seedance-2.0](https://github.com/Emily2040/seedance-2.0) | 8314 | — | ✅ MIT | Comprehensive production pipeline for quad-modal AI filmmaking… |
| [FastVideo](https://github.com/hao-ai-lab/FastVideo) | 4862 | — | ✅ Apache-2.0 | A unified inference and post-training framework for accelerate… |
| [ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo) | 4290 | — | ⚠️ 自定义（读原文） | LTX-Video Support for ComfyUI |
| [VBench](https://github.com/Vchitect/VBench) | 1859 | — | ✅ Apache-2.0 | [CVPR2024 Highlight] VBench - We Evaluate Video Generation |
| [ComfyUI-MiniMaxH3-Easy](https://github.com/nkxx188/ComfyUI-MiniMaxH3-Easy) | 937 | — | ✅ MIT | The easiest way to use MiniMax H3. One compact workflow for T2… |
| [awesome-video-generation](https://github.com/AlonzoLeeeooo/awesome-video-generation) | 796 | — | ✅ MIT | A collection of awesome video generation studies |
| [Stand-In](https://github.com/WeChatCV/Stand-In) | 795 | — | ✅ Apache-2.0 | [CVPR2026 🎉] Stand-In is a lightweight, plug-and-play framewor… |
| [ltx-video-mac](https://github.com/james-see/ltx-video-mac) | 464 | — | ✅ MIT | Native macOS app for local AI video on Apple Silicon — LTX-2, … |
| [ComfyUI-ALLinONE-MinimaxH3](https://github.com/LeonQ8/ComfyUI-ALLinONE-MinimaxH3) | 374 | — | 📚 GPL-3.0 | All-in-one MiniMax H3 node for ComfyUI - T2V, T2I, I2V, R2V, M… |
| [X-Dub](https://github.com/KlingAIResearch/X-Dub) | 242 | — | ✅ Apache-2.0 | [ICML 2026] Try X-Dub to sync any character in a video with an… |
| [awesome-ai-video-models](https://github.com/Anil-matcha/awesome-ai-video-models) | 220 | — | ⚠️ 自定义（读原文） | AI video generation model comparison: Seedance, Wan, and MiniM… |
| [ShotStream](https://github.com/KlingAIResearch/ShotStream) | 186 | — | ⚠️ 自定义（读原文） | [ECCV 2026] ShotStream: Streaming Multi-Shot Video Generation … |
| [vibeframe](https://github.com/vericontext/vibeframe) | 186 | — | ✅ MIT | Frontier AI video generation for coding agents - Seedance, Run… |
| [ai-video-agent](https://github.com/xuanyuanzhifeng/ai-video-agent) | 167 | — | ⚠️ 自定义（读原文） | AI生成图片轮播视频和HTML动画视频 |
| [kineo](https://github.com/Agions/kineo) | 138 | — | ✅ MIT | 🎬 端到端 AI 漫剧 / 动画短剧 Multi-Agent 多智能体协作创作平台 (Kineo AI)。基于 Hub-an… |
| [reshot](https://github.com/maosika-ai/reshot) | 133 | — | ✅ Apache-2.0 | ReShot — copy the shot, not the actors. Video → depth map, Ope… |
| [AIGCCanvasFlow](https://github.com/MaLunan/AIGCCanvasFlow) | 130 | — | ✅ MIT | 基于 Vue 3 + VueFlow 的 AIGC 无限画布工作流编辑器。类似可灵、libTv等编辑器， |
<!-- /manyu:table:video -->

### 3.3 🎙️ 配音 / 口型 / 音频

<!-- manyu:table:audio -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [whisper](https://github.com/openai/whisper) | 113619 | 语音识别，字幕与时间轴制作标配 | ✅ MIT |
| [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | 45 | 少样本中文音色克隆，漫剧配音主力 | ✅ MIT |
| [OpenVoice](https://github.com/myshell-ai/OpenVoice) | 38340 | 即时音色克隆，多语种 | ✅ MIT 🏢 |
| [fish-speech](https://github.com/fishaudio/fish-speech) | 33887 | 多语种 TTS，效果好（注意：模型权重 NC） | ⚠️ CC BY-NC-SA |
| [audiocraft](https://github.com/facebookresearch/audiocraft) | 23977 | Meta MusicGen/AudioGen，BGM 与音效生成 | ✅ MIT |
| [Wav2Lip](https://github.com/Rudrabha/Wav2Lip) | 13290 | 语音驱动口型老牌方案 | ❌ 仅研究用途，禁商用 🏢 |
| [LatentSync](https://github.com/bytedance/LatentSync) | 6335 | 字节开源，SD 架构口型同步 | ✅ Apache-2.0 🏢 |
| [rhubarb-lip-sync](https://github.com/DanielSWolf/rhubarb-lip-sync) | 2817 | 2D 动画口型自动生成，动态漫画对口 | ⚠️ 自定义（读原文） |
| [VoiceStudio](https://github.com/debpalash/VoiceStudio) | 119078 | VoiceStudio is the open-source, fully-local ElevenLabs alterna… | 📚 AGPL-3.0 |
| [index-tts](https://github.com/index-tts/index-tts) | 25319 | An Industrial-Level Controllable and Efficient Zero-Shot Text-… | ⚠️ 自定义（读原文） |
| [pipecat](https://github.com/pipecat-ai/pipecat) | 17469 | Open Source framework for voice agents, multimodal apps, and r… | ✅ BSD-2 |
| [agents](https://github.com/livekit/agents) | 15361 | A framework for building realtime voice AI agents 🤖🎙️📹 | ✅ Apache-2.0 |
| [ten-framework](https://github.com/TEN-framework/ten-framework) | 11247 | Open-source framework for conversational voice AI agents | ⚠️ 自定义（读原文） |
| [openai-agents-js](https://github.com/openai/openai-agents-js) | 4036 | A lightweight, powerful framework for multi-agent workflows an… | ✅ MIT |
| [no-cost-ai](https://github.com/zebbern/no-cost-ai) | 2455 | 80+ free AI services for chat, image, video, voice & APIs (may… | ✅ MIT |
| [cli](https://github.com/MiniMax-AI/cli) | 2238 | Generate text, images, video, speech, and music by MiniMax | ⚠️ 自定义（读原文） |
| [video-podcast-maker](https://github.com/Agents365-ai/video-podcast-maker) | 1733 | Topic → 4K narrated video for coding agents. v5.3.0: local TTS… | ✅ MIT |
| [MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP) | 1615 | Official MiniMax Model Context Protocol (MCP) server that enab… | ✅ MIT |
| [clipforge](https://github.com/xixihhhh/clipforge) | 1451 | ClipForge（原『带货剪手』/ daihuo-jianshou）：开源 AI 带货短视频神器——上传一张商品图，AI … | 📚 AGPL-3.0 |
| [MOSS-TTSD](https://github.com/OpenMOSS/MOSS-TTSD) | 1428 | A multilingual model for long-form, multi-speaker dialogue syn… | ✅ Apache-2.0 |
| [JJYB_AI_VideoAutoCut](https://github.com/jianjieyiban/JJYB_AI_VideoAutoCut) | 1281 | JJYB_AI 智剪 - 智能视频自动剪辑与AI解说工具（离线TTS、原创解说、混剪、AI配音） | ⚠️ 自定义（读原文） |
| [agnes-video-generator](https://github.com/lcy362/agnes-video-generator) | 778 | Free AI video generator — open-source & self-hosted. Text/imag… | ✅ MIT |
<!-- /manyu:table:audio -->

### 3.4 🌏 漫画翻译与出海

<!-- manyu:table:translate -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|

<!-- /manyu:table:translate -->

### 3.5 ✂️ 合成与剪辑

<!-- manyu:table:compose -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|

<!-- /manyu:table:compose -->

## 四、📖 网文改编专题（征集中）

网文→漫剧是国内独有的最大场景。当前社区公认的参考链路：

```
网文 txt
  → shuohao-skills / drama-skills 拆角色、排大纲、切分镜
  → Toonflow / ArcReel / LumenX 生成角色资产与分镜图
  → Wan2.2 / HunyuanVideo 图生视频
  → GPT-SoVITS 配音 + Whisper 字幕
  → FFmpeg 合成成片
```

**实测笔记征集中**：欢迎用上面的链路跑一本你自己的小说，把成本、耗时、翻车点写成笔记提 PR，被收录的笔记在本节长期展示。

## 🤝 贡献

欢迎提 PR 收录新项目！请先读 [CONTRIBUTING.md](./CONTRIBUTING.md) 的收录标准。

快速通道：[点这里提 Issue 推荐项目](https://github.com/TWO-ICE/awesome-manyu/issues/new?template=recommend.yml)

## ⚠️ 免责声明

- 本仓库只做链接与信息整理，不托管任何项目代码；
- License 标注来自 GitHub API 与公开资料，可能滞后或错漏，**商用前请务必阅读原仓库 LICENSE 原文**；
- 与本项目收录的任何工具之间无利益关联。

## 🔄 数据保鲜

星数、License、活跃状态由 [GitHub Actions](./.github/workflows/refresh.yml) 每周一自动刷新。数据源在 [`data/projects.json`](./data/projects.json)，README 表格由 [`scripts/refresh.py`](./scripts/refresh.py) 自动生成——**收录新项目请改 JSON 并提 PR，不要直接改 README 表格**。发现数据不对？直接提 Issue。

---

⭐ 觉得有用就点个 Star，这是对整理者最大的激励。
