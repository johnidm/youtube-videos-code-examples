# MySQL Profiling Queries 

This project demonstrates how to log all queries executed on a MySQL database.

The logs are stored in the `log/mysql` directory.

## Usage

```bash
docker compose up --build --force-recreate
```

## Enabled Logging 


The `general_log` is a special feature in MySQL that records all queries and client connections that the server processes. Think of it as MySQL’s "black box recorder" for SQL activity.

This is making the MySQL container always start with query logging enabled, writing every SQL statement to `/var/log/mysql/general.log`.

`--general_log=1`: This enables MySQL’s general query log, which logs every SQL query that the server receives (including connections and statements). It’s mostly used for debugging or auditing, but should be avoided in production because it can slow down the server and generate very large log files.

`--general_log_file=/var/log/mysql/general.log`: This tells MySQL to save the general log entries into a specific file inside the container: `/var/log/mysql/general.log`. You can then access this file (for example, by mounting it to your host system) to see what queries are being executed.
