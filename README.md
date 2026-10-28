<div align="center">
  <img src="assets/banner.png" alt="Awesome 漫剧 · 开源 AI 漫剧工具集合" width="100%" />
</div>

# 🎬 Awesome 漫剧 · 开源 AI 漫剧 / AI 短剧工具集合

> 中文世界最全的开源漫剧工具地图：**按生产流水线分类 · License 红绿灯 · 数据每周自动刷新**

<!-- manyu:meta -->
📊 收录 **97** 个项目 ｜ 数据更新于 **2026-10-28** ｜ 由 GitHub Actions 每周自动刷新
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
| [OpenMontage](https://github.com/calesthio/OpenMontage) | 72579 | 全球最大开源 AI 视频生产系统：12 条生产流水线、100+ 工具、Agent 驱动，一句话创意到成片 | 📚 AGPL-3.0 |
| [Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | 19708 | 无限画布 AI 视频创作平台：剧本创作、智能分镜、角色场景资产管理、生图生视频 | ✅ MIT |
| [huobao-drama](https://github.com/chatfire-AI/huobao-drama) | 16685 | 一句话生成完整短剧：剧本→分镜→视频→配音→FFmpeg 合成全自动 | ⚠️ CC BY-NC-SA |
| [waoowaoo](https://github.com/waooAI/waoowaoo) | 14698 | 工业级全流程 AI 影视生产平台，短片到真人级影视 | ⚠️ Elastic-2.0 |
| [dramaclaw](https://github.com/dramaclaw/dramaclaw) | 6509 | 通用 AIGC 视频引擎：剧本到成片一条流水线 | ⚠️ Elastic-2.0 |
| [Jellyfish](https://github.com/Forget-C/Jellyfish) | 7056 | 端到端生产工作台：章节脚本→分镜与关联资产 | ✅ Apache-2.0 |
| [ArcReel](https://github.com/ArcReel/ArcReel) | 5781 | 小说/剧本→角色场景道具资产→分镜→视频→剪映草稿 | 📚 AGPL-3.0 |
| [printfilm](https://github.com/yi1108/printfilm) | 7225 | 模板驱动 AI 短视频/漫剧平台（FastAPI），含计费与管理后台、开放 API | ✅ MIT |
| [moyin-creator](https://github.com/MemeCalculate/moyin-creator) | 4787 | AI 影视生产级工具，支持 Seedance 2.0，剧本到成片批量化 | 📚 AGPL-3.0 |
| [LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | 2256 | 纯 JavaScript 本地运行，数据零上传，支持 AI 真人剧+漫剧 | ✅ MIT |
| [AIComicBuilder](https://github.com/LingyiChen-AI/AIComicBuilder) | 1927 | AI 动态漫画生成器：脚本→分格→成片 | ✅ Apache-2.0 |
| [VideoClaw](https://github.com/HITsz-TMG/VideoClaw) | 1878 | AI 全自动化视频生成员工：一个想法→完整短剧/漫剧 | ✅ MIT |
| [lumenx](https://github.com/alibaba/lumenx) | 1423 | 阿里开源：小说文本→剧本分析→角色定制→分镜→动态漫剧视频 | ✅ MIT |
| [aid-studio](https://github.com/gzxx-2025/aid-studio) | 1158 | 自托管 AI 短剧/动态漫画工作室，Docker/systemd 部署，多模型多供应商 | ✅ MIT |
| [OpenMontage](https://github.com/charliewwdev/OpenMontage) | 6 | 自托管AI短剧工坊：剧本→角色场景道具→分镜→视频→配音剪辑 | 📚 AGPL-3.0 |
| [ViMax](https://github.com/HKUDS/ViMax) | 12787 | Agentic 视频生成：导演 Agent 驱动，从想法到成片自动化 | ✅ MIT |
| [BigBanana-AI-Director](https://github.com/shuyu-labs/BigBanana-AI-Director) | 2383 | 工业级一站式 AI 短剧导演：定妆→搭景→分镜→成片全程可控 | ⚠️ 自定义（读原文） |
| [ai_story](https://github.com/xhongc/ai_story) | 1941 | AI 视频/动漫/漫剧自动化生成工具，故事输入成片输出 | ⚠️ 自定义（读原文） |
| [ai-fusion-video](https://github.com/Stonewuu/ai-fusion-video) | 1667 | 融光：基于 Agent 的全流程 AI 短剧/漫剧/视频创作平台 | ✅ MIT |
| [LingGuo-Drama](https://github.com/LingGuoAI/LingGuo-Drama) | 1615 | 灵果短剧 AI：一句话生成完整短剧/漫剧 | ⚠️ 自定义（读原文） |
| [infinite-creation](https://github.com/SwotAtmk/infinite-creation) | 141 | 提交小说/剧本，本地 ComfyUI 全流程出片 | ✅ MIT |
<!-- /manyu:table:allinone -->

## 二、🤖 编剧与 Agent Skills（漫剧圈新物种）

给 Claude Code / Codex 等 Agent 用的技能包，不装平台、直接在终端里排生产。

### 2.1 📝 编剧 / 网文改编

<!-- manyu:table:writing -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) | 7724 | 基于 Claude Code 的长篇网文辅助创作系统：一致性与长程记忆 | 📚 GPL-3.0 |
| [human-writing](https://github.com/KKKKhazix/human-writing) | 4253 | 让 AI 写的中文读起来像一个具体的人，通用创作与改稿 Skill | ✅ MIT |
| [sepia](https://github.com/Nanako0129/sepia) | 3533 | 去 AI 味写作 Skill，任意 Agent 可装 | ✅ MIT |
| [screenwriting-skills](https://github.com/jtydhr88/screenwriting-skills) | 1854 | 专业影视编剧 Agent 技能集 | ✅ MIT |
| [short-drama](https://github.com/0xsline/short-drama) | 1512 | 专业短剧剧本创作：选题立项→分集撰写→质量自检→合规审核→海外 | ✅ MIT |
| [shanyin-screenwriting-master](https://github.com/Shanyin-ai/shanyin-screenwriting-master) | 1404 | 山音超级编剧：全格式影视编剧技能，1-3 分钟到长剧全覆盖 | ✅ MIT |
| [Chinese-WebNovel-Skill](https://github.com/Tomsawyerhu/Chinese-WebNovel-Skill) | 930 | 中文网文小说写作 skill | ⚠️ 自定义（读原文） |
| [narrative-to-screen-reader](https://github.com/zhlmi/narrative-to-screen-reader) | 125 | 叙事转译：把手上的故事翻译成影视开发语言 | ⚠️ 自定义（读原文） |
| [novel-to-manju](https://github.com/senmanx/novel-to-manju) | 66 | 小说转漫剧短视频全流程提示词 Skill：爆款改文→剧本→人物场景资产 | ⚠️ 自定义（读原文） |
| [novel-to-ai-short-drama-skill](https://github.com/muxia0396/novel-to-ai-short-drama-skill) | 32 | 小说改编 AI 短剧：分镜、运镜、表演调度与时长 | ✅ MIT |
<!-- /manyu:table:writing -->

### 2.2 🧰 全流程技能包

<!-- manyu:table:skills -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [shuohao-skills](https://github.com/eternityspring/shuohao-skills) | 5617 | AI 短剧制作 skill 集合：拆角色、排大纲、出场景道具设定、写剧本、切分镜 | ✅ Apache-2.0 |
| [drama-skills](https://github.com/zenstory-ai/drama-skills) | 3464 | 短剧/漫剧 skill 合集：剧本、角色资产、分镜、图/视频提示词、审查，适配 Claude Code 与 Codex | ✅ MIT |
| [story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | 2311 | 中文故事文案→手绘白板动画视频 | ✅ MIT |
| [ai-shotlive](https://github.com/sorker/ai-shotlive) | 346 | 小说→剧本→分镜→提示词→关键帧→视频→AI 剪辑一站式 | ⚠️ 自定义（读原文） |
| [manju-laoli-skill](https://github.com/lixiaoxiao9888-create/manju-laoli-skill) | 1733 | 漫剧老李 AIGC 创作全流程多技能套装 | ✅ MIT |
| [XiaoLuo-AI-Drama-Skill](https://github.com/zhurui0523/XiaoLuo-AI-Drama-Skill) | 499 | 小罗 AI 漫剧创作技能包 | ⚠️ 自定义（读原文） |
| [short-drama-factory](https://github.com/lixiaoxiao9888-create/short-drama-factory) | 485 | Short-Drama Factory：抖音/红果爆款短剧工厂 | ✅ MIT |
| [screen-creative-skills](https://github.com/VanGong1999/screen-creative-skills) | 483 | 影视创作技能集合：编剧到导演全链路 | ✅ MIT |
| [OnlyShot](https://github.com/A-cat-with-carrots/OnlyShot) | 340 | 神仙鱼 AI 短剧工业流水线 Claude Skill | ✅ MIT |
| [Micro-Drama-Skills](https://github.com/zhaihao118/Micro-Drama-Skills) | 326 | AI 驱动的短剧全流程自动化制作系统（Claude Skills） | ⚠️ 自定义（读原文） |
| [DirectorSKILL](https://github.com/wuwangzhang1216/DirectorSKILL) | 289 | Claude Code AI 电影制作技能 | ✅ MIT |
| [workrally](https://github.com/Tencent/workrally) | 179 | 腾讯：面向 AI Agent 的 AIGC 漫剧视频创作全流程工具集 | ⚠️ 自定义（读原文） |
| [film-studio-skills](https://github.com/machina-exm/film-studio-skills) | 160 | 7 个可安装的电影制片厂 Agent 技能 | ⚠️ 自定义（读原文） |
| [ComfyUI-Agent-Kit](https://github.com/SlavaSexton/ComfyUI-Agent-Kit) | 111 | 给 AI coding agent 用的一个 ComfyUI 全能技能 | ✅ Apache-2.0 |
| [ai-film-skills](https://github.com/62656456/ai-film-skills) | 94 | Open Film Skills：21 个独立模块化电影技能 | ✅ Apache-2.0 |
| [ai-short-drama-skill](https://github.com/xixihhhh/ai-short-drama-skill) | 78 | Dramake：面向 Codex / Claude Code / WorkBuddy 的短剧技能 | ✅ MIT |
| [ai-short-drama](https://github.com/Hao0321/ai-short-drama) | 74 | AI 短剧故事架构与剧本创作 skill | ✅ MIT |
| [open-source-video-gen-skill](https://github.com/mini-yifan/open-source-video-gen-skill) | 40 | Vibe Video：一句话想法→成片，开源 MiniMax H3 方案 | ⚠️ 自定义（读原文） |
| [spark-video](https://github.com/JohnKeating1997/spark-video) | 34 | AI 视频生产 skill：premise→成片 | ⚠️ 自定义（读原文） |
<!-- /manyu:table:skills -->

### 2.3 🎬 导演 / 分镜 / 镜头设计

<!-- manyu:table:directing -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [Seedance2-Storyboard-Generator](https://github.com/liangdabiao/Seedance2-Storyboard-Generator) | 2703 | Seedance 分镜生成：故事→直接能拿去出图出视频的制作文档 | ⚠️ 自定义（读原文） |
| [seedance-2-5-video-director](https://github.com/liyue-aigc/seedance-2-5-video-director) | 740 | Seedance 2.5 视频导演 Skill：提示词、脚本、诊断、人物锁定 | ✅ MIT |
| [shanyin-director-master](https://github.com/Shanyin-ai/shanyin-director-master) | 607 | 山音超级导演：导演定调→节奏规划→剧本微调→分镜拆解 | ✅ MIT |
| [visual-skills](https://github.com/smixs/visual-skills) | 592 | AI 电影导演技能集：电影语言与视觉叙事 | ✅ CC-BY-4.0 |
| [h3-storyboard-skill](https://github.com/phileiny/h3-storyboard-skill) | 188 | MiniMax H3 分镜/运镜 Claude Code skill | ✅ MIT |
| [short-drama-production](https://github.com/suihe1/short-drama-production) | 187 | 短剧生产总控 skill：专业导演分镜 + MiniMax H3 | ✅ Apache-2.0 |
| [Seedance-ShotDesign-Skills](https://github.com/woodfantasy/Seedance-ShotDesign-Skills) | 130 | Seedance 2.5 镜头设计技能 | ⚠️ MIT-0 |
| [seedance-2-5-fight-director](https://github.com/liyue-aigc/seedance-2-5-fight-director) | 101 | Seedance 2.5 高燃动作戏导演 skill（Codex） | ⚠️ 自定义（读原文） |
| [fight-video-create-skill](https://github.com/qualsenWeb/fight-video-create-skill) | 100 | AI 打斗视频创作/设计技能 | ⚠️ 自定义（读原文） |
| [fight-prompt-director](https://github.com/irenerachel/fight-prompt-director) | 66 | AI 动作导演：打斗场面提示词编排 | ✅ MIT |
| [seedance-skill](https://github.com/alchaincyf/seedance-skill) | 52 | 白模驱动的 AI 视频工作台（Seedance） | ✅ MIT |
| [acheng-director-skill](https://github.com/AharaOoO/acheng-director-skill) | 49 | 阿城导演：电影级导演综合引擎 | ✅ Apache-2.0 |
| [muse-video-skill](https://github.com/LuoJiangYong/muse-video-skill) | 47 | 视频创作虚拟剧组引擎：创意→剧本/分镜/美术/提示词 | ✅ MIT |
| [storyboard-director](https://github.com/kevinchin12/storyboard-director) | 35 | 提示词可控的分镜 skill（Codex） | ✅ MIT |
| [story-video-director](https://github.com/zlbigger/story-video-director) | 34 | 任意故事→图片素材、分镜、中文视听提示词与 API 清单 | ✅ MIT |
<!-- /manyu:table:directing -->

### 2.4 💬 提示词库

<!-- manyu:table:prompts -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [seedance2-skill](https://github.com/dexhunter/seedance2-skill) | 4372 | Seedance 2 最佳提示词生成 skill | ✅ MIT |
| [awesome-seedance](https://github.com/LearnPrompt/awesome-seedance) | 2321 | Evidence-led Seedance 提示词库，带实测画面对照 | ✅ MIT |
| [higgsfield-ai-prompt-skill](https://github.com/OSideMedia/higgsfield-ai-prompt-skill) | 812 | Higgsfield 电影感提示词 Claude skill | ✅ MIT |
| [zy-cinematic-realism](https://github.com/popopo-99/zy-cinematic-realism) | 640 | 场景想法→克制电影写实感提示词 | ⚠️ 自定义（读原文） |
| [ai-shortfilm-prompts](https://github.com/jnMetaCode/ai-shortfilm-prompts) | 498 | 任意想法→AI 短片提示词 Claude Code Skill | ✅ MIT |
| [lanshu-awesome-ai-video-kit](https://github.com/cclank/lanshu-awesome-ai-video-kit) | 435 | 411 个提示词 · 15 模型 · 7 个 Claude skill，企业项目实战沉淀 | ✅ MIT |
| [minimax-h3-prompt-skill-T8](https://github.com/T8mars/minimax-h3-prompt-skill-T8) | 311 | MiniMax H3 Creative DNA 提示词案例 | ✅ MIT |
| [awesome-seedance-2.5-prompts-skills](https://github.com/AtlasCloudAI/awesome-seedance-2.5-prompts-skills) | 248 | 100+ 精选 Seedance 2.5 提示词，附真实出片 | ⚠️ 自定义（读原文） |
<!-- /manyu:table:prompts -->

## 三、生产流水线单环节工具

### 3.1 🖼️ 生图与角色一致性

<!-- manyu:table:img -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 143685 | 节点式生成工作流引擎，漫剧出图/出视频的事实标准底座 | 📚 GPL-3.0 |
| [PhotoMaker](https://github.com/TencentARC/PhotoMaker) | 10082 | 照片级人物一致性定制（腾讯 ARC） | ⚠️ 自定义（读原文） 🏢 |
| [Qwen-Image](https://github.com/QwenLM/Qwen-Image) | 8433 | 阿里文生图，中文文字渲染强，海报/字幕图好用 | ✅ Apache-2.0 |
| [IP-Adapter](https://github.com/tencent-ailab/IP-Adapter) | 6703 | 图像提示词适配器，角色参考控制的事实标准 | ✅ Apache-2.0 🏢 |
| [StoryDiffusion](https://github.com/HVision-NKU/StoryDiffusion) | 6490 | 一致性角色 + 漫画序列生成，连续分格不换脸 | ✅ Apache-2.0 🏢 |
<!-- /manyu:table:img -->

### 3.2 🎥 开源视频生成模型速查

<!-- manyu:table:video -->
| 模型 | ⭐ | 最低显存 | License | 点评 |
|---|---|---|---|---|
| [Wan2.2](https://github.com/Wan-Video/Wan2.2) | 18230 | 24GB（量化） | ✅ Apache-2.0 | 开源质量标杆，中文提示词原生支持，T2V+I2V |
| [CogVideo](https://github.com/zai-org/CogVideo) | 13120 | 16-24GB | ✅ Apache-2.0 | 智谱出品，可控性好，适合微调 |
| [HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo) | 12679 | 24GB（量化） | ⚠️ 自定义（读原文） | 腾讯，画质上限高，电影感强 |
| [LTX-Video](https://github.com/Lightricks/LTX-Video) | 11204 | 12-16GB | ✅ Apache-2.0 | 秒级出片，支持同步生成音频 |
| [SkyReels-V2](https://github.com/SkyworkAI/SkyReels-V2) | 7744 | 14GB+ | ⚠️ 自定义（读原文） | 昆仑万维，电影感镜头运动，支持无限时长 |
| [HunyuanVideo-1.5](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5) | 4580 | 14GB（卸载） | ⚠️ 自定义（读原文） | 轻量版，消费级显卡可跑 |
| [Index-anisora](https://github.com/bilibili/Index-anisora) | 2533 | — | ✅ Apache-2.0 | B 站二次元动漫风格视频模型，漫剧对口 |
<!-- /manyu:table:video -->

### 3.3 🎙️ 配音 / 口型 / 音频

<!-- manyu:table:audio -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [whisper](https://github.com/openai/whisper) | 111449 | 语音识别，字幕与时间轴制作标配 | ✅ MIT |
| [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | 64001 | 少样本中文音色克隆，漫剧配音主力 | ✅ MIT |
| [OpenVoice](https://github.com/myshell-ai/OpenVoice) | 38096 | 即时音色克隆，多语种 | ✅ MIT 🏢 |
| [fish-speech](https://github.com/fishaudio/fish-speech) | 33446 | 多语种 TTS，效果好（注意：模型权重 NC） | ⚠️ CC BY-NC-SA |
| [audiocraft](https://github.com/facebookresearch/audiocraft) | 23771 | Meta MusicGen/AudioGen，BGM 与音效生成 | ✅ MIT |
| [Wav2Lip](https://github.com/Rudrabha/Wav2Lip) | 13261 | 语音驱动口型老牌方案 | ❌ 仅研究用途，禁商用 🏢 |
| [LatentSync](https://github.com/bytedance/LatentSync) | 6206 | 字节开源，SD 架构口型同步 | ✅ Apache-2.0 🏢 |
| [rhubarb-lip-sync](https://github.com/DanielSWolf/rhubarb-lip-sync) | 2701 | 2D 动画口型自动生成，动态漫画对口 | ⚠️ 自定义（读原文） |
<!-- /manyu:table:audio -->

### 3.4 🌏 漫画翻译与出海

<!-- manyu:table:translate -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [manga-image-translator](https://github.com/zyddnys/manga-image-translator) | 10546 | 图片内文字一键翻译，生肉变熟肉 | 📚 GPL-3.0 |
| [koharu](https://github.com/koharu-rs/koharu) | 6520 | Rust 写的 ML 漫画翻译器，快 | ✅ Apache-2.0 |
| [BallonsTranslator](https://github.com/dmMaze/BallonsTranslator) | 5239 | 深度学习辅助漫画翻译，带图像/文本编辑 | 📚 GPL-3.0 |
<!-- /manyu:table:translate -->

### 3.5 ✂️ 合成与剪辑

<!-- manyu:table:compose -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | 65937 | 视频合成、字幕烧录、转码的事实标准，各家流水线最后一步都靠它 | 📚 LGPL-2.1 / GPL-2.0 |
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
