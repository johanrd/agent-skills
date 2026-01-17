import re

sections = {
    "route": ["Use Route-Based Code Splitting", "Use Loading Substates for Better UX", "Parallel Data Loading in Model Hooks"],
    "bundle": ["Avoid Importing Entire Addon Namespaces", "Use Embroider Static Mode", "Lazy Load Heavy Dependencies"],
    "component": ["Use @cached for Expensive Getters", "Avoid Unnecessary Tracking", "Use Tracked Toolbox for Complex State", "Use Glimmer Components Over Classic Components"],
    "a11y": ["Use ember-a11y-testing for Automated Checks", "Form Labels and Error Announcements", "Keyboard Navigation Support", "Announce Route Transitions to Screen Readers", "Semantic HTML and ARIA Attributes"],
    "service": ["Cache API Responses in Services", "Optimize Ember Data Queries", "Use Services for Shared State"],
    "template": ["Avoid Heavy Computation in Templates", "Use {{#each}} with @key for Lists", "Use {{#let}} to Avoid Recomputation"],
    "advanced": ["Use Helpers for Template Logic", "Use Modifiers for DOM Side Effects"],
}

with open("AGENTS.md", "r") as f:
    content = f.read()

print("Verifying all rules are present in AGENTS.md:")
print("=" * 60)

total_rules = 0
for prefix, rules in sections.items():
    print(f"\n{prefix.upper()} ({len(rules)} rules):")
    for rule in rules:
        if f"## {rule}" in content:
            print(f"  ✓ {rule}")
            total_rules += 1
        else:
            print(f"  ✗ MISSING: {rule}")

print(f"\n{'=' * 60}")
print(f"Total rules found: {total_rules}/23")
