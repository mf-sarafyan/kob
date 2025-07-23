const fs = require("fs");
const path = require("path");

const ROOT = path.join(__dirname, "content"); // Adjust if needed

const START = "<!-- AUTO-LINKS-START -->";
const END = "<!-- AUTO-LINKS-END -->";
const RECENT_START = "<!-- RECENT-START -->";
const RECENT_END = "<!-- RECENT-END -->";

function walkDirs(dir) {
  const subdirs = fs.readdirSync(dir, { withFileTypes: true });
  for (const item of subdirs) {
    const fullPath = path.join(dir, item.name);
    if (item.isDirectory()) {
      renameOldIndex(fullPath);     // ← rename _index.md if found
      generateIndex(fullPath);
      walkDirs(fullPath);           // Recurse
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

function generateIndex(folderPath) {
  const files = fs.readdirSync(folderPath)
    .filter(f => f.endsWith(".md") && f !== "index.md");

  if (files.length === 0) return;

  const links = files
    .map(f => {
      const name = path.basename(f, ".md");
      return `- [[${name}]]`;
    })
    .join("\n");

  const autoLinkSection = `${START}\n${links}\n${END}`;
  const indexPath = path.join(folderPath, "index.md");

  let indexContent = "";

  if (fs.existsSync(indexPath)) {
    indexContent = fs.readFileSync(indexPath, "utf8");

    if (indexContent.includes(START) && indexContent.includes(END)) {
      indexContent = indexContent.replace(
        new RegExp(`${START}[\\s\\S]*?${END}`),
        autoLinkSection
      );
    } else {
      indexContent = `${indexContent.trim()}\n\n${autoLinkSection}`;
    }
  } else {
    const title = path.basename(folderPath);
    indexContent = `---\ntitle: "${title}"\n---\n\n${autoLinkSection}\n`;
  }

  // If it's the main index, also insert a "Recently Updated" section
  const relativePath = path.relative(ROOT, folderPath);
  const isMainIndex = relativePath === "1 Keepers' Compendium";

  if (isMainIndex) {
    const recentFiles = collectMarkdownFiles(folderPath)
      .sort((a, b) => b.mtime - a.mtime)
      .slice(0, 3)
      .map(f => `- [[${f.name}]]`)
      .join("\n");

    const recentSection = `${RECENT_START}\n${recentFiles}\n${RECENT_END}`;

    if (indexContent.includes(RECENT_START) && indexContent.includes(RECENT_END)) {
      indexContent = indexContent.replace(
        new RegExp(`${RECENT_START}[\\s\\S]*?${RECENT_END}`),
        recentSection
      );
    } else {
      indexContent += `\n\n${recentSection}`;
    }
  }

  fs.writeFileSync(indexPath, indexContent);
  console.log(`✅ Updated index: ${indexPath}`);
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

// Run the script
walkDirs(ROOT);
