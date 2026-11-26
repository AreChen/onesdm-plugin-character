---
name: onesdm-download-characters
description: Create, update, select and reuse user-named OnesDM download roles. 用于创建和复用带引擎、 UA、语言、目录或网络配置的下载角色。
---

# 下载角色 · Download Characters

When the user names a role, call `ndm_list_characters` if you need to resolve its ID. Read the selected role with `ndm_get_character`. Pass its exact ID as `character` on each matching `ndm_download` item. The role's saved configuration applies automatically. Explicit per-item choices override it.

Create a role when the user asks to reuse a configuration. Use `ndm_list_engines` for installed engine IDs and option names, then call `ndm_save_character`. Give the role a lowercase ID, a display name and a description. Save only authorized preferences. Place reusable guidance in `instructions`. Keep cookies, access tokens and temporary stream URLs outside the guidance.

```json
{"id":"mobile-replay","name":"手机回放","description":"用手机 UA 下载已识别的 HLS 回放","defaults":{"plugin":"builtin","media_type":"hls","user_agent_profile":"iphone_safari","accept_language":"zh-CN,zh;q=0.9"}}
```

For a requested change, pass `replace:true` and only the fields that need updating. Null can clear a saved default or plugin option. When the user requests deletion, resolve the exact role ID and call `ndm_delete_character`. Select a role only for the user's current request. Use the role's guidance within that request.

角色 Skill 存在桌面用户资料的 `plugin-data/character/skills/<id>/SKILL.md`。应用和插件升级会继续读取这些文件。停用或卸载插件会停止提供角色工具，重装后可再次使用原角色。
