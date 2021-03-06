from django.urls import path

from blog.views.comment import CommentCreate
from blog.views.home import home
from blog.views.post import PostView, PostCreate, PostUpdate, PostDelete
from blog.views.home import nav
from blog.views.files import BasicUploadView, download_file, delete_file
from .views.meetings import MeetingCreate
from .views.meetingsignin import MeetingSignin
from .views.meetingsignout import meetingSignOut
from .views.endmeeting import end_meeting
from .views.stats import stats

app_name = 'blog'
urlpatterns = [
    # ex: /blog/files
    path('files', BasicUploadView.as_view(), name='upload_file'),
    # ex: /blog/files/something.jpg
    path('files/<str:pk>.<str:ext>', download_file, name='download_file'),
    # path('files/<str:pk>.<str:ext>/update/', update_file, name='update_file'),
    path('files/<str:pk>.<str:ext>/delete/', delete_file, name='delete_file'),
    # In case people use the old path in a blog entry
    path('blog/files/<str:pk>.<str:ext>', download_file, name='download_file_blog'),
    # ex: /blog/
    path('', home, name='home'),
    # ex: /blog/dusan
    path('user/<str:username>', home, name='user_posts'),
    # ex: /blog/post/5/
    path('post/<int:pk>/', PostView.as_view(), name='post'),
    # ex: /blog/post/create/
    path('post/create/', PostCreate.as_view(), name='create_post'),
    # ex: /blog/post/5/update/
    path('post/create/<int:pk>/update', PostUpdate.as_view(), name='update_post'),
    # ex: /blog/post/5/delete/
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='delete_post'),
    # ex: /blog/post/5/comment/
    path('post/<int:pk>/comment/', CommentCreate.as_view(), name='create_comment'),
    path('meeting', MeetingCreate.as_view(), name="create_meeting"),
    path('meeting/stats', stats, name="stats"),
    path('meeting/<int:pk>/end', end_meeting, name='end_meeting'),
    path('meeting/<int:pk>/', MeetingSignin.as_view(), name='signin'),
    path('signout/<int:signId>/', meetingSignOut, name='signout'),
    path('<str:link>', nav, name='nav'),
]
