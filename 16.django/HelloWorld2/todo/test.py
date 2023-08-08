from django.test import TestCase
from todo.models import Todo
from django.urls import reverse
# Create your tests here.
class TodoModelTests(TestCase): #Test할 모델 뒤에 Test를 붙이는게 일반적임 ex) PostModelsTests
    def test_str_representaion(self):
        todo = Todo.objects.create(title = 'Todo Todo',content = 'Test')
        self.assertEqual(str(todo), 'Todo Todo')
        # assert~() # 내가 원하는 테스트케이스가 정상적으로 작동되는지 확인하는 구문임
    
    def test_str_representation2(self):
        todo = Todo.objects.create(title = 'Todoadas',content = 'Test')
        self.assertEqual(str(todo), 'Todoadas')

class TodoViewTests(TestCase):
    def test_todo_list_view(self): # 전체 뷰 조회 디버깅
        response = self.client.get(reverse('todo_list'))
        # print(response)
        # print(response.status_code) # 상태코드
        # print(response.content) # 컨텐츠 내용 가져오기
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/list.html')

    def test_todo_detail_view(self): # 디테일 뷰 조회 디버깅
        todo = Todo.objects.create(title ='Test1', content='test1 content')
        response = self.client.get(reverse('todo_detail', args=[todo.pk])) # 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/detail.html')
        self.assertContains(response, 'Test1')
        self.assertContains(response, 'test1 content')

    def test_todo_create_view(self): # 생성시 디버깅
        response = self.client.get(reverse('todo_write'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/write.html')

        data = {
            'title' : 'Test2',
            'content' : 'Test2 content'
        }
        
        response = self.client.post(reverse('task_create'), data)
        self.assertEqual(response.status_code, 302) # 우리가 리다이렉트를 했기때문에 기대값은 302임

    def test_todo_update_view(self):
        todo = Todo.objects.create(title='Test3', content='Test3 content')
        response = self.client.get(reverse('update_todo', args=[todo.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edithtml')
        # 컨텐츠 확인
        self.assertEqual(todo.title, 'Test3')
        self.assertEqual(todo.content, 'Test3 content')

        # 업데이트 수행
        update_data = {
            'title':'Change Test3',
            'content':'Change Test3 content'
        }

        response = self.client.post(reverse('update_todo', args=[todo.pk]), update_data)
        
        # 전달된 데이터가 잘 반영되었는지 확인
        self.assertEqual(response.status_code, 302)

        # DB로부터 task내용 재갱신
        todo.refresh_from_db()
        self.assertEqual(todo.title, 'Change Test3')
        self.assertEqual(todo.content, 'Change Test3 content')

    def test_todo_delete_view(self):
        todo = Todo.objects.create(title='Test4', content='Test4')
        self.assertEqual(Todo.objects.count(), 1) # 생성된 갯수 확인

        # 지우는 코드
        response = self.client.get(reverse('del_todo', args=[todo.pk]))
        self.assertEqual(Todo.objects.count(), 0) # 삭제된 갯수 확인
        self.assertEqual(response.status_code, 302)