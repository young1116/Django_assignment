
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# 게시글 목록 보기 (Read)
class PostListView(ListView):  # ListView를 사용하여 게시글 목록을 표시
    model = Post  # 사용할 모델
    template_name = 'post/post_list.html'  # 템플릿 지정

# 게시글 상세 보기 (Read)
class PostDetailView(DetailView):  # DetailView를 사용하여 특정 게시글 상세 내용 표시
    model = Post
    template_name = 'post/post_detail.html'

# 게시글 생성 (Create)
class PostCreateView(CreateView):  # CreateView를 사용하여 새 게시글 생성
    model = Post
    fields = ['title', 'content']
    template_name = 'post/post_form.html'

# 게시글 수정 (Update)
class PostUpdateView(UpdateView):  # UpdateView를 사용하여 게시글 수정
    model = Post
    fields = ['title', 'content']
    template_name = 'post/post_form.html'

# 게시글 삭제 (Delete)
class PostDeleteView(DeleteView):  # DeleteView를 사용하여 게시글 삭제
    model = Post
    template_name = 'post/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')  # 삭제 후 목록 페이지로 이동
