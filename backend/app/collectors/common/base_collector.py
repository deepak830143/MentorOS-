from abc import ABC, abstractmethod


class BaseCollector(ABC):
    """
    Base class for all government notification collectors.
    """

    @abstractmethod
    def fetch(self):
        """
        Download data from the official website.
        """
        pass

    @abstractmethod
    def parse(self, raw_data):
        """
        Convert raw HTML/JSON into notification objects.
        """
        pass

    @abstractmethod
    def validate(self, notifications):
        """
        Remove invalid or incomplete notifications.
        """
        pass

    @abstractmethod
    def save(self, notifications):
        """
        Save notifications into PostgreSQL.
        """
        pass

    def collect(self):
        """
        Complete workflow executed by the scheduler.
        """

        print("=" * 60)
        print(f"🚀 Running {self.__class__.__name__}")

        raw_data = self.fetch()

        notifications = self.parse(raw_data)

        notifications = self.validate(notifications)

        self.save(notifications)

        print(f"✅ {self.__class__.__name__} Finished")
        print("=" * 60)