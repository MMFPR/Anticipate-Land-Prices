import tkinter as tk
from tkinter import ttk, messagebox

# Define district coefficients
district_coefficients = {
    "Riyadh": 1.0,
    "Jeddah": 1.2,
    "Mecca": 1.5,
    "Medina": 1.1,
    "Dammam": 1.3,
    "Khobar": 1.4,
    "Dhahran": 1.2,
    "Taif": 1.6,
    "Abha": 1.8,
    "Jubail": 1.4,
    "Hofuf": 1.3,
    "Qatif": 1.5,
}

def calculate_expected_price(*args):
    try:
        current_land_area = float(land_area_entry.get())
        num_rooms = int(rooms_entry.get())
        selected_corners = int(corners_combobox.get())

        # Custom coefficients for your specific calculation
        room_coefficient = 100
        corner_coefficient = 1.2
        base_price_per_sq_meter = 500  # Adjust this based on your specific needs

        selected_district = district_combobox.get()

        # Get the district coefficient
        district_coefficient = district_coefficients.get(selected_district, 1.0)

        expected_land_area = current_land_area + (num_rooms * room_coefficient)

        # Adjust for the selected number of corners and district coefficient
        expected_land_area *= (corner_coefficient ** selected_corners) * district_coefficient

        expected_price = expected_land_area * base_price_per_sq_meter

        result_label.config(text=f"The expected price in {selected_district} is: {expected_price:.2f} SAR")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

# Create the main window
window = tk.Tk()
window.title("Expected Price Calculator")

# Create and place widgets
land_area_label = tk.Label(window, text="Current Land Area:")
land_area_label.grid(row=0, column=0, padx=5, pady=5)

land_area_entry = tk.Entry(window)
land_area_entry.grid(row=0, column=1, padx=5, pady=5)

rooms_label = tk.Label(window, text="Number of Rooms:")
rooms_label.grid(row=1, column=0, padx=5, pady=5)

rooms_entry = tk.Entry(window)
rooms_entry.grid(row=1, column=1, padx=5, pady=5)

corners_label = tk.Label(window, text="Number of Corners:")
corners_label.grid(row=2, column=0, padx=5, pady=5)

# Dropdown for selecting the number of corners
corner_options = [0, 1, 2, 3]  # You can customize this list based on your needs
corners_combobox = ttk.Combobox(window, values=corner_options)
corners_combobox.grid(row=2, column=1, padx=5, pady=5)
corners_combobox.set(0)  # Default to 0 corners

district_label = tk.Label(window, text="Select District:")
district_label.grid(row=3, column=0, padx=5, pady=5)

# Real districts in Saudi Arabia
districts = [
    "Riyadh", "Jeddah", "Mecca", "Medina",
    "Dammam", "Khobar", "Dhahran", "Taif",
    "Abha", "Jubail", "Hofuf", "Qatif"
]
district_combobox = ttk.Combobox(window, values=districts)
district_combobox.grid(row=3, column=1, padx=5, pady=5)
district_combobox.bind("<<ComboboxSelected>>", calculate_expected_price)  # Bind the selection event

calculate_button = tk.Button(window, text="Calculate", command=calculate_expected_price)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Start the main loop
window.mainloop()