# AL-FOLIO

## Docker

```bash
docker compose up  # 启动
docker compose up -d  # 后台启动
```

## 说明

```yaml
_data/repositories.yml: 主页的 repository
```

## 使用

```markdown
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
