from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = {
    "first-words": "Level 1",
    "short-vowel-stories": "Level 2",
    "blends-and-digraphs": "Level 3",
    "long-vowels-and-sneaky-letters": "Level 4",
}

changed = []

for folder, level in FOLDERS.items():
    for path in sorted((ROOT / folder).glob("*.*htm*")):
        text = path.read_text(encoding="utf-8")
        old = f'<a href="../index.html">{level}</a>'
        new = f'<a href="index.html">{level}</a>'
        if old in text:
            path.write_text(text.replace(old, new), encoding="utf-8")
            changed.append(path.relative_to(ROOT))

transitions = {
    "the-cute-cube-magic-e.html": (
        'href="magic-e-stories.html">Back to Magic E Stories →',
        'href="ai-stories.html">Continue to ai Stories →',
    ),
    "beach-cat-gets-mail-ai.html": (
        'href="ai-stories.html">Back to ai Stories →',
        'href="ay-stories.html">Continue to ay Stories →',
    ),
    "beach-cat-has-a-tray-ay.html": (
        'href="ay-stories.html">Back to ay Stories →',
        'href="ee-stories.html">Continue to ee Stories →',
    ),
    "a-seed-by-the-sea-ee.html": (
        'href="ee-stories.html">Back to ee Stories →',
        'href="ea-stories.html">Continue to ea Stories →',
    ),
    "the-beach-team-ea.html": (
        'href="ea-stories.html">Back to ea Stories →',
        'href="oa-stories.html">Continue to oa Stories →',
    ),
    "foam-on-the-boat-oa.html": (
        'href="../index.html">Back to Level 4 →',
        'href="ow-stories.html">Continue to ow Stories →',
    ),
    "beach-cat-goes-slow-ow.html": (
        'href="../index.html">Back to Level 4 →',
        'href="igh-stories.html">Continue to igh Stories →',
    ),
}

level4 = ROOT / "long-vowels-and-sneaky-letters"
for filename, (old, new) in transitions.items():
    path = level4 / filename
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"Expected navigation markup not found in {filename}")
    path.write_text(text.replace(old, new), encoding="utf-8")
    rel = path.relative_to(ROOT)
    if rel not in changed:
        changed.append(rel)

# Remove the temporary maintenance files in the same commit as the fixes.
workflow = ROOT / ".github" / "workflows" / "fix-level-navigation.yml"
script = Path(__file__).resolve()
if workflow.exists():
    workflow.unlink()
if script.exists():
    script.unlink()

print(f"Updated {len(changed)} HTML files")
for path in changed:
    print(path)
