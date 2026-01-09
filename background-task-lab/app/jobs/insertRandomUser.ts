import 'dotenv/config'
import { db } from '@/db';
import { users } from '@/db/schema';

// Helper function to generate random names
function getRandomName(): string {
  const firstNames = ['Alex', 'Jordan', 'Taylor', 'Morgan', 'Casey', 'Riley', 'Avery', 'Quinn', 'Skyler', 'Dakota'];
  const lastNames = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez'];
  
  const firstName = firstNames[Math.floor(Math.random() * firstNames.length)];
  const lastName = lastNames[Math.floor(Math.random() * lastNames.length)];
  
  return `${firstName} ${lastName}`;
}

// Helper function to generate random email
function getRandomEmail(name: string): string {
  const domain = ['example.com', 'test.com', 'demo.com', 'sample.com'];
  const emailName = name.toLowerCase().replace(' ', '.');
  const randomDomain = domain[Math.floor(Math.random() * domain.length)];
  const randomNum = Math.floor(Math.random() * 1000);
  
  return `${emailName}${randomNum}@${randomDomain}`;
}

// Helper function to generate random age
function getRandomAge(): number {
  return Math.floor(Math.random() * (65 - 18 + 1)) + 18; // Age between 18 and 65
}

async function main() {
  console.log('[CRON] Starting random user insertion...')
  const databaseFile = process.env.DATABASE_FILE;
  
  console.log('[CRON] Database file:', databaseFile)

  try {
    const randomName = getRandomName();
    const randomEmail = getRandomEmail(randomName);
    const randomAge = getRandomAge();

    const newUser = await db.insert(users).values({
      name: randomName,
      email: randomEmail,
      age: randomAge,
    }).returning();

    console.log(`[CRON] Successfully inserted new user:`, newUser[0]);
    console.log(`[CRON] Name: ${randomName}, Email: ${randomEmail}, Age: ${randomAge}`);
    
    // Get total user count
    const allUsers = await db.select().from(users);
    console.log(`[CRON] Total users in database: ${allUsers.length}`);

    console.log('[CRON] Random user insertion completed successfully')
    process.exit(0)
  } catch (error) {
    console.error('[CRON] User insertion failed:', error)
    process.exit(1)
  }
}

main()
