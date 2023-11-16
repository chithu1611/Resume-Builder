from . import views
from django.urls import path

urlpatterns = [
    path('home/',views.home,name='home'),
    path('personal_details/',views.personal_details,name='personal_details'),
    path('education/',views.education,name='education'),
    path('Experience/',views.Exp,name='Exp'),
    path('skills/',views.skills,name='skills'),
    path('obj/',views.obj,name='obj'),
    path('project/',views.project,name='project'),
    path('Aoi/',views.aoi,name='Aoi'),
    path('Eca/',views.eca,name='Eca'),
    path('Hobbies/',views.hobby,name='Hobbies'),
    path('Language/',views.lang,name='Language'),
    path('Achieve/',views.ach,name='Achieve'),
    path('Templates/',views.temp,name='Templates'),
    path('Resume1/',views.res1,name='Resume1'),
    path('Resume2/',views.res2,name='Resume2'),
    path('Resume3/',views.res3,name='Resume3'),
    path('Resume4/',views.res4,name='Resume4'),
    path('Resume5/',views.res5,name='Resume5'),
    path('register/',views.register,name="register"),
    path('',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),
    #path('form-submit/', views.form_submit_view, name='my_form_submit_url')
]