
import { db } from '@/db';
import { users } from '@/db/schema';

export const dynamic = 'force-dynamic';

export default async function Home() {

  const allUsers = await db.select().from(users);

  return (
    <div>
      <pre>{JSON.stringify(allUsers, null, 2)}</pre>
    </div>
  );
}
