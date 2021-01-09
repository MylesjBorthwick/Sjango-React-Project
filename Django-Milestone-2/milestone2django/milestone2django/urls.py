"""milestone2django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include                 
from rest_framework import routers                    
from recommended_textbooks import views as recommended_textbooks_views                           
from required_textbooks import views as required_textbooks_views                           
from sections import views as sections_views 
from notes import views as notes_views 
from instructors import views as instructors_views  
from gpa_conversions import views as gpa_conversions_views
from final_grades import views as final_grades_views
from examinations import views as examinations_views
from course_policies import views as course_policies_views
from course_objectives import views as course_objectives_views
from calendar_information import views as calendar_information_views
from calculator_use import views as calculator_use_views


from echo.views import echo_view,echo_response_view,echo_dynamic_lookup_view

router1 = routers.DefaultRouter()                      
router1.register(r'required_textbooks', required_textbooks_views.Required_Textbooks_View, 'required_textbooks')     
router2 = routers.DefaultRouter()                      
router2.register(r'recommended_textbooks', recommended_textbooks_views.Recommended_Textbooks_View, 'recommended_textbooks')     
router3 = routers.DefaultRouter()                      
router3.register(r'sections', sections_views.Sections_View, 'sections')     
router4 = routers.DefaultRouter()                      
router4.register(r'notes', notes_views.Notes_View, 'notes')     
router5 = routers.DefaultRouter()                      
router5.register(r'instructors', instructors_views.Instructors_View, 'instructors')     
router6 = routers.DefaultRouter()                      
router6.register(r'gpa_conversions', gpa_conversions_views.GPA_Conversions_View, 'gpa_conversions')     
router7 = routers.DefaultRouter()                      
router7.register(r'final_grades', final_grades_views.Final_Grades_View, 'final_grades')     
router8 = routers.DefaultRouter()                      
router8.register(r'examinations', examinations_views.Examinations_View, 'examinations')     
router9 = routers.DefaultRouter()                      
router9.register(r'course_policies', course_policies_views.Course_Policies_View, 'course_policies')     
router10 = routers.DefaultRouter()                      
router10.register(r'course_objectives', course_objectives_views.Course_Objectives_View, 'course_objectives')     
router11 = routers.DefaultRouter()                      
router11.register(r'calendar_information', calendar_information_views.Calendar_Information_View, 'calendar_information')     
router12 = routers.DefaultRouter()                      
router12.register(r'calculator_use', calculator_use_views.Calculator_Use_View, 'calculator_use')     



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',echo_view, name = 'home'),
    path('api/echos/',echo_response_view, name = 'echo response'),
    path('api/echos/<int:id>',echo_dynamic_lookup_view, name = 'single echo'),
    path('api/', include(router1.urls)),
    path('api/', include(router2.urls)), 
    path('api/', include(router3.urls)),
    path('api/', include(router4.urls)),
    path('api/', include(router5.urls)),
    path('api/', include(router6.urls)),
    path('api/', include(router7.urls)),
    path('api/', include(router8.urls)),
    path('api/', include(router9.urls)),
    path('api/', include(router10.urls)),
    path('api/', include(router11.urls)),
    path('api/', include(router12.urls))
]
