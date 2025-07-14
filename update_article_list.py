import re
import subprocess

README_FILE = 'README.md'

# List of items (label and link)
articles = [
    "- [Research Institute Andishe Online Germany (AOG)](https://aogdata.wikibase.cloud/wiki/Item:Q12)",
    "- [Faramarz Tabesh](https://aogdata.wikibase.cloud/wiki/Item:Q10)",
    "- [Appearance of instinctive characteristics – Step 1: New Concepts and Ideas](https://aogdata.wikibase.cloud/wiki/Item:Q2)",
    "- [Who´s Elite](https://aogdata.wikibase.cloud/wiki/Item:Q3)"
]

def update_readme(articles):
    with open(README_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    new_block = '\n'.join(articles)

    updated = re.sub(
        r'<!-- ARTICLE LIST START -->(.*?)<!-- ARTICLE LIST END -->',
        f'<!-- ARTICLE LIST START -->\n{new_block}\n<!-- ARTICLE LIST END -->',
        content,
        flags=re.DOTALL
    )

    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(updated)

    print("✅ README.md updated successfully.")

def git_push():
    try:
        subprocess.run(["git", "add", "."], check=True)  # اضافه کردن همه تغییرات
        subprocess.run(["git", "commit", "-m", "Update article list"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Changes pushed to GitHub successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git command failed: {e}")

if __name__ == "__main__":
    update_readme(articles)
    git_push()
