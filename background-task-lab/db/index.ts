import Database from 'better-sqlite3';
import { drizzle } from 'drizzle-orm/better-sqlite3';
import * as schema from './schema';

const databaseFile = process.env.DATABASE_FILE || 'data.db';
const sqlite = new Database(databaseFile);
export const db = drizzle(sqlite, { schema });
