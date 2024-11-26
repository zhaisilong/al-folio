# AL-FOLIO

## Using docker for development

```bash
docker compose up  # 启动
docker compose up -d  # 后台启动
```

## Description

```yaml
_data/repositories.yml: 主页的 repository
_pages:
  - teaching.md: 课程
  - profiles: 实验室成员
  - dropdown: 下拉菜单
  - about: 开始界面
_news: about 页面的新闻
_projects: 项目
_bibliography:
  - papers.bib
```

```bash
_config.yml:
    - Blog: blog heading
```

- git flow 需要更新 `LIGHTHOUSE_BADGER_TOKEN`

## Usage

- This page

```markdown
[publications page](/al-folio/publications/)
```

- Remove Workflow Prettier Check

````markdown
{% raw %}

```html
<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
```

{% endraw %}
```

## Debug

- `git merge` get `Gemfile.lock` changed, just remove it.
```
