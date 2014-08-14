from django.conf.urls import patterns, url

from timepiece.crm import views


urlpatterns = patterns('',
    # Search
    url(r'^quick_search/$',
        views.QuickSearch.as_view(),
        name='quick_search'),

    # Users
    url(r'^user/settings/$',
        views.EditSettings.as_view(),
        name='edit_settings'),
    url(r'^user/$',
        views.ListUsers.as_view(),
        name='list_users'),
    url(r'^user/create/$',
        views.CreateUser.as_view(),
        name='create_user'),
    url(r'^user/(?P<user_id>\d+)/$',
        views.ViewUser.as_view(),
        name='view_user'),
    url(r'^user/(?P<user_id>\d+)/edit/$',
        views.EditUser.as_view(),
        name='edit_user'),
    url(r'^user/(?P<user_id>\d+)/delete/$',
        views.DeleteUser.as_view(),
        name='delete_user'),

    # User timesheets
    url(r'^user/(?P<user_id>\d+)/timesheet/' +
                '(?:(?P<active_tab>overview|all-entries|daily-summary)/)?$',
        views.view_user_timesheet,
        name='view_user_timesheet'),
    url(r'^user/(?P<user_id>\d+)/timesheet/reject/$',
        views.reject_user_timesheet,
        name='reject_user_timesheet'),
    url(r'^user/(?P<user_id>\d+)/timesheet/(?P<action>verify|approve)/$',
        views.change_user_timesheet,
        name='change_user_timesheet'),

    # Projects
    url(r'^project/$',
        views.ListProjects.as_view(),
        name='list_projects'),
    url(r'^project/create/$',
        views.CreateProject.as_view(),
        name='create_project'),
    url(r'^project/(?P<project_id>\d+)/$',
        views.ViewProject.as_view(),
        name='view_project'),
    url(r'^project/(?P<project_id>\d+)/edit/$',
        views.EditProject.as_view(),
        name='edit_project'),
    url(r'^project/(?P<project_id>\d+)/delete/$',
        views.DeleteProject.as_view(),
        name='delete_project'),
    url(r'^project/(?P<project_id>\d+)/activities/$',
        views.get_project_activities,
        name='project_activities'),

    # Project timesheets
    url(r'^project/(?P<project_id>\d+)/timesheet/$',
        views.ProjectTimesheet.as_view(),
        name='view_project_timesheet'),
    url(r'^project/(?P<project_id>\d+)/timesheet/csv/$',
        views.ProjectTimesheetCSV.as_view(),
        name='view_project_timesheet_csv'),

    # Businesses
    url(r'^business/$',
        views.ListBusinesses.as_view(),
        name='list_businesses'),
    url(r'^business/create/$',
        views.CreateBusiness.as_view(),
        name='create_business'),
    url(r'^business/(?P<business_id>\d+)/$',
        views.ViewBusiness.as_view(),
        name='view_business'),
    url(r'^business/(?P<business_id>\d+)/edit/$',
        views.EditBusiness.as_view(),
        name='edit_business'),
    url(r'^business/(?P<business_id>\d+)/delete/$',
        views.DeleteBusiness.as_view(),
        name='delete_business'),
    url(r'^business/(?P<business_id>\d+)/get_users/$',
        views.get_users_for_business,
        name='get_users_for_business'),
    

    # User-project relationships
    url(r'^relationship/create/$',
        views.CreateRelationship.as_view(),
        name='create_relationship'),
    url(r'^relationship/edit/$',
        views.EditRelationship.as_view(),
        name='edit_relationship'),
    url(r'^relationship/delete/$',
        views.DeleteRelationship.as_view(),
        name='delete_relationship'),
    

    # Paid Time Off
    url(r'^pto/(?:(?P<active_tab>summary|requests|history|approvals|all_history)/)?$',
        views.pto_home,
        name='pto'),
    url(r'^pto/request/(?P<pto_request_id>\d+)$',
        views.pto_request_details,
        name='pto_request_details'),
    url(r'^pto/request/create/$',
        views.CreatePTORequest.as_view(),
        name='create_pto_request'),
    url(r'^pto/request/(?P<pto_request_id>\d+)/edit/$',
        views.EditPTORequest.as_view(),
        name='edit_pto_request'),
    url(r'^pto/request/(?P<pto_request_id>\d+)/delete/$',
        views.DeletePTORequest.as_view(),
        name='delete_pto_request'),
    url(r'^pto/request/(?P<pto_request_id>\d+)/approve/$',
        views.ApprovePTORequest.as_view(),
        name='approve_pto_request'),
    url(r'^pto/request/(?P<pto_request_id>\d+)/deny/$',
        views.DenyPTORequest.as_view(),
        name='deny_pto_request'),

    
    # Milestones
    url(r'^project/(?P<project_id>\d+)/milestone/(?P<milestone_id>\d+)/$',
        views.ViewMilestone.as_view(),
        name='view_milestone'),
    url(r'^project/(?P<project_id>\d+)/milestone/create/$',
        views.CreateMilestone.as_view(),
        name='create_milestone'),
    url(r'^project/(?P<project_id>\d+)/milestone/(?P<milestone_id>\d+)/edit/$',
        views.EditMilestone.as_view(),
        name='edit_milestone'),
    url(r'^project/(?P<project_id>\d+)/milestone/(?P<milestone_id>\d+)/delete/$',
        views.DeleteMilestone.as_view(),
        name='delete_milestone'),

    
    # Activity Goals
    # url(r'^project/(?P<project_id>\d+)/milestones/(?P<milestone_id>\d+)/activity_goals$',
    #     views.ListProjects.as_view(),
    #     name='view_activity_goals'),
    url(r'^project/(?P<project_id>\d+)/milestone/(?P<milestone_id>\d+)/activity_goal/create/$',
        views.CreateActivityGoal.as_view(),
        name='create_activity_goal'),
    url(r'^project/(?P<project_id>\d+)/milestone/(?P<milestone_id>\d+)/activity_goal/(?P<activity_goal_id>\d+)/edit/$',
        views.EditActivityGoal.as_view(),
        name='edit_activity_goal'),
    url(r'^project/(?P<project_id>\d+)/milestone/(?P<milestone_id>\d+)/activity_goal/(?P<activity_goal_id>\d+)/delete/$',
        views.DeleteActivityGoal.as_view(),
        name='delete_activity_goal'),
)
