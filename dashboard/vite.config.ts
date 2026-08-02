import fs from "node:fs"
import path from "node:path"
import tailwindcss from "@tailwindcss/vite"
import react from "@vitejs/plugin-react"
import { type Plugin, defineConfig } from "vite"

const DOCS = path.resolve(import.meta.dirname, "../docs")

/**
 * In dev, serve the collector's output straight out of ../docs. Keeping these
 * files out of public/ matters: everything in public/ is copied into the build
 * output, so a build would overwrite freshly collected data with whatever
 * snapshot happened to be sitting in the repo.
 */
function serveCollectorData(): Plugin {
  const served = ["/report.json", "/history.json", "/report.md"]
  return {
    name: "sentinel-data",
    configureServer(server) {
      server.middlewares.use((req, res, next) => {
        const url = (req.url ?? "").split("?")[0]
        if (!served.includes(url)) return next()
        const file = path.join(DOCS, path.basename(url))
        if (!fs.existsSync(file)) {
          res.statusCode = 404
          return res.end(
            `${path.basename(url)} not found — run \`python3 -m sentinel.main --once\` first.`
          )
        }
        res.setHeader(
          "Content-Type",
          url.endsWith(".md") ? "text/markdown" : "application/json"
        )
        res.setHeader("Cache-Control", "no-store")
        return res.end(fs.readFileSync(file))
      })
    },
  }
}

// Builds straight into ../docs (the GitHub Pages root). emptyOutDir stays false
// because the Python collector writes report.json / history.json / report.md
// into the same folder.
export default defineConfig({
  plugins: [react(), tailwindcss(), serveCollectorData()],
  base: "./",
  build: {
    outDir: DOCS,
    emptyOutDir: false,
  },
  resolve: {
    alias: {
      "@": path.resolve(import.meta.dirname, "./src"),
    },
  },
})
