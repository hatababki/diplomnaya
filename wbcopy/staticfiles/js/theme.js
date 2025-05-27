// Функция для переключения темы
function toggleTheme() {
    const body = document.body;
    const currentTheme = body.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    // Обновляем иконку
    const themeIcon = document.getElementById('theme-icon');
    themeIcon.innerHTML = newTheme === 'dark' ? '☀️' : '🌙';
}

// Функция для инициализации темы при загрузке страницы
function initTheme() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.body.setAttribute('data-theme', savedTheme);
    
    // Устанавливаем начальную иконку
    const themeIcon = document.getElementById('theme-icon');
    if (themeIcon) {
        themeIcon.innerHTML = savedTheme === 'dark' ? '☀️' : '🌙';
    }
}

// Инициализируем тему при загрузке страницы
document.addEventListener('DOMContentLoaded', initTheme); 