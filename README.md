# gitskills

## 飞书 Channel 集成

本项目已配置 [lark-for-claude](https://www.npmjs.com/package/lark-for-claude) 飞书 Channel 插件，可在飞书中直接与 Claude Code 对话。

### 首次使用

**1. 确认飞书应用权限**

在[飞书开放平台](https://open.feishu.cn)的应用中配置：

- **事件配置**：切换为"使用长连接"，添加事件 `im.message.receive_v1`
- **回调配置**：切换为"使用长连接"，添加回调 `card.action.trigger`
- **权限管理**：添加以下权限并发布版本
  - `im:message`、`im:message.receive_v1`
  - `im:message.p2p_msg:readonly`、`im:message.group_at_msg:readonly`
  - `im:chat:readonly`、`im:resource`

**2. 启动 Claude Code 飞书频道**

```bash
claude-feishu
```

**3. 配对飞书账号**

向机器人发送任意消息，机器人回复配对码后在终端运行：

```
/feishu:access pair <code>
```

然后将你的账号加入白名单：

```bash
claude-feishu access allow <your_open_id>
```

### 日常使用

```bash
# 进入项目目录并启动
cd /path/to/project && claude-feishu
```

启动后即可在飞书私聊或群聊（需 @机器人）中与 Claude 对话。

### 配置文件位置

| 文件 | 说明 |
|------|------|
| `~/.claude/channels/feishu/.env` | 应用凭据 |
| `~/.claude/channels/feishu/access.json` | 访问控制 |
| `~/.claude/channels/feishu/debug.log` | 调试日志 |
