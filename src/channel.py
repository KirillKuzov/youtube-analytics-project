import json
import os
from distutils.command.build import build


class Channel:
    """Класс для ютуб-канала"""
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

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

    @classmethod
    def get_channel_info(cls, channel_id: str) -> dict:
        """Получает информацию о канале по его ID."""
        response = cls.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        return response['items'][0]

    @classmethod
    def get_service(cls):
        """Класс-метод возвращающий объект для работы с YouTube API."""
        return cls.youtube

    def to_json(self, file_name):
        """Метод сохраняющий в файл значения атрибутов экземпляра Channel."""
        channel_info = {
            "channel_id": self.__channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscribers": self.subscribers,
            "videoCount": self.video_count,
            "viewCount": self.view_count,
        }

        json_data = json.dumps(channel_info, indent=2, ensure_ascii=False)

        with open(file_name, "w", encoding="UTF-8") as outfile:
            outfile.write(json_data)

