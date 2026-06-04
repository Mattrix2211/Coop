# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

All commands use the project's virtual environment:

```powershell
# Run development server
C:/Coop1.0/.venv/Scripts/python.exe manage.py runserver 8001 --noreload

# Apply migrations after model changes
C:/Coop1.0/.venv/Scripts/python.exe manage.py migrate

# Create new migrations
C:/Coop1.0/.venv/Scripts/python.exe manage.py makemigrations

# Open Django shell
C:/Coop1.0/.venv/Scripts/python.exe manage.py shell

# Install dependencies
C:/Coop1.0/.venv/Scripts/python.exe -m pip install -r requirements.txt
```

No test suite is configured. Verify changes by running the server and using the UI.

Key URLs after starting the server:
- Dashboard: `http://127.0.0.1:8001/`
- Kiosk (new sale): `http://127.0.0.1:8001/sales/new/`
- Admin: `http://127.0.0.1:8001/admin/`

## Architecture

Single Django project (`coop/`) with one app (`store/`). All business logic, models, views, URLs, and forms live in the `store/` app. Templates are in `templates/store/` with a shared `templates/base.html`. User-uploaded product images go to `media/`.

### Data model

```
Category → Product (stock, image, min_stock threshold)
Customer → Sale → SaleItem (product × qty × unit_price)
                → Payment (CASH/CHEQUE/OTHER)
                → StockMovement (inventory audit log)
CashSession → CashMovement (PAYMENT/ADJUST_IN/ADJUST_OUT/DROP/CHANGE/COUNT)
```

- `Sale` has computed properties: `total`, `amount_paid`, `balance`, `is_credit`
- `CashSession`/`CashMovement` store denomination breakdowns as JSON fields
- `StockMovement` is append-only — stock changes are always logged with a reason and optional sale link

### Views pattern

`store/views.py` contains 30+ views split into functional areas: products, sales (kiosk), customers, debts, cash management, dashboard, and exports.

- AJAX endpoints return `JsonResponse`; HTML endpoints return rendered templates
- Sale confirmation (`sale_confirm`) is AJAX — validates stock and returns receipt modal HTML
- Bulk operations (settle debts, bulk product move) use `@transaction.atomic`
- Excel exports use openpyxl; PDF receipts use ReportLab

### Frontend

Bootstrap with vanilla JavaScript. No build step — static files are served directly from `static/`. The kiosk sale UI (`templates/store/sale_create.html`) is the most complex template: product grid grouped by category with collapsible sections, cart management, and customer selector.

### Localization

The app is in French (locale `fr`, timezone `Europe/Paris`). Model field names, template strings, and admin labels are all in French. Keep new additions consistent with this.
