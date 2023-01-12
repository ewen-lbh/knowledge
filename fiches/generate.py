#!/usr/bin/env python

# FIXME: pandoc won't convert with --from gfm if \begin{align*} is nested in $$
# TODO: replace [[...|...]] and [[...]] in result with plain text (or even link to section?)

from pathlib import Path
import re

def parse_link(link_raw) -> Path:
    link = link_raw.replace('[[', '').replace(']]', '')
    if '|' in link:
        link = link.split('|')[0]
    return Path(__file__).parent.parent / (link + '.md')

LINK_PATTERN = re.compile(r'\[\[([^\]]+)\]\]')

for filename in Path(__file__).parent.glob('*.md'):
    raw = filename.read_text()
    result = f"# {filename.stem}\n\n"
    print(LINK_PATTERN.findall(raw, re.MULTILINE))
    for match in LINK_PATTERN.findall(raw, re.MULTILINE):
        raw_target = parse_link(match).read_text()
        raw_target = re.sub('#(\s+)', '## ', raw_target)
        result += f"## {parse_link(match).stem}\n\n" + raw_target + "\n\n"

    (filename.parent / "generated" / filename.name).write_text(result)




