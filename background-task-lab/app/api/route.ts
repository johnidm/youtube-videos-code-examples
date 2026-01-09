import { NextResponse } from 'next/server';
import { db } from '@/db';
import { users } from '@/db/schema';

export async function GET() {
  const allUsers = await db.select().from(users);
  return NextResponse.json({ users: allUsers });
}
