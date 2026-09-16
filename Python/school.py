import psycopg2

try:
    conn = psycopg2.connect(
        host = "localhost",
        dbname = "schdetail",
        user = "postgres",
        password = "1234"
        )
    cursor = conn.cursor()
    insert_query = """insert into schdetail(student_id,student_name,student_percentage)
    values(%s,%s,%s);
    """
    print("--- Dynamic Student Data Entry ---")
    while True:
        try:
            student_id = int(input("\nEnter Student ID (integer): "))
            student_name = input("Enter Student Name: ")
            student_percentage = float(input("Enter Student Percentage: "))
            cursor.execute(insert_query,(student_id,student_name,student_percentage)) 
            print(f"Successfully staged: {student_name}") 
        except ValueError:
            print("❌ Invalid input type! ID must be an integer, and percentage must be a number. Try again.")
        except psycopg2.errors.UniqueViolation:
            print(f"❌ Error: Student ID {student_id} already exists in the database!")
            conn.rollback()
            continue
        another = input("\nDo you want to add another student? (yes/no): ").strip().lower()
        if another not in ['y', 'yes']:
            break
    conn.commit()
    print("\n All data has been successfully saved to PostgreSQL!")
except Exception as e:
    print(f"\nA critical database error occurred: {e}")
    if 'conn' in locals():
        conn.rollback()
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
print("Database connection closed.")