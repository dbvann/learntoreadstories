from pathlib import Path


def replace_once(path_str: str, old: str, new: str) -> None:
    path = Path(path_str)
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"Expected text not found in {path_str}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")

card_anchor = '<a class="article-card" href="what-are-letter-sounds.html" id="guide-what-are-letter-sounds"><div class="article-icon">👂</div><h3>What Are Letter Sounds?</h3><p>How to help your child hear the first sound in beach, big, bat, and Beach Cat.</p><span class="read-link">Read guide →</span></a>'
new_card = card_anchor + '\n<a class="article-card" href="letter-sounds-vs-letter-names.html" id="guide-letter-sounds-vs-letter-names"><div class="article-icon">🔠</div><h3>Letter Sounds vs. Letter Names</h3><p>What each skill does, which one helps children read words, and how to practice both together.</p><span class="read-link">Read guide →</span></a>'
replace_once("parent-guide/index.html", card_anchor, new_card)

callout = '<div class="article-callout"><strong>Simple version:</strong> The letter name is what we call the letter. The letter sound is the sound we use when we read a word.</div>'
linked_callout = callout + '\n<p>Parents often wonder which skill should come first. The answer is that children can learn both together, while giving plenty of attention to the sounds that help them read. See <a href="letter-sounds-vs-letter-names.html">Letter Sounds vs. Letter Names: What Should Children Learn First?</a></p>'
replace_once("parent-guide/what-are-letter-sounds.html", callout, linked_callout)

hero = '<section class="level-hero"><h1>Level 1: First Words</h1><p>Learn one sound, a few words, and a tiny story.</p></section>'
level_link = hero + '\n<div class="parent-tip"><strong>New to letter sounds?</strong> Read <a href="../parent-guide/letter-sounds-vs-letter-names.html">Letter Sounds vs. Letter Names</a> to see how both skills work together, then choose one lesson below.</div>'
replace_once("first-words/index.html", hero, level_link)

# Remove the one-time maintenance files before committing.
Path("scripts/add_letter_names_links.py").unlink(missing_ok=True)
Path(".github/workflows/add-letter-names-links.yml").unlink(missing_ok=True)
