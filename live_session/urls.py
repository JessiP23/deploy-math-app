from django.urls import path
from .views import ScheduleSession, SessionDetails, SessionList

#name of app is live_session that attends any user to schedule live sessions with me (tutor) for all math subjects
app_name= 'live_session'

urlpatterns = [
    path('schedule_session/', ScheduleSession.as_view(), name='schedule_session'),
    path('list_session/', SessionList.as_view(), name='list_session'),
    path('detail_session/<int:session_id>/', SessionDetails.as_view(), name="detail_session"),
] 