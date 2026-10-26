# 🎬 Awesome 漫剧 · 开源 AI 漫剧 / AI 短剧工具集合

> 中文世界最全的开源漫剧工具地图：**按生产流水线分类 · License 红绿灯 · 数据每周自动刷新**

<!-- manyu:meta -->
📊 收录 **41** 个项目 ｜ 数据更新于 **2026-10-26** ｜ 由 GitHub Actions 每周自动刷新
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
| [Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) | 19411 | 无限画布 AI 视频创作平台：剧本创作、智能分镜、角色场景资产管理、生图生视频 | ✅ MIT |
| [huobao-drama](https://github.com/chatfire-AI/huobao-drama) | 16605 | 一句话生成完整短剧：剧本→分镜→视频→配音→FFmpeg 合成全自动 | ⚠️ CC BY-NC-SA |
| [waoowaoo](https://github.com/waooAI/waoowaoo) | 14681 | 工业级全流程 AI 影视生产平台，短片到真人级影视 | ⚠️ Elastic-2.0 |
| [dramaclaw](https://github.com/dramaclaw/dramaclaw) | 6453 | 通用 AIGC 视频引擎：剧本到成片一条流水线 | ⚠️ Elastic-2.0 |
| [Jellyfish](https://github.com/Forget-C/Jellyfish) | 7028 | 端到端生产工作台：章节脚本→分镜与关联资产 | ✅ Apache-2.0 |
| [ArcReel](https://github.com/ArcReel/ArcReel) | 5724 | 小说/剧本→角色场景道具资产→分镜→视频→剪映草稿 | 📚 AGPL-3.0 |
| [printfilm](https://github.com/yi1108/printfilm) | 6967 | 模板驱动 AI 短视频/漫剧平台（FastAPI），含计费与管理后台、开放 API | ✅ MIT |
| [moyin-creator](https://github.com/MemeCalculate/moyin-creator) | 4780 | AI 影视生产级工具，支持 Seedance 2.0，剧本到成片批量化 | 📚 AGPL-3.0 |
| [LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) | 2226 | 纯 JavaScript 本地运行，数据零上传，支持 AI 真人剧+漫剧 | ✅ MIT |
| [AIComicBuilder](https://github.com/LingyiChen-AI/AIComicBuilder) | 1924 | AI 动态漫画生成器：脚本→分格→成片 | ✅ Apache-2.0 |
| [VideoClaw](https://github.com/HITsz-TMG/VideoClaw) | 1878 | AI 全自动化视频生成员工：一个想法→完整短剧/漫剧 | ✅ MIT |
| [lumenx](https://github.com/alibaba/lumenx) | 1412 | 阿里开源：小说文本→剧本分析→角色定制→分镜→动态漫剧视频 | ✅ MIT |
| [aid-studio](https://github.com/gzxx-2025/aid-studio) | 1135 | 自托管 AI 短剧/动态漫画工作室，Docker/systemd 部署，多模型多供应商 | ✅ MIT |
<!-- /manyu:table:allinone -->

## 二、🤖 Agent Skills 与工作流（漫剧圈新物种）

给 Claude Code / Codex 等 Agent 用的技能包，不装平台、直接在终端里排生产。

<!-- manyu:table:skills -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [shuohao-skills](https://github.com/eternityspring/shuohao-skills) | 5115 | AI 短剧制作 skill 集合：拆角色、排大纲、出场景道具设定、写剧本、切分镜 | ✅ Apache-2.0 |
| [drama-skills](https://github.com/zenstory-ai/drama-skills) | 3357 | 短剧/漫剧 skill 合集：剧本、角色资产、分镜、图/视频提示词、审查，适配 Claude Code 与 Codex | ✅ MIT |
| [story-to-handdrawn-video](https://github.com/gnipbao/story-to-handdrawn-video) | 2299 | 中文故事文案→手绘白板动画视频 | ✅ MIT |
| [ai-shotlive](https://github.com/sorker/ai-shotlive) | 344 | 小说→剧本→分镜→提示词→关键帧→视频→AI 剪辑一站式 | ⚠️ 自定义（读原文） |
<!-- /manyu:table:skills -->

## 三、生产流水线单环节工具

### 3.1 🖼️ 生图与角色一致性

<!-- manyu:table:img -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 143013 | 节点式生成工作流引擎，漫剧出图/出视频的事实标准底座 | 📚 GPL-3.0 |
| [PhotoMaker](https://github.com/TencentARC/PhotoMaker) | 10087 | 照片级人物一致性定制（腾讯 ARC） | ⚠️ 自定义（读原文） 🏢 |
| [Qwen-Image](https://github.com/QwenLM/Qwen-Image) | 8427 | 阿里文生图，中文文字渲染强，海报/字幕图好用 | ✅ Apache-2.0 |
| [IP-Adapter](https://github.com/tencent-ailab/IP-Adapter) | 6700 | 图像提示词适配器，角色参考控制的事实标准 | ✅ Apache-2.0 🏢 |
| [StoryDiffusion](https://github.com/HVision-NKU/StoryDiffusion) | 6489 | 一致性角色 + 漫画序列生成，连续分格不换脸 | ✅ Apache-2.0 🏢 |
<!-- /manyu:table:img -->

### 3.2 🎥 开源视频生成模型速查

<!-- manyu:table:video -->
| 模型 | ⭐ | 最低显存 | License | 点评 |
|---|---|---|---|---|
| [Wan2.2](https://github.com/Wan-Video/Wan2.2) | 18178 | 24GB（量化） | ✅ Apache-2.0 | 开源质量标杆，中文提示词原生支持，T2V+I2V |
| [CogVideo](https://github.com/zai-org/CogVideo) | 13108 | 16-24GB | ✅ Apache-2.0 | 智谱出品，可控性好，适合微调 |
| [HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo) | 12668 | 24GB（量化） | ⚠️ 自定义（读原文） | 腾讯，画质上限高，电影感强 |
| [LTX-Video](https://github.com/Lightricks/LTX-Video) | 11179 | 12-16GB | ✅ Apache-2.0 | 秒级出片，支持同步生成音频 |
| [SkyReels-V2](https://github.com/SkyworkAI/SkyReels-V2) | 7735 | 14GB+ | ⚠️ 自定义（读原文） | 昆仑万维，电影感镜头运动，支持无限时长 |
| [HunyuanVideo-1.5](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5) | 4579 | 14GB（卸载） | ⚠️ 自定义（读原文） | 轻量版，消费级显卡可跑 |
| [Index-anisora](https://github.com/bilibili/Index-anisora) | 2531 | — | ✅ Apache-2.0 | B 站二次元动漫风格视频模型，漫剧对口 |
<!-- /manyu:table:video -->

### 3.3 🎙️ 配音 / 口型 / 音频

<!-- manyu:table:audio -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [whisper](https://github.com/openai/whisper) | 111270 | 语音识别，字幕与时间轴制作标配 | ✅ MIT |
| [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | 63728 | 少样本中文音色克隆，漫剧配音主力 | ✅ MIT |
| [OpenVoice](https://github.com/myshell-ai/OpenVoice) | 38073 | 即时音色克隆，多语种 | ✅ MIT 🏢 |
| [fish-speech](https://github.com/fishaudio/fish-speech) | 33403 | 多语种 TTS，效果好（注意：模型权重 NC） | ⚠️ CC BY-NC-SA |
| [audiocraft](https://github.com/facebookresearch/audiocraft) | 23760 | Meta MusicGen/AudioGen，BGM 与音效生成 | ✅ MIT |
| [Wav2Lip](https://github.com/Rudrabha/Wav2Lip) | 13256 | 语音驱动口型老牌方案 | ❌ 仅研究用途，禁商用 🏢 |
| [LatentSync](https://github.com/bytedance/LatentSync) | 6191 | 字节开源，SD 架构口型同步 | ✅ Apache-2.0 🏢 |
| [rhubarb-lip-sync](https://github.com/DanielSWolf/rhubarb-lip-sync) | 2690 | 2D 动画口型自动生成，动态漫画对口 | ⚠️ 自定义（读原文） |
<!-- /manyu:table:audio -->

### 3.4 🌏 漫画翻译与出海

<!-- manyu:table:translate -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [manga-image-translator](https://github.com/zyddnys/manga-image-translator) | 10541 | 图片内文字一键翻译，生肉变熟肉 | 📚 GPL-3.0 |
| [koharu](https://github.com/koharu-rs/koharu) | 6497 | Rust 写的 ML 漫画翻译器，快 | ✅ Apache-2.0 |
| [BallonsTranslator](https://github.com/dmMaze/BallonsTranslator) | 5235 | 深度学习辅助漫画翻译，带图像/文本编辑 | 📚 GPL-3.0 |
<!-- /manyu:table:translate -->

### 3.5 ✂️ 合成与剪辑

<!-- manyu:table:compose -->
| 项目 | ⭐ | 说明 | License |
|---|---|---|---|
| [FFmpeg](https://github.com/FFmpeg/FFmpeg) | 65761 | 视频合成、字幕烧录、转码的事实标准，各家流水线最后一步都靠它 | 📚 LGPL-2.1 / GPL-2.0 |
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
