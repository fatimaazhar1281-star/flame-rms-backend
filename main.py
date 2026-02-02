import sys
import time
from core.utils import project_banner, pause, header, loading_spinner
from modules.auth import admin_login, staff_login
from modules.staff import manage_staff
from modules.menu import manage_menu
from modules.inventory import manage_inventory
from modules.tables import manage_tables
from modules.customers import manage_customers
from modules.orders import create_order, add_order_items, view_active_orders
from modules.billing import billing_menu
from modules.feedback import manage_feedback, collect_feedback
from modules.reports import view_reports

# --- DASHBOARDS ---
def admin_dashboard(user):
    while True:
        header(f"ADMIN DASHBOARD - {user['username']}") # Display main admin menu
        print("1. Manage Staff")
        print("2. Manage Menu")
        print("3. Manage Inventory")
        print("4. Manage Tables")
        print("5. Manage Feedback")
        print("6. Reports")
        print("7. Logout")
        print("-" * 80)
        choice = input("Choice: ").strip()
        if choice == '1': manage_staff()
        elif choice == '2': manage_menu()
        elif choice == '3': manage_inventory()
        elif choice == '4': manage_tables()
        elif choice == '5': manage_feedback()
        elif choice == '6': view_reports()
        elif choice == '7': return
        else: print("Invalid Choice."); pause()

def staff_dashboard(user): # Core staff operations
    while True:
        header(f"STAFF DASHBOARD - {user['username']}") # Staff menu view
        print("1. New Order")
        print("2. Add Order Items")
        print("3. View Active Orders")
        print("4. Table Management")
        print("5. Billing & Payment")
        print("6. Customer Management")
        print("7. Collect Feedback")
        print("8. Logout")
        print("-" * 80)
        choice = input("Choice: ").strip()
        if choice == '1': create_order(user)
        elif choice == '2': add_order_items()
        elif choice == '3': view_active_orders()
        elif choice == '4': manage_tables()
        elif choice == '5': billing_menu()
        elif choice == '6': manage_customers()
        elif choice == '7': collect_feedback()
        elif choice == '8': return
        else: print("Invalid Choice."); pause()

def entry_menu(): # Application entry point
    loading_spinner("Initializing Restaurant Management System", 2) # Boot animation
    while True:
        project_banner()
        print("1. Admin Login")
        print("2. Staff Login")
        print("3. Exit")
        print("-" * 80)
        choice = input("Choice: ").strip()
        if choice == '1':
            user = admin_login()
            if user: admin_dashboard(user)
        elif choice == '2':
            user = staff_login()
            if user: staff_dashboard(user)
        elif choice == '3':
            print("\n" + "="*30)
            print("SESSION TERMINATED. THANKS FOR USING OUR SYSTEM")
            print("="*30 + "\n")
            sys.exit()
        else:
            print("Invalid Option.")
            time.sleep(1)

if __name__ == "__main__": # Execution starts here
    import logging
    try:
        entry_menu() # Start the app
    except KeyboardInterrupt:
        print("\n\n" + "!" * 30)
        print("SESSION TERMINATED. THANKS FOR USING OUR SYSTEM")
        print("!" * 30 + "\n")
        sys.exit()

    except Exception as e:
        # Unexpected crash - log it and show a user-friendly message
        logging.critical(f"UNHANDLED SYSTEM CRASH: {e}", exc_info=True)
        print(f"\n" + "!" * 80)
        print("CRITICAL SYSTEM ERROR".center(80))
        print(f"Details: {e}".center(80))
        print("This incident has been logged. Please contact support.".center(80))
        print("!" * 80)
        input("\nPress Enter to Exit...")
        sys.exit(1)

