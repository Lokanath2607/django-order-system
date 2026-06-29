# Django Order Management System

A backend project built with **Django** and **Django REST Framework** to manage products, orders, and inventory.  
This system demonstrates core e‑commerce functionality with clean lifecycle enforcement and stock management.

---

## 🚀 Features
- [Order creation](ca://s?q=Explain_order_creation_flow) → reduces product stock immediately.
- [Quantity adjustment](ca://s?q=Explain_quantity_adjustment_logic) → safely updates stock.
- [Order cancellation](ca://s?q=Explain_stock_rollback_on_cancellation) → restores stock before delivery.
- [Status transitions](ca://s?q=Explain_order_status_transitions) → realistic lifecycle (Pending → Confirmed → Shipped → Delivered/Cancelled).
- [Error handling](ca://s?q=Explain_error_handling_in_orders) → invalid transitions return clear 400 responses.
- Optional [timestamps](ca://s?q=Expose_order_timestamps_in_API) → track when each status change occurs.

---

## 🛠 Tech Stack
- Python 3.x  
- Django  
- Django REST Framework  
- SQLite (default) or PostgreSQL  

---

## ⚙️ Setup Instructions
1. Clone the repository:
   ```powershell
   git clone https://github.com/<your-username>/django-order-system.git
   cd django-order-system
2. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
4. Run migrations:
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
5. Start the server:
   ```powershell
   python manage.py runserver

**📡 API Usage Examples
* Create Order
POST /api/orders/
Content-Type: application/json

{
  "user": 5,
  "product": 2,
  "quantity": 2
}
* Update Quantity
PATCH /api/orders/3/
Content-Type: application/json

{
  "quantity": 3
}
* Cancel Order
PATCH /api/orders/3/
Content-Type: application/json

{
  "status": "CANCELLED"
}

📖 Notes
* Stock reduces on order creation.
* Stock restores on cancellation.
* Invalid transitions (e.g., PENDING → DELIVERED) return a 400 error.
* Optional timestamps track lifecycle events (confirmed_at, shipped_at, etc.).

👤 Author
* Lokanath
* Built in Bengaluru, India
