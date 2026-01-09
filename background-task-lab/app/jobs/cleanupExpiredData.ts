import 'dotenv/config'
import { db } from '@/db';
import { users } from '@/db/schema';


async function main() {
  console.log('[CRON] Starting daily cleanup...')
  const databaseFile = process.env.DATABASE_FILE;

  console.log('[CRON] Database file:', databaseFile)

  try {
    const allUsers = await db.select().from(users);
    console.log('[CRON] All users:', allUsers)

    console.log('[CRON] Cleanup completed successfully')
    process.exit(0)
  } catch (error) {
    console.error('[CRON] Cleanup failed:', error)
    process.exit(1)
  }
}

main()
