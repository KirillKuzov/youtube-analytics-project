
import json


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.get_channel_info(channel_id)
        self.title = self.channel['snippet']["title"]
        self.description = self.channel['snippet']["description"]
        self.url = f"https://www.youtube.com/channel/{self.__channel_id}"
        self.subscribers = self.channel["statistics"]["subscriberCount"]
        self.video_count = self.channel["statistics"]["videoCount"]
        self.view_count = self.channel["statistics"]["viewCount"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))
