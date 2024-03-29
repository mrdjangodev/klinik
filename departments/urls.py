from django.urls import path

from .views import (
    main_index, department_detail,
    main_index2, show_all_patients_by_department,
    search_patients, show_all_rooms,
    search_rooms, show_doctors_by_department,
    search_doctors_by_department, 
    show_staffs_by_department, search_staffs_by_department,
    show_admissions_by_department, search_admissions_by_department,
    show_beds_by_department, search_beds_by_department,

)

urlpatterns = [
    path('main/', main_index, name='main_index'),
    path('main/2', main_index2, name='main_index2'),
    path('detail/<int:pk>/', department_detail, name='detail-department'),
    path('<int:department_id>/show_patients/', show_all_patients_by_department, name='show-patients-by-department'),
    path('departent/<int:department_id>/search_patients/', search_patients, name="search_patients_in_department"),
    path('<int:department_id>/show_rooms/', show_all_rooms, name='show-all-rooms'),
    path('<int:department_id>/search_rooms/', search_rooms, name='search-rooms'),
    
    path('<int:department_id>/show_doctors/', show_doctors_by_department, name='show-doctors-by-department'),
    path('<int:department_id>/search_doctors/', search_doctors_by_department, name='search-doctors-by-department'),

    path('<int:department_id>/show_staffs/', show_staffs_by_department, name='show-staffs-by-department'),
    path('<int:department_id>/search_staffs/', search_staffs_by_department, name='search-staffs-by-department'),

    path('<int:department_id>/show_admissions/', show_admissions_by_department, name='show-admissions-by-department'),
    path('<int:department_id>/search_admissions/', search_admissions_by_department, name='search-admissions-by-department'),

    path('<int:department_id>/show_beds/', show_beds_by_department, name='show-beds-by-department'),
    path('<int:department_id>/search_beds/', search_beds_by_department, name='search-beds-by-department'),

]   