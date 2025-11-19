def get_employee_info(name,emp_id,department,salary):
    
    #Returns a formatted string containing employee details.
    return(
        f"employee name:{name},"
        f"Employee ID:{emp_id},"
        f"Departments:{department},"
        f"Salary:{salary:.2f}"
    )
#Example usage(optional)
if __name__ == "__main__":
    print(get_employee_info("John Doe", "E101","IT",55000))