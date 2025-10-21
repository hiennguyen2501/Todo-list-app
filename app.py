# Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")
# --- Điểm bắt đầu của chương trình ---
def list_task():
    for i in range(len(tasks)):
        if tasks[i]['completed']== True:
            print(f"[x] {tasks[i]['name']}")
        else:
            print(f"[ ] {tasks[i]['name']}")
def complete_task(task_index):
    tasks[task_index]['completed']= True
    
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task({'name': 'Học bài Git và GitHub', 'completed': False})
    add_task({'name': 'Làm bài tập thực hành ở nhà', 'completed': True})
    list_task()
    
