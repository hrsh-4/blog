from django.urls import path,include,re_path
from blog import views



urlpatterns = [ 
	
	path('',views.PostListView.as_view(),name='post_list'),
	path('about/',views.AboutView.as_view(),name='about'),  
	re_path(r'post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
	re_path(r'post/new/',views.CreatePostView.as_view(),name='post_create'),
	re_path(r'post/update/(?P<pk>\d+)$',views.UpdatePostView.as_view(),name='post_update'),
	re_path(r'post/delete/(?P<pk>\d+)$',views.DeletePostView.as_view(),name='post_delete'),
	re_path(r'post/draft/(?P<pk>\d+)$',views.DraftPostView.as_view(),name='post_draft'),
	re_path(r'post/publish/(?P<pk>\d+)$',views.publish_post,name='post_publish'),
	re_path(r'post/comment/(?P<pk>\d+)$',views.add_comment_to_post,name='add_comment_to_post'),
	re_path(r'post/approvecomment/(?P<pk>\d+)$',views.approve_comment,name='approve_comment'),
	re_path(r'post/deletecomment/(?P<pk>\d+)$',views.delete_comment,name='delete_comment'),
	
	
] 