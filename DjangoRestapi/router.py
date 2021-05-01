from audioserverapi.viewsets import PodcastViewset, SongViewset, AudiobookViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('podcast',PodcastViewset)
router.register('song',SongViewset)
router.register('audiobook',AudiobookViewset)
# localhost:p/api/song/5
# GET, POST, PUT, DELETE
# list , retrive