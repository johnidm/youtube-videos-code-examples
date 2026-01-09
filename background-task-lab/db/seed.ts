import { db } from './index';
import { users } from './schema';

const seedUsers = [
  { name: 'Alice Johnson', email: 'alice.johnson@example.com', age: 28 },
  { name: 'Bob Smith', email: 'bob.smith@example.com', age: 35 },
  { name: 'Charlie Brown', email: 'charlie.brown@example.com', age: 42 },
  { name: 'Diana Prince', email: 'diana.prince@example.com', age: 31 },
  { name: 'Ethan Hunt', email: 'ethan.hunt@example.com', age: 39 },
  { name: 'Fiona Green', email: 'fiona.green@example.com', age: 26 },
  { name: 'George Wilson', email: 'george.wilson@example.com', age: 45 },
  { name: 'Hannah Lee', email: 'hannah.lee@example.com', age: 29 },
  { name: 'Ian Malcolm', email: 'ian.malcolm@example.com', age: 52 },
  { name: 'Julia Roberts', email: 'julia.roberts@example.com', age: 33 },
  { name: 'Kevin Hart', email: 'kevin.hart@example.com', age: 38 },
  { name: 'Laura Palmer', email: 'laura.palmer@example.com', age: 24 },
  { name: 'Michael Scott', email: 'michael.scott@example.com', age: 44 },
  { name: 'Nina Simone', email: 'nina.simone@example.com', age: 37 },
  { name: 'Oscar Martinez', email: 'oscar.martinez@example.com', age: 41 },
  { name: 'Pam Beesly', email: 'pam.beesly@example.com', age: 32 },
  { name: 'Quincy Jones', email: 'quincy.jones@example.com', age: 48 },
  { name: 'Rachel Green', email: 'rachel.green@example.com', age: 30 },
  { name: 'Steve Rogers', email: 'steve.rogers@example.com', age: 36 },
  { name: 'Tina Turner', email: 'tina.turner@example.com', age: 43 },
];

async function seed() {
  console.log('Seeding database...');
  
  await db.insert(users).values(seedUsers);
  
  console.log('✓ Seeded 20 users successfully!');
}

seed()
  .catch((error) => {
    console.error('Error seeding database:', error);
    process.exit(1);
  });
