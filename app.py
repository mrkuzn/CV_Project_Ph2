import streamlit as st
import os
import sys

# Добавляем корень проекта и папку pages в пути поиска Python,
# чтобы сервер гарантированно видел модули при любом деплое
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, "pages"))

st.set_page_config(
    page_title="CV Project • DetecronTeam",
    page_icon="🚀",
    layout="wide"
)

# --- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ-ЗАГЛУШКИ ---
def _missing_face_page():
    st.error("❌ Модуль `face.py` не найден или не содержит функцию `render_face_detection_page`.\n"
             "Убедитесь, что файл `face.py` лежит в папке `pages/` и в нём определена указанная функция.")

def _missing_wind_page():
    st.error("❌ Модуль `wind.py` не найден или не содержит функцию `render_wind_detection_page`.\n"
             "Убедитесь, что файл `wind.py` лежит в папке `pages/` и в нём определена указанная функция.")

# --- БЕЗОПАСНЫЙ ИМПОРТ МОДУЛЕЙ КОМАНДЫ ---
# Импорт страницы детекции лиц
try:
    from face import render_face_detection_page
except ImportError:
    try:
        from pages.face import render_face_detection_page
    except ImportError:
        render_face_detection_page = _missing_face_page

# Импорт страницы детекции ветрогенераторов
try:
    from wind import render_wind_detection_page
except ImportError:
    try:
        from pages.wind import render_wind_detection_page
    except ImportError:
        render_wind_detection_page = _missing_wind_page

# --- БОКОВАЯ ПАНЕЛЬ НАВИГАЦИИ ---
with st.sidebar:
    st.title("🧩 Навигация")
    page = st.radio(
        "Выберите интересующий модуль:",
        [
            "🏠 Главная страница",
            "🎭 Детекция и маскирование лиц",
            "💨 Детекция ветрогенераторов",
            "✳️ Семантическая сегментация аэрокосмических снимков"
        ]
    )
    st.markdown("---")
    st.markdown("### 👥 Наша команда:")
    st.caption("Разработчик Роман: Детекция и маскирование лиц")
    st.caption("Разработчик Дорджи: Детекция ветрогенераторов")
    st.caption("Совместно: Семантическая сегментация аэрокосмических снимков")

# --- РЕНДЕРИНГ ВЫБРАННОЙ СТРАНИЦЫ ---
if page == "🏠 Главная страница":
    st.title("🚀 Командный проект по Компьютерному Зрению (CV)")
    st.subheader("Веб-сервис искусственного интеллекта DetecronTeam")

    if os.path.exists("images/logo.jpg"):
        st.image("images/logo.jpg", width=300, caption="DetecronTeam Logo")

    st.markdown("""
    ### 👋 Добро пожаловать!
    Данное multipage-приложение представляет собой комплексный аналитический инструмент, объединяющий современные архитектуры глубокого обучения для решения различных прикладных задач Computer Vision.
    
    #### 🛠️ Доступные модули и технологии:
    1. **Детекция и маскирование лиц:** Автоматическое обнаружение лиц на базе обученной модели **YOLOv11n** с последующим конфиденциальным размытием Гаусса (OpenCV). Поддерживает множественную загрузку файлов и инференс по URL-ссылке.
    2. **Детекция ветрогенераторов:** Поиск промышленных объектов на аэрофотоснимках с использованием архитектуры **YOLOv11n**, с поддержкой подгрузки изображений по прямым интернет-ссылкам.
    3. **Семантическая сегментация космоснимков:** (Бонусный модуль) Попиксельная классификация аэрокосмических снимков земной поверхности с использованием кастомной архитектуры **U-Net** на базе бэкбона ResNet.
    
    *Используйте боковое меню слева, чтобы переключиться на нужный модуль приложения.*
    """)

elif page == "🎭 Детекция и маскирование лиц":
    render_face_detection_page()

elif page == "💨 Детекция ветрогенераторов":
    render_wind_detection_page()

elif page == "✳️ Семантическая сегментация аэрокосмических снимков":
    st.header("✳️ Семантическая сегментация аэрокосмических снимков")
    st.write("Раздел интеграции модели U-Net.")
    st.info("Модуль находится на этапе финальной интеграции.")
