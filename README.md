# Проект Самобалансуючих Дерев

## Огляд

Цей проект реалізує кілька типів самобалансуючих деревоподібних структур даних і використовує їх як основу для створення SQL-подібної даних. Реалізовані структури дерев:

- AVL-дерево
- Червоно-чорне дерево
- Splay-дерево
- B-дерево
- 2-3-дерево

## Алгоритми та Структури Даних

### 1. AVL-tree

AVL-дерева - це збалансовані за висотою двійкові дерева пошуку, де різниця висот лівого і правого піддерев (фактор балансування) для будь-якого вузла не перевищує 1.

**Ключові характеристики:**
- Самобалансування через обертання
- Операції пошуку, вставки та видалення за час O(log n)
- Фактор балансування = висота(ліве піддерево) - висота(праве піддерево)

**Операції балансування:**
- Ліве обертання
- Праве обертання
- Ліво-праве обертання (подвійне)
- Право-ліве обертання (подвійне)

### 2. Red-black tree

Червоно-чорні дерева - це двійкові дерева пошуку з додатковим бітом для кольору (червоний або чорний), що забезпечує баланс через набір властивостей.

**Ключові властивості:**
- Кожен вузол або червоний, або чорний
- Корінь завжди чорний
- Усі NIL-листки чорні
- Якщо вузол червоний, обидва його нащадки чорні
- Всі шляхи від вузла до його нащадків-листків NIL містять однакову кількість чорних вузлів

**Операції балансування:**
- Перефарбування
- Ліве обертання
- Праве обертання

### 3. Splay-tree

Splay-дерева - це самоналаштовувані двійкові дерева пошуку, які переміщують нещодавно доступні вузли ближче до кореня.

**Ключові характеристики:**
- Відсутність явного фактора балансування або суворих правил балансування
- Нещодавно доступні елементи знову доступні швидко
- Амортизований час операцій O(log n)

**Операції:**
- Splay-операція (переміщення вузла до кореня)
- Кроки Zig, Zig-Zig та Zig-Zag

### 4. B-tree

B-дерева - це збалансовані дерева пошуку, розроблені для ефективної роботи на дисковому сховищі.

**Ключові характеристики:**
- Усі листки знаходяться на одному рівні
- Вузол може мати кілька ключів та дітей
- Ключі всередині вузла відсортовані
- Ефективні для систем, де доступ до даних коштовний (наприклад, дисковий ввід/вивід)

**Операції:**
- Пошук
- Вставка (з розщепленням вузла при необхідності)
- Видалення (з об'єднанням вузлів при необхідності)

### 5. 2-3-tree

2-3-дерева - це збалансовані дерева пошуку, де кожен внутрішній вузол має або 2, або 3 дітей.

**Ключові характеристики:**
- Усі листки знаходяться на одному рівні
- Вузли можуть містити 1 або 2 ключі
- Завжди підтримується ідеальний баланс

**Операції:**
- Пошук
- Вставка (з розщепленням вузла)
- Видалення (з об'єднанням або перерозподілом вузлів)

## Використані принципи дискретної математики

1. **Теорія графів**:
   - Дерева як спеціалізовані графи
   - Алгоритми обходу дерев (inorder, preorder)
   - Властивості шляхів та обчислення глибини

3. **Рекурентні співвідношення**:
   - Аналіз висоти збалансованих дерев
   - Аналіз складності операцій

4. **Властивості балансування**:
   - Фактор балансування AVL
   - Обмеження кольорів червоно-чорного дерева
   - Структурні обмеження B-дерева та 2-3-дерева

5. **Інваріанти**:
   - Підтримка властивостей дерева під час операцій
   - Інваріанти циклів в реалізації алгоритмів


## Структура проекту

- `abstract_class.py`: Визначає абстрактний базовий клас для всіх реалізацій дерев
- `AVL_Tree.py`: Реалізація AVL-дерева
- `red_black_tree.py`: Реалізація червоно-чорного дерева
- `splay_tree.py`: Реалізація Splay-дерева
- `b_tree.py`: Реалізація B-дерева
- `two_three_tree.py`: Реалізація 2-3-дерева
- `tree_adapters.py`: Класи-адаптери для забезпечення уніфікованого інтерфейсу для всіх типів дерев
- `tree_factory.py`: Фабричний клас для створення екземплярів дерев
- `data_manager.py`: Клас для керування базами даних і таблицями
- `tree_sql.py`: SQL-подібний інтерфейс для роботи з системою керування даними

## Інструкції з використання

### Запуск SQL-інтерфейсу

```python
from tree_sql import TreeSQL

sql = TreeSQL()

sql.parse_command("CREATE DATABASE mydb")
sql.parse_command("USE mydb")
sql.parse_command("CREATE TABLE users (id, name, age) USING avl")
sql.parse_command("INSERT INTO users VALUES (1, 'Іван', 25)")
sql.parse_command("SELECT * FROM users")