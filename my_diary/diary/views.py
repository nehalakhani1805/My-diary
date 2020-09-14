from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Entry
# Create your views here.
def home(request):
	return render(request,'diary/home.html',{'title':'Home Page'})

@login_required
def userdiary(request):
	u=request.user
	entries=u.entry_set.order_by('-date_posted').all()
	return render(request, 'diary/userdiary.html',{'entries':entries})
class EntryListView(ListView,LoginRequiredMixin):
	model=Entry
	template_name='diary/userdiary.html'
	context_object_name='entries'
	ordering=['-date_posted']
class EntryDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
	model=Entry

	def test_func(self):
		self.object=self.get_object()
		if self.request.user==self.object.owner:
			return True
		return False

class EntryCreateView(LoginRequiredMixin,CreateView):
	model=Entry
	fields=['title','content','date_posted']

	def form_valid(self,form):
		form.instance.owner=self.request.user
		return super().form_valid(form)

class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
	model=Entry
	fields=['title','content']

	'''def form_valid(self,form):
		form.instance.owner=self.request.user
		return super().form_valid(form)'''
	def test_func(self):
		if self.get_object().owner == self.request.user:
			return True
		return False

class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
	model=Entry
	#fields=['title','content']
	success_url='/userdiary/'
	'''def form_valid(self,form):
		form.instance.owner=self.request.user
		return super().form_valid(form)'''
	def test_func(self):
		if self.get_object().owner == self.request.user:
			return True
		return False
