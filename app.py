from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)  # Включаем CORS для всех маршрутов

# База данных расходов (в памяти)
expenses = []
expense_id_counter = 1

# Категории расходов
categories = {
    "Продукты": "🛒",
    "Транспорт": "🚗",
    "Развлечения": "🎬",
    "Здоровье": "💊",
    "Образование": "📚",
    "Коммунальные услуги": "💡",
    "Одежда": "👕",
    "Прочее": "📌"
}


@app.route('/')
def index():
    return render_template('index.html', categories=categories)


@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    response = make_response(jsonify({"expenses": expenses, "total": len(expenses)}))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response, 200


@app.route('/api/expenses', methods=['POST'])
def add_expense():
    global expense_id_counter

    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Нет данных"}), 400

        if 'amount' not in data or 'category' not in data:
            return jsonify({"error": "Необходимо указать сумму и категорию"}), 400

        expense = {
            "id": expense_id_counter,
            "amount": float(data['amount']),
            "category": data['category'],
            "description": data.get('description', ''),
            "date": data.get('date', datetime.now().strftime('%Y-%m-%d')),
            "created_at": datetime.now().isoformat()
        }

        expenses.append(expense)
        expense_id_counter += 1

        response = make_response(jsonify(expense))
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response, 201

    except Exception as e:
        print(f"Ошибка при добавлении расхода: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    global expenses
    expense = next((e for e in expenses if e['id'] == expense_id), None)

    if not expense:
        response = make_response(jsonify({"error": "Расход не найден"}))
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response, 404

    expenses = [e for e in expenses if e['id'] != expense_id]

    response = make_response(jsonify({"message": "Расход удален", "id": expense_id}))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response, 200


@app.route('/api/categories', methods=['GET'])
def get_categories():
    response = make_response(jsonify({"categories": categories}))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response, 200


@app.route('/api/stats', methods=['GET'])
def get_stats():
    total = sum(e['amount'] for e in expenses)

    # Статистика по категориям
    category_stats = {}
    for expense in expenses:
        cat = expense['category']
        if cat not in category_stats:
            category_stats[cat] = {"total": 0, "count": 0, "icon": categories.get(cat, "📌")}
        category_stats[cat]['total'] += expense['amount']
        category_stats[cat]['count'] += 1

    # Статистика по датам
    today = datetime.now().strftime('%Y-%m-%d')
    today_expenses = sum(e['amount'] for e in expenses if e['date'] == today)

    stats = {
        "total": total,
        "today": today_expenses,
        "count": len(expenses),
        "by_category": category_stats
    }

    response = make_response(jsonify(stats))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
