import tkinter as tk
from tkinter import messagebox
import json

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Account Configuration")

        # Variables to store input values
        self.origin_api_key_var = tk.StringVar()
        self.origin_user_id_var = tk.StringVar()
        self.end_api_key_var = tk.StringVar()
        self.end_user_id_var = tk.StringVar()
        
        self.origin_api_key = "Origin Account Api Key"
        self.origin_api_key = "Origin Account Api Key"

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Origin Account Section
        origin_label = tk.Label(self.root, text="Origin Account")
        origin_label.grid(row=0, column=0, columnspan=2, pady=10)

        origin_api_key_label = tk.Label(self.root, text="API Key:")
        origin_api_key_label.grid(row=1, column=0, padx=5, pady=5)
        origin_api_key_entry = tk.Entry(self.root, textvariable=self.origin_api_key_var)
        origin_api_key_entry.insert(0, "DefaultOriginAPIKey")
        origin_api_key_entry.grid(row=1, column=1, padx=5, pady=5)

        origin_user_id_label = tk.Label(self.root, text="User ID:")
        origin_user_id_label.grid(row=2, column=0, padx=5, pady=5)
        origin_user_id_entry = tk.Entry(self.root, textvariable=self.origin_user_id_var)
        origin_user_id_entry.grid(row=2, column=1, padx=5, pady=5)

        # Separator
        separator = tk.Frame(self.root, height=1, width=300, bg="black")
        separator.grid(row=3, column=0, columnspan=2, pady=10)

        # End Account Section
        end_label = tk.Label(self.root, text="End Account")
        end_label.grid(row=4, column=0, columnspan=2, pady=10)

        end_api_key_label = tk.Label(self.root, text="API Key:")
        end_api_key_label.grid(row=5, column=0, padx=5, pady=5)
        end_api_key_entry = tk.Entry(self.root, textvariable=self.end_api_key_var)
        end_api_key_entry.grid(row=5, column=1, padx=5, pady=5)

        end_user_id_label = tk.Label(self.root, text="User ID:")
        end_user_id_label.grid(row=6, column=0, padx=5, pady=5)
        end_user_id_entry = tk.Entry(self.root, textvariable=self.end_user_id_var)
        end_user_id_entry.grid(row=6, column=1, padx=5, pady=5)

        # Separator
        separator = tk.Frame(self.root, height=1, width=300, bg="black")
        separator.grid(row=7, column=0, columnspan=2, pady=10)
        
        # Save Button
        save_button = tk.Button(self.root, text="Save", command=self.save_configuration)
        save_button.grid(row=8, column=0, columnspan=2, pady=10)

        # Deploy Button
        deploy_button = tk.Button(self.root, text="Deploy", command=self.deploy_logic)
        deploy_button.grid(row=9, column=0, columnspan=2, pady=10)

    def save_configuration(self):
        # Create a dictionary to store the configuration
        config_data = {
            "origin": {
                "api_key": self.origin_api_key_var.get(),
                "user_id": self.origin_user_id_var.get(),
            },
            "end": {
                "api_key": self.end_api_key_var.get(),
                "user_id": self.end_user_id_var.get(),
            }
        }

        # Save the configuration to a JSON file
        with open("config.json", "w") as json_file:
            json.dump(config_data, json_file)

        messagebox.showinfo("Saved", "Configuration saved successfully!")

    def deploy_logic(self):
        # Implement your personal business logic here
        # You can access the API keys and user IDs using self.origin_api_key_var.get(), etc.
        messagebox.showinfo("Deploy", "Business logic deployed!")


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
