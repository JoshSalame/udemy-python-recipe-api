"""
Django command to wait for database to be available.
Used on app startup to prevent crashing before DB is ready.
"""

import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_available = False
        check_count = 0

        while (db_available is False) and (check_count < 60):
            try:
                self.check(databases=['default'])
                db_available = True
            except (Psycopg2OpError, OperationalError):
                check_count += 1
                if (check_count >= 60):
                    break

                self.stdout.write("Database unavailable, waiting 2 seconds then checking again...") # noqa
                time.sleep(2)

        if (db_available):
            self.stdout.write(self.style.SUCCESS("Database is now available"))
        else:
            self.stdout.write(self.style.ERROR("Database unavailable for 2 minutes, crashing.")) # noqa
