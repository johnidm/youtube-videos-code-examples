# Background Task Lab

A Next.js application with SQLite database and background job system using Docker.

## 🚀 Quick Start

### Build and Run the Application
```bash
docker compose up --build
```

The application will automatically:
- Start the Next.js server on port 3000
- Set up cron jobs in the background
- Run scheduled jobs according to the cron schedule

All cron job are in `app/jobs` folder.

## ⏰ Cron Schedule Configuration

The cron jobs are configured in `entrypoint.sh` and automatically set up when the container starts. To modify schedules, edit the cron expressions:

Example:

```bash
0 * * * * cd /app && npm run job:notify # Every hour
```

**Common cron patterns:**
- `0 1 * * *` - Daily at 1:00 AM
- `0 * * * *` - Every hour
- `*/15 * * * *` - Every 15 minutes
- `0 1 * * 0` - Weekly on Sunday at 1:00 AM
- `0 0 1 * *` - Monthly on the 1st at midnight

## 🛠️ Development Commands

### Run Jobs Locally (Development)
```bash
# Run notify job with TypeScript
npm run job:notify:dev
```

### Run Jobs Locally (Production Build)
```bash
# Build all jobs
npm run build:cron

# Run compiled notify job
npm run job:notify
```

### Run Jobs in Docker
```bash
# Execute notify job manually (bypasses cron schedule)
docker compose exec app npm run job:notify

# View cron logs (jobs run by cron are logged to container stdout)
docker compose logs -f app
```

## 🏗️ Architecture

### Job Compilation
All TypeScript files in `app/jobs/` are automatically compiled to JavaScript using esbuild during the build process:
- Source: `app/jobs/*.ts`
- Output: `.next/standalone/jobs/*.js`
- External dependencies: `better-sqlite3`, `drizzle-orm`

### Docker Structure
```
/app/
├── server.js              # Next.js server
├── jobs/                  # Compiled job files
│   ├── cleanupExpiredData.js
│   └── notifyLateServiceOrder.js
├── node_modules/          # Runtime dependencies
├── .next/
│   └── static/
└── public/

/entrypoint.sh             # Startup script that:
                           # 1. Configures cron jobs
                           # 2. Starts cron daemon
                           # 3. Starts Next.js server

/etc/cron.d/app            # Cron job definitions
```

## 🔧 Adding New Jobs

1. Create a new TypeScript file in `app/jobs/`:
```typescript
// app/jobs/myNewJob.ts
import 'dotenv/config'
import { db } from '@/db';

async function main() {
  console.log('[CRON] Starting my new job...')
  // Your job logic here
  process.exit(0)
}

main()
```

2. Add scripts to `package.json`:
```json
"job:mynew": "node jobs/myNewJob.js",
"job:mynew:dev": "tsx app/jobs/myNewJob.ts"
```

3. Add cron schedule to `entrypoint.sh`:
```bash
# Schedule new job - runs every 6 hours
echo "0 */6 * * * nextjs cd /app && npm run job:mynew > /proc/1/fd/1 2>&1" >> $cron_file
```

4. Rebuild and run:
```bash
docker compose up --build
```

The new job will automatically be scheduled and run according to the cron expression.

## 📝 Environment Variables

- `DATABASE_FILE`: Path to SQLite database file (default: `sqlite.db`)
- `NODE_ENV`: Environment mode (`production` or `development`)

## Understanding External Dependencies in esbuild

### Why Some Dependencies Must Be External

When building jobs with esbuild, certain dependencies are marked as `--external`, meaning they won't be bundled into the compiled JavaScript file. Instead, they're loaded from `node_modules` at runtime.

### When to Use `--external`

#### ❌ **Must Be External** (Cannot Bundle)

**Native Modules** - Packages with C/C++ bindings:
- `better-sqlite3` - SQLite native bindings
- `bcrypt` - Cryptography native module
- `sharp` - Image processing native module
- `node-gyp` based packages
- Any package with `.node` binary files

**Why?** esbuild only works with JavaScript/TypeScript. Native modules contain compiled platform-specific binaries that cannot be bundled.

**Error if bundled:** `Cannot find module 'better_sqlite3.node'`

#### ⚠️ **Should Be External** (Complex Modules)

**Packages with complex module structures:**
- `drizzle-orm` - Complex internal imports and subpath patterns
- `prisma` - Has native binaries and generated code
- Packages with dynamic imports or conditional exports

**Why?** Bundling can break internal module resolution and cause runtime errors.

#### ✅ **Can Be Bundled** (Pure JavaScript)

**Most npm packages:**
- `nodemailer` - Email library
- `axios` - HTTP client
- `lodash` - Utility functions
- `date-fns` - Date manipulation
- `zod` - Schema validation

**Benefits of bundling:**
- Smaller `node_modules` in Docker
- Faster startup time
- Self-contained job files

### Current Configuration

```bash
# In package.json
"build:cron": "esbuild app/jobs/*.ts --bundle --platform=node --outdir=.next/standalone/jobs --external:better-sqlite3 --external:drizzle-orm"
```

**Result:**
- Compiled files: ~19KB (only your code)
- Dependencies loaded from: `/app/node_modules/` at runtime
- Works with native modules ✅

### Adding New Dependencies

**If adding a pure JavaScript package (e.g., nodemailer):**
```bash
# No changes needed - it will be bundled automatically
npm install nodemailer
```

**If adding a native module (e.g., bcrypt):**
```bash
# Add to external list in package.json
"build:cron": "... --external:better-sqlite3 --external:drizzle-orm --external:bcrypt"
```

## 🔍 View Logs

```bash
# View all logs (includes Next.js server and cron job output)
docker compose logs -f

# View app logs
docker compose logs -f app

# Check if cron is running
docker compose exec app ps aux | grep cron

# View cron job file
docker compose exec app cat /etc/cron.d/app

# Manually verify cron daemon is running
# If it returns a process ID number, crond is running.
docker compose exec app pgrep crond


# Check if cron jobs are actually executing:
# Wait a minute or two, then check logs for job output
docker compose logs app | grep "\[CRON\]"