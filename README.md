# Amber LENS Public

**看见表象之下｜一个可安装的中文关系与沟通分析 Skill**

> **这是公开通用版，不是 Amber 的私人知识库。** 仓库名称中的 `private-knowledge` 是历史命名；本仓库当前发布的内容只有专门新写的公开版规则、方法和虚构示例，**不包含任何私人课程、书籍原文、聊天记录、个人案例、固定记忆或 LENS 软件源码**。

Amber LENS Public 是一组可复用的 AI 指令，帮助使用者分析聊天和人际互动，区分可观察事实与猜测、理解不同解释，并制定尊重边界的下一步行动。

## 能做什么

- **解释互动**：不把“消息少”“语气冷淡”等单一信号直接判为喜欢、不喜欢或操控。
- **整理复杂情境**：把已知事实、解释、未知信息和影响分开。
- **起草自然回复**：可输出简洁、口语化、尊重双方的聊天建议。
- **识别边界与风险**：避免把施压、监控或情绪勒索包装成技巧。
- **辅助复盘**：在事实发生变化时更新判断，而不是为最初的猜想找证据。

## 安装（个人电脑上的 Codex）

在终端运行：

```bash
git clone https://github.com/ambersely319-dev/amber-lens-private-knowledge.git ~/.codex/skills/amber-lens-public
```

也可以点击 **Code → Download ZIP**，解压后把包含 `SKILL.md` 的文件夹放进支持 Skills 的 AI 助手的技能目录（例如 `~/.codex/skills/amber-lens-public/`）。如果电脑已有同名目录，请先检查后再操作，**不要覆盖私人版 Skill**。

> 是否自动识别此 Skill 取决于客户端版本与支持的 Skills 功能。GitHub 仓库本身不是可在线直接使用的聊天机器人，也不会自动取得用户聊天记录。

## 使用示例

向支持 Skill 的助手提出：

```
请使用 amber-lens-public 分析这段互动：
对方这周回复频率明显变少，但没有明确解释原因。
先区分事实和猜测，再给两种可能解释，以及一条自然、不施压的询问消息。
```

或：

```
用 LENS 的四步法整理这段对话，指出哪些信息不足以支持结论；
如果不需要回复，就直接告诉我不回复也是一种选择。
```

## 文件结构

| 文件 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | AI 技能入口与执行规则 |
| [references/framework.md](references/framework.md) | LENS 四步分析框架 |
| [references/communication.md](references/communication.md) | 回复写作与沟通质量标准 |
| [references/privacy-safety.md](references/privacy-safety.md) | 隐私、风险与边界 |
| [examples/demo-01.md](examples/demo-01.md) | 虚构互动分析示例 |
| [examples/demo-02.md](examples/demo-02.md) | 虚构边界表达示例 |
| [tests/check_public.py](tests/check_public.py) | 公开版结构与隐私最小化自检 |

## 公开版与私人版

| | 公开版 | 私人版 |
| --- | --- | --- |
| 新编写的分析方法 | ✓ | 可按需采用 |
| 虚构示例 | ✓ | 可按需采用 |
| 私人课程/书籍全文 | ✗ | 本人本地保存 |
| 私人聊天/个人案例/固定记忆 | ✗ | 不进入公开版 |
| LENS 软件开发与部署资料 | ✗ | ✗ |

## 隐私与授权

本仓库**不包含上传个人数据的功能**；但如果你将私人聊天粘贴给其他 AI 服务，请自行确认其数据处理条款并先去除可识别信息。请勿提交他人身份信息、聊天截图或秘密凭据。

本工具不是心理诊断、治疗或法律意见；遇到威胁、跟踪、胁迫或人身风险时，应优先联系可信的人和当地专业支持。

**内容授权：** © Amber. All rights reserved. 公开可查看、可按 GitHub 平台功能获取代码，不代表自动授权商业改编或再分发。后续如决定开源，可另行选择许可证。

---

**Amber LENS Public · 公开通用版 v1.0**
