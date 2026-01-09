import { db } from './index';
import { users } from './schema';

async function queryUsers() {
  console.log('Querying all users from database...\n');
  
  const allUsers = await db.select().from(users);
  
  console.log(`Found ${allUsers.length} users:\n`);
  
  allUsers.forEach((user) => {
    console.log(`ID: ${user.id}`);
    console.log(`Name: ${user.name}`);
    console.log(`Email: ${user.email}`);
    console.log(`Age: ${user.age}`);
    console.log(`Created At: ${user.createdAt}`);
    console.log('---');
  });
  
  console.log('\nQuery completed successfully!');
}

queryUsers()
  .catch((error) => {
    console.error('Error querying database:', error);
    process.exit(1);
  });
