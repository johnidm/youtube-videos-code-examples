#!/bin/sh

cron_file=/etc/cron.d/app

echo "Setting up cron jobs..."
echo >> $cron_file

echo "PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin" >> $cron_file

# Schedule cleanup job - runs every minute
echo "* * * * * cd /app && npm run job:cleanup > /proc/1/fd/1 2>&1" >> $cron_file

# Schedule notify job - runs every minute
echo "* * * * * cd /app && npm run job:notify > /proc/1/fd/1 2>&1" >> $cron_file

# Schedule insert random user job - runs every minute
echo "* * * * * cd /app && npm run job:insert > /proc/1/fd/1 2>&1" >> $cron_file

echo "Publishing environment variables to cron..."
printenv | grep -v "no_proxy" >> /etc/environment

echo "Starting cron service in background..."
crond

echo "Starting Next.js server..."
exec node server.js
