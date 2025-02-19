from django.urls import include, path
from rest_framework import routers
from courses.api import views

app_name = "courses"

router = routers.DefaultRouter()
router.register("courses", views.CourseViewSet)
router.register("subjects", views.SubjectViewSet)

urlpatterns = [
    # path(
    #     "subjects/",
    #     views.SubjectListView.as_view(),
    #     name="subject_list"
    # ),
    # path(
    #     "subjects/<pk>/", 
    #     views.SubjectDetailView.as_view(), 
    #     name="subject_detail"
    # ),
    path("", include(router.urls)),
    path(
        "courses/<pk>/enroll/",
        views.CourseEnrollView.as_view(),
        name="course_enroll"
    ),
]