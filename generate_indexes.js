const fs = require("fs");
const path = require("path");

const ROOT = path.join(__dirname, "content"); // Adjust if needed
const RECENT_START = "<!-- RECENT-START -->";
const RECENT_END = "<!-- RECENT-END -->";

function walkDirs(dir) {
  const subdirs = fs.readdirSync(dir, { withFileTypes: true });
  for (const item of subdirs) {
    const fullPath = path.join(dir, item.name);
    if (item.isDirectory()) {
      renameOldIndex(fullPath);     // rename _index.md if needed
      generateIndexIfMissing(fullPath);
      walkDirs(fullPath);           // recurse
    }
  }
}

function renameOldIndex(folderPath) {
  const oldPath = path.join(folderPath, "_index.md");
  const newPath = path.join(folderPath, "index.md");

  if (fs.existsSync(oldPath) && !fs.existsSync(newPath)) {
    fs.renameSync(oldPath, newPath);
    console.log(`🔁 Renamed _index.md → index.md in ${folderPath}`);
  }
}

function generateIndexIfMissing(folderPath) {
  const indexPath = path.join(folderPath, "index.md");
  if (fs.existsSync(indexPath)) {
    // Update recent files section only if it's the main index
    const relativePath = path.relative(ROOT, folderPath);
    if (relativePath === "1 Keepers' Compendium") {
      updateRecentSection(indexPath, folderPath);
    }
    return;
  }

  const title = path.basename(folderPath);
  const relativePath = path.relative(ROOT, folderPath);
  const isMainIndex = relativePath === "1 Keepers' Compendium";

  let content = `---\ntitle: "${title}"\n---\n`;

  if (isMainIndex) {
    const recentFiles = collectMarkdownFiles(folderPath)
      .sort((a, b) => b.mtime - a.mtime)
      .slice(0, 3)
      .map(f => `- [[${f.name}]]`)
      .join("\n");

    content += `\n${RECENT_START}\n${recentFiles}\n${RECENT_END}\n`;
  }

  fs.writeFileSync(indexPath, content);
  console.log(`✅ Created index: ${indexPath}`);
}

function updateRecentSection(indexPath, folderPath) {
  const original = fs.readFileSync(indexPath, "utf8");

  const recentFiles = collectMarkdownFiles(folderPath)
    .sort((a, b) => b.mtime - a.mtime)
    .slice(0, 3)
    .map(f => `- [[${f.name}]]`)
    .join("\n");

  const recentBlock = `${RECENT_START}\n${recentFiles}\n${RECENT_END}`;

  let newContent;

  if (original.includes(RECENT_START) && original.includes(RECENT_END)) {
    newContent = original.replace(
      new RegExp(`${RECENT_START}[\\s\\S]*?${RECENT_END}`),
      recentBlock
    );
  } else {
    newContent = `${original.trim()}\n\n${recentBlock}\n`;
  }

  fs.writeFileSync(indexPath, newContent);
  console.log("♻️ Updated RECENT block in main index.");
}

function collectMarkdownFiles(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  let files = [];

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);

    if (entry.isDirectory()) {
      files = files.concat(collectMarkdownFiles(fullPath));
    } else if (
      entry.isFile() &&
      entry.name.endsWith(".md") &&
      entry.name !== "index.md"
    ) {
      const stats = fs.statSync(fullPath);
      files.push({
        name: path.basename(entry.name, ".md"),
        mtime: stats.mtime,
        path: fullPath,
      });
    }
  }

  return files;
}

// Run it
walkDirs(ROOT);
