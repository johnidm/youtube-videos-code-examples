import 'dotenv/config'
import { db } from '@/db';
import { users } from '@/db/schema';

async function main() {
  console.log('[CRON] Starting late service order notification...')
  const databaseFile = process.env.DATABASE_FILE;
  
  console.log('[CRON] Database file:', databaseFile)

  try {
    const allUsers = await db.select().from(users);
    const lateOrders = allUsers.filter(user => user.age && user.age > 40);
    
    console.log(`[CRON] Found ${lateOrders.length} users with age > 40 (simulating late orders)`)
    
    lateOrders.forEach(user => {
      console.log(`[CRON] Notifying user: ${user.name} (${user.email})`)
    });

    console.log('[CRON] Late service order notifications completed successfully')
    process.exit(0)
  } catch (error) {
    console.error('[CRON] Notification failed:', error)
    process.exit(1)
  }
}

main()
