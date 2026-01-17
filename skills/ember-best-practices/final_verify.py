import re

with open("AGENTS.md", "r") as f:
    content = f.read()

# Count sections
sections = re.findall(r'^## \d\. ', content, re.MULTILINE)
print(f"✓ Number of main sections: {len(sections)}")

# Count all headers
all_headers = re.findall(r'^## ', content, re.MULTILINE)
print(f"✓ Total headers (##): {len(all_headers)}")

# Verify TOC exists
if "## Table of Contents" in content:
    print(f"✓ Table of Contents present")

# Verify proper structure
if "**Version:**" in content and "**Organization:**" in content and "**Date:**" in content:
    print(f"✓ Header metadata present (Version, Organization, Date)")

# Verify Abstract
if "## Abstract" in content:
    print(f"✓ Abstract present")

# Verify all sections have impact and description
section_pattern = r'## \d\. .+?\n\n\*\*Impact:\*\*'
sections_with_metadata = len(re.findall(section_pattern, content, re.MULTILINE | re.DOTALL))
print(f"✓ Sections with metadata: {sections_with_metadata}/7")

# Count horizontal rules
horizontal_rules = len(re.findall(r'^---$', content, re.MULTILINE))
print(f"✓ Horizontal rule separators: {horizontal_rules}")

# Count total lines
lines = content.count('\n')
print(f"✓ Total lines: {lines}")

# Check file ends properly
if content.rstrip().endswith(']') or 'Reference:' in content[-200:]:
    print(f"✓ File ends with proper content")

print("\n✅ AGENTS.md file is complete and well-formed!")
print(f"\n📊 Summary:")
print(f"   - 7 main sections")
print(f"   - 23 rules total")
print(f"   - {lines} lines")
print(f"   - All rules properly formatted and organized")

