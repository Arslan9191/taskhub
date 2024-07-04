import os
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QListWidgetItem, QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QTextEdit, QDesktopWidget, QDateTimeEdit
from PyQt5.QtCore import Qt, pyqtSignal, QDateTime
from PyQt5.uic import loadUi
from datetime import datetime
import sqlite3
import qdarkstyle

# Определяем путь к директории, где находится текущий скрипт
current_directory = os.path.dirname(os.path.abspath(__file__))

# Определяем путь к базе данных
db_path = os.path.join(current_directory, "taskhub.db")

def truncate_text(text, max_length=30):
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text

# Окно регистрации
class RegistrationWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        ui_path = os.path.join(current_directory, "registration.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found: {ui_path}")
        loadUi(ui_path, self)
        self.pushButtonRegister.clicked.connect(self.register_user)
        self.pushButtonLogin.clicked.connect(self.login_user)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint)
        self.menu_window = MenuWindow()

    def register_user(self):
        username = self.lineEditUsername.text()
        password = self.lineEditPassword.text()
        if not username or not password:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните поля.")
            return

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = cur.fetchone()

        if existing_user:
            QMessageBox.warning(self, "Ошибка", "Пользователь с таким именем уже существует.")
        else:
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            QMessageBox.information(self, "Успех", "Регистрация прошла успешно!")
        conn.close()

    def login_user(self):
        username = self.lineEditUsername.text()
        password = self.lineEditPassword.text()
        if not username or not password:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните поля.")
            return

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        existing_user = cur.fetchone()

        if existing_user:
            self.hide()
            self.menu_window.set_user_id(existing_user[0])
            self.menu_window.show()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверное имя пользователя или пароль.")
        conn.close()

# Окно меню
class MenuWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        ui_path = os.path.join(current_directory, "menu.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found: {ui_path}")
        loadUi(ui_path, self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint)
        self.user_id = None
        self.viewCreateTaskButton.clicked.connect(self.open_create_task_window)
        self.viewMyTaskButton.clicked.connect(self.open_view_my_task_window)
        self.viewTaskButton.clicked.connect(self.open_view_public_task_window)
        self.goToMySentResponcesButton.clicked.connect(self.open_my_sent_responses_window)
        self.create_task_window = CreateTaskWindow(self)
        self.view_my_task_window = ViewMyTaskWindow(self, self.create_task_window)
        self.view_public_task_window = ViewPublicTaskWindow(self)

        self.create_task_window.task_saved.connect(self.view_my_task_window.load_tasks)

    def set_user_id(self, user_id):
        self.user_id = user_id
        self.create_task_window.set_user_id(user_id)
        self.view_my_task_window.set_user_id(user_id)
        self.view_public_task_window.set_user_id(user_id)

    def open_create_task_window(self):
        self.hide()
        self.create_task_window.clear_fields()
        self.create_task_window.show()

    def open_view_my_task_window(self):
        self.hide()
        self.view_my_task_window.load_tasks()
        self.view_my_task_window.show()

    def open_view_public_task_window(self):
        self.hide()
        self.view_public_task_window.load_tasks()
        self.view_public_task_window.show()

    def open_my_sent_responses_window(self):
        self.hide()
        self.my_sent_responses_window = MySentResponsesWindow(self.user_id, self)
        self.my_sent_responses_window.show()

# Окно создания задачи
class CreateTaskWindow(QDialog):
    task_saved = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        ui_path = os.path.join(current_directory, "createTask.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found: {ui_path}")
        loadUi(ui_path, self)
        self.exitCreateTaskButton.clicked.connect(self.close_create_task_window)
        self.createTaskButton.clicked.connect(self.save_task)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint)
        self.user_id = None
        self.task_id = None
        self.parent_window = parent

    def set_user_id(self, user_id):
        self.user_id = user_id

    def load_task(self, task_id, title, description):
        self.task_id = task_id
        self.titleTaskEdit.setText(title)
        self.descriptionTaskEdit.setText(description)

    def clear_fields(self):
        self.task_id = None
        self.titleTaskEdit.clear()
        self.descriptionTaskEdit.clear()

    def close_create_task_window(self):
        self.hide()
        self.parent_window.show()

    def save_task(self):
        title = self.titleTaskEdit.toPlainText()
        description = self.descriptionTaskEdit.toPlainText()
        deadline = self.deadlineEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss")  # Assuming you have a QDateTimeEdit widget for deadline

        if not title or not description or not deadline:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля.")
            return

        creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Получаем текущее время

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        if self.task_id:
            cur.execute("UPDATE tasks SET title = ?, description = ?, deadline = ? WHERE id = ?",
                        (title, description, deadline, self.task_id))
        else:
            cur.execute("INSERT INTO tasks (user_id, title, description, deadline, status, creation_time) VALUES (?, ?, ?, ?, ?, ?)",
                        (self.user_id, title, description, deadline, "Публичный", creation_time))

        conn.commit()
        conn.close()

        QMessageBox.information(self, "Успех", "Задача успешно сохранена!")
        self.task_saved.emit()
        self.clear_fields()
        self.hide()
        self.parent_window.show()
        
        if hasattr(self.parent_window, 'view_public_task_window'):
            self.parent_window.view_public_task_window.load_tasks()

# Окно просмотра своих созданных задач
class ViewMyTaskWindow(QDialog):
    def __init__(self, parent=None, create_task_window=None):
        super().__init__(parent)
        ui_path = os.path.join(current_directory, "viewMyTask.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found: {ui_path}")
        loadUi(ui_path, self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint)
        self.user_id = None
        self.parent_window = parent
        self.create_task_window = create_task_window
        self.backToMenuButton.clicked.connect(self.back_to_menu)

    def set_user_id(self, user_id):
        self.user_id = user_id
        self.load_tasks()

    def load_tasks(self):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT id, title, description, deadline, status, creation_time, completion_time FROM tasks WHERE user_id=?", (self.user_id,))
        tasks = cur.fetchall()
        conn.close()

        self.taskListWidget.clear()

        for task in tasks:
            item_widget = TaskItemWidget(task, self)
            item = QListWidgetItem()
            item.setSizeHint(item_widget.sizeHint())
            self.taskListWidget.addItem(item)
            self.taskListWidget.setItemWidget(item, item_widget)

    def back_to_menu(self):
        self.hide()
        self.parent_window.show()

# Виджет управления созданными нами задачами
class TaskItemWidget(QWidget):
    def __init__(self, task, parent_window):
        super().__init__()
        self.task_id, title, description, deadline, status, creation_time, completion_time = task
        self.full_title = title
        self.full_description = description
        self.deadline = deadline
        self.creation_time = creation_time
        self.completion_time = completion_time
        self.parent_window = parent_window

        layout = QHBoxLayout()
        self.setLayout(layout)

        self.titleLabel = QLabel(truncate_text(title))
        self.descriptionLabel = QLabel(truncate_text(description))
        self.deadlineLabel = QLabel(deadline)
        self.creationTimeLabel = QLabel(creation_time)
        self.statusLabel = QLabel(status)
        self.completionTimeLabel = QLabel(completion_time if completion_time else "Не завершено")
        self.editButton = QPushButton("Редактировать")
        self.deleteButton = QPushButton("Удалить")
        self.detailsButton = QPushButton("Подробнее")
        self.viewResponsesButton = QPushButton("Отклики")

        layout.addWidget(self.titleLabel)
        layout.addWidget(self.descriptionLabel)
        layout.addWidget(self.deadlineLabel)
        layout.addWidget(self.creationTimeLabel)
        layout.addWidget(self.statusLabel)
        layout.addWidget(self.completionTimeLabel)
        layout.addWidget(self.editButton)
        layout.addWidget(self.deleteButton)
        layout.addWidget(self.detailsButton)
        layout.addWidget(self.viewResponsesButton)

        self.editButton.clicked.connect(self.edit_task)
        self.deleteButton.clicked.connect(self.delete_task)
        self.detailsButton.clicked.connect(self.show_details)
        self.viewResponsesButton.clicked.connect(self.view_responses)
        
    def edit_task(self):
        self.parent_window.create_task_window.load_task(self.task_id, self.full_title, self.full_description)
        self.parent_window.create_task_window.show()
        self.parent_window.hide()

    def delete_task(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle('Подтвердите удаление')
        msg_box.setText('Вы уверены, что хотите удалить эту задачу?')

        yes_button = msg_box.addButton('Да', QMessageBox.YesRole)
        no_button = msg_box.addButton('Нет', QMessageBox.NoRole)

        msg_box.exec_()

        if msg_box.clickedButton() == yes_button:
            conn = sqlite3.connect(db_path)
            cur = conn.cursor()
            cur.execute("DELETE FROM responses WHERE task_id = ?", (self.task_id,))
            cur.execute("DELETE FROM tasks WHERE id = ?", (self.task_id,))
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Успех", "Задача и связанные с ней отклики успешно удалены!")
            self.parent_window.load_tasks()

    def show_details(self):
        self.details_window = TaskDetailsWindow(self.full_title, self.full_description, self.deadline, self.creation_time, self.parent_window)  # Передаем дедлайн
        self.details_window.show()

    def view_responses(self):
        self.responses_window = MyResponsesWindow(self.task_id, self)
        self.responses_window.show()

# Окно просмотра публичных задач
class ViewPublicTaskWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        ui_path = os.path.join(current_directory, "viewPublicTask.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found: {ui_path}")
        loadUi(ui_path, self)
        self.user_id = None
        self.parent_window = parent  # Сохраняем ссылку на родительское окно
        self.backToMenuButton.clicked.connect(self.go_back_to_menu)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint)

    def set_user_id(self, user_id):
        self.user_id = user_id

    def load_public_tasks(self):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT tasks.id, users.username, tasks.title, tasks.description, tasks.deadline, tasks.status, tasks.creation_time FROM tasks JOIN users ON tasks.user_id = users.id WHERE tasks.status = 'Публичный'")
        tasks = cur.fetchall()
        conn.close()

        self.taskListWidget.clear()

        for task in tasks:
            item_widget = PublicTaskItemWidget(task, self)
            item = QListWidgetItem()
            item.setSizeHint(item_widget.sizeHint())
            self.taskListWidget.addItem(item)
            self.taskListWidget.setItemWidget(item, item_widget)

    def load_tasks(self):
        self.load_public_tasks()

    def go_back_to_menu(self):
        self.hide()  # Скрываем текущее окно
        self.parent_window.show()  # Показываем родительское окно

# Виджет публичных задач созданными другими пользователями
class PublicTaskItemWidget(QWidget):
    def __init__(self, task, parent_window):
        super().__init__()
        self.task_id, username, title, description, deadline, status, creation_time = task
        self.full_title = title
        self.full_description = description
        self.deadline = deadline
        self.creation_time = creation_time
        self.parent_window = parent_window

        layout = QHBoxLayout()
        self.setLayout(layout)

        self.usernameLabel = QLabel(username)
        self.titleLabel = QLabel(truncate_text(title))
        self.descriptionLabel = QLabel(truncate_text(description))
        self.deadlineLabel = QLabel(deadline)
        self.creationTimeLabel = QLabel(creation_time)  # Новое поле для даты создания
        self.statusLabel = QLabel(status)
        self.detailsButton = QPushButton("Подробнее")
        self.respondButton = QPushButton("Откликнуться")

        layout.addWidget(self.usernameLabel)
        layout.addWidget(self.titleLabel)
        layout.addWidget(self.descriptionLabel)
        layout.addWidget(self.deadlineLabel)
        layout.addWidget(self.creationTimeLabel)  # Добавляем виджет в макет
        layout.addWidget(self.statusLabel)
        layout.addWidget(self.detailsButton)
        layout.addWidget(self.respondButton)

        self.detailsButton.clicked.connect(self.show_details)
        self.respondButton.clicked.connect(self.open_response_window)
        
    def show_details(self):
        self.details_window = TaskDetailsWindow(self.full_title, self.full_description, self.deadline, self.creation_time)  # Передаем дедлайн
        self.details_window.show()

    def open_response_window(self):
        self.response_window = ResponseWindow(self.task_id, self.parent_window.user_id, self)
        self.response_window.show()

# Окно отклика на задачу
class ResponseWindow(QDialog):
    def __init__(self, task_id, user_id, parent=None):
        super().__init__(parent)
        ui_path = os.path.join(current_directory, "responseWindow.ui")
        loadUi(ui_path, self)
        self.task_id = task_id
        self.user_id = user_id
        self.sendResponseButton.clicked.connect(self.send_response)
        self.cancelButton.clicked.connect(self.close)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint)

    def is_task_owner(self):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT user_id FROM tasks WHERE id = ?", (self.task_id,))
        task_owner_id = cur.fetchone()
        conn.close()
        return task_owner_id[0] == self.user_id

    def has_already_responded(self):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM responses WHERE task_id = ? AND user_id = ?", (self.task_id, self.user_id))
        response_count = cur.fetchone()[0]
        conn.close()
        return response_count > 0

    def send_response(self):
        response_text = self.responseTextEdit.toPlainText()
        if not response_text:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите текст отклика.")
            return

        if not self.user_id:
            QMessageBox.warning(self, "Ошибка", "Не удалось определить пользователя.")
            return

        if self.is_task_owner():
            QMessageBox.warning(self, "Ошибка", "Вы не можете откликнуться на собственную задачу.")
            return

        if self.has_already_responded():
            QMessageBox.warning(self, "Ошибка", "Вы уже отправили отклик на эту задачу!")
            return

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("INSERT INTO responses (task_id, user_id, response_text, status) VALUES (?, ?, ?, ?)",
        (self.task_id, self.user_id, response_text, "Открыта"))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Успех", "Ваш отклик успешно отправлен!")
        self.close()

# Окно откликов к созданным нами задачам
class MyResponsesWindow(QDialog):
    def __init__(self, task_id, parent=None):
        super().__init__(parent)
        ui_path = os.path.join(current_directory, "myResponses.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found: {ui_path}")
        loadUi(ui_path, self)
        self.task_id = task_id
        self.user_id = None
        self.parent_window = parent
        self.load_responses()
        self.assignTaskButton.clicked.connect(self.assign_selected_task)
        self.acceptWorkButton.clicked.connect(self.accept_work)
        self.rejectWorkButton.clicked.connect(self.reject_work)
        self.reportsButton.clicked.connect(self.view_report)
        self.backButton.clicked.connect(self.back_to_menu)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint)

    def load_responses(self):
        try:
            conn = sqlite3.connect(db_path)
            cur = conn.cursor()
            cur.execute("""
            SELECT users.id, users.username, responses.response_text, responses.status, responses.id, responses.acceptance_time, responses.submission_time
            FROM responses
            JOIN users ON responses.user_id = users.id
            WHERE responses.task_id = ?
            """, (self.task_id,))
            responses = cur.fetchall()
            conn.close()

            self.responseListWidget.clear()

            for response in responses:
                user_id, username, response_text, status, response_id, acceptance_time, submission_time = response
                if acceptance_time is None:
                    acceptance_time = "Не назначено"
                if submission_time is None:
                    submission_time = "Не сдано"
                item = QListWidgetItem(f"{username}: {response_text} ({status}) - {acceptance_time} - {submission_time}")
                item.response_id = response_id
                item.user_id = user_id
                self.responseListWidget.addItem(item)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить отклики: {e}")
            print(f"Ошибка загрузки откликов: {e}")
            
    def assign_selected_task(self):
        if self.is_task_completed():
            QMessageBox.warning(self, "Ошибка", "Вы не можете отдать задачу в работу, так как она уже завершена.")
            return

        selected_items = self.responseListWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите отклик для назначения.")
            return

        selected_item = selected_items[0]
        response_id = selected_item.response_id
        self.assign_task(response_id)

    def assign_task(self, response_id):
        try:
            acceptance_time = QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss')

            conn = sqlite3.connect(db_path)
            cur = conn.cursor()

            cur.execute("""
            UPDATE responses
            SET status = 'В исполнении', acceptance_time = ?
            WHERE id = ?
            """, (acceptance_time, response_id))

            cur.execute("""
            UPDATE tasks
            SET status = 'В исполнении'
            WHERE id = ?
            """, (self.task_id,))

            conn.commit()
            conn.close()

            self.load_responses()
            QMessageBox.information(self, "Успех", "Задача передана в работу.")
            
            if hasattr(self.parent_window, 'load_tasks'):
                self.parent_window.load_tasks()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось назначить задачу: {e}")
            print(f"Ошибка назначения задачи: {e}")

    def accept_work(self):
        if self.is_task_completed():
            QMessageBox.warning(self, "Ошибка", "Эта задача уже завершена. Вы не можете принять работу.")
            return

        selected_items = self.responseListWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите отклик.")
            return

        selected_item = selected_items[0]
        response_id = selected_item.response_id

        try:
            completion_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            conn = sqlite3.connect(db_path)
            cur = conn.cursor()

            cur.execute("""
            UPDATE responses
            SET status = 'Завершено'
            WHERE id = ?
            """, (response_id,))

            cur.execute("""
            UPDATE tasks
            SET status = 'Завершено', completion_time = ?
            WHERE id = ?
            """, (completion_time, self.task_id))

            conn.commit()
            conn.close()

            self.load_responses()
            QMessageBox.information(self, "Успех", "Работа принята и статус задачи изменен на 'Завершено'.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось принять работу: {e}")
            print(f"Ошибка принятия работы: {e}")

    def reject_work(self):
        if self.is_task_completed():
            QMessageBox.warning(self, "Ошибка", "Эта задача уже завершена. Вы не можете отклонить работу.")
            return

        selected_items = self.responseListWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите отклик.")
            return

        selected_item = selected_items[0]
        response_id = selected_item.response_id

        try:
            conn = sqlite3.connect(db_path)
            cur = conn.cursor()

            cur.execute("""
            UPDATE responses
            SET status = 'В исполнении'
            WHERE id = ?
            """, (response_id,))

            conn.commit()
            conn.close()

            self.load_responses()
            QMessageBox.information(self, "Успех", "Работа отклонена.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось отклонить работу: {e}")
            print(f"Ошибка отклонения работы: {e}")
            
    def is_task_completed(self):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT status FROM tasks WHERE id = ?", (self.task_id,))
        status = cur.fetchone()[0]
        conn.close()
        return status == 'Завершено'
        
    def view_report(self):
        selected_items = self.responseListWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите отклик.")
            return

        selected_item = selected_items[0]
        response_id = selected_item.response_id

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("""
        SELECT report_text
        FROM responses
        WHERE id = ?
        """, (response_id,))
        report = cur.fetchone()
        conn.close()

        if report and report[0]:
            self.report_view_window = ReportViewWindow(report[0], self)
            self.report_view_window.show()
        else:
            QMessageBox.information(self, "Информация", "Отчёт ещё не добавлен.")

    def back_to_menu(self):
        self.close()
        self.parent_window.show()

# Окно просмотра отчётов к задачам
class ReportViewWindow(QDialog):
    def __init__(self, report_text, parent=None):
        super().__init__(parent)
        ui_path = os.path.join(current_directory, "reportView.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found: {ui_path}")
        loadUi(ui_path, self)
        self.reportTextEdit.setPlainText(report_text)
        self.closeButton.clicked.connect(self.close)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint)

class ReportWindow(QDialog):
    def __init__(self, response_id, parent=None):
        super().__init__(parent)
        ui_path = os.path.join(current_directory, "report.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found: {ui_path}")
        loadUi(ui_path, self)
        self.response_id = response_id
        self.sendButton.clicked.connect(self.send_report)
        self.cancelButton.clicked.connect(self.close)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint)

    def send_report(self):
        report_text = self.reportTextEdit.toPlainText()
        if not report_text:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, напишите отчет.")
            return

        submission_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("""
        UPDATE responses
        SET report_text = ?, status = 'Завершено', submission_time = ?
        WHERE id = ?
        """, (report_text, submission_time, self.response_id))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Успех", "Отчёт отправлен и статус отклика изменен на 'Завершено'.")
        self.close()
        self.parent().load_responses()

# Окно подробного просмотра задач
class TaskDetailsWindow(QDialog):
    def __init__(self, title, description, deadline, creation_time, parent=None):
        super().__init__(parent)
        ui_path = os.path.join(current_directory, "taskDetails.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found: {ui_path}")
        loadUi(ui_path, self)
        self.titleLabel.setText(title)
        self.descriptionLabel.setText(description)
        self.deadlineLabel.setText(deadline)  # Устанавливаем текст дедлайна
        self.startDateLabel.setText(creation_time)
        self.closeButton.clicked.connect(self.close_window)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint)

    def close_window(self):
        self.hide()
        if self.parent():  # Check if parent exists
            self.parent().show()

# Окно отправленных нами откликов
class MySentResponsesWindow(QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__(parent)
        ui_path = os.path.join(current_directory, "mySentResponses.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found: {ui_path}")
        loadUi(ui_path, self)
        self.user_id = user_id
        self.parent_window = parent
        self.load_responses()
        self.detailsButton.clicked.connect(self.show_response_details)
        self.submitButton.clicked.connect(self.open_report_window)
        self.backButton.clicked.connect(self.back_to_menu)
        self.responseListWidget.itemSelectionChanged.connect(self.update_submit_button_state)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint)

    def load_responses(self):
        try:
            conn = sqlite3.connect(db_path)
            cur = conn.cursor()
            cur.execute("""
            SELECT tasks.title, tasks.description, tasks.deadline, responses.response_text, responses.status, responses.acceptance_time, responses.submission_time, responses.id, tasks.status, tasks.completion_time
            FROM responses
            JOIN tasks ON responses.task_id = tasks.id
            WHERE responses.user_id = ?
            """, (self.user_id,))
            responses = cur.fetchall()
            conn.close()

            self.responseListWidget.clear()

            for response in responses:
                title, description, deadline, response_text, status, acceptance_time, submission_time, response_id, task_status, completion_time = response
                if acceptance_time is None:
                    acceptance_time = "Not assigned"
                if submission_time is None:
                    submission_time = "Не сдано"
                if completion_time is None:
                    completion_time = "Не завершено"
                item_text = f"Задача: {title}\nОписание: {description}\nСрок: {deadline}\nОтклик: {response_text}\nСтатус: {status}\nПринят: {acceptance_time}\nСдано: {submission_time}\nЗавершено: {completion_time}"
                item = QListWidgetItem(item_text)
                item.setData(Qt.UserRole, (response_id, title, description, deadline, response_text, status, acceptance_time, submission_time, task_status, completion_time))  # Добавляем все необходимые данные в элемент списка
                self.responseListWidget.addItem(item)

            self.update_submit_button_state()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить отклики: {e}")
            print(f"Ошибка загрузки откликов: {e}")


    def update_submit_button_state(self):
        selected_items = self.responseListWidget.selectedItems()
        if not selected_items:
            self.submitButton.setEnabled(False)
            return

        selected_item = selected_items[0]
        data = selected_item.data(Qt.UserRole)
        if data is not None:
            response_id, title, description, deadline, response_text, status, acceptance_time, submission_time, task_status, completion_time = data

        if task_status == 'Завершено':
            self.submitButton.setEnabled(False)
        else:
            self.submitButton.setEnabled(True)


    def show_response_details(self):
        selected_items = self.responseListWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите отклик.")
            return

        selected_item = selected_items[0]
        data = selected_item.data(Qt.UserRole)
        if data is not None:
            response_id, title, description, deadline, response_text, status, acceptance_time, submission_time, task_status, completion_time = data

        self.details_window = ResponseDetailsWindow(title, description, deadline, self)
        self.details_window.show()


    def submit_work(self):
        selected_items = self.responseListWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите отклик.")
            return

        selected_item = selected_items[0]
        data = selected_item.data(Qt.UserRole)

        if data is None:
            QMessageBox.critical(self, "Error", "Не удалось получить данные отклика.")
            return

        title, description, deadline, response_text, status, acceptance_time = data

        if status == "Not assigned":
            QMessageBox.warning(self, "Ошибка", "Отклик не обработан.")
            return

        # Подключаемся к базе данных и обновляем статус
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("""
        UPDATE responses
        SET status = 'На рассмотрении'
        WHERE task_id = (SELECT id FROM tasks WHERE title = ? AND description = ? AND deadline = ?)
        AND response_text = ? AND user_id = ?
        """, (title, description, deadline, response_text, self.user_id))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Успех", "Статус отклика изменен на 'На рассмотрении'.")
        self.load_responses()

    def get_task_id(self, title, description, deadline):
        try:
            conn = sqlite3.connect(db_path)
            cur = conn.cursor()
            cur.execute("""
            SELECT id FROM tasks WHERE title = ? AND description = ? AND deadline = ?
            """, (title, description, deadline))
            task = cur.fetchone()
            conn.close()
            if task:
                return task[0]
            else:
                return None
        except Exception as e:
            print(f"Ошибка получения ID задачи: {e}")
            return None

    def open_report_window(self):
        selected_items = self.responseListWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите отклик.")
            return

        selected_item = selected_items[0]
        data = selected_item.data(Qt.UserRole)
        if data is not None:
            response_id, title, description, deadline, response_text, status, acceptance_time, submission_time, task_status, completion_time = data

        if task_status == 'Завершено':
            QMessageBox.warning(self, "Ошибка", "Эта задача уже завершена. Вы не можете сдать работу.")
            return

        self.report_window = ReportWindow(response_id, self)
        self.report_window.show()

        
    def is_task_completed(self, response_id):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("""
        SELECT tasks.status
        FROM responses
        JOIN tasks ON responses.task_id = tasks.id
        WHERE responses.id = ?
        """, (response_id,))
        status = cur.fetchone()[0]
        conn.close()
        return status == 'Завершено'

    def back_to_menu(self):
        self.close()
        self.parent_window.show()

    def view_report(self):
        selected_items = self.responseListWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите отклик.")
            return

        selected_item = selected_items[0]
        response_id = selected_item.response_id

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("""
        SELECT report_text
        FROM responses
        WHERE id = ?
        """, (response_id,))
        report = cur.fetchone()
        conn.close()

        if report and report[0]:
            self.report_view_window = ReportViewWindow(report[0], self)
            self.report_view_window.show()
        else:
            QMessageBox.information(self, "Информация", "Отчёт ещё не добавлен.")
    
    def back_to_menu(self):
        self.close()  # Закрываем текущее окно
        self.parent_window.show()  # Показываем родительское окно (главное меню)

# Окно просмотра деталей откликов
class ResponseDetailsWindow(QDialog):
    def __init__(self, title, description, deadline, parent=None):
        super().__init__(parent)
        ui_path = os.path.join(current_directory, "responseDetails.ui")
        if not os.path.exists(ui_path):
            raise FileNotFoundError(f"UI file not found: {ui_path}")
        loadUi(ui_path, self)
        self.task_details = f"Заголовок: {title}\nОписание: {description}"
        self.response_details = f"Дедлайн: {deadline}"
        self.deadline = deadline

        self.taskDetailsButton.clicked.connect(self.show_task_details)
        self.responseDetailsButton.clicked.connect(self.show_response_details)
        self.closeButton.clicked.connect(self.close)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint)

        self.show_task_details()

    def show_task_details(self):
        self.detailsTextEdit.setPlainText(self.task_details)
        self.deadlineLabel.setText(f"Дедлайн: {self.deadline}")  # Отображаем дедлайн как строку

    def show_response_details(self):
        self.detailsTextEdit.setPlainText(self.response_details)


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    registration_window = RegistrationWindow()
    registration_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
