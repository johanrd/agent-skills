---
title: Use {{#each}} with @key for Lists
impact: MEDIUM
impactDescription: 50-70% faster list updates
tags: templates, each, performance, rendering
---

## Use {{#each}} with @key for Lists

Always use the `@key` parameter with `{{#each}}` for lists of objects to help Ember efficiently track and update items.

**Incorrect (no key):**

```handlebars
<ul>
  {{#each this.users as |user|}}
    <li>
      <UserCard @user={{user}} />
    </li>
  {{/each}}
</ul>
```

**Correct (with key):**

```handlebars
<ul>
  {{#each this.users key="id" as |user|}}
    <li>
      <UserCard @user={{user}} />
    </li>
  {{/each}}
</ul>
```

**For arrays without stable IDs, use @identity:**

```handlebars
{{#each this.tags key="@identity" as |tag|}}
  <span class="tag">{{tag}}</span>
{{/each}}
```

**For complex scenarios with @index:**

```handlebars
{{#each this.items key="@index" as |item index|}}
  <div data-index={{index}}>
    {{item.name}}
  </div>
{{/each}}
```

Using proper keys allows Ember's rendering engine to efficiently update, reorder, and remove items without re-rendering the entire list.

**Performance comparison:**
- Without key: Re-renders entire list on changes
- With key by id: Only updates changed items (50-70% faster)
- With @identity: Good for primitive arrays (strings, numbers)
- With @index: Only use when items never reorder

Reference: [Glimmer Rendering](https://guides.emberjs.com/release/components/looping-through-lists/)
