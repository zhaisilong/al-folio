# AL-FOLIO

## Docker

```bash
docker compose up  # 启动
docker compose up -d  # 后台启动
```

## 说明

```yaml
_data/repositories.yml: 主页的 repository
_pages:
    - teaching.md: 课程
    - profiles: 实验室成员
    - dropdown: 下拉菜单
_news: about 页面的新闻
```

```bash
_config.yml:
    - Blog: blog 页面的开头
```

## 使用

- 本页面

```markdown
[publications page](/al-folio/publications/)
```

- `baseurl` 应该为空，否则会 prettier 失败
