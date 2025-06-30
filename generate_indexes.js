const fs = require("fs");
const path = require("path");

const ROOT = path.join(__dirname, "content"); // Adjust if your notes live elsewhere

function walkDirs(dir) {
  const subdirs = fs.readdirSync(dir, { withFileTypes: true });
  for (const item of subdirs) {
    const fullPath = path.join(dir, item.name);
    if (item.isDirectory()) {
      generateIndex(fullPath);
      walkDirs(fullPath); // recurse
    }
  }
}

function generateIndex(folderPath) {
  const files = fs.readdirSync(folderPath)
    .filter(f => f.endsWith(".md") && f !== "_index.md");

  if (files.length === 0) return;

  const links = files
    .map(f => {
      const name = path.basename(f, ".md");
      return `- [[${name}]]`;
    })
    .join("\n");

  const indexPath = path.join(folderPath, "_index.md");

  const frontmatter = `---\ntitle: "${path.basename(folderPath)}"\n---\n`;
  const body = `${frontmatter}\n${links}\n`;

  fs.writeFileSync(indexPath, body);
  console.log(`✅ Generated index: ${indexPath}`);
}

// Run it!
walkDirs(ROOT);
